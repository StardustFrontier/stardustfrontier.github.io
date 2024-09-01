# Move Object Functions

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

## ObjRender_SetPosition
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
</pre>
Sets the x and y coordinates of the object to the coordinates of the parent object.

## ObjRender_SetSpeed
<pre>
    Arguments:
        1) real: objectID
        2) real: speed
</pre>
Sets the movement speed for the object.

## ObjRender_SetAngle
<pre>
    Arguments:
        1) real: objectID
        2) real: angle
</pre>
Sets the movement angle for the object.

## ObjMove_SetAcceleration
<pre>
    Arguments:
        1) real: objectID
        2) real: acceleration
</pre>
Sets the movement acceleration per frame for the object.

## ObjMove_SetAngularVelocity
<pre>
    Arguments:
        1) real: objectID
        2) real: angularVelocity
</pre>
Sets the change in movement angle per frame for the object.

## ObjMove_SetDestAtSpeed
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: speed
</pre>
Moves the object towards the given coordinates at the speed specified.

## ObjMove_SetDestAtFrame
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: frames
</pre>
Moves the object towards the given coordinates in the number of frames specified.

## ObjMove_SetDestAtWeight
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: frames
</pre>
Moves the object towards the given coordinates.

It will slow down near the end of the movement based on the weight specified.

## ObjMove_SetDestAtInterpolate
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: frames
        5) real const: interpolationType
</pre>
Moves the object towards the given coordinates in the number of frames specified with the given [interpolation type](./docs_interpolation_types.html).

## ObjMove_AddPatternA1
<pre>
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speed
        4) real: angle
</pre>
After the specified number of frames, changes the speed and angle of the object.

NO_CHANGE can be used to preserve the original speed or angle.

## ObjMove_AddPatternA2
<pre>
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speed
        4) real: angle
        5) real: acceleration
        6) real: angularVelocity
        7) real: maxSpeed
</pre>
After the specified number of frames, changes the speed, angle, acceleration, angular velocity, and maximum speed of the object.

NO_CHANGE can be used to preserve the original speed, angle, acceleration, angular velocity, or maximum speed.

## ObjMove_AddPatternA3
<pre>
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speed
        4) real: angle
        5) real: acceleration
        6) real: angularVelocity
        7) real: maxSpeed
        8) real: shotGraphic
</pre>
After the specified number of frames, changes the speed, angle, acceleration, angular velocity, maximum speed, and shot graphic of the object.

NO_CHANGE can be used to preserve the original speed, angle, acceleration, angular velocity, maximum speed, or shot graphic.

## ObjMove_AddPatternA4
<pre>
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
</pre>
After the specified number of frames, changes the speed, angle, acceleration, angular velocity, maximum speed, and shot graphic of the object with angle being relative to the angle from the object to targetObjectID.

NO_CHANGE can be used to preserve the original speed, angle, acceleration, angular velocity, maximum speed, or shot graphic.\
The angle parameter is relative to the angle from the object to the target.\
For example, if GetPlayerObjectID is used as the target, an angle of 0 will cause the object to aim for the player.

## ObjMove_AddPatternB1
<pre>
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speedX
        4) real: speedY
</pre>
After the specified number of frames, changes the x and y movement speeds of the object.

NO_CHANGE can be used to preserve the original speeds.

## ObjMove_AddPatternB2
<pre>
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speedX
        4) real: speedY
        5) real: accelX
        6) real: accelY
        7) real: maxSpeedX
        8) real: maxSpeedY
</pre>
After the specified number of frames, changes the x and y speeds, accelerations, and maximum speeds of the object.

NO_CHANGE can be used to preserve the original x or y speeds, accelerations, and maximum speeds.

## ObjMove_AddPatternB3
<pre>
    Arguments:
        1) real: objectID
        2) real: frame
        3) real: speedX
        4) real: speedY
        5) real: accelX
        6) real: accelY
        7) real: maxSpeedX
        8) real: maxSpeedY
</pre>
After the specified number of frames, changes the x and y speeds, accelerations, maximum speeds, and shot graphic of the object.

NO_CHANGE can be used to preserve the original x or y speeds, accelerations, maximum speeds, and bullet graphic.

## ObjMove_GetX
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Gets the x-coordinate of the object.

If the object is deleted, this will return NULL_POS.

## ObjMove_GetY
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Gets the y-coordinate of the object.

If the object is deleted, this will return NULL_POS.

## ObjMove_GetSpeed
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the movement speed of the object.

## ObjMove_GetAngle
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the movement angle of the object.