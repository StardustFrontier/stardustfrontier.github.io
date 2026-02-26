# ObjRender Functions

[Return to Functions](../functions.html)

## ObjRender_SetX
```
    Arguments:
        1) real: objectID
        2) real: x
```
Sets the x-coordinate of the object.

## ObjRender_SetY
```
    Arguments:
        1) real: objectID
        2) real: y
```
Sets the y-coordinate of the object.

## ObjRender_SetZ
```
    Arguments:
        1) real: objectID
        2) real: z
```
Sets the z-coordinate of the object.

## ObjRender_SetXY
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
```
Sets the x and y coordinates of the object.

## ObjRender_SetPosition
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: z
```
Sets the x, y, and z coordinates of the object.

## ObjRender_SetPositionO
```
    Arguments:
        1) real: objectID
        2) real: parentObjectID
```
Sets the x, y, and z coordinates of the object to the coordinates of the parent object.

## ObjRender_SetAngleX
```
    Arguments:
        1) real: objectID
        2) real: angleX
```
Sets the x-angle of the object.

## ObjRender_SetAngleY
```
    Arguments:
        1) real: objectID
        2) real: angleY
```
Sets the y-angle of the object.

## ObjRender_SetAngleZ
```
    Arguments:
        1) real: objectID
        2) real: angleZ
```
Sets the z-angle of the object.

## ObjRender_SetAngleXYZ
```
    Arguments:
        1) real: objectID
        2) real: angleX
        3) real: angleY
        4) real: angleZ
```
Sets the x, y, and z angles of the object.

## ObjRender_SetScaleX
```
    Arguments:
        1) real: objectID
        2) real: scaleX
```
Sets the x-scale of the object.

## ObjRender_SetScaleY
```
    Arguments:
        1) real: objectID
        2) real: scaleY
```
Sets the y-scale of the object.

## ObjRender_SetScaleZ
```
    Arguments:
        1) real: objectID
        2) real: scaleZ
```
Sets the z-scale of the object.

## ObjRender_SetScaleXY
```
    Arguments:
        1) real: objectID
        2) real: scaleX
        3) real: scaleY
```
Sets the x and y scales of the object.

## ObjRender_SetScaleXYZ
```
    Arguments:
        1) real: objectID
        2) real: scaleX
        3) real: scaleY
        4) real: scaleZ
```
Sets the x, y, and z scales of the object.

## ObjRender_SetColor
```
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
```
Sets the color of the object using RGB (0-255).

## ObjRender_SetColorHex
```
    Arguments:
        1) real: objectID
        2) real: color
```
Sets the color of the object using RGB in hexadecimal format (0xRRGGBB)

For example, pure green would be: `0x00FF00`

## ObjRender_SetColorHSV
```
    Arguments:
        1) real: objectID
        2) real: hue
        3) real: saturation
        4) real: value
```
Sets the hue (0-359), saturation (0-255), and value (0-255) of an object.

## ObjRender_SetAlpha
```
    Arguments:
        1) real: objectID
        2) real: alpha
```
Sets the alpha value of the object.

A value of 0 will make the object invisible.\
A value of 255 will give the object full opacity.\
This function has no effect on an object using BLEND_ADD_RGB - use BLEND_ADD_ARGB instead.

## ObjRender_SetBlendType
```
    Arguments:
        1) real: objectID
        2) real const: blendType
```
Sets the [blend type](./blend_types.html) for the specified object.

## ObjRender_SetTextureFilter
```
    Arguments:
        1) real: objectID
        2) real const: filterType
```
Sets both the minification and magnification [filter type](./filter_types.html) for the render object.

***Warning**: This will not work correctly on items or shots because of how the rendering for them is handled.*

## ObjRender_SetTextureFilterMin
```
    Arguments:
        1) real: objectID
        2) real const: filterType
```
Sets the minification [filter type](./filter_types.html) for the render object.

