# Input Functions

[Return to Functions](../functions.html)

## <a name="keystatelist"></a>Key State List
```
KEY_FREE: the key is not pressed.
KEY_PUSH: the key has been pressed.
KEY_HOLD: the key is being held.
KEY_PULL: the key has been released.
```

## <a name="virtualkeylist"></a>Virtual Key List
```
VK_LEFT     (ID: 0)  - Move left
VK_RIGHT    (ID: 1)  - Move right
VK_UP       (ID: 2)  - Move up
VK_DOWN     (ID: 3)  - Move down
VK_OK       (ID: 4)  - Confirm
VK_CANCEL   (ID: 5)  - Cancel
VK_SHOT     (ID: 6)  - Player Shot
VK_BOMB     (ID: 7)  - Player Spell/Bomb
VK_SPELL    (ID: 7)  - (Alias for VK_BOMB)
VK_SLOWMOVE (ID: 8)  - Focus
VK_USER1    (ID: 9)  - User Key 1
VK_USER2    (ID: 10) - User Key 2
VK_PAUSE    (ID: 11) - Pause

VK_USER_ID_STAGE to VK_USER_ID_STAGE + 255 (Stage script)
VK_USER_ID_PLAYER to VK_USER_ID_PLAYER + 255 (Player script)
```

## <a name="keylist"></a>Key List
```
KEY_0 ... KEY_9: 0-9 Keys
KEY_A ... KEY_Z: A-Z Keys
KEY_F1 ... KEY_F10: F1-F10 Keys
KEY_MINUS: -
KEY_EQUALS: =
KEY_SLASH: /
KEY_BACK: Backspace
KEY_TAB: Tab
KEY_SPACE: Space
KEY_LBRACKET: [
KEY_RBRACKET: ]
KEY_SEMICOLON: ;
KEY_APOSTROPHE: '
KEY_GRAVE: `
KEY_BACKSLASH: \ Note: Refers to the key on Western keyboards.
KEY_YEN: \ Note: Refers to the key on Japanese keyboards.
KEY_AT: @
KEY_COLON: :
KEY_UNDERLINE: _
KEY_CIRCUMFLEX: ^
KEY_COMMA: ,
KEY_PERIOD: .
KEY_INSERT: Insert
KEY_DELETE: Delete
KEY_RETURN: Enter
KEY_LCONTROL: Left Ctrl key
KEY_RCONTROL: Right Ctrl key
KEY_LSHIFT: Left Shift
KEY_RSHIFT: Right Shift
KEY_LEFT: Left Arrow Key
KEY_RIGHT: Right Arrow Key
KEY_UP: Up Arrow Key
KEY_DOWN: Down Arrow Key
KEY_NUMPAD0 ... KEY_NUMPAD9: 0-9 on the Number Pad
KEY_ADD: Number Pad +
KEY_SUBTRACT: Number Pad -
KEY_MULTIPLY: Number Pad *
KEY_DIVIDE: Number Pad /
KEY_DECIMAL: Number Pad .
KEY_NUMPADEQUALS: Number Pad =
KEY_ESCAPE: Escape
```

## GetVirtualKeyState
```
    Arguments:
        1) real const: virtualKey
    Return Type:
        real const
```
Returns the [state](#keystatelist) of the specified [virtual key](#virtualkeylist).

## SetVirtualKeyState
```
    Arguments:
        1) real const: virtualKey
        2) real const: keyState
```
Sets the given [virtual key](#virtualkeylist) to the given [state](#keystatelist).

The virtual key will be restored to its true state a frame after you stop calling this function.\
Keep in mind that if you set it to KEY_HOLD it will not go to KEY_PULL or KEY_PUSH.

## AddVirtualKey
```
    Arguments:
        1) real const: virtualKey
        2) real const: key
        3) real const: padKey
```
Registers the given [virtual key](#virtualkeylist) with the given [key](#keylist).

On top of the existing virtual keys, there are also special ranges of values that can be passed as the virtualKey argument to define new custom keys:\
Stage: VK_USER_ID_STAGE to VK_USER_ID_STAGE + 255\
Player: VK_USER_ID_PLAYER to VK_USER_ID_PLAYER + 255

You may map any number of virtual keys to a single key, but virtual keys may only be mapped to a single key.\
Use KEY_INVALID if you do not want pad input.\
Example: If you were to use `AddVirtualKey(VK_SHOT, KEY_UP, KEY_INVALID);`, whenever you press the up arrow key, the virtual shot key will be pressed.\
However, you will not be able to move up. To fix this, you add `AddVirtualKey(VK_UP, KEY_UP, KEY_INVALID);`. You will now shoot and move up at the same time.

## AddReplayTargetVirtualKey
```
    Arguments:
        1) real const: virtualKey
