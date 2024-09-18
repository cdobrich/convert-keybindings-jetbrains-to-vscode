# TODO

List of features, with notes, needing to be worked on.

## Editor Font Increase Size, Decrease Size, Reset

The translation output for the following section does not seem to generate correctly. The conversion code does not match the expected output.

It should match the following. This sample is output when done through the VSCode GUI:

    {
        "key": "alt+numpad_subtract",
        "command": "editor.action.fontZoomOut"
    },
    {
        "key": "alt+numpad_add",
        "command": "editor.action.fontZoomIn"
    },
    {
        "key": "alt+=",
        "command": "editor.action.fontZoomReset"
    },

## Close Active Window (multiple keys)

This does not appear to be working for the CloseContent feature. Example:

From the default bindings (works):

    { "key": "ctrl+f4",               "command": "workbench.action.closeActiveEditor" },

In the command translation dictionary, but not appearing in the output (and therefore not working):

    { "key": "ctrl+w",               "command": "workbench.action.closeActiveEditor" },
    { "key": "meta+w",               "command": "workbench.action.closeActiveEditor" },

## Hide Side Panel

Currently, this seems to shift to Zen-Mode, not hide the panel.

    { "key": "alt+numpad1",           "command": "workbench.view.explorer",
                                     "when": "viewContainer.workbench.view.explorer.enabled && !explorerViewletFocus" },
    { "key": "alt+1",                 "command": "workbench.action.toggleSidebarVisibility",
                                     "when": "explorerViewletFocus" },
    { "key": "alt+numpad1",           "command": "workbench.action.toggleSidebarVisibility",
                                     "when": "explorerViewletFocus" },

## Re-usable Data for Regression Testing

TBD, WIP.
