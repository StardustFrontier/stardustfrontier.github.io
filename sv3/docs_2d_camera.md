# 2D Camera Functions

[Return to Functions](./docs.html)

## Set2DCameraFocusX
<pre>
    Arguments:
        1) real: x
</pre>
Sets the x-coordinate of the 2D world camera's focus point.

Defaults to half of the STG frame's width (center of the playing field).

## Set2DCameraFocusY
<pre>
    Arguments:
        1) real: y
</pre>
Sets the y-coordinate of the 2D world camera's focus point.

Defaults to half of the STG frame's height (center of the playing field).

## Set2DCameraAngleZ
<pre>
    Arguments:
        1) real: rotation
</pre>
Sets the z angle (rotation) of the 2D camera.

## Set2DCameraRatio
<pre>
    Arguments:
        1) real: zoom
</pre>
Sets the zoom of the camera (centered on the focus point).

Defaults to 1.

## Set2DCameraRatioX
<pre>
    Arguments:
        1) real: xZoom
</pre>
Sets the magnification of the x axis of the 2D camera (centered on the focus point).

For example, if you set this value to 2, the x axis will be doubled in size.\
Defaults to 1.\
If you specify a negative value, the x axis will be flipped.

## Set2DCameraRatioY
<pre>
    Arguments:
        1) real: yZoom
</pre>
Sets the magnification of the y axis of the 2D camera (centered on the focus point).

For example, if you set this value to 2, the y axis will be doubled in size.\
Defaults to 1.\
If you specify a negative value, the y axis will be flipped.

## Reset2DCamera
Resets both the focus point and the zoom ratio, respectively, to the center of the screen and 1.

## Get2DCameraX
<pre>
    Return Type:
        real
</pre>
Returns the x-coordinate of the camera.

## Get2DCameraY
<pre>
    Return Type:
        real
</pre>
Returns the y-coordinate of the camera.

## Get2DCameraAngleZ
<pre>
    Return Type:
        real
</pre>
Returns the z angle (rotation) of the camera.

## Get2DCameraRatio
<pre>
    Return Type:
        real
</pre>
Returns the zoom ratio of the camera.

## Get2DCameraRatioX
<pre>
    Return Type:
        real
</pre>
Returns the x zoom ratio of the camera.

## Get2DCameraRatioY
<pre>
    Return Type:
        real
</pre>
Returns the y zoom ratio of the camera.