```
Registers the given [virtual key](#virtualkeylist) id to the replay file.

This key id should be one that you have already registered with [AddVirtualKey](#addvirtualkey).

## CheckPadState
```
    Return Type:
        real
```
Checks if any buttons on the pad at the given padIndex are pressed and returns the pressed button ID.

*Note: Returns KEY_INVALID if no buttons are pressed or a number between 0 and 16 if one is pressed.*

## GetPadStateAll
```
    Arguments:
        1) real: padIndex
        2) array[real]: resArr
    Return Type:
        bool
```
Stores all the key states for the given bad the provided array.

If it fails for some reason (like because a pad with that index doesn't exist), it will return false, otherwise it returns true.

## GetPadDeviceCount
```
    Return Type:
        real
```
Returns the number of connected pad devices.

## GetPadType
```
    Arguments:
        1) real: padIndex
    Return Type:
        real const
```
Gets the type of pad at the given padIndex.

As it's possible for detection to fail, it's not recommended to rely entirely on this function. If you display button names in-game, it's recommended to allow the player to select which set of buttons to display.

Types:
```
PAD_TYPE_UNKNOWN
PAD_TYPE_STANDARD
PAD_TYPE_XBOX360
PAD_TYPE_XBOXONE
PAD_TYPE_PS3
PAD_TYPE_PS4
PAD_TYPE_PS5
PAD_TYPE_NINTENDO_SWITCH_PRO (unsupported)
PAD_TYPE_NINTENDO_SWITCH_JOYCON_LEFT (unsupported)
PAD_TYPE_NINTENDO_SWITCH_JOYCON_RIGHT (unsupported)
PAD_TYPE_NINTENDO_SWITCH_JOYCON_PAIR (unsupported)
```

## GetPadDeviceInfo
```
    Arguments:
        1) real: padIndex
    Return Type:
        string array
```
Returns info about the pad device at the given padIndex

Info is returned as an array of strings: [instanceName, productName]

## GetPadDeviceName
```
    Arguments:
        1) real: padIndex
    Returns:
        string
```
Returns the name of the pad device at the given padIndex.

## GetKeyboardKeyName
```
    Arguments:
        1) real const: key
    Returns:
        string
```
Returns the name associated with the given key depending on the currently set layout.

To keep this up-to-date, store the result of GetKeyboardLayout() and check if successive calls to it change. If they do, call UpdateKeyboardKeyNames()

## GetKeyboardKeyNameIndex
```
    Arguments:
        1) real const: key
    Returns:
        real
```
Returns the index of the given key's name in the name array. This is identical to its Windows virtual key code, which is keyboard layout independent.

## UpdateKeyboardKeyNames
Updates the keyboard key name array based on the user's current keyboard layout at the point this function is called.

## GetKeyboardLayout
```
    Returns:
        real
```
Gets a unique ID to the user's current keyboard layout. Only useful for checking if the layout has changed since the previous frame.

## GetKeyState
```
    Arguments:
        1) real const: key
    Return Type:
        real const
```
Returns the [state](#keystatelist) of the specified [key](#keylist).

## GetMouseState
```
    Arguments:
        1) real const: mouseButton
    Return Type:
        real const
```
Returns the given mouse button's current [state](#keystatelist).

mouseButton can be: `MOUSE_LEFT`, `MOUSE_RIGHT`, or `MOUSE_MIDDLE`

## GetMouseX
```
    Return Type:
        real
```
Returns the mouse's x position.

The origin for the mouse coordinates is the upper left of the Danmakufu window (0, 0).\
Mouse coordinates will be properly adjusted according to the resizing of the window.

## GetMouseY
```
    Return Type:
        real
```
Returns the mouse's y position.

The origin for the mouse coordinates is the upper left of the Danmakufu window (0, 0).\
Mouse coordinates will be properly adjusted according to the resizing of the window.

## GetMouseMoveZ
```
    Return Type:
        real
```
Returns the amount of change that has occurred to the mouse's Z axis.

The Z axis is normally the middle mouse wheel. If there is no mouse wheel, the value will be 0.\
The value returned will be negative if the wheel was moved back, and positive if the wheel moved forward.

## IsKeyFree
```
    Arguments:
        1) real const: key
    Return Type:
        real const
```
Returns true if the given key's state is KEY_FREE, otherwise returns false.

## IsKeyPushed
```
    Arguments:
        1) real const: key
    Return Type:
        real const
```
Returns true if the given key's state is KEY_PUSH, otherwise returns false.

## IsKeyPulled
```
    Arguments:
        1) real const: key
    Return Type:
        real const
```
Returns true if the given key's state is KEY_PULL, otherwise returns false.

## IsKeyHeld
```
    Arguments:
        1) real const: key
    Return Type:
        real const
```
Returns true if the given key's state is KEY_HOLD, otherwise returns false.

## IsKeyDown
```
    Arguments:
        1) real const: key
    Return Type:
        real const
