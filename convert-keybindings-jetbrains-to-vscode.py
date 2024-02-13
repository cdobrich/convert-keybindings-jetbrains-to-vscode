import argparse

import sys
import json
import os
import xml.etree.ElementTree as ET


def xml_to_dict(xml_file):
    """
    Used for internal memory processing and compatibility support of XMl files.
    :param xml_file:
    :return: A dictionary representing the XML data.
    """
    keybindings = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for action in root.findall('.//action'):
        action_id = action.attrib.get('id')
        shortcut = action.find('.//keyboard-shortcut')
        if shortcut is not None:
            shortcut_value = shortcut.attrib.get('first-keystroke')
            keybindings[action_id] = shortcut_value
    return keybindings


def convert_to_vscode_format(pycharm_keybindings):
    vscode_keybindings = []
    for action_id, shortcut_value in pycharm_keybindings.items():
        vscode_keybindings.append({
            "key": shortcut_value,
            "command": action_id,
            "when": "editorTextFocus"
        })
    return vscode_keybindings


def save_to_json(keybindings, output_file):
    with open(output_file, 'w') as f:
        json.dump(keybindings, f, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Convert Jetbrains (Pycharm, Webstorm, etc.) keybinding XML keybindings commands to a VSCode JSON format.")
    parser.add_argument("translation_json_file", help="Path to the Command Translation file for converting between Jetbrains and VSCode commands")
    parser.add_argument("jetbrains_xml_file", help="Path to the target Jetbrains keybindings XML file to convert")
    parser.add_argument("-o", "--output", help="Output file name (default: keybindings.json)", default="keybindings.json")
    args = parser.parse_args()

    translation_json_file = args.translation_json_file
    jetbrains_xml_file = args.jetbrains_xml_file
    vscode_keybindings_file = args.output

    if not os.path.exists(translation_json_file):
        print(f"Translation JSON file '{translation_json_file}' does not exist.")
        sys.exit(1)

    if not os.path.exists(jetbrains_xml_file):
        print(f"Jetbrains XML file '{jetbrains_xml_file}' does not exist.")
        sys.exit(1)

    translation_dict = {}

    # Create a searchable dictionary with strings input for both VSCode and Jetbrains commands as keys.
    with open(translation_json_file, 'r') as f:
        translation_list = json.load(f)
        for item in translation_list:
            translation_dict[item.get('jetbrains_command')] = item
            translation_dict[item.get('vscode_command')] = item

    data_dict = xml_to_dict(jetbrains_xml_file)
    jetbrains_data = convert_to_vscode_format(data_dict)

    translated_commands = []

    # Convert Jetbrains format to VSCode format
    for command_data in jetbrains_data:
        command = command_data.get("command")
        translation_unit = translation_dict.get(command)
        if translation_unit:
            # convert jetbrains key property whitespace ' ' to vscode plus-sign '+'
            converted_key = translation_unit.get("jetbrains_key", "").replace(' ', '+')
            translated_command = {
                "key": converted_key,
                "command": translation_unit.get("vscode_command"),
                "when": translation_unit.get("vscode_when", ""),
            }
            translated_commands.append(translated_command)

    # TODO / FIXME: Account for multiple key-bindings for the same command.
    # TODO / FIXME: Include any 'args' when converting out of VSCode format to Jetbrains? At least note the assumption.

    save_to_json(translated_commands, vscode_keybindings_file)
    print("Conversion complete. Output saved to", vscode_keybindings_file)


if __name__ == "__main__":
    main()
