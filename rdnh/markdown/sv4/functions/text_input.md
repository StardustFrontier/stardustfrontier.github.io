# Text Input Functions

[Return to Functions](../functions.html)

## TextInput_Begin
Begins internal processing of text input.\
This will fill the text buffer which can be retrieved and/or cleared with [TextInput_GetBuffer](#textinput_getbuffer).

*Note: The internal text buffer will continue to be filled with characters every time a key is pressed until [TextInput_End](#textinput_end) is called.*

## TextInput_End
Ends internal processing of text input and clears the text buffer.

## TextInput_IsActive
```
    Return Type:
        real
```
Returns true if text input processing is active, otherwise returns false.

## TextInput_GetBuffer
```
    Arguments:
        1) bool: bClear
    Return Type:
        string
```
Returns a string with a copy of the text buffer.\
If bClear is true, the buffer will be cleared.

## TextInput_SetImePosition
```
    Arguments:
        1) real: x
        2) real: y
```
Sets the position of the Windows IME box

*Note: No consistency is guaranteed with this function as it relies entirely on Windows functions.*

## TextInput_GetImePositionX
```
    Return Type:
        real
```
Gets the x position of the Windows IME box

*Note: No consistency is guaranteed with this function as it relies entirely on Windows functions.*

## TextInput_GetImePositionY
```
    Return Type:
        real
```
Gets the y position of the Windows IME box

*Note: No consistency is guaranteed with this function as it relies entirely on Windows functions.*