```
Returns true if the given key's state is KEY_PUSH or KEY_HOLD, otherwise returns false.

## IsKeyUp
```
    Arguments:
        1) real const: key
    Return Type:
        real const
```
Returns true if the given key's state is KEY_FREE or KEY_PULL, otherwise returns false.

## IsAnyKeyFree
```
    Arguments:
        1+) real const: keys...
    Return Type:
        real const
```
Returns true if the any of the given keys' states are KEY_FREE, otherwise returns false.

## IsAnyKeyPushed
```
    Arguments:
        1+) real const: keys...
    Return Type:
        real const
```
Returns true if the any of the given keys' states are KEY_PUSH, otherwise returns false.

## IsAnyKeyPulled
```
    Arguments:
        1+) real const: keys...
    Return Type:
        real const
```
Returns true if the any of the given keys' states are KEY_PULL, otherwise returns false.

## IsAnyKeyHeld
```
    Arguments:
        1+) real const: keys...
    Return Type:
        real const
```
Returns true if the any of the given keys' states are KEY_HOLD, otherwise returns false.

## IsAnyKeyDown
```
    Arguments:
        1+) real const: keys...
    Return Type:
        real const
```
Returns true if the any of the given keys' states are KEY_PUSH or KEY_HOLD, otherwise returns false.

## IsAnyKeyUp
```
    Arguments:
        1+) real const: keys...
    Return Type:
        real const
```
Returns true if the any of the given keys' states are KEY_FREE or KEY_PULL, otherwise returns false.

## IsVirtualKeyFree
```
    Arguments:
        1) real const: virtualKey
    Return Type:
        real const
```
Returns true if the given virtual key's state is KEY_FREE, otherwise returns false.

## IsVirtualKeyPushed
```
    Arguments:
        1) real const: virtualKey
    Return Type:
        real const
```
Returns true if the given virtual key's state is KEY_PUSH, otherwise returns false.

## IsVirtualKeyPulled
```
    Arguments:
        1) real const: virtualKey
    Return Type:
        real const
```
Returns true if the given virtual key's state is KEY_PULL, otherwise returns false.

## IsVirtualKeyHeld
```
    Arguments:
        1) real const: virtualKey
    Return Type:
        real const
```
Returns true if the given virtual key's state is KEY_HOLD, otherwise returns false.

## IsVirtualKeyDown
```
    Arguments:
        1) real const: virtualKey
    Return Type:
        real const
```
Returns true if the given virtual key's state is KEY_PUSH or KEY_HOLD, otherwise returns false.

## IsVirtualKeyUp
```
    Arguments:
        1) real const: virtualKey
    Return Type:
        real const
```
Returns true if the given virtual key's state is KEY_FREE or KEY_PULL, otherwise returns false.

## IsAnyVirtualKeyFree
```
    Arguments:
        1+) real const: virtualKeys...
    Return Type:
        real const
```
Returns true if the any of the given virtual keys' states are KEY_FREE, otherwise returns false.

## IsAnyVirtualKeyPushed
```
    Arguments:
        1+) real const: virtualKeys...
    Return Type:
        real const
```
Returns true if the any of the given virtual keys' states are KEY_PUSH, otherwise returns false.

## IsAnyVirtualKeyPulled
```
    Arguments:
        1+) real const: virtualKeys...
    Return Type:
        real const
```
Returns true if the any of the given virtual keys' states are KEY_PULL, otherwise returns false.

## IsAnyVirtualKeyHeld
```
    Arguments:
        1+) real const: virtualKeys...
    Return Type:
        real const
```
Returns true if the any of the given virtual keys' states are KEY_HOLD, otherwise returns false.

## IsAnyVirtualKeyDown
```
    Arguments:
        1+) real const: virtualKeys...
    Return Type:
        real const
```
Returns true if the any of the given virtual keys' states are KEY_PUSH or KEY_HOLD, otherwise returns false.

## IsAnyVirtualKeyUp
```
    Arguments:
        1+) real const: virtualKeys...
    Return Type:
        real const
```
Returns true if the any of the given virtual keys' states are KEY_FREE or KEY_PULL, otherwise returns false.

## SetClipboardText
```
    Arguments:
        1) string: text
```
Sets the system clipboard text to the given string.

## GetClipboardText
```
    Return Type:
        string
```
Returns the contents of the system clipboard as a string.

If the contents of the clipboard cannot be encoded as a string, this returns an empty string.

## SetSkipModeKey
```
    Arguments:
        1) real const: key
```
Specifies the key to use for fast playback mode.

The default key is KEY_LCONTROL.\
Specify KEY_INVALID if you do not wish to enable fast playback.

## SetDebugStageRetryKey
```
    Arguments:
        1) real const: key
```
Specifies the key to use for restarting stage scripts that were started from the RDNH menu.

The default key is KEY_BACK.\
Specify KEY_INVALID to disable this feature.