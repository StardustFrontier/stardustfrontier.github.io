# ObjMesh Functions

[Return to Functions](../functions.html)

## ObjMesh_Create
<pre>
    Return Type:
        real
</pre>
Creates a 3D mesh object and returns its ID.

## ObjMesh_Load
<pre>
    Arguments:
        1) real: objectID
        2) string: pathMesh
</pre>
Loads a 3D mesh file.

Returns true if successful, otherwise false.\
The file must be either .mqo (Metasequoia) or .elem (Elfreina). Metasequoia software is available for free in English.

## ObjMesh_SetColor
<pre>
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
</pre>
Sets the color of the mesh (0-255).

## ObjMesh_SetAlpha
<pre>
    Arguments:
        1) real: objectID
        2) real: alpha
</pre>
Sets the alpha value of the mesh (0-255).

## ObjMesh_SetAnimation
<pre>
    Arguments:
        1) real: objectID
        2) string: animationName
        3) real: animationFrame
</pre>
Sets the animation of the mesh object.

The animation frame of the specified animation name is drawn.

## ObjMesh_SetCoordinate2D
<pre>
    Arguments:
        1) real: objectID
        2) bool bEnable
</pre>
When set to true, allows the mesh to be positioned using 2D coordinates.