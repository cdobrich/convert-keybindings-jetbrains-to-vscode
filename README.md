# Convert keybinding from JetBrains Products to VSCode

Convert keybindings from JetBrains products (PyCharm, Webstorm, RustRover, etc.) to VSCode. This also works for community forks of VSCode, such as VSCodium (with adjusted folder paths).

# How to Use

The _command_translation_dictionary.json_ is a set of translation data in JSON format. It is provided with this program, mapping what the developer has determined translates between the two program environments (JetBrains and VSCode). This is the first argument passed to the program.

Users may supply their own _Jetbrain's XML_ file. This is provided by using the '-x' or '--xml' command line switch.

The default output uses the name 'keybindings.json'.

Example command:
```
convert-keybindings-jetbrains-to-vscode.py command_translation_dictionary.json --xml data/jetbrains_keybindings_example.xml --output my_output.json
```

## Where to Get Your Current JetBrains Product (PyCharm, Webstorm, etc.) keybindings file

The precise location will depend on the product AND the version number.

### MacOS

Syntax: ```~/Library/Application Support/JetBrains/<product><version>/keymaps/```

#### Example filepaths

    ~/Library/Application\ Support/JetBrains/WebStorm2021.3/keymaps/SomeKeybingingName.xml

### Linux

Syntax: ```~/.config/JetBrains/<product><version>/keymaps/```

#### Example filepaths

    "~/.config/JetBrains/PyCharmCE2024.1/keymaps/Windows-like for macOS.xml"
    "~/.config/JetBrains/IntelliJIdea2021.3/keymaps/Windows-like for macOS.xml"
    ~/.config/JetBrains/IntelliJIdea2021.3/keymaps/SomeKeybingingName.xml

### Linux (on flatpak)

Syntax: ```~/.var/app/com.jetbrains.PyCharm-Community/config/JetBrains/<product><version>/keymaps/```

#### Example filepaths

    ~/.var/app/com.jetbrains.PyCharm-Community/config/JetBrains/PyCharmCE2023.1/keymaps/SomeKeybingingName.xml

### Troubleshooting: Keybindings Not Applying (Linux / Flatpak)

If you are using Linux—especially if VSCodium/VSCode is installed via **Flatpak**—you might notice that your converted keybindings (such as custom overrides like `Ctrl+R`) do not take effect, and the application continues to use its default global shortcuts.

This happens because sandboxed installations isolate their configuration files, causing them to ignore direct edits made to the host system's default generic paths (e.g., `~/.config/`).

To force the application to register your custom configuration, follow these steps to paste the file contents directly through the application GUI:

1. **Open VSCodium / VSCode**.
2. **Open the Command Palette**: Press `F1` (or `Ctrl+Shift+P`).
3. **Locate the Configuration File**: Type `Preferences: Open Keyboard Shortcuts (JSON)` and press `Enter`. 
   > **Note:** This forces the editor to open the exact `keybindings.json` file it is actively reading inside its sandbox environment.
4. **Apply Your Custom Keybindings**: 
   * Select all existing text in the window that opens and delete it.
   * Copy the entire contents of your newly generated `keybindings.json` file.
   * Paste it directly into the editor tab.
5. **Save and Apply**: Save the file (`Ctrl+S`). The new mappings will apply immediately without needing a full application restart.

# Installing the Generated File

Copy the output file (default filename is `keybindings.json`) to the user configured key map storage Locations. See below for operation system specific locations.

## VSCodium

### Linux (Standard, non-Flatpak)

    ~/.config/VSCodium/User/keybindings.json

There is a shellscript `install-keybindings-to-vscode-on-linux.sh` which will copy the default output `keybindings.json` to the default VSCode installation location on Linux. Close VSCode before running this shellscript.

### Linux (Flatpak Installation)

If you installed VSCodium as a Flatpak, the path is sandboxed:

    ~/.var/app/com.vscodium.codium/config/VSCodium/User/keybindings.json

## VSCode

### Linux (Standard, non-Flatpak)

    ~/.config/Code/User/keybindings.json

There is a shellscript `install-keybindings-to-vscode-on-linux.sh` which will copy the default output `keybindings.json` to the default VSCode installation location on Linux. Close VSCode before running this shellscript.

### Linux (Flatpak Installation)

TBD

### MacOS

    ~/Library/Application Support/VSCodium/User/keybindings.json

### Windows

    %APPDATA%\VSCodium\User\keybindings.json

# Limitations

## Multiple keys for the same command

A bug has been identified and a solution proposed. 

FIXME: For example, currently only `Ctrl+UpPg` or `Ctrl+DownPg` work to switch tabs. Ideally we want to include support for `Ctrl+Tab`.

# TODO

See the [TODO.md](TODO.md) file for roadmap data.

## Command Translation Dictionary Incomplete

The list of translatable commands between Jetbrains and VScode is (1) not complete, and (2) not fully tested, though I will be fixing any problems I encounter along the way.

Regarding the incomplete list of commands, I have finished adding the commands that I personally use. I will probably not add (many) more.

Input patches or simple user comments for more valid command translations between the IDEs is welcome. I will add more to the project when I receive them.

## Only Jetbrains to VSCode currently

At this time, the program only converts from Jetbrains to VSCode format.

Though it would not be very difficult to reverse the process.

# Developer Notes

The JSON value "args" is specific to VSCode.
