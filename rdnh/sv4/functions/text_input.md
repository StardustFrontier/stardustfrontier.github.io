# Text Input Functions

[Return to Functions](../functions.html)

## TextInput_Begin
Begins internal processing of text input.\
This will fill the text buffer which can be retrieved and/or cleared with [TextInput_GetBuffer](#textinput_getbuffer).

*Note: The internal text buffer will continue to be filled with characters every time a key is pressed until [TextInput_End](#textinput_end) is called.*

## TextInput_End
Ends internal processing of text input and clears the text buffer.

## TextInput_IsActive
<pre>
    Return Type:
        real
</pre>
Returns true if text input processing is active, otherwise returns false.

## TextInput_GetBuffer
<pre>
    Arguments:
        1) bool: bClear
    Return Type:
        string
</pre>
Returns a string with a copy of the text buffer.\
If bClear is true, the buffer will be cleared.

## TextInput_SetImePosition
<pre>
    Arguments:
        1) real: x
        2) real: y
</pre>
Sets the position of the Windows IME box

*Note: No consistency is guaranteed with this function as it relies entirely on Windows functions.*

## TextInput_GetImePositionX
<pre>
    Return Type:
        real
</pre>
Gets the x position of the Windows IME box

*Note: No consistency is guaranteed with this function as it relies entirely on Windows functions.*

## TextInput_GetImePositionY
<pre>
    Return Type:
        real
</pre>
Gets the y position of the Windows IME box

*Note: No consistency is guaranteed with this function as it relies entirely on Windows functions.*