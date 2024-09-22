#!/bin/bash

DEFAULT_VSCODE_KEYBINDINGS_PATH="$HOME/.config/Code/User/keybindings.json"
DEFAULT_KEYBINDINGS_FILENAME="keybindings.json"

echo "Copying default output file: 'keybindings.json'"

if [ "$1" != "" ] && [ -f $1 ]; then
	echo "Installing '$1' keybindings file into $USER default VSCode path."
	echo "  DEFAULT INSTALL PATH: $DEFAULT_VSCODE_KEYBINDINGS_PATH"
	cp $1 $DEFAULT_VSCODE_KEYBINDINGS_PATH
else
	echo "Installing '$DEFAULT_KEYBINDINGS_FILENAME' file into $USER default VSCode path."
	echo "  DEFAULT INSTALL PATH: $DEFAULT_VSCODE_KEYBINDINGS_PATH"
	cp $DEFAULT_KEYBINDINGS_FILENAME $DEFAULT_VSCODE_KEYBINDINGS_PATH
fi
