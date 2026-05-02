# ObjPopupList Functions

[Return to Functions](../functions.html)

## ObjPopupList_Create
```
    Arguments:
        1) real: maxPopups
    Return Type:
        real
```
Creates a score number popup list object that can display up to maxPopups popups at once.

If maxPopups is exceeded when creating a popup, the oldest existing popup will be recycled.

## ObjPopupList_SetTexture
```
    Arguments:
        1) real: objectID
        2) string: pathTexture
```
Sets the texture for the popup list.

## ObjPopupList_SetScale
```
    Arguments:
        1) real: objectID
        2) real: scaleX
        3) real: scaleY
```
Sets the scale of the popup digits.

## ObjPopupList_SetSize
```
    Arguments:
        1) real: objectID
        2) real: width
        3) real: height
```
Sets the width and height of each digit on the texture.

## ObjPopupList_SetPowerUpData
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: width
        5) real: height
        6) real: frameFadeOutStart = -1
```
Sets the source rect (x, y, width, height) of the "PowerUp" sprite on the texture.

Optionally, a fade out start time can be passed, which will otherwise default to -1 (no fade out).

## ObjPopupList_SetPowerUpScale
```
    Arguments:
        1) real: objectID
        2) real: scaleX
        3) real: scaleY
```
Sets the scale of the "PowerUp" sprite.

## ObjPopupList_SetStartSpeed
```
    Arguments:
        1) real: objectID
        2) real: startSpeed
```
Sets the speed at which the score popups begin moving at.

## ObjPopupList_SetDecelerationEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
If true, enables the deceleration effect for score popups.

Every frame, speed will be set to speed * 0.95.

## ObjPopupList_SetDeleteTime
```
    Arguments:
        1) real: objectID
        2) real: time
```
Sets the time at which a created score popup will be deleted.

## ObjPopupList_AddDigitsFrame
```
    Arguments:
        1) real: objectID
        2) real: duration
        3) real: firstDigitX
        4) real: firstDigitY
```
Adds an animation frame for a set of digits to the popop list renderer.

If only a single frame is added, digits will fade out after the given duration instead of animating.\
The duration of the last frame in an animated sequence does not matter since the animation is not looped.

_**Note**: There is currently no way to set the spacing between digits on the texture. They must be evenly spaced._

## ObjPopupList_SetPlayerObjectID
```
    Arguments:
        1) real: objectID
        2) real: objPlayer
```
Attaches a player object to the popup list.

This will cause score popups to fade out when close to the player (distance is currently hardcoded).

## ObjPopupList_SetFadeRange
```
    Arguments:
        1) real: objectID
        2) real: minDistance
        3) real: maxDistance
```
Sets the distance parameters for the fade effect when score popups are close to the player.

If the player is within the range of [minDistance, maxDistance], the popup's alpha value will be interpolated from 128 to 255 depending on the distance.

Defaults to (64, 128).

## ObjPopupList_CreatePopup
```
    Arguments:
        1) real: objectID
        2) real: value
        3) real: x
        4) real: y
        5) real: colorHex
```
Creates a score number popup with the given value at (x, y) and sets the color to colorHex.

_**Note**: The popup itself is not an object and cannot be controlled externally._