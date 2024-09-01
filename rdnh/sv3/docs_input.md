# Input Functions

[Return to Functions](./docs.html)

## <a name="keystatelist"></a>Key State List
<pre>
KEY_FREE: the key is not pressed.
KEY_PUSH: the key has been pressed.
KEY_HOLD: the key is being held.
KEY_PULL: the key has been released.
</pre>

## <a name="virtualkeylist"></a>Virtual Key List
<pre>
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
</pre>

## <a name="keylist"></a>Key List
<pre>
KEY_0 ... KEY_9： 0-9 Keys
KEY_A ... KEY_Z： A-Z Keys
KEY_F1 ... KEY_F10： F1-F10 Keys
KEY_MINUS： -
KEY_EQUALS： =
KEY_SLASH： /
KEY_BACK： Backspace
KEY_TAB： Tab
KEY_SPACE： Space
KEY_LBRACKET： [
KEY_RBRACKET： ]
KEY_SEMICOLON： ;
KEY_APOSTROPHE： '
KEY_GRAVE： `
KEY_BACKSLASH： \ Note: Refers to the key on Western keyboards.
KEY_YEN： \ Note: Refers to the key on Japanese keyboards.
KEY_AT： @
KEY_COLON： :
KEY_UNDERLINE： _
KEY_CIRCUMFLEX： ^
KEY_COMMA： ,
KEY_PERIOD： .
KEY_INSERT： Insert
KEY_DELETE： Delete
KEY_RETURN： Enter
KEY_LCONTROL： Left Ctrl key
KEY_RCONTROL： Right Ctrl key
KEY_LSHIFT： Left Shift
KEY_RSHIFT： Right Shift
KEY_LEFT： Left Arrow Key
KEY_RIGHT： Right Arrow Key
KEY_UP： Up Arrow Key
KEY_DOWN： Down Arrow Key
KEY_NUMPAD0 ... KEY_NUMPAD9： 0-9 on the Number Pad
KEY_ADD： Number Pad +
KEY_SUBTRACT： Number Pad -
KEY_MULTIPLY： Number Pad *
KEY_DIVIDE： Number Pad /
KEY_DECIMAL： Number Pad .
KEY_NUMPADEQUALS： Number Pad =
KEY_ESCAPE: Escape
</pre>

## GetVirtualKeyState
<pre>
    Arguments:
        1) real const: virtualKey
    Return Type:
        real const
</pre>
Returns the [state](#keystatelist) of the specified [virtual key](#virtualkeylist).

## SetVirtualKeyState
<pre>
    Arguments:
        1) real const: virtualKey
        2) real const: keyState
</pre>
Sets the given [virtual key](#virtualkeylist) to the given [state](#keystatelist).

The virtual key will be restored to its true state a frame after you stop calling this function.\
Keep in mind that if you set it to KEY_HOLD it will not go to KEY_PULL or KEY_PUSH.

## AddVirtualKey
<pre>
    Arguments:
        1) real const: virtualKey
        2) real const: key
        3) real const: padKey
</pre>
Registers the given [virtual key](#virtualkeylist) with the given [key](#keylist).

You may map any number of virtual keys to a single key, but virtual keys may only be mapped to a single key.\
Use KEY_INVALID if you do not want pad input.\
Example: If you were to use `AddVirtualKey(VK_SHOT, KEY_UP, KEY_INVALID);`, whenever you press the up arrow key, the virtual shot key will be pressed.\
However, you will not be able to move up. To fix this, you add `AddVirtualKey(VK_UP, KEY_UP, KEY_INVALID);`. You will now shoot and move up at the same time.

## AddReplayTargetVirtualKey
<pre>
    Arguments:
        1) real const: virtualKey
</pre>
Registers the given [virtual key](#virtualkeylist) id to the replay file.

This key id should be one that you have already registered with [AddVirtualKey](addvirtualkey).

## CheckPadState
<pre>
    Return Type:
        real
</pre>
Checks if any buttons on the pad at the given padIndex are pressed and returns the pressed button ID.

*Note: Returns KEY_INVALID if no buttons are pressed or a number between 0 and 16 if one is pressed.*

## GetPadDeviceCount
<pre>
    Return Type:
        real
</pre>
Returns the number of connected pad devices.

## GetPadDeviceInfo
<pre>
    Arguments:
        1) real: padIndex
    Return Type:
        string array
</pre>
Returns info about the pad device at the given padIndex

Info is returned as an array of strings: [instanceName, productName]

## GetKeyState
<pre>
    Arguments:
        1) real const: key
    Return Type:
        real const
</pre>
Returns the [state](#keystatelist) of the specified [key](#keylist).

## GetMouseState
<pre>
    Arguments:
        1) real const: mouseButton
    Return Type:
        real const
</pre>
Returns the given mouse button's current [state](#keystatelist).

mouseButton can be: `MOUSE_LEFT`, `MOUSE_RIGHT`, or `MOUSE_MIDDLE`

## GetMouseX
<pre>
    Return Type:
        real
</pre>
Returns the mouse's x position.

The origin for the mouse coordinates is the upper left of the Danmakufu window (0, 0).\
Mouse coordinates will be properly adjusted according to the resizing of the window.

## GetMouseY
<pre>
    Return Type:
        real
</pre>
Returns the mouse's y position.

The origin for the mouse coordinates is the upper left of the Danmakufu window (0, 0).\
Mouse coordinates will be properly adjusted according to the resizing of the window.

## GetMouseMoveZ
<pre>
    Return Type:
        real
</pre>
Returns the amount of change that has occurred to the mouse's Z axis.

The Z axis is normally the middle mouse wheel. If there is no mouse wheel, the value will be 0.\
The value returned will be negative if the wheel was moved back, and positive if the wheel moved forward.

## SetSkipModeKey
<pre>
    Arguments:
        1) real const: key
</pre>
Specifies the key to use for fast playback mode.

The default key is KEY_LCONTROL.\
Specify KEY_INVALID if you do not wish to enable fast playback.