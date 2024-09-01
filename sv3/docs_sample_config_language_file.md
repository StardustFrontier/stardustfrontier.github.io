# Sample RDnh Config Language File

[Return to Functions](./docs.html)

#
Below is a sample of a language definition file for config.exe, with some comments provided.

<pre>
language = English

// window title
title = Re:Dnh Configuration Utility (English)

// tab names
title.graphics = Graphics
title.key      = Key
title.option   = Option

// graphics tab
graphics.windowstyle            = Window Style
graphics.windowstyle.fullscreen = Fullscreen
graphics.windowstyle.window     = Window

graphics.windowsize = Window Size

graphics.frameskip             = Frameskip
graphics.frameskip.full        = 1/1 (Recommended)
graphics.frameskip.half        = 1/2
graphics.frameskip.third       = 1/3
graphics.frameskip.auto        = Automatic

graphics.misc              = Miscellaneous
graphics.misc.vsync        = Enable vertical sync
graphics.misc.borderless   = Enable borderless windowed fullscreen
graphics.misc.integerscale = Use integer scale values in fullscreen mode (DOT by DOT)

// input tab
input.paddevice     = Pad Device
input.list.action   = Action
input.list.keyboard = Keyboard

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

// option tab
option.list.option               = Option
option.list.option.showlogwindow = Show LogWindow
option.list.option.savelogfile   = Save Log file
option.list.option.hidemouse     = Hide mouse cursor
</pre>