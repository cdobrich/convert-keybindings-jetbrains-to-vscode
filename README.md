# Convert keybinding from Jetbrains Products to VSCode

Convert keybindings from Jetbrains products (PyCharm, Webstorm, etc.) to VSCode.

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