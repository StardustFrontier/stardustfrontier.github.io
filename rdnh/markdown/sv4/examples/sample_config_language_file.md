# Sample Config Language File

[Return to Index](../docs.html)

#
Below is a sample of a language definition file for config.exe, with some comments provided.

```
language = English

// Window title
title = Re:Dnh Configuration Utility (English)

// Tab names
title.general  = General
title.input    = Input

// Main Button Names
main.button.cancel = Cancel
main.button.saveandclose = Save && Close
main.button.saveandlaunch = Save && Launch

// ----------------------------------------------------------------------------
// General Tab
// ----------------------------------------------------------------------------

// Group Names
general.display  = Display
general.graphics = Graphics
general.option   = Option

// Display Group
general.display.screenmode            = Screen Mode
general.display.screenmode.fullscreen = Fullscreen
general.display.screenmode.window     = Windowed

general.display.windowsize = Window Size

general.display.vsync        = Enable vertical sync
general.display.borderless   = Enable borderless windowed fullscreen
general.display.integerscale = Use integer scaling for borderless window (DOT by DOT)

// Graphics Group
general.graphics.frameskip             = Frameskip
general.graphics.frameskip.full        = None (Recommended)
general.graphics.frameskip.half        = 1/2
general.graphics.frameskip.third       = 1/3
general.graphics.frameskip.auto        = Automatic

general.graphics.antialiasing          = Anti-aliasing
general.graphics.antialiasing.none     = None

// Option Group
general.option.showlogwindow = Show log window
general.option.savelogfile   = Save log file
general.option.hidemouse     = Hide mouse cursor

// ----------------------------------------------------------------------------
// Input Tab
// ----------------------------------------------------------------------------

input.paddevice      = Gamepad Device
input.button.refresh = Refresh Devices
input.paddeadzone    = Joystick Deadzone
input.list.action    = Action
input.list.keyboard  = Keyboard
input.list.pad       = Pad

// Action Names
input.list.action.left   = Left
input.list.action.right  = Right
input.list.action.up     = Up
input.list.action.down   = Down
input.list.action.accept = Accept
input.list.action.cancel = Cancel
input.list.action.shot   = Shot
input.list.action.bomb   = Bomb
input.list.action.slow   = Slow
input.list.action.user1  = User1
input.list.action.user2  = User2
input.list.action.pause  = Pause
```