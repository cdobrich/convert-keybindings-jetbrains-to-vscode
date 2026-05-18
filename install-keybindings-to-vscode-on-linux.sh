#!/bin/bash

# Define the target paths
VSCODE_PATH="$HOME/.config/Code/User/keybindings.json"
VSCODIUM_PATH="$HOME/.config/VSCodium/User/keybindings.json"
FLATPAK_CODIUM_PATH="$HOME/.var/app/com.vscodium.codium/config/VSCodium/User/keybindings.json"

DEFAULT_KEYBINDINGS_FILENAME="keybindings.json"

# Determine which source file to use
SOURCE_FILE=$DEFAULT_KEYBINDINGS_FILENAME
if [ "$1" != "" ] && [ -f "$1" ]; then
	SOURCE_FILE=$1
fi

if [ ! -f "$SOURCE_FILE" ]; then
	echo "Error: Source keybindings file '$SOURCE_FILE' not found."
	exit 1
fi

echo "Preparing to install keybindings from: '$SOURCE_FILE'"
echo "--------------------------------------------------"

# Function to handle the copying and directory creation if the ecosystem exists
install_if_supported() {
	local target_file="$1"
	local app_name="$2"
	local target_dir=$(dirname "$target_file")

	# Check if the base configuration directory exists to assume the app is installed/used
	# For Flatpak, we check the application's root config sandbox directory
	local check_dir="$target_dir"
	if [[ "$app_name" == *"Flatpak"* ]]; then
		check_dir="$HOME/.var/app/com.vscodium.codium"
	else
		check_dir=$(dirname "$target_dir") # Checks ~/.config/Code or ~/.config/VSCodium
	fi

	if [ -d "$check_dir" ]; then
		echo "Detected $app_name environment."
		echo "  Installing to: $target_file"
		mkdir -p "$target_dir"
		cp "$SOURCE_FILE" "$target_file"
		echo "  Success!"
	else
		echo "Skipping $app_name (Environment not detected)."
	fi
	echo ""
}

# Run the installation checks
install_if_supported "$VSCODE_PATH" "VS Code (Standard)"
install_if_supported "$VSCODIUM_PATH" "VSCodium (Standard)"
install_if_supported "$FLATPAK_CODIUM_PATH" "VSCodium (Flatpak)"

echo "--------------------------------------------------"
echo "Installation process complete."
