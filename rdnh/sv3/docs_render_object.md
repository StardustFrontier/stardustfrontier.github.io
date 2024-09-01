# Render Object Functions

[Return to Functions](./docs.html)

## ObjRender_SetX
<pre>
    Arguments:
        1) real: objectID
        2) real: x
</pre>
Sets the x-coordinate of the object.

## ObjRender_SetY
<pre>
    Arguments:
        1) real: objectID
        2) real: y
</pre>
Sets the y-coordinate of the object.

## ObjRender_SetZ
<pre>
    Arguments:
        1) real: objectID
        2) real: z
</pre>
Sets the z-coordinate of the object.

## ObjRender_SetXY
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
</pre>
Sets the x and y coordinates of the object.

## ObjRender_SetPosition
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: z
</pre>
Sets the x, y, and z coordinates of the object.

## ObjRender_SetPositionO
<pre>
    Arguments:
        1) real: objectID
        2) real: parentObjectID
</pre>
Sets the x, y, and z coordinates of the object to the coordinates of the parent object.

## ObjRender_SetAngleX
<pre>
    Arguments:
        1) real: objectID
        2) real: angleX
</pre>
Sets the x-angle of the object.

## ObjRender_SetAngleY
<pre>
    Arguments:
        1) real: objectID
        2) real: angleY
</pre>
Sets the y-angle of the object.

## ObjRender_SetAngleZ
<pre>
    Arguments:
        1) real: objectID
        2) real: angleZ
</pre>
Sets the z-angle of the object.

## ObjRender_SetAngleXYZ
<pre>
    Arguments:
        1) real: objectID
        2) real: angleX
        3) real: angleY
        4) real: angleZ
</pre>
Sets the x, y, and z angles of the object.

## ObjRender_SetScaleX
<pre>
    Arguments:
        1) real: objectID
        2) real: scaleX
</pre>
Sets the x-scale of the object.

## ObjRender_SetScaleY
<pre>
    Arguments:
        1) real: objectID
        2) real: scaleY
</pre>
Sets the y-scale of the object.

## ObjRender_SetScaleZ
<pre>
    Arguments:
        1) real: objectID
        2) real: scaleZ
</pre>
Sets the z-scale of the object.

## ObjRender_SetScaleXY
<pre>
    Arguments:
        1) real: objectID
        2) real: scaleX
        3) real: scaleY
</pre>
Sets the x and y scales of the object.

## ObjRender_SetScaleXYZ
<pre>
    Arguments:
        1) real: objectID
        2) real: scaleX
        3) real: scaleY
        4) real: scaleZ
</pre>
Sets the x, y, and z scales of the object.

## ObjRender_SetColor
<pre>
    Arguments:
        1) real: objectID
        2) real: red
        3) real: green
        4) real: blue
</pre>
Sets the color of the object using RGB (0-255).

## ObjRender_SetColorHex
<pre>
    Arguments:
        1) real: objectID
        2) real: color
</pre>
Sets the color of the object using RGB in the hexadecimal format: `0xRRGGBB`

For example, pure green would be: `0x00FF00`\
*Note: **Colour** is not spelled correctly for the original function, for consistency, this function uses "Color" as well.*

## ObjRender_SetColorHSV
<pre>
    Arguments:
        1) real: objectID
        2) real: hue
        3) real: saturation
        4) real: value
</pre>
Sets the hue (0-359), saturation (0-255), and value (0-255) of an object.

## ObjRender_SetAlpha
<pre>
    Arguments:
        1) real: objectID
        2) real: alpha
</pre>
Sets the alpha value of the object.

A value of 0 will make the object invisible.\
A value of 255 will give the object full opacity.\
This function has no effect on an object using BLEND_ADD_RGB - use BLEND_ADD_ARGB instead.

## ObjRender_SetBlendType
<pre>
    Arguments:
        1) real: objectID
        2) real const: blendType
</pre>
Sets the [blend type](./docs_blend_types.html) for the specified object.

## ObjRender_SetTextureFilter
<pre>
    Arguments:
        1) real: objectID
        2) real const: filterType
</pre>
Sets the texture filtering for a render object.

Available filter types are:
<pre>
FILTER_NONE
FILTER_POINT
FILTER_LINEAR
</pre>
***Warning**: This will not work correctly on items or shots because of how the rendering for them is handled.*

## ObjRender_GetX
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the x-coordinate of the object.

*Note: If the specified object is deleted, the value returned will be NULL_POS (-999999)*

