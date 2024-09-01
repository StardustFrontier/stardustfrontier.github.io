# ObjSprite3D Functions

[Return to Functions](../functions.html)

## ObjSprite3D_SetSourceRect
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

## ObjSprite3D_SetSourceRectB
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

## ObjSprite3D_SetDest
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

## ObjSprite3D_SetDestRect
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

## ObjSprite3D_SetSourceDestRect
<pre>
    Arguments:
        1) real: objectID
</pre>
Sets the texture rectangle for the sprite, and maps the center of the rectangle to the destination coordinates (0, 0).

## ObjSprite3D_SetBillboard
<pre>
    Arguments:
        1) real: objectID
        2) bool: bBillboard
</pre>
If set to true, the object will always be facing the camera.