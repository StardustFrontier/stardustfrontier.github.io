# 2D Sprite List Object Functions

[Return to Functions](./docs.html)

## ObjSpriteList2D_SetSourceRect
<pre>
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
</pre>
Sets the texture rectangle for the next sprite to be added.

This is the rectangle on the original texture from which the sprite will be drawn.

## ObjSpriteList2D_SetSourceRectB
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: width
        5) real: height
</pre>
Sets the texture rectangle for the next sprite to be added, using x, y, width, and height.

This is the rectangle on the original texture from which the sprite will be drawn.

## ObjSpriteList2D_SetDest
<pre>
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
</pre>
Sets the drawing rectangle for the sprite based on a pre-defined constant.

This is the rectangle where the sprite will be drawn, relative to the sprite's position.\
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

## ObjSpriteList2D_SetDestRect
<pre>
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
</pre>
Sets the drawing rectangle for the next sprite to be added.

This is the rectangle where the sprite will be drawn, relative to the sprite's position.

## ObjSpriteList2D_SetDestCenter
<pre>
    Arguments:
        1) real: objectID
</pre>
Sets the drawing rectangle for the next sprite to be added, by mapping the center of the source rectangle to (0, 0), relative to the sprite's position.

For instance, if the rectangle set with ObjSpriteList2D_SetSourceRect is (24, 32, 48, 46) (which is 24 wide and 14 high), the destination rectangle becomes (-12, -7, 12, 7).

## ObjSpriteList2D_SetCenterRotationEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether to use forced center point rotation mode for the given object.

This may fix the wobbling associated with rotation (angular velocity) of even-sized sprites.\
*Note: This function must be called before setting the destination rectangle.*

## ObjSpriteList2D_AddVertex
<pre>
    Arguments:
        1) real: objectID
</pre>
Adds a sprite vertex to the specified object, i.e. the current sprite is finalized and added to the list to be drawn.

After using this function, using functions to modify the object will target the next sprite to be added.

## ObjSpriteList2D_CloseVertex
<pre>
    Arguments:
        1) real: objectID
</pre>
Finalizes the object by preventing more sprites from being added to the list to be drawn.

After using this function, using ObjRender_ functions to transform coordinates (e.g. position, angle, scale, etc) will affect all added sprites as a group.\
The object's initial position is set at (0,0), so the sprites previously added are positioned relative to the overall object's position.

## ObjSpriteList2D_ClearVertexCount
<pre>
    Arguments:
        1) real: objectID
</pre>
Clears the sprite vertices for the specified object, i.e. removes all of the sprites previously added.