## ObjRender_GetY
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the y-coordinate of the object.

*Note: If the specified object is deleted, the value returned will be NULL_POS (-999999)*

## ObjRender_GetZ
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the z-coordinate of the object.

*Note: If the specified object is deleted, the value returned will be NULL_POS (-999999)*

## ObjRender_GetAngleX
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the x-angle of the object.

## ObjRender_GetAngleY
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the y-angle of the object.

## ObjRender_GetAngleZ
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the z-angle of the object.

## ObjRender_GetScaleX
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the x-scale of the object.

## ObjRender_GetScaleY
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the y-scale of the object.

## ObjRender_GetScaleZ
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the z-scale of the object.

## ObjRender_GetAlpha
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the alpha value of the object.

## ObjRender_GetBlendType
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real const
</pre>
Returns the [blend type](./docs_blend_types.html) of the object.

## ObjRender_GetTextureFilter
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real const
</pre>
Returns the current texture filtering for a render object.

Available filter types are:
<pre>
FILTER_NONE
FILTER_POINT
FILTER_LINEAR
</pre>

## ObjRender_SetZWrite
<pre>
    Arguments:
        1) real: objectID
        2) bool: bZWrite
</pre>
Allows or prevents the object from writing in the Z-buffer.

## ObjRender_SetZTest
<pre>
    Arguments:
        1) real: objectID
        2) bool: bZTest
</pre>
Sets whether or not the object uses the Z-buffer.

## ObjRender_SetScissorTest
<pre>
    Arguments:
        1) real: objectID
        2) bool: bScissorTest
</pre>
Sets whether or not the object uses scissor testing.

This culls pixels that are outside of the scissor rectangle that is set by ObjRender_SetScissorRect\
*Note: Occurs after pixel shaders.*

## ObjRender_SetScissorRect
<pre>
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
</pre>
Sets the rectangle to use for scissor testing.

## ObjRender_SetFogEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bFogEnable
</pre>
Allows or prevents the object from being affected by the fog.

Defaults to true.

## ObjRender_SetPermitCamera
<pre>
    Arguments:
        1) real: objectID
        2) bool: bPermitCamera
</pre>
Determines whether the object is affected by the 2D camera.

If set to false, the object will not be affected by the camera regardless of render priority.

## ObjRender_SetMoveSpeed
<pre>
    Arguments:
        1) real: objectID
        2) real: speedX
        3) real: speedY
        4) real: speedZ
</pre>
Sets the object's (render) move speed.

This will increment the object's x, y, z coordinates by the given values every frame until set to 0.

## ObjRender_SetRotationSpeed
<pre>
    Arguments:
        1) real: objectID
        2) real: rotationSpeedX
        3) real: rotationSpeedY
        4) real: rotationSpeedZ
</pre>
Sets the object's rotation speed (angular velocity).

This will increment the object's x, y, z angles by the given values every frame until set to 0.

## ObjRender_SetScaleSpeed
<pre>
    Arguments:
        1) real: objectID
        2) real: scaleSpeedX
        3) real: scaleSpeedY
        4) real: scaleSpeedZ
</pre>
Sets the object's scale speed.

This will increment the object's x, y, z scales by the given values every frame until set to 0.

## ObjRender_TweenPosition
<pre>
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: x
        5) real: y
        6) real: z
</pre>
Moves the object to position (x, y, z) over duration frames with [interpolationType](./docs_interpolation_types.html). interpolation.

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_TweenColor
<pre>
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: red
        5) real: green
        6) real: blue
</pre>
Changes the object's color to (r, g, b) over duration frames with the given [interpolation type](./docs_interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_TweenAlpha
<pre>
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: alpha
</pre>
Changes the object's alpha over duration frames with the given [interpolation type](./docs_interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_TweenAngle
<pre>
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: angleX
        5) real: angleY
        6) real: angleZ
</pre>
Changes the object's angle to (angleX, angleY, angleZ) over duration frames with the given [interpolation type](./docs_interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*

## ObjRender_TweenScale
<pre>
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpolationType
        4) real: scaleX
        5) real: scaleY
        6) real: scaleZ
</pre>
Changes the object's scale to (scaleX, scaleY, scaleZ) over duration frames with the given [interpolation type](./docs_interpolation_types.html).

NO_CHANGE can be used to preserve any of the current values.

*Note: Tweens of the same type (for example, two ObjRender_TweenPosition) will cancel the currently running one and start the new one.*