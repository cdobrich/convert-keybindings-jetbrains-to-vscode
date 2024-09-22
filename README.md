# Convert keybinding from JetBrains Products to VSCode

Convert keybindings from JetBrains products (PyCharm, Webstorm, RustRover, etc.) to VSCode.

# How to Use

The _command_translation_dictionary_ is a set of translation data in JSON format. It is provided with this program, mapping what the developer has determined translates between the two program environments. This is the first argument passed to the program. (This file can also be substituted by users.)

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


# Installing the Generated File

Copy the output file (default filename is keybindings.json) to the user configured key map storage Locations. See below for operation system specific locations.

## MacOS

    ~/Library/Application\ Support/Code/User/keybindings.json

## Linux

    ~/.config/Code/User/keybindings.json

There is a shellscript `install-keybindings-to-vscode-on-linux.sh` which will copy the default output `keybindings.json` to the default VSCode installation location on Linux. Close VSCode before running this shellscript.

## Windows

    %APPDATA%\Code\User\keybindings.json

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
