# Primitive Object Functions

[Return to Functions](./docs.html)

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
        real array
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
        2) real: red
        3) real: green
        4) real: blue
</pre>
Sets the color of the specified vertex (0-255).

## ObjPrim_SetVertexAlpha
<pre>
    Arguments:
        1) real: objectID
        2) real: alpha
</pre>
Sets the alpha value of the specified vertex (0-255).