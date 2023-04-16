"""Add on to scrape from google image search and download it to the media folder.

Alois Thibert
alois.devlp@gmail.com

MIT License

Copyright (c) 2022 Alois Thibert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import re
import time
from io import BytesIO
from typing import List

import requests
import subprocess
from aqt import gui_hooks
from aqt.operations import QueryOp
from aqt.qt import QApplication, QDialog
from aqt.utils import qconnect, showInfo, tooltip

from .gui.gui import Ui_Definitions_getter

from pathlib import Path
import zipfile
import json
import os
import sys
SCRIPT_DIR = Path(__file__).parent 
libfolder = os.path.join(SCRIPT_DIR, "env\Lib\site-packages")
sys.path.insert(0, libfolder)

from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary(dict_type='small').create()
mode = tokenizer.Tokenizer.SplitMode.A

dictionary_map = {}



QApplication.instance().processEvents()


def parse_user_src_field(addon_window) -> str:
    return addon_window.combo_field_src.currentText()


def parse_user_dst_field(addon_window) -> str:
    return addon_window.combo_field_dst.currentText()


def parse_user_mode(addon_window) -> str:
    return addon_window.combo_action.currentText()


def parse_user_nb_definitions(addon_window) -> int:
    return int(addon_window.selector_NbDefinitions.value())

def load_dictionary(dictionary):
    output_map = {}
    archive = zipfile.ZipFile(dictionary, 'r')

    result = list()
    for file in archive.namelist():
        if file.startswith('term'):
            with archive.open(file) as f:
                data = f.read()  
                d = json.loads(data.decode("utf-8"))
                result.extend(d)

    for entry in result:
        if (entry[0] in output_map):
            output_map[entry[0]].append(entry) 
        else:
            output_map[entry[0]] = [entry] # Using headword as key for finding the dictionary entry
    return output_map

def setup():
    global dictionary_map 
    dictionary_map = load_dictionary(str(Path(SCRIPT_DIR, 'dictionaries', 'jmdict_english.zip')))
    


def look_up(word, nb_definitions):
    word = word.strip()
    if word not in dictionary_map:
        m = tokenizer_obj.tokenize(word, mode)[0]
        word = m.dictionary_form()
        if word not in dictionary_map:
            return None
    result = [{
        'headword': entry[0],
        'reading': entry[1],
        'tags': entry[2],
        'glossary_list': entry[5],
        'sequence': entry[6]
    } for entry in dictionary_map[word]]
    definitions = ""
    for definition in result[:nb_definitions]:
        definitions += f"<h3>{definition['reading']}【{definition['headword']}】</h3>"
        definitions += f"{definition['tags']}<br>"
        for index, item in enumerate(definition['glossary_list']):
            if len(definition['glossary_list']) == 1:
                if index == 0:
                    definitions += f"<ul><li>{item}</li></ul>"
            else:
                if index == 0:
                    definitions += f"<ul><li>{item}</li>"
                elif index == len(definition['glossary_list'])-1:
                    definitions += f"<li>{item}</li></ul>"
                else:
                    definitions += f"<li>{item}</li>"
        definitions += f"<br>"

    definitions = definitions[:-4]
    return definitions

setup()

def setup_gui_addon(browser) -> None:
    cards_id = browser.selectedNotes()
    if not cards_id:
        tooltip("Please select at least one card")
        return

    main_window = browser.mw
    dialog = QDialog(browser)
    addon_window = Ui_Definitions_getter()
    addon_window.setupUi(dialog)

    notes = []
    for card_id in cards_id:
        notes.append(main_window.col.getNote(card_id))

    fields = notes[0].keys()
    addon_window.combo_field_src.addItems(fields)
    addon_window.combo_field_dst.addItems(fields)

    dialog.setVisible(True)

    dialog.accepted.connect(
        lambda: launch_bg_note_processing(
            mw=main_window,
            notes=notes,
            addon_window=addon_window,
        )
    )


def _add_definitions_to_card(note, field, mode, word, nb_definitions):
    result_def = look_up(word,nb_definitions)
    if mode == "Overwrite":
        note[field] = ""
    if result_def:
        note[field] += result_def
    else:
        pass
    note.flush()

def on_success(_) -> None:
    showInfo("Processing has finished.")


def launch_bg_note_processing(mw, notes, addon_window):
    op = QueryOp(
        parent=mw,
        op=lambda _: update_notes(mw, notes, addon_window),
        success=on_success,
    )

    op.with_progress().run_in_background()


def update_notes(mw, notes, addon_window):
    nb_definitions = parse_user_nb_definitions(addon_window=addon_window)
    src_field = parse_user_src_field(addon_window=addon_window)
    dst_field = parse_user_dst_field(addon_window=addon_window)
    nb_notes = len(notes)
    for i, note in enumerate(notes):
        start = time.time()
        time_elapsed = time.time() - start
        if time_elapsed != 0:
            mw.taskman.run_on_main(
                lambda: mw.progress.update(
                    label="{done}/{total} cards. {frac}cards/s. Remainining:~{timeremaining} s".format(
                        done=i,
                        total=nb_notes,
                        frac=round(1 / (time_elapsed), 2),
                        timeremaining=round((nb_notes - i) * (time_elapsed), 1),
                    ),
                )
            )

        _add_definitions_to_card(
            note=note,
            field=dst_field,
            mode=parse_user_mode(addon_window=addon_window),
            word=note[src_field],
            nb_definitions = nb_definitions
        )

    mw.requireReset()


def set_up_addon_menu(browser) -> None:
    menu = browser.form.menu_Cards
    menu.addSeparator()
    menu_action = menu.addAction("Add Definitions")
    qconnect(menu_action.triggered, lambda _: setup_gui_addon(browser=browser))


def init():
    gui_hooks.browser_menus_did_init.append(set_up_addon_menu)


init()
