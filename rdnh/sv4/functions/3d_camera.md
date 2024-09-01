# 3D Camera Functions

[Return to Functions](../functions.html)

## SetCameraFocusX
<pre>
    Arguments:
        1) real: x
</pre>
Sets the x coordinate of the camera focus.

## SetCameraFocusY
<pre>
    Arguments:
        1) real: y
</pre>
Sets the y coordinate of the camera focus.

## SetCameraFocusZ
<pre>
    Arguments:
        1) real: z
</pre>
Sets the z coordinate of the camera focus.

## SetCameraFocusXYZ
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: z
</pre>
Sets the x, y, and z coordinates of the camera focus.

## SetCameraRadius
<pre>
    Arguments:
        1) real: distance
</pre>
Sets the distance of the camera to the focus point.

## SetCameraAzimuthAngle
<pre>
    Arguments:
        1) real: azimuth
</pre>
Sets the azimuth angle from the focus point.

## SetCameraElevationAngle
<pre>
    Arguments:
        1) real: elevation
</pre>
Sets the elevation angle from the focus point.

## SetCameraYaw
<pre>
    Arguments:
        1) real: yaw
</pre>
Sets the horizontal yaw angle of the camera.

## SetCameraPitch
<pre>
    Arguments:
        1) real: pitch
</pre>
Sets the vertical pitch angle of the camera.

## SetCameraRoll
<pre>
    Arguments:
        1) real: roll
</pre>
Sets the rotational roll angle of the camera.

## GetCameraX
<pre>
    Return Type:
        real
</pre>
Returns the x coordinate of the camera.

Defaults to 341.506348.

## GetCameraY
<pre>
    Return Type:
        real
</pre>
Returns the y coordinate of the camera.

Defaults to 353.553375.

## GetCameraZ
<pre>
    Return Type:
        real
</pre>
Returns the z coordinate of the camera.

Defaults to 91.506348.

## GetCameraFocusX
<pre>
    Return Type:
        real
</pre>
Returns the x coordinate of the camera focus point.

Defaults to 0.

## GetCameraFocusY
<pre>
    Return Type:
        real
</pre>
Returns the y coordinate of the camera focus point.

Defaults to 0.

## GetCameraFocusZ
<pre>
    Return Type:
        real
</pre>
Returns the z coordinate of the camera focus point.

Defaults to 0.

## GetCameraRadius
<pre>
    Return Type:
        real
</pre>
Returns the distance from the focus point to the camera.

Defaults to 500.

## GetCameraAzimuthAngle
<pre>
    Return Type:
        real
</pre>
Returns the azimuth angle from the focus point to the camera.

Defaults to 15.

## GetCameraElevationAngle
<pre>
    Return Type:
        real
</pre>
Returns the elevation angle from the focus point to the camera.

Defaults to 45.

## GetCameraYaw
<pre>
    Return Type:
        real
</pre>
Returns the horizontal yaw angle of the camera.

Defaults to 0.

## GetCameraPitch
<pre>
    Return Type:
        real
</pre>
Returns the vertical pitch angle of the camera.

Defaults to 0.

## GetCameraRoll
<pre>
    Return Type:
        real
</pre>
Returns the rotational roll angle of the camera.

Defaults to 0.

## SetCameraPerspectiveClip
<pre>
    Arguments:
        1) real: nearClip
        2) real: farClip
</pre>
Sets camera clipping distances.\
Objects that are further or nearer than the clipping distance will not be drawn.

## TweenCameraFocusXYZ
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: x
        4) real: y
        5) real: z
</pre>
Changes the focus of the camera to (x, y, z) over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve any of the current values.

## TweenCameraFocusX
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: x
</pre>
Changes the x-focus of the camera to the given value over duration frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraFocusY
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: y
</pre>
Changes the y-focus of the camera to the given value over duration frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraFocusZ
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: z
</pre>
Changes the z-focus of the camera to the given value over duration frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraRadius
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: radius
</pre>
Changes the radius of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraAzimuthAngle
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: azimuth
</pre>
Changes the azimuth angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraElevationAngle
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: elevation
</pre>
Changes the elevation angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraYaw
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: yaw
</pre>
Changes the yaw angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraPitch
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: pitch
</pre>
Changes the pitch angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraRoll
<pre>
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: roll
</pre>
Changes the roll angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## CancelCameraTweens
Cancels all of the active camera tweens.