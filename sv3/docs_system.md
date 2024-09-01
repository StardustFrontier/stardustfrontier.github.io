# System Functions

[Return to Functions](./docs.html)

## SetStgFrame
<pre>
    Arguments:
        1) real: left
        2) real: top
        3) real: right
        4) real: bottom
        5) real: minRenderPriorityI
        6) real: maxRenderPriorityI
</pre>
Sets the STG space frame with the given rectangle and minimum and maximum (integer) render priorities.

Default values are (32, 16, 416, 464, 20, 80).

## GetScore
<pre>
    Return Type:
        real
</pre>
Returns the current score.

## AddScore
<pre>
    Arguments:
        1) real: score
</pre>
Adds the given value to the score.

## GetGraze
<pre>
    Return Type:
        real
</pre>
Returns the current graze count.

## AddGraze
<pre>
    Arguments:
        1) real: graze
</pre>
Adds the given value to the graze count.

## GetPoint
<pre>
    Return Type:
        real
</pre>
Returns the current amount of point items collected.

## AddPoint
<pre>
    Arguments:
        1) real: point
</pre>
Adds the given value to the point count.

## SetItemRenderPriorityI
<pre>
    Arguments:
        1) real: renderPriorityI
</pre>
Sets the render priority for items, on a 0 to 100 scale.

Default is 60.

## SetShotRenderPriorityI
<pre>
    Arguments:
        1) real: renderPriorityI
</pre>
Sets the render priority for shots, on a 0 to 100 scale.

Default is 50.

## GetStgFrameRenderPriorityMinI
<pre>
    Return Type:
        real
</pre>
Returns the lowest render priority for the STG frame, on a 0 to 100 scale.

Default is 20.

## GetStgFrameRenderPriorityMaxI
<pre>
    Return Type:
        real
</pre>
Returns the highest render priority for the STG frame, on a 0 to 100 scale.

Default is 80.

## GetItemRenderPriorityI
<pre>
    Return Type:
        real
</pre>
Returns the render priority for items, on a 0 to 100 scale.

## GetShotRenderPriorityI
<pre>
    Return Type:
        real
</pre>
Returns the render priority for shots, on a 0 to 100 scale.

## GetPlayerRenderPriorityI
<pre>
    Return Type:
        real
</pre>
Returns the render priority for the player, on a 0 to 100 scale.

## GetCameraFocusPermitPriorityI
<pre>
    Return Type:
        real
</pre>
Returns the highest render priority the 2D camera can affect, on a 0 to 100 scale.

Default is 79.

## GetStgFrameLeft
<pre>
    Return Type:
        real
</pre>
Returns the leftmost coordinate of the STG frame (playing field).

Default is 32.

## GetStgFrameTop
<pre>
    Return Type:
        real
</pre>
Returns the topmost coordinate of the STG frame (playing field).

Default is 16.

## GetStgFrameWidth
<pre>
    Return Type:
        real
</pre>
Returns the width of the STG frame (playing field).

Default is 384.

## GetStgFrameHeight
<pre>
    Return Type:
        real
</pre>
Returns the height of the STG frame (playing field).

Default is 448.

## GetScreenWidth
<pre>
    Return Type:
        real
</pre>
Returns the width of the screen (resolution) as defined in the .def.

Default is 640.

## GetScreenHeight
<pre>
    Return Type:
        real
</pre>
Returns the height of the screen (resolution) as defined in the .def.

Default is 480.

## GetMaxScreenWidth
<pre>
    Return Type:
        real
</pre>
Returns the largest screen width defined in the .def.

If only one screen size is defined, this has the same effect as GetScreenWidth.

## GetMaxScreenHeight
<pre>
    Return Type:
        real
</pre>
Returns the largest screen height defined in the .def.

If only one screen size is defined, this has the same effect as GetScreenHeight.

## GetWindowWidth
<pre>
    Return Type:
        real
</pre>
Returns the current width of the window.

## GetWindowHeight
<pre>
    Return Type:
        real
</pre>
Returns the current height of the window.

## IsReplay
<pre>
    Return Type:
        bool
</pre>
Returns true if a replay is playing, otherwise returns false.

## AddArchiveFile
<pre>
    Return Type:
        bool
</pre>
Adds the path to use when reading images or sounds from an archive file.

Returns true if the archive was successfully read, otherwise returns false.

## IsSkipMode
<pre>
    Return Type:
        bool
</pre>
Returns true if the game is currently in skip (fast-forward) mode, otherwise returns false.

## GetDnhConfigValue
<pre>
    Arguments:
        1) real const: configType
        2) varies: ... (varargs args)
    Return Type:
        varies
</pre>
Returns a value from dnh's current config data based on the given [config type](./docs_config_types.html).

## SetDnhConfigValue
<pre>
    Arguments:
        1) real const: configType
        2) varies: ... (varargs args)
</pre>
Sets a value to dnh's current config data based on the given [config type](./docs_config_types.html).

*Note: This will persist for the rest of the session, but in order to be saved, [SaveDnhConfigFile](savednhconfigfile) must be called.*

## DnhConfig_GetWindowStyle
<pre>
    Return Type:
        real
</pre>
Returns the window style from DnhConfig.

(fullscreen, windowed)

## DnhConfig_GetWindowSizeIndex
<pre>
    Return Type:
        real
</pre>
Returns the window size index from DnhConfig.

This is an index into the window size list defined in rdnh.def.

