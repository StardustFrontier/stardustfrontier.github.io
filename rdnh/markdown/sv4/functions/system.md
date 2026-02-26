# System Functions

[Return to Functions](../functions.html)

## SetStgFrame
```
    Arguments:
        1) real: left
        2) real: top
        3) real: right
        4) real: bottom
        5) real: minRenderPriorityI = nil
        6) real: maxRenderPriorityI = nil
```
Sets the STG space frame with the given rectangle and minimum and maximum (integer) render priorities.

If a render priority argument is nil, it will not be modified.

The default STG frame values are (32, 16, 416, 464, 20, 80).

## GetScore
```
    Return Type:
        real
```
Returns the current score.

## AddScore
```
    Arguments:
        1) real: score
```
Adds the given value to the score.

## GetGraze
```
    Return Type:
        real
```
Returns the current graze count.

## AddGraze
```
    Arguments:
        1) real: graze
```
Adds the given value to the graze count.

## GetPoint
```
    Return Type:
        real
```
Returns the current amount of point items collected.

## AddPoint
```
    Arguments:
        1) real: point
```
Adds the given value to the point count.

## GetDifficulty
```
    Return Type:
        real
```
Gets the difficulty level of all running scripts.

## SetDifficulty
```
    Arguments:
        1) real: difficulty
```
Sets the difficulty level of all scripts, affecting both currently running scripts and future started ones.

