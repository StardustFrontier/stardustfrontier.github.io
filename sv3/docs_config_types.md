# Config Types

[Return to Functions](./docs.html)

#
Config types are used for getting and setting values to the config file.\
The available config types are:

- **DNHCONFIG_SCREEN_MODE**\
The screen mode (fullscreen, windowed)\
\
Get Arguments: `(none)`\
Set Arguments: `real: mode`

<br />

- **DNHCONFIG_WINDOW_SIZE**\
The window size (4 size options, varies depending on settings in .def file)\
\
Get Arguments: `(none)`\
Set Arguments: `real: windowSize`

<br />

- **DNHCONFIG_FPS_TYPE**\
The FPS type (1/1, 1/2, 1/3, flexible)\
\
Get Arguments: `(none)`\
Set Arguments: `real: fpsType`

<br />

- **DNHCONFIG_VSYNC**\
Whether or not vertical sync is enabled (true, false)\
\
Get Arguments: `(none)`\
Set Arguments: `bool: bVsync`

<br />

- **DNHCONFIG_PAD_INDEX**\
The currently set pad index, chosen from the list of pads displayed in config.exe (index)\
\
Get Arguments: `(none)`\
Set Arguments: `real: index`

<br />

- **DNHCONFIG_VIRTUAL_KEY**\
A virtual key mapped to a keyboard key and/or pad button.\
Note: The pad button can be acquired from CheckPadState()\
\
Get Arguments: `real const: virtualKeyID`\
Set Arguments: `real const: virtualKeyID, real const: keyboardKey, real: padIndex, real: padButton`

<br />

- **DNHCONFIG_LOG_WINDOW**\
Whether or not the LogWindow is enabled.\
\
Get Arguments: `(none)`\
Set Arguments: `bool: bLogWindow`

<br />

- **DNHCONFIG_LOG_FILE**\
Whether or not file logging is enabled.\
\
Get Arguments: `(none)`\
Set Arguments: `bool: bLogFile`

<br />

- **DNHCONFIG_MOUSE_VISIBLE**\
Whether or not the mouse is visible whilst hovering over the game window.\
\
Get Arguments: `(none)`\
Set Arguments: `bool: bMouseVisible`

<br />

- **DNHCONFIG_USER_VALUE**\
A user-defined real number value at a given index.\
8 indices (0-7) are available.\
\
Get Arguments: `real: valueIndex`\
Set Arguments: `real: valueIndex, real: value`

<br />