***Warning**: This will not work correctly on items or shots because of how the rendering for them is handled.*

## ObjRender_SetTextureFilterMag
```
    Arguments:
        1) real: objectID
        2) real const: filterType
```
Sets the magnification [filter type](./filter_types.html) for the render object.

***Warning**: This will not work correctly on items or shots because of how the rendering for them is handled.*

## ObjRender_SetTextureFilterMip
```
    Arguments:
        1) real: objectID
        2) real const: filterType
```
Sets the mipmap [filter type](./filter_types.html) for the render object.

***Warning**: This will not work correctly on items or shots because of how the rendering for them is handled.*

## ObjRender_SetTextureAnisotropyLevel
```
    Arguments:
        1) real: objectID
        2) real: level
```
Sets the texture anisotropy level for the object.

The value will automatically be clamped to a value between 1 and GetMaxTextureAnisotropy().\
Defaults to ANISOTROPY_LEVEL_NONE, which is 1.

## ObjRender_GetX
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the x-coordinate of the object.

*Note: If the specified object is deleted, the value returned will be NULL_POS (-999999)*

## ObjRender_GetY
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the y-coordinate of the object.

*Note: If the specified object is deleted, the value returned will be NULL_POS (-999999)*

## ObjRender_GetZ
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the z-coordinate of the object.

*Note: If the specified object is deleted, the value returned will be NULL_POS (-999999)*

## ObjRender_GetAngleX
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the x-angle of the object.

## ObjRender_GetAngleY
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the y-angle of the object.

## ObjRender_GetAngleZ
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the z-angle of the object.

## ObjRender_GetScaleX
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the x-scale of the object.

## ObjRender_GetScaleY
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the y-scale of the object.

## ObjRender_GetScaleZ
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the z-scale of the object.

## ObjRender_GetColor
```
    Arguments:
        1) real: objectID
    Returns:
        array[real]: color
```
Returns the object's color as an array with the format [r, g, b].

## ObjRender_GetColorHex
```
    Arguments:
        1) real: objectID
    Returns:
        real: colorHex
```
Returns the object's color as an XRGB hexadecimal color value.

## ObjRender_GetAlpha
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the alpha value of the object.

## ObjRender_GetBlendType
```
    Arguments:
        1) real: objectID
    Return Type:
        real const
```
Returns the [blend type](./blend_types.html) of the object.

## ObjRender_SetZWrite
```
    Arguments:
        1) real: objectID
        2) bool: bZWrite
```
Allows or prevents the object from writing in the Z-buffer.

## ObjRender_SetZTest
```
    Arguments:
        1) real: objectID
        2) bool: bZTest
```
Sets whether or not the object uses the Z-buffer.

## ObjRender_SetScissorTest
```
    Arguments:
        1) real: objectID
        2) bool: bScissorTest
```
Sets whether or not the object uses scissor testing.

This culls pixels that are outside of the scissor rectangle that is set by ObjRender_SetScissorRect\
*Note: Occurs after pixel shaders.*

## ObjRender_SetScissorRect
```
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
```
Sets the rectangle to use for scissor testing.

## ObjRender_SetFogEnable
```
    Arguments:
        1) real: objectID
        2) bool: bFogEnable
```
Allows or prevents the object from being affected by the fog.

Defaults to true.

## ObjRender_SetPermitCamera
```
    Arguments:
        1) real: objectID
        2) bool: bPermitCamera
```
Determines whether the object is affected by the 2D camera.

If set to false, the object will not be affected by the camera regardless of render priority.

## ObjRender_SetDeleteFrame
```
    Arguments:
        1) real: objectID
        2) real: frames
```
Deletes the render object after the specified number of frames.

## ObjRender_SetMoveSpeed
```
    Arguments:
        1) real: objectID
        2) real: speedX
        3) real: speedY
        4) real: speedZ
```
Sets the object's (render) move speed.

This will increment the object's x, y, z coordinates by the given values every frame until set to 0.