The following values should be used for functions like [vdif](#vdif) to make sense:
```
0 = Easy
1 = Normal
2 = Hard
3 = Lunatic
```

## vdif
```
    Arguments:
        1) any: args...
    Return:
        any: value
```
Returns the argument value at the index equivalent to the difficulty level (uses [GetDifficulty](#getdifficulty) internally).

If the index is out of bounds, the last argument will be returned.\
This allows you to return the last argument in cases where you want every difficulty beyond a certain one to have the same value.

Example:
```
let value1 = [2, 4, 6, 8][GetDifficulty()];
let value2 = vdif(2, 4, 6, 8); // same result as the above line

let value3 = vdif(4, 16); // if difficulty >= 1 (Normal), 16 will be returned
```

## SetScriptDifficultyNames
```
    Arguments:
        1) array[string]: names
```
Sets the internal difficulty names shown in the log window's info panel.

The names are indexed based on the value set by SetDifficulty.\
Out of bounds values are displayed as "Invalid".

Defaults to:\
["Easy", "Normal", "Hard", "Lunatic", "Extra", "Phantasm", "Overdrive", "Difficulty_7"]

## SetEnemyRenderPriorityI
```
    Arguments:
        1) real: renderPriorityI
```
Sets the render priority for enemies, on a 0 to 100 scale.

Default is 40.

## SetItemRenderPriorityI
```
    Arguments:
        1) real: renderPriorityI
```
Sets the render priority for items, on a 0 to 100 scale.

Default is 60.

## SetShotRenderPriorityI
```
    Arguments:
        1) real: renderPriorityI
```
Sets the render priority for shots, on a 0 to 100 scale.

Default is 50.

## SetCameraFocusPermitPriorityI
```
    Arguments:
        1) real: renderPriorityI
```
Sets the render priority for the 2D camera, on a 0 to 100 scale.

Default is 69.

## SetIntersectionVisualization
```
    Arguments:
        1) bool: bEnable
```
Enables or disables visualization of all intersection object hitboxes.

Colors:
```
Green:  Player hitbox+grazebox
Blue:   Player shot
Cyan:   Player spell
Yellow: Enemy hitbox+killbox
Red:    Enemy shot
```

## SetIntersectionVisualizationRenderPriority
```
    Arguments:
        1) real: renderPriorityI
```
Sets the render priority for hitbox visualizations, on a 0 to 100 scale.

Default value is 68 (GetCameraFocusPermitPriorityI() - 1).

## GetStgFrameRenderPriorityMinI
```
    Return Type:
        real
```
Returns the lowest render priority for the STG frame, on a 0 to 100 scale.

Default is 20.

## GetStgFrameRenderPriorityMaxI
```
    Return Type:
        real
```
Returns the highest render priority for the STG frame, on a 0 to 100 scale.

Default is 80.

## GetEnemyRenderPriorityI
```
    Returns:
        real: priorityI
```
Returns the render priority for enemies, on a 0 to 100 scale.

## GetItemRenderPriorityI
```
    Return Type:
        real
```
Returns the render priority for items, on a 0 to 100 scale.

## GetShotRenderPriorityI
```
    Return Type:
        real
```
Returns the render priority for shots, on a 0 to 100 scale.

## GetPlayerRenderPriorityI
```
    Return Type:
        real
```
Returns the render priority for the player, on a 0 to 100 scale.

## GetCameraFocusPermitPriorityI
```
    Return Type:
        real
```
Returns the highest render priority the 2D camera can affect, on a 0 to 100 scale.

Default is 79.

## GetStgFrameLeft
```
    Return Type:
        real
```
Returns the leftmost coordinate of the STG frame (playing field).

Default is 32.

## GetStgFrameTop
```
    Return Type:
        real
```
Returns the topmost coordinate of the STG frame (playing field).

Default is 16.

## GetStgFrameRight
```
    Return Type:
        real
```
Returns the rightmost coordinate of the STG frame (playing field).

Default is 416.

## GetStgFrameBottom
```
    Return Type:
        real
```
Returns the bottommost coordinate of the STG frame (playing field).

Default is 464.

## GetStgFrameWidth
```
    Return Type:
        real
```
Returns the width of the STG frame (playing field).

Default is 384.

## GetStgFrameHeight
```
    Return Type:
        real
```
Returns the height of the STG frame (playing field).

Default is 448.

## GetScreenWidth
```
    Return Type:
        real
```
Returns the width of the screen (resolution) as defined in the .def.

Default is 640.

## GetScreenHeight
```
    Return Type:
        real
```
Returns the height of the screen (resolution) as defined in the .def.

Default is 480.

## GetMaxScreenWidth
```
    Return Type:
        real
```
Returns the largest screen width defined in the .def.

If only one screen size is defined, this has the same effect as GetScreenWidth.

## GetMaxScreenHeight
```
    Return Type:
        real
```
Returns the largest screen height defined in the .def.

If only one screen size is defined, this has the same effect as GetScreenHeight.

## GetWindowWidth
```
    Return Type:
        real
```
Returns the current width of the window.

## GetWindowHeight
```
    Return Type:
        real
```
Returns the current height of the window.

## GetMonitorResolution
```
    Return Type:
        array[real]
```
Returns the resolution of the monitor the window is currently on as an array [x, y].

## GetSupportedResolutions
```
    Return Type:
        array[array[real]]
```
Returns an array of all supported resolutions [width, height, refreshRate].

## IsReplay
```
    Return Type:
        bool
```
Returns true if a replay is playing, otherwise returns false.

## AddArchiveFile
```
    Return Type:
        bool
```
Adds the path to use when reading files from an archive file.

Returns true if the archive was successfully read, otherwise returns false.

## IsSkipMode
```
    Return Type:
        bool
```
Returns true if the game is currently in skip (fast-forward) mode, otherwise returns false.

## IsPackageRunning
```
    Returns:
        bool: bRunning
```
Returns true in any script if a package script is running, otherwise returns false.

## IsLoadThreadComplete
```
    Returns:
        bool: bComplete
```
Returns true if all load thread events have completed.

_**Note**: This should not be used to **yield;** during a stage, since this will cause replay desync, but yielding on package loading screens should be fine._

## IsScriptLoadThreadComplete
```
    Returns:
        bool: bComplete
```
Returns true if all script load thread events have completed.

_**Note**: This should not be used to **yield;** during a stage, since this will cause replay desync, but yielding on package loading screens should be fine._

## IsResourceLoadThreadComplete
```
    Returns:
        bool: bComplete
```
Returns true if all resource load thread events have completed.

_**Note**: This should not be used to **yield;** during a stage, since this will cause replay desync, but yielding on package loading screens should be fine._

## GetDnhConfigValue
```
    Arguments:
        1) real const: configType
        2) varies: ... (varargs args)
    Return Type:
        varies
```
**Deprecated:** Use the DnhConfig_ functions instead.

Returns a value from dnh's current config data based on the given [config type](./docs_config_types.html).

## SetDnhConfigValue
```
    Arguments:
        1) real const: configType
        2) varies: ... (varargs args)
```
**Deprecated:** Use the DnhConfig_ functions instead.

Sets a value to dnh's current config data based on the given [config type](./docs_config_types.html).

*Note: This will persist for the rest of the session, but in order to be saved, [SaveDnhConfigFile](savednhconfigfile) must be called.*

## DnhConfig_GetWindowStyle
```
    Return Type:
        real
```
Returns the window style from DnhConfig.

(fullscreen, windowed)

## DnhConfig_GetWindowSizeIndex
```
    Return Type:
        real
```
Returns the window size index from DnhConfig.

This is an index into the window size list defined in rdnh.def.

## DnhConfig_GetFrameskipMode
```
    Return Type:
        real
```
Returns the frameskip mode from DnhConfig

(1/1, 1/2, 1/3, Automatic)

## DnhConfig_IsVsync
```
    Return Type:
        bool
```
Returns a boolean indicating whether or not vertical sync is enabled in DnhConfig.

## DnhConfig_IsBorderlessFullScreen
```
    Return Type:
        bool
```
Returns a boolean indicating whether or not borderless fullscreen mode is enabled in DnhConfig.

## DnhConfig_IsIntegerScale
```
    Return Type:
        bool
```
Returns a boolean indicating whether or not integer scaling for borderless fullscreen mode is enabled in DnhConfig.

*Note: In official Touhou this is known as "DOT by DOT" mode.*

## DnhConfig_GetPadIndex
```
    Return Type:
        real
```
Returns the currently set pad index, chosen from the list of pads displayed in config.exe.

## DnhConfig_GetVirtualKey
```
    Arguments:
        1) real const: virtualKeyID
    Return Type:
        real array
```
Returns an array of info about the given virtual key in DnhConfig.

[keyboardKey, padIndex, padButton]

## DnhConfig_GetPadDeadzone
```
    Arguments:
        1) real: padIndex
    Return Type:
        real
```
Gets the deadzone for the pad at the given index.

_**Note:** Currently, padIndex is ignored as deadzone is a global setting for all pads. This may change in the future._

## DnhConfig_IsLogWindow
```
    Return Type:
        bool
```
Returns a boolean indicating whether or not the LogWindow is enabled in DnhConfig.

## DnhConfig_IsLogFile
```
    Return Type:
        bool
```
Returns a boolean indicating whether or not logging to a file is enabled in DnhConfig.

## DnhConfig_IsMouseVisible
```
    Return Type:
        bool
```
Returns a boolean indicating whether or not mouse visibility is enabled in DnhConfig.

## DnhConfig_GetUserValue
```
    Arguments:
        1) real const: valueIndex
    Return Type:
        bool
```
Returns a user-defined real number value that was saved within DnhConfig at a given index.
8 user-defined indices (0-7) are available.

## DnhConfig_SetWindowStyle
```
    Arguments:
        1) real const: style
```
Sets the window style in DnhConfig.

(fullscreen, windowed)

## DnhConfig_SetWindowSizeIndex
```
    Arguments:
        1) real: windowSizeIndex
```
Sets the window size index in DnhConfig.

This is an index into the window size list defined in rdnh.def.

## DnhConfig_SetFrameskipMode
```
    Arguments:
        1) real const: mode
```
Sets the frameskip mode in DnhConfig.

## DnhConfig_SetVsync
```
    Arguments:
        1) bool: enable
```
Enables or disables vertical sync in DnhConfig.

## DnhConfig_SetBorderlessFullScreen
```
    Arguments:
        1) bool: enable
```
Enables or disables borderless fullscreen mode in DnhConfig.

## DnhConfig_SetIntegerScale
```
    Arguments:
        1) bool: enable
```
Enables or disables integer scaling for borderless fullscreen mode is enabled in DnhConfig.

*Note: In official Touhou this is known as "DOT by DOT" mode.*

## DnhConfig_SetPadIndex
```
    Arguments:
        1) real: padIndex
```
Sets the pad index, chosen from the list of pads displayed in config.exe.

## DnhConfig_SetVirtualKey
```
    Arguments:
        1) real const: virtualKeyID
        2) real const: keyboardKey
        3) real: padIndex
        4) real: padButton
```
Maps a virtual key to a keyboard key and/or pad button.

*Note: The pad button can be acquired from CheckPadState()*

## DnhConfig_SetPadDeadzone
```
    Arguments:
        1) real: padIndex
        2) real: deadzonePercent
    Return Type:
        real
```
Sets the deadzone in percent (0-100) for the pad at the given index.

Pass PAD_DEADZONE_DEFAULT to reset the value to its default.

_**Note:** Currently, padIndex is ignored as deadzone is a global setting for all pads. This may change in the future._

## DnhConfig_SetLogWindow
```
    Arguments:
        1) bool: enable
```
Enables or disables the LogWindow in DnhConfig.

## DnhConfig_SetLogFile
```
    Arguments:
        1) bool: enable
```
Enables or disables logging to files in DnhConfig.

## DnhConfig_SetMouseVisible
```
    Arguments:
        1) bool: enable
```
Enables or disables mouse visibility in DnhConfig.

## DnhConfig_SetUserValue
```
    Arguments:
        1) real: index
        2) real: value
```
Sets a user-defined real number value that is saved within DnhConfig at a given index.
8 user-defined indices (0-7) are available.

## SaveDnhConfigFile
```
    Return Type:
        bool
```
Saves the current config data to the module directory and returns true if successful.

This file is named config.dat by default.

## DnhDef_GetWindowTitle
```
    Return Type:
        string
```
Returns the window title defined in rdnh.def (WindowTitle)

## DnhDef_GetPackageScriptPath
```
    Return Type:
        string
```
Returns the package script path defined in rdnh.def (PackageScriptMain)

## DnhDef_GetScreenSizes
```
    Return Type:
        2D real array
```
Returns an array of screen sizes defined in rdnh.def in the format: [[x, y], [x, y], [etc]]

This will be the screen size defined for each aspect ratio (Screen_4_3, Screen_16_9, etc)

## DnhDef_GetWindowSizes
```
    Return Type:
        2D real array
```
Returns the full array of window sizes defined in rdnh.def in the format: [[x, y], [x, y], [etc]]

## DnhDef_GetDefaultWindowSizeIndex
```
    Return Type:
        real
```
Returns the default window size index.

This is the index of the window size to start with by default when no config data exists.

## SetWindowTitle
```
    Arguments:
        1) string: title
```
Sets the window title.

If an empty string is passed, the initial window title will be restored.