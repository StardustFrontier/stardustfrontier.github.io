# 2D Camera Functions

[Return to Functions](../functions.html)

## Set2DCameraFocusX
```
    Arguments:
        1) real: x
```
Sets the x-coordinate of the 2D world camera's focus point.

Defaults to half of the STG frame's width (center of the playing field).

## Set2DCameraFocusY
```
    Arguments:
        1) real: y
```
Sets the y-coordinate of the 2D world camera's focus point.

Defaults to half of the STG frame's height (center of the playing field).

## Set2DCameraAngleZ
```
    Arguments:
        1) real: rotation
```
Sets the z angle (rotation) of the 2D camera.

## Set2DCameraRatio
```
    Arguments:
        1) real: zoom
```
Sets the zoom of the camera (centered on the focus point).

Defaults to 1.

## Set2DCameraRatioX
```
    Arguments:
        1) real: xZoom
```
Sets the magnification of the x axis of the 2D camera (centered on the focus point).

For example, if you set this value to 2, the x axis will be doubled in size.\
Defaults to 1.\
If you specify a negative value, the x axis will be flipped.

## Set2DCameraRatioY
```
    Arguments:
        1) real: yZoom
```
Sets the magnification of the y axis of the 2D camera (centered on the focus point).

For example, if you set this value to 2, the y axis will be doubled in size.\
Defaults to 1.\
If you specify a negative value, the y axis will be flipped.

## Reset2DCamera
Resets both the focus point and the zoom ratio, respectively, to the center of the screen and 1.

## Get2DCameraX
```
    Return Type:
        real
```
Returns the x-coordinate of the camera.

## Get2DCameraY
```
    Return Type:
        real
```
Returns the y-coordinate of the camera.

## Get2DCameraAngleZ
```
    Return Type:
        real
```
Returns the z angle (rotation) of the camera.

## Get2DCameraRatio
```
    Return Type:
        real
```
Returns the zoom ratio of the camera.

## Get2DCameraRatioX
```
    Return Type:
        real
```
Returns the x zoom ratio of the camera.

## Get2DCameraRatioY
```
    Return Type:
        real
```
Returns the y zoom ratio of the camera.