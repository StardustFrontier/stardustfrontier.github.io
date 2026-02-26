# ObjText Functions

[Return to Functions](../functions.html)

## ObjText_Create
```
    Return Type:
        real
```
Creates a text object and returns its ID.

## ObjText_SetText
```
    Arguments:
        1) real: objectID
        2) string: text
```
Gives the text object some text to display.

## ObjText_SetFontType
```
    Arguments:
        1) real: objectID
        2) string: fontName
```
Sets the specified font to the text object.

## ObjText_SetFontSize
```
    Arguments:
        1) real: objectID
        2) real: size
```
Sets the size of the font for the text object.

## ObjText_SetFontBold
```
    Arguments:
        1) real: objectID
        2) bool: bBold
```
If set to true, the text will be displayed in bold characters.

## ObjText_SetFontColorTop
```
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
```
Sets the top color of the text (0-255).

## ObjText_SetFontColorBottom
```
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
```
Sets the bottom color of the text (0-255).

## ObjText_SetFontBorderWidth
```
    Arguments:
        1) real: objectID
        2) real: borderWidth
```
Sets the width of the font border.

## ObjText_SetFontBorderType
```
    Arguments:
        1) real: objectID
        2) real: borderWidth
```
Sets the type of the font border.

Border types are:
```
BORDER_NONE (no border)
BORDER_FULL (full border)
BORDER_SHADOW (shadow at the bottom right of the text)
```

## ObjText_SetFontBorderColor
```
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
```
Sets the color of the border (0-255).

## ObjText_SetMaxWidth
```
    Arguments:
        1) real: objectID
        2) real: width
```
Sets the maximum width of the text object.

The text will automatically create a new line whenever needed.

## ObjText_SetMaxHeight
```
    Arguments:
        1) real: objectID
        2) real: height
```
Sets the maximum height of the text object.

Any part of the text exceeding this height will not be drawn.

## ObjText_SetLinePitch
```
    Arguments:
        1) real: objectID
        2) real: pitch
```
Sets the line pitch (space between lines) of the text object.

## ObjText_SetSidePitch
```
    Arguments:
        1) real: objectID
        2) real: pitch
```
Sets the side pitch (space between characters) of the text object.

## ObjText_SetTransCenter
```
    Arguments:
        1) real: objectID
        2) real: centerX
        3) real: centerY
```
Sets the given coordinates of the text object as its transformation center (rotation, zoom...).

*Note: ObjText_SetAutoTransCenter must first be set to false for this function to work.*

## ObjText_SetAutoTransCenter
```
    Arguments:
        1) real: objectID
        2) bool: bTransCenter
```
When true, sets the center of the text object as its transformation center.

Defaults to true.

## ObjText_SetHorizontalAlignment
```
    Arguments:
        1) real: objectID
        2) real const: alignmentType
```
Sets the alignment of the text.

Defaults to ALIGNMENT_LEFT.
Alignment types are:
```
ALIGNMENT_LEFT
ALIGNMENT_CENTER
ALIGNMENT_RIGHT
```
To use center or right aligned text, you have to set the maximum width using ObjText_SetMaxWidth (in order to know where the right border is).

## ObjText_SetSyntacticAnalysis
```
    Arguments:
        1) real: objectID
        2) bool: bSyntacticAnalysis
```
Allows or prevents checking for the existence of bracket tags (such as line break or ruby text) within the text for this object.

## ObjText_GetTextLength
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the length of the specified text object.

When using Japanese characters, a half-width character counts as 1 and a full-width character counts as 2 characters.

## ObjText_GetTextLengthCU
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the length of the specified text object.

Newlines and ruby text are not counted. When using Japanese characters, both half-width and full-width characters count as 1 character.

## ObjText_GetTextLengthCUL
```
    Arguments:
        1) real: objectID
    Return Type:
        real array
```
Returns an array of the lengths of each line of the specified text object.

Newlines and ruby text are not counted.\
When using Japanese characters, both half-width and full-width characters count as 1 character.

## ObjText_GetTotalWidth
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the overall width of all lines of the text object.

***Warning**: Known to give an inaccurate figure under certain circumstances*

## ObjText_GetTotalHeight
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the combined height of all lines of the text object.

This function's behavior appears to depend only on the number of newlines, as opposed to the number of lines actually displayed with word wrapping taken into account.