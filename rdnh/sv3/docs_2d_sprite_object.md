# 2D Sprite Object Functions

[Return to Functions](./docs.html)

## ObjSprite2D_SetSourceRect
<pre>
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
</pre>
Sets the texture rectangle for the sprite.

This is the rectangle on the original texture from which the sprite will be drawn.

## ObjSprite2D_SetSourceRectB
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: width
        5) real: height
</pre>
Sets the texture rectangle for the sprite, using x, y, width, and height.

This is the rectangle on the original texture from which the sprite will be drawn.

## ObjSprite2D_SetDest
<pre>
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
</pre>
Sets the drawing rectangle for the sprite based on a pre-defined constant.

This is the rectangle where the sprite will be drawn.\
Destination constants are in the form `DESTINATION_<type> where type is:
<pre>
CENTER
LEFT
RIGHT
TOP
BOTTOM
TOP_LEFT
TOP_RIGHT
BOTTOM_LEFT
BOTTOM_RIGHT
</pre>
Additionally, `_ROTATE` may be appended to the end of the type to enable center rotation mode.

## ObjSprite2D_SetDestRect
<pre>
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
</pre>
Sets the drawing rectangle for the sprite.

This is the rectangle where the sprite will be drawn.

## ObjSprite2D_SetDestCenter
<pre>
    Arguments:
        1) real: objectID
</pre>
Sets the drawing rectangle for the sprite by mapping the center of the source rectangle to (0, 0).

For example, if the rectangle set with ObjSprite2D_SetSourceRect is (24, 32, 48, 46) (which is 24 wide and 14 high), the destination rectangle becomes (-12, -7, 12, 7).

## ObjSprite2D_SetCenterRotationEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether to use forced center point rotation mode for the given object.

This may fix the wobbling associated with rotation (angular velocity) of even-sized sprites.\
*Note: This function must be called before setting the destination rectangle.*