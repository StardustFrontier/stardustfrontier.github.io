# Sample Definition File

[Return to Index](../docs.html)

#
Below is a sample rdnh.def file, with comments provided.

<pre>
// the path to a package script to automatically run on launch
PackageScriptMain = script/THUotAR/Main.dnh

// the path to save replays to, relative to the module directory
// all instances of %s will be replaced with the script name
// comment this out to use the default save path
//ReplayPath = replay/%s

// title of the game window
WindowTitle = Unification of the Artful Rain

// the game executable file, used for Start Game in config.exe
GameFile = rdnh.exe

// window title for the config.exe
ConfigWindowTitle = THUotAR Configuration Utility

// name of the file to save config data to
ConfigDataFile = config.dat

// a map of paths to config.exe translations, relative to config.exe's directory
// {languageID:path}
ConfigLanguagePaths = {0:lang/config/en.def, 1:lang/config/jp.def, 2:lang/config/fr.def}

// keyboard keys to use as defaults for VK_USER1 and VK_USER2
// valid keys are:
// Z, X, C, V, W, A, S, D, LCONTROL, LSHIFT, ESCAPE, BACKSPACE, LEFT, RIGHT, UP, DOWN, RETURN, DELETE
//UserKeyDefaults = {LCONTROL, S}

// screen resolution for each aspect ratio
// can have all of Screen_4_3, Screen_16_9, Screen_16_10, and Screen_Other
// if multiple are defined, it is possible to switch between them at runtime.
Screen_4_3  = 640x480

// list of all window sizes
// this will be automatically matched with the screen resolution for its ratio
WindowSizes = {640x480, 800x600, 1024x768, 1280x960}

// index of the window size to start with by default when no config data exists
WindowSizeIndexDefault = 0

// multiplier applied when the fast forward key is pressed
FastForwardSpeed = 8

// if non-zero, the game will run when the window isn't in focus
// input will not be processed while out of focus.
RunUnfocused = 1

// limits the fps to a specific value
FpsLimit = 60

// if non-zero, enables the dark theme for the Log tab of the Log Window
LogWindowDarkTheme = 1
</pre>