# Text Object Functions

[Return to Functions](./docs.html)

## ObjText_Create
<pre>
    Return Type:
        real
</pre>
Creates a text object and returns its ID.

## ObjText_SetText
<pre>
    Arguments:
        1) real: objectID
        2) string: text
</pre>
Gives the text object some text to display.

## ObjText_SetFontType
<pre>
    Arguments:
        1) real: objectID
        2) string: fontName
</pre>
Sets the specified font to the text object.

## ObjText_SetFontSize
<pre>
    Arguments:
        1) real: objectID
        2) real: size
</pre>
Sets the size of the font for the text object.

## ObjText_SetFontBold
<pre>
    Arguments:
        1) real: objectID
        2) bool: bBold
</pre>
If set to true, the text will be displayed in bold characters.

## ObjText_SetFontColorTop
<pre>
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
</pre>
Sets the top color of the text (0-255).

## ObjText_SetFontColorBottom
<pre>
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
</pre>
Sets the bottom color of the text (0-255).

## ObjText_SetFontBorderWidth
<pre>
    Arguments:
        1) real: objectID
        2) real: borderWidth
</pre>
Sets the width of the font border.

## ObjText_SetFontBorderType
<pre>
    Arguments:
        1) real: objectID
        2) real: borderWidth
</pre>
Sets the type of the font border.

Border types are:
<pre>
BORDER_NONE (no border)
BORDER_FULL (full border)
BORDER_SHADOW (shadow at the bottom right of the text)
</pre>

## ObjText_SetFontBorderColor
<pre>
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
</pre>
Sets the color of the border (0-255).

## ObjText_SetMaxWidth
<pre>
    Arguments:
        1) real: objectID
        2) real: width
</pre>
Sets the maximum width of the text object.

The text will automatically create a new line whenever needed.

## ObjText_SetMaxHeight
<pre>
    Arguments:
        1) real: objectID
        2) real: height
</pre>
Sets the maximum height of the text object.

Any part of the text exceeding this height will not be drawn.

## ObjText_SetLinePitch
<pre>
    Arguments:
        1) real: objectID
        2) real: pitch
</pre>
Sets the line pitch (space between lines) of the text object.

## ObjText_SetSidePitch
<pre>
    Arguments:
        1) real: objectID
        2) real: pitch
</pre>
Sets the side pitch (space between characters) of the text object.

## ObjText_SetTransCenter
<pre>
    Arguments:
        1) real: objectID
        2) real: centerX
        3) real: centerY
</pre>
Sets the given coordinates of the text object as its transformation center (rotation, zoom...).

*Note: ObjText_SetAutoTransCenter must first be set to false for this function to work.*

## ObjText_SetAutoTransCenter
<pre>
    Arguments:
        1) real: objectID
        2) bool: bTransCenter
</pre>
When true, sets the center of the text object as its transformation center.

Defaults to true.

## ObjText_SetHorizontalAlignment
<pre>
    Arguments:
        1) real: objectID
        2) real const: alignmentType
</pre>
Sets the alignment of the text.

Defaults to ALIGNMENT_LEFT.
Alignment types are:
<pre>
ALIGNMENT_LEFT
ALIGNMENT_CENTER
ALIGNMENT_RIGHT
</pre>
To use center or right aligned text, you have to set the maximum width using ObjText_SetMaxWidth (in order to know where the right border is).

## ObjText_SetSyntacticAnalysis
<pre>
    Arguments:
        1) real: objectID
        2) bool: bSyntacticAnalysis
</pre>
Allows or prevents checking for the existence of bracket tags (such as line break or ruby text) within the text for this object.

## ObjText_GetTextLength
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the length of the specified text object.

When using Japanese characters, a half-width character counts as 1 and a full-width character counts as 2 characters.

## ObjText_GetTextLengthCU
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the length of the specified text object.

Newlines and ruby text are not counted. When using Japanese characters, both half-width and full-width characters count as 1 character.

## ObjText_GetTextLengthCUL
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real array
</pre>
Returns an array of the lengths of each line of the specified text object.

Newlines and ruby text are not counted.\
When using Japanese characters, both half-width and full-width characters count as 1 character.

## ObjText_GetTotalWidth
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the overall width of all lines of the text object.

***Warning**: Known to give an inaccurate figure under certain circumstances*

## ObjText_GetTotalHeight
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the combined height of all lines of the text object.

This function's behavior appears to depend only on the number of newlines, as opposed to the number of lines actually displayed with word wrapping taken into account.