## ObjRender_SetRotationSpeed
```
    Arguments:
        1) real: objectID
        2) real: rotationSpeedX
        3) real: rotationSpeedY
        4) real: rotationSpeedZ
```
Sets the object's rotation speed (angular velocity).

This will increment the object's x, y, z angles by the given values every frame until set to 0.

## ObjRender_SetScaleSpeed
```
    Arguments:
        1) real: objectID
        2) real: scaleSpeedX
        3) real: scaleSpeedY
        4) real: scaleSpeedZ
```
Sets the object's scale speed.

This will increment the object's x, y, z scales by the given values every frame until set to 0.

## ObjRender_TweenPosition
```
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: x
        5) real: y
        6) real: z
```
Moves the object to position (x, y, z) over duration frames with the given [interpolation type](./interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_TweenColor
```
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: red
        5) real: green
        6) real: blue
```
Changes the object's color to (r, g, b) over duration frames with the given [interpolation type](./interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_TweenAlpha
```
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: alpha
```
Changes the object's alpha over duration frames with the given [interpolation type](./interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_TweenAngle
```
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: angleX
        5) real: angleY
        6) real: angleZ
```
Changes the object's angle to (angleX, angleY, angleZ) over duration frames with the given [interpolation type](./interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_TweenScale
```
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: scaleX
        5) real: scaleY
        6) real: scaleZ
```
Changes the object's scale to (scaleX, scaleY, scaleZ) over duration frames with the given [interpolation type](./interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_CancelTweens
```
    Arguments:
        1) real: objectID
```
Cancels all of the object's active tweens started by ObjRender_Tween* functions.

## ObjRender_GetParentID
```
    Arguments:
        1) real: objectID
```
_This function is for child render objects._

Returns the object's parent render object ID if it has one, otherwise returns ID_INVALID.

## ObjRender_SetParentPositionEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
_This function is for child render objects._

Sets whether the object's position should be relative to its parent render object.

## ObjRender_SetParentRotationEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
_This function is for child render objects._

Sets whether the object's angle should be relative to its parent render object.

## ObjRender_SetParentScaleEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
_This function is for child render objects._

Sets whether the object's scale should be relative to its parent render object.

## ObjRender_GetAbsoluteX
```
    Arguments:
        1) real: objectID
    Returns:
        real: x
```
_This function is for child render objects._

Returns the actual x-coordinate of a child render object.

_Note: ObjRender_GetX returns the relative position for child objects._

## ObjRender_GetAbsoluteY
```
    Arguments:
        1) real: objectID
    Returns:
        real: y
```
_This function is for child render objects._

Returns the actual y-coordinate of a child render object.

_Note: ObjRender_GetY returns the relative position for child objects._

## ObjRender_GetAbsoluteZ
```
    Arguments:
        1) real: objectID
    Returns:
        real: z
```
_This function is for child render objects._

Returns the actual z-coordinate of a child render object.

_Note: ObjRender_GetZ returns the relative position for child objects._

## ObjRender_AddChild
```
    Arguments:
        1) real: objectID
        2) real: childObjectID
```
_This function is for parent render objects._

Adds a render object as a child of this object.

## ObjRender_RemoveChild
```
    Arguments:
        1) real: objectID
        2) real: childObjectID
```
_This function is for parent render objects._

Removes a child object from this object.

_**Note:** This does not delete the child object._

## ObjRender_RemoveChildren
```
    Arguments:
        1) real: objectID
```
_This function is for parent render objects._

Removes all child objects from this object.

_**Note:** This does not delete the child objects._

## ObjRender_DeleteChildren
```
    Arguments:
        1) real: objectID
```
_This function is for parent render objects._

Removes and deletes all child objects from this object.

## ObjRender_GetListOfChildID
```
    Arguments:
        1) real: objectID
    Returns:
        array[real]: objectIDs
```
_This function is for parent render objects._

Returns an array of object IDs of all the object's children.