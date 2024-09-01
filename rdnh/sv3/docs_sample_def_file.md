# Sample RDnh Definition File

[Return to Functions](./docs.html)

#
Below is a sample rdnh.def file, with comments provided.

<pre>
// The package script to automatically start when opening the game executable.
PackageScriptMain = script/mystic_square/main.dnh

// The title for the game's window.
WindowTitle = Really Cool Mystic Square Remake Lol It's Happening I Swear

// The game's executable file.
// This sets the file to launch from config.exe when pressing "Start Game".
GameFile = rednh.exe

// The window title for the config.exe.
ConfigWindowTitle = TH05 Configuration Utility

// The name of the file for configuration to be saved and loaded from.
// This applies to config.exe as well as all rdnh functions that work with config (such as GetDnhConfigValue).
ConfigDataFile = rdnh.cfg

// The size of the drawing screen, all window scales will be applied to this
ScreenWidth = 640
ScreenHeight = 480

// Multiplier for window size scaling
// This also affects the window sizes displayed in config.exe
WindowScale0 = 1.0
WindowScale1 = 1.25
WindowScale2 = 1.5
WindowScale3 = 2.0
// Set this to whatever index 1.0 scale is
WindowBaseScale = 0

// Multiplier applied when the fast forward key is pressed
FastForwardSpeed = 8

// Make the game run when the window isn't in focus.
// Input will not be processed while out of focus.
RunUnfocused = 1
</pre>