# ObjMesh Functions

[Return to Functions](../functions.html)

## ObjMesh_Create
```
    Return Type:
        real
```
Creates a 3D mesh object and returns its ID.

## ObjMesh_Load
```
    Arguments:
        1) real: objectID
        2) string: pathMesh
```
Loads a 3D mesh file.

Returns true if successful, otherwise false.\
The file must be either .mqo (Metasequoia) or .elem (Elfreina). Metasequoia software is available for free in English.

## ObjMesh_SetColor
```
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
```
Sets the color of the mesh (0-255).

## ObjMesh_SetAlpha
```
    Arguments:
        1) real: objectID
        2) real: alpha
```
Sets the alpha value of the mesh (0-255).

## ObjMesh_SetAnimation
```
    Arguments:
        1) real: objectID
        2) string: animationName
        3) real: animationFrame
```
Sets the animation of the mesh object.

The animation frame of the specified animation name is drawn.

## ObjMesh_SetCoordinate2D
```
    Arguments:
        1) real: objectID
        2) bool bEnable
```
When set to true, allows the mesh to be positioned using 2D coordinates.