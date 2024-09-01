# ObjPrim Functions

[Return to Functions](../functions.html)

## ObjPrim_Create
<pre>
    Arguments:
        1) real: objectType
    Return Type:
        real
</pre>
Creates a Primitive object.

Object types are:
<pre>
OBJ_PRIMITIVE_2D: primitive (triangle) in the 2D space
OBJ_SPRITE_2D: rectangle in the 2D space (usable by the ObjSprite2D_ functions).
OBJ_SPRITE_LIST_2D: list of rectangles in the 2D space (usable by the ObjSpriteList2D_ functions).
OBJ_PRIMITIVE_3D: primitive (triangle) in the 3D space
OBJ_SPRITE_3D: rectangle in the 3D space (usable by the ObjSprite3D_ functions).
</pre>

## ObjPrim_SetPrimitiveType
<pre>
    Arguments:
        1) real: objectID
        2) real const: primitiveType
</pre>
Creates a Primitive object.

Primitive types are:
<pre>
PRIMITIVE_TRIANGLELIST
PRIMITIVE_TRIANGLESTRIP
PRIMITIVE_TRIANGLEFAN
PRIMITIVE_LINELIST
PRIMITIVE_LINESTRIP
PRIMITIVE_POINT_LIST
</pre>

## ObjPrim_SetVertexCount
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexCount
</pre>
Sets the number of vertices the object contains.

## ObjPrim_GetVertexCount
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the number of vertices the object contains.

*Note: When used on a sprite list object, returns the number of vertices added with ObjSpriteList2D_AddVertex * 6*

## ObjPrim_SetTexture
<pre>
    Arguments:
        1) real: objectID
        2) string: pathTexture
</pre>
Sets the specified texture on the object.

Loads the texture file if it has not already been loaded.

## ObjPrim_GetTexture
<pre>
    Arguments:
        1) real: objectID
    Returns:
        string: texture
</pre>
Returns the path or name of the object's texture.

## ObjPrim_GetTextureWidth
<pre>
    Arguments:
        1) real: objectID
    Returns:
        real: width
</pre>
Returns the width of the object's texture.

If the object doesn't have a texture set, this will return 0.

## ObjPrim_GetTextureHeight
<pre>
    Arguments:
        1) real: objectID
    Returns:
        real: height
</pre>
Returns the height of the object's texture.

If the object doesn't have a texture set, this will return 0.

## ObjPrim_SetVertexPosition
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
        3) real: x
        4) real: y
        5) real: z
</pre>
Sets the position of the specified vertex.

## ObjPrim_GetVertexPosition
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
    Return Type:
        array[real]: position
</pre>
Returns the position of the specified vertex in an array [x,y,z].

## ObjPrim_SetVertexUV
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
        3) real: textureX
        4) real: textureY
</pre>
Sets the UV-coordinates for the specified vertex.

The value for the coordinates must be in the range (0.0-1.0).\
For example, if you want a vertex to be at the center-top of a 512×512 texture, you have to set x to 0.5 and y to 1.0.
As it may be troublesome to convert pixels into a 0.0-1.0 value, ObjPrim_SetVertexUVT is recommended.

## ObjPrim_SetVertexUVT
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
        3) real: textureX
        4) real: textureY
</pre>
Sets the UV-coordinates for the specified vertex.

You must set the object's texture using ObjPrim_SetTexture beforehand.

## ObjPrim_SetVertexColor
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
        3) real: red
        4) real: green
        5) real: blue
</pre>
Sets the color of the specified vertex (0-255).

## ObjPrim_GetVertexColor
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
    Returns:
        array[real]: color
</pre>
Returns the vertex color as an array with the format [r, g, b].

## ObjPrim_SetVertexColorHex
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
        3) real: color
</pre>
Sets the color of the specified vertex using RGB in hexadecimal format (0xRRGGBB).

For example, pure green would be: `0x00FF00`

## ObjPrim_GetVertexColorHex
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
    Returns:
        real: color
</pre>
Returns the vertex color as an XRGB hexadecimal color value.

## ObjPrim_SetVertexAlpha
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
        3) real: alpha
</pre>
Sets the alpha value of the specified vertex (0-255).

## ObjPrim_GetVertexAlpha
<pre>
    Arguments:
        1) real: objectID
        2) real: vertexIndex
    Returns:
        real: color
</pre>
Returns the vertex alpha value.