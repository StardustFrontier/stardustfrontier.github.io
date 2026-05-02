# 3D Camera Functions

[Return to Functions](../functions.html)

## SetCameraFocusX
```
    Arguments:
        1) real: x
```
Sets the x coordinate of the camera focus.

## SetCameraFocusY
```
    Arguments:
        1) real: y
```
Sets the y coordinate of the camera focus.

## SetCameraFocusZ
```
    Arguments:
        1) real: z
```
Sets the z coordinate of the camera focus.

## SetCameraFocusXYZ
```
    Arguments:
        1) real: x
        2) real: y
        3) real: z
```
Sets the x, y, and z coordinates of the camera focus.

## SetCameraRadius
```
    Arguments:
        1) real: distance
```
Sets the distance of the camera to the focus point.

## SetCameraAzimuthAngle
```
    Arguments:
        1) real: azimuth
```
Sets the azimuth angle from the focus point.

## SetCameraElevationAngle
```
    Arguments:
        1) real: elevation
```
Sets the elevation angle from the focus point.

## SetCameraYaw
```
    Arguments:
        1) real: yaw
```
Sets the horizontal yaw angle of the camera.

## SetCameraPitch
```
    Arguments:
        1) real: pitch
```
Sets the vertical pitch angle of the camera.

## SetCameraRoll
```
    Arguments:
        1) real: roll
```
Sets the rotational roll angle of the camera.

## GetCameraX
```
    Return Type:
        real
```
Returns the x coordinate of the camera.

Defaults to 341.506348.

## GetCameraY
```
    Return Type:
        real
```
Returns the y coordinate of the camera.

Defaults to 353.553375.

## GetCameraZ
```
    Return Type:
        real
```
Returns the z coordinate of the camera.

Defaults to 91.506348.

## GetCameraFocusX
```
    Return Type:
        real
```
Returns the x coordinate of the camera focus point.

Defaults to 0.

## GetCameraFocusY
```
    Return Type:
        real
```
Returns the y coordinate of the camera focus point.

Defaults to 0.

## GetCameraFocusZ
```
    Return Type:
        real
```
Returns the z coordinate of the camera focus point.

Defaults to 0.

## GetCameraRadius
```
    Return Type:
        real
```
Returns the distance from the focus point to the camera.

Defaults to 500.

## GetCameraAzimuthAngle
```
    Return Type:
        real
```
Returns the azimuth angle from the focus point to the camera.

Defaults to 15.

## GetCameraElevationAngle
```
    Return Type:
        real
```
Returns the elevation angle from the focus point to the camera.

Defaults to 45.

## GetCameraYaw
```
    Return Type:
        real
```
Returns the horizontal yaw angle of the camera.

Defaults to 0.

## GetCameraPitch
```
    Return Type:
        real
```
Returns the vertical pitch angle of the camera.

Defaults to 0.

## GetCameraRoll
```
    Return Type:
        real
```
Returns the rotational roll angle of the camera.

Defaults to 0.

## SetCameraPerspectiveClip
```
    Arguments:
        1) real: nearClip
        2) real: farClip
```
Sets camera clipping distances.\
Objects that are further or nearer than the clipping distance will not be drawn.

## TweenCameraFocusXYZ
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: x
        4) real: y
        5) real: z
```
Changes the focus of the camera to (x, y, z) over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve any of the current values.

## TweenCameraFocusX
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: x
```
Changes the x-focus of the camera to the given value over duration frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraFocusY
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: y
```
Changes the y-focus of the camera to the given value over duration frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraFocusZ
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: z
```
Changes the z-focus of the camera to the given value over duration frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraRadius
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: radius
```
Changes the radius of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraAzimuthAngle
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: azimuth
```
Changes the azimuth angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraElevationAngle
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: elevation
```
Changes the elevation angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraYaw
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: yaw
```
Changes the yaw angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraPitch
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: pitch
```
Changes the pitch angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## TweenCameraRoll
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: roll
```
Changes the roll angle of the camera to the given value over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve the current value.

## CancelCameraTweens
```
    Return Type:
        nil
```
Cancels all of the active camera tweens.