## DnhConfig_GetFrameskipMode
<pre>
    Return Type:
        real
</pre>
Returns the frameskip mode from DnhConfig

(1/1, 1/2, 1/3, Automatic)

## DnhConfig_IsVsync
<pre>
    Return Type:
        bool
</pre>
Returns a boolean indicating whether or not vertical sync is enabled in DnhConfig.

## DnhConfig_IsBorderlessFullScreen
<pre>
    Return Type:
        bool
</pre>
Returns a boolean indicating whether or not borderless fullscreen mode is enabled in DnhConfig.

## DnhConfig_IsIntegerScale
<pre>
    Return Type:
        bool
</pre>
Returns a boolean indicating whether or not integer scaling for borderless fullscreen mode is enabled in DnhConfig.

*Note: In official Touhou this is known as "DOT by DOT" mode.*

## DnhConfig_GetPadIndex
<pre>
    Return Type:
        real
</pre>
Returns the currently set pad index, chosen from the list of pads displayed in config.exe.

## DnhConfig_GetVirtualKey
<pre>
    Arguments:
        1) real const: virtualKeyID
    Return Type:
        real array
</pre>
Returns an array of info about the given virtual key in DnhConfig.

[keyboardKey, padIndex, padButton]

## DnhConfig_IsLogWindow
<pre>
    Return Type:
        bool
</pre>
Returns a boolean indicating whether or not the LogWindow is enabled in DnhConfig.

## DnhConfig_IsLogFile
<pre>
    Return Type:
        bool
</pre>
Returns a boolean indicating whether or not logging to a file is enabled in DnhConfig.

## DnhConfig_IsMouseVisible
<pre>
    Return Type:
        bool
</pre>
Returns a boolean indicating whether or not mouse visibility is enabled in DnhConfig.

## DnhConfig_GetUserValue
<pre>
    Arguments:
        1) real const: valueIndex
    Return Type:
        bool
</pre>
Returns a user-defined real number value that was saved within DnhConfig at a given index.
8 user-defined indices (0-7) are available.

## DnhConfig_SetWindowStyle
<pre>
    Arguments:
        1) real const: style
</pre>
Sets the window style in DnhConfig.

(fullscreen, windowed)

## DnhConfig_SetWindowSizeIndex
<pre>
    Arguments:
        1) real: windowSizeIndex
</pre>
Sets the window size index in DnhConfig.

This is an index into the window size list defined in rdnh.def.

## DnhConfig_SetFrameskipMode
<pre>
    Arguments:
        1) real const: mode
</pre>
Sets the frameskip mode in DnhConfig.

## DnhConfig_SetVsync
<pre>
    Arguments:
        1) bool: enable
</pre>
Enables or disables vertical sync in DnhConfig.

## DnhConfig_SetBorderlessFullScreen
<pre>
    Arguments:
        1) bool: enable
</pre>
Enables or disables borderless fullscreen mode in DnhConfig.

## DnhConfig_SetIntegerScale
<pre>
    Arguments:
        1) bool: enable
</pre>
Enables or disables integer scaling for borderless fullscreen mode is enabled in DnhConfig.

*Note: In official Touhou this is known as "DOT by DOT" mode.*

## DnhConfig_SetPadIndex
<pre>
    Arguments:
        1) real: padIndex
</pre>
Sets the pad index, chosen from the list of pads displayed in config.exe.

## DnhConfig_SetVirtualKey
<pre>
    Arguments:
        1) real const: virtualKeyID
        2) real const: keyboardKey
        3) real: padIndex
        4) real: padButton
</pre>
Maps a virtual key to a keyboard key and/or pad button.

*Note: The pad button can be acquired from CheckPadState()*

## DnhConfig_SetLogWindow
<pre>
    Arguments:
        1) bool: enable
</pre>
Enables or disables the LogWindow in DnhConfig.

## DnhConfig_SetLogFile
<pre>
    Arguments:
        1) bool: enable
</pre>
Enables or disables logging to files in DnhConfig.

## DnhConfig_SetMouseVisible
<pre>
    Arguments:
        1) bool: enable
</pre>
Enables or disables mouse visibility in DnhConfig.

## DnhConfig_SetUserValue
<pre>
    Arguments:
        1) real: index
        2) real: value
</pre>
Sets a user-defined real number value that is saved within DnhConfig at a given index.
8 user-defined indices (0-7) are available.

## SaveDnhConfigFile
<pre>
    Return Type:
        bool
</pre>
Saves the current config data to the module directory and returns true if successful.

This file is named config.dat by default.

## DnhDef_GetPackageScriptPath
<pre>
    Return Type:
        string
</pre>
Returns the package script path defined in rdnh.def (PackageScriptMain)

## DnhDef_GetScreenSizes
<pre>
    Return Type:
        2D real array
</pre>
Returns an array of screen sizes defined in rdnh.def in the format: [[x, y], [x, y], [etc]]

This will be the screen size defined for each aspect ratio (Screen_4_3, Screen_16_9, etc)

## DnhDef_GetWindowSizes
<pre>
    Return Type:
        2D real array
</pre>
Returns the full array of window sizes defined in rdnh.def in the format: [[x, y], [x, y], [etc]]

## DnhDef_GetDefaultWindowSizeIndex
<pre>
    Return Type:
        real
</pre>
Returns the default window size index.

This is the index of the window size to start with by default when no config data exists.