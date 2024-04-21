# Convert keybinding from JetBrains Products to VSCode

Convert keybindings from JetBrains products (PyCharm, Webstorm, etc.) to VSCode.

# How to Use

The _command_translation_dictionary_ is a set of translation data in JSON format. It is provided with this program, mapping what the developer has determined translates between the two program environments. This is the first argument passed to the program. (This file can also be substituted by users.)

Users may supply their own _Jetbrain's XML_ file. This is provided by using the '-x' or '--xml' command line switch.

Example command:
```
convert-keybindings-jetbrains-to-vscode.py command_translation_dictionary.json --xml jetbrains_keybindings_example.xml --output my_output.json
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

## Windows

    %APPDATA%\Code\User\keybindings.json


# Limitations

## Multiple keys for the same command

This feature is currently in work. It is not difficult and should be added soon.

## Command Translation Dictionary Incomplete

The list of translatable commands between Jetbrains and VScode is (1) not complete, and (2) not fully tested, though I will be fixing any problems I encounter along the way.

Regarding the incomplete list of commands, I have finished adding the commands that I personally use. I will probably not add (many) more.

Input patches or simple user comments for more valid command translations between the IDEs is welcome. I will add more to the project when I receive them.

## Only Jetbrains to VSCode currently

At this time, the program only converts from Jetbrains to VSCode format.

Though it would not be very difficult to reverse the process.

# Developer Notes

The JSON value "args" is specific to VSCode.