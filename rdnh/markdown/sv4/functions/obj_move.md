# ObjMove Functions

[Return to Functions](../functions.html)

## ObjMove_SetX
```
    Arguments:
        1) real: objectID
        2) real: x
```
Sets the x-coordinate of the object.

## ObjMove_SetY
```
    Arguments:
        1) real: objectID
        2) real: y
```
Sets the y-coordinate of the object.

## ObjMove_SetPosition
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
```
Sets the x and y coordinates of the object.

## ObjMove_SetPosition
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
```
Sets the x and y coordinates of the object to the coordinates of the parent object.

## ObjMove_SetSpeed
```
    Arguments:
        1) real: objectID
        2) real: speed
```
Sets the movement speed for the object.

## ObjMove_SetAngle
```
    Arguments:
        1) real: objectID
        2) real: angle
```
Sets the movement angle for the object.

## ObjMove_SetAcceleration
```
    Arguments:
        1) real: objectID
        2) real: acceleration
```
Sets the movement acceleration per frame for the object.

## ObjMove_SetAngularVelocity
```
    Arguments:
        1) real: objectID
        2) real: angularVelocity
```
Sets the change in movement angle per frame for the object.

## ObjMove_SetMovementEnable
```
    Arguments:
        1) real: objectID
        2) bool: enable
```
Enables or disabled movement processing for the object.

## ObjMove_SetDestAtSpeed
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: speed
```
Moves the object towards the given coordinates at the speed specified.

## ObjMove_SetDestAtFrame
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: frames
```
Moves the object towards the given coordinates in the number of frames specified.

## ObjMove_SetDestAtWeight
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: frames
```
Moves the object towards the given coordinates.

It will slow down near the end of the movement based on the weight specified.

## ObjMove_SetDestAtInterpolate
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: frames
        5) real const: interpolationType
```
Moves the object towards the given coordinates in the number of frames specified with the given [interpolation type](./interpolation_types.html).

## ObjMove_AddPatternA1
```
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speed
        4) real: angle
```
After the specified number of frames, changes the speed and angle of the object.

NO_CHANGE can be used to preserve the original speed or angle.

## ObjMove_AddPatternA2
```
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speed
        4) real: angle
        5) real: acceleration
        6) real: angularVelocity
        7) real: maxSpeed
```
After the specified number of frames, changes the speed, angle, acceleration, angular velocity, and maximum speed of the object.

NO_CHANGE can be used to preserve the original speed, angle, acceleration, angular velocity, or maximum speed.

## ObjMove_AddPatternA3
```
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speed
        4) real: angle
        5) real: acceleration
        6) real: angularVelocity
        7) real: maxSpeed
        8) real: shotGraphic
```
After the specified number of frames, changes the speed, angle, acceleration, angular velocity, maximum speed, and shot graphic of the object.

NO_CHANGE can be used to preserve the original speed, angle, acceleration, angular velocity, maximum speed, or shot graphic.

## ObjMove_AddPatternA4
```
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speed
        4) real: angle
        5) real: acceleration
        6) real: angularVelocity
        7) real: maxSpeed
        8) real: shotGraphic
        9) real: targetObjectID
```
After the specified number of frames, changes the speed, angle, acceleration, angular velocity, maximum speed, and shot graphic of the object with angle being relative to the angle from the object to targetObjectID.

NO_CHANGE can be used to preserve the original speed, angle, acceleration, angular velocity, maximum speed, or shot graphic.\
The angle parameter is relative to the angle from the object to the target.\
For example, if GetPlayerObjectID is used as the target, an angle of 0 will cause the object to aim for the player.

## ObjMove_AddPatternB1
```
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speedX
        4) real: speedY
```
After the specified number of frames, changes the x and y movement speeds of the object.

NO_CHANGE can be used to preserve the original speeds.

## ObjMove_AddPatternB2
```
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speedX
        4) real: speedY
        5) real: accelX
        6) real: accelY
        7) real: maxSpeedX
        8) real: maxSpeedY
```
After the specified number of frames, changes the x and y speeds, accelerations, and maximum speeds of the object.

NO_CHANGE can be used to preserve the original x or y speeds, accelerations, and maximum speeds.

## ObjMove_AddPatternB3
```
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speedX
        4) real: speedY
        5) real: accelX
        6) real: accelY
        7) real: maxSpeedX
        8) real: maxSpeedY
```
After the specified number of frames, changes the x and y speeds, accelerations, maximum speeds, and shot graphic of the object.

NO_CHANGE can be used to preserve the original x or y speeds, accelerations, maximum speeds, and bullet graphic.

## ObjMove_GetX
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Gets the x-coordinate of the object.

If the object is deleted, this will return NULL_POS.

## ObjMove_GetY
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Gets the y-coordinate of the object.

If the object is deleted, this will return NULL_POS.

## ObjMove_GetSpeed
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the movement speed of the object.

## ObjMove_GetAngle
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the movement angle of the object.

## ObjMove_IsMovementEnable
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if movement processing is enabled for the object, otherwise returns false.

## ObjMove_CancelMovement
```
    Arguments:
        1) real: objectID
```
Cancels the currently active move pattern.

## ObjMove_ClearPatterns
```
    Arguments:
        1) real: objectID
```
Clears all move patterns that were added with ObjMove_AddPattern functions.

## ObjMove_StartHomingToEnemyA1
```
    Arguments:
        1) real: objectID
        2) real: maxTurn
        3) real: maxTurnInc
        4) real: homingTime
```
Makes the object begin homing toward enemies for homingTime frames.

maxTurn is the maximum angle the shot can turn per frame.\
maxTurnInc is added to maxTurn each frame, which can be used to prevent infinite circling around the target or to curve the angle.

## ObjMove_StartHomingToEnemyA2
```
    Arguments:
        1) real: objectID
        2) real: maxTurn
        3) real: maxTurnInc
        4) real: homingTime
        5) real: acceleration
        6) real: minSpeed
        7) real: maxSpeed
```
Makes the object begin homing toward enemies for homingTime frames using the given acceleration. minimum speed, and maximum speed.

maxTurn is the maximum angle the shot can turn per frame.\
maxTurnInc is added to maxTurn each frame, which can be used to prevent infinite circling around the target or to curve the angle.

_**Note**: The acceleration value must be positive, since it is used as both acceleration and deceleration._

## ObjMove_StartHomingToEnemyZ1
```
    Arguments:
        1) real: objectID
        2) real: angleWeight
        3) real: homingTime
```
Makes the object begin homing toward enemies for homingTime frames in a ZUN-like way.\
This works similarly to Reimu's homing amulets in most official Touhou games from MoF onward.

angleWeight can be used to control the smoothness of the turning.

## ObjMove_StartHomingToEnemyZ2
```
    Arguments:
        1) real: objectID
        2) real: angleWeight
        3) real: homingTime
        4) real: acceleration
        5) real: minSpeed
        6) real: maxSpeed
```
Makes the object begin homing toward enemies for homingTime frames in a ZUN-like way using the given acceleration. minimum speed, and maximum speed.\
This works similarly to Reimu's homing amulets in most official Touhou games from MoF onward.

angleWeight can be used to control the smoothness of the turning.

_**Note**: The acceleration value must be positive, since it is used as both acceleration and deceleration._

## ObjMove_StopHomingToEnemy
```
    Arguments:
        1) real: objectID
```
Disables homing for the given object if it was enabled.

## ObjMove_SetHomingToEnemyTargetType
```
    Arguments:
        1) real: objectID
        2) real: homingTargetType
```
Sets the targeting type for the object's enemy homing movement.

Types are:
```
HOMING_TARGET_NEAREST_TO_SHOT
HOMING_TARGET_NEAREST_TO_PLAYER
HOMING_TARGET_LOWEST_ON_SCREEN
```

_**Note**: This function must be called after homing has been enabled for the shot object._