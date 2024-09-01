# Shot Object Functions

[Return to Functions](./docs.html)

## ObjEnemy_Create
<pre>
    Arguments:
        1) real const: objectType
    Return Type:
        real
</pre>
Creates a shot object of the specified type and returns its ID.

Object types are:
<pre>
OBJ_SHOT
OBJ_LOOSE_LASER
OBJ_STRAIGHT_LASER
OBJ_CURVE_LASER
</pre>
In order to draw and fire the shot object and have it listed as an existing bullet, you have to register it using [ObjShot_Regist](objshot_regist).

## ObjShot_Regist
<pre>
    Arguments:
        1) real: objectID
</pre>
Activates the specified shot object.

Shot objects cannot be utilized until this functions is called.

## ObjShot_SetAutoDelete
<pre>
    Arguments:
        1) real: objectID
        2) bool: bAutoDelete
</pre>
Enables or disables auto-deletion of the shot object when outside of the screen boundaries.

Defaults to true.

## ObjShot_FadeDelete
<pre>
    Arguments:
        1) real: objectID
</pre>
Fades out the shot object and deletes it.

## ObjShot_SetDeleteFrame
<pre>
    Arguments:
        1) real: objectID
        2) real: frames
</pre>
Deletes the shot object after the specified number of frames.

## ObjShot_SetDelay
<pre>
    Arguments:
        1) real: objectID
        2) real: frames
</pre>
Delays the shot object, firing it after the specified number of frames.

Bullets will glow to announce delay; lasers will be shown very thin.

## ObjShot_SetSpellResist
<pre>
    Arguments:
        1) real: objectID
        2) bool: bSpellResist
</pre>
When set to true, the shot object will not be deleted by the player's spell.

Defaults to false.

## ObjShot_SetGraphic
<pre>
    Arguments:
        1) real: objectID
        2) real: graphicID
</pre>
Gives the shot object the specified graphic.

## ObjShot_SetSourceBlendType
<pre>
    Arguments:
        1) real: objectID
        2) real const: blendType
</pre>
Gives the shot object's delay graphic the specified [blend type](./docs_blend_types.html).

## ObjShot_SetDamage
<pre>
    Arguments:
        1) real: objectID
        2) real: damage
</pre>
Sets the damage of the specified shot object.

For player shots only.

## ObjShot_SetPenetration
<pre>
    Arguments:
        1) real: objectID
        2) real: penetration
</pre>
Sets the penetration of the shot object.

The shot object can hit enemies as many times as the penetration value before being deleted.\
For player shots only.

## ObjShot_SetEraseShot
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Enables/disables the ability to erase enemy shots when the specified shot object comes into contact with it.

Each time a shot is erased, the penetration of the shot object will go down by 1.\
For player shots only.

## ObjShot_SetSpellFactor
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether or not to use the spell damage factor for the shot object.

For player shots only.

## ObjShot_SetGrazeInvalidFrame
<pre>
    Arguments:
        1) real: objectID
        2) real: frames
</pre>
Sets the amount of frames that must pass before the specified shot can be grazed again.

Use GRAZE_INVALID_NONE to reset this value to normal.\
Default value is GRAZE_INVALID_NONE

## ObjShot_ToItem
<pre>
    Arguments:
        1) real: objectID
</pre>
Turns the bullet into an item.

## ObjShot_AddShotA1
<pre>
    Arguments:
        1) real: sourceObjectID
        2) real: targetObjectID
        3) real: frame
</pre>
At the specified frame, spawns the added shot object at the source shot object's position.

## ObjShot_AddShotA2
<pre>
    Arguments:
        1) real: sourceObjectID
        2) real: targetObjectID
        3) real: frame
        4) real: distance
        5) real: angle
</pre>
At the specified frame, spawns the added shot object at the specified distance and angle from the source shot object's position.

## ObjShot_SetIntersectionCircleA1
<pre>
    Arguments:
        1) real: objectID
        2) real: radius
</pre>
Creates a hitbox of specified radius for collision detection of the shot object.

In order to maintain the hitbox, it must be set every frame.\
There can be multiple hitboxes set for one shot object.\
At the specified frame, spawns the added shot object at the source shot object's position.

## ObjShot_SetIntersectionCircleA2
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: radius
</pre>
Creates a hitbox of specified radius for collision detection of the shot object.

In order to maintain the hitbox, it must be set every frame.\
There can be multiple hitboxes set for one shot object.

## ObjShot_SetIntersectionLine
<pre>
    Arguments:
        1) real: objectID
        2) real: x1
        3) real: y1
        4) real: x2
        5) real: y2
        6) real: width
</pre>
Creates a line segment hitbox between the specified coordinates for collision detection of the shot object.

In order to maintain the hitbox, it must be set every frame.\
There can be multiple hitboxes set for one shot object.

## ObjShot_SetIntersectionEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether collision detection of the shot object will be checked.

If set to false, the shot object will have no collision detection.

## ObjShot_SetItemChange
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether the shot object will turn into an item when deleted.

If set to false, the shot object will not turn into an item.

## ObjShot_GetDamage
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the damage of the specified shot object.

## ObjShot_GetPenetration
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the penetration of the specified shot object.

## ObjShot_GetDelay
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the number of frames remaining in the shot's delay.

## ObjShot_IsSpellResist
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns whether the shot object can be deleted by a player spell.

Shot object spell resistance can be set with ObjShot_SetSpellResist.

## ObjShot_GetGrazeStatus
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Returns true if the player is colliding with the specified shot's graze hitbox

## ObjShot_GetImageID
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the graphic ID of the shot object.

## ObjLaser_SetLength
<pre>
    Arguments:
        1) real: objectID
        2) real: length
</pre>
Sets the length of the laser object.

## ObjLaser_SetRenderWidth
<pre>
    Arguments:
        1) real: objectID
        2) real: renderWidth
</pre>
Sets the visible width of the laser object (not the same as the laser object's collision width).

## ObjLaser_SetIntersectionWidth
<pre>
    Arguments:
        1) real: objectID
        2) real: collisionWidth
</pre>
Sets the collision width of the laser object.

This can be set to be larger than the laser object's render width, so take caution.

## ObjLaser_SetGrazeInvalidFrame
<pre>
    Arguments:
        1) real: objectID
        2) real: grazeInvalidFrames
</pre>
Specify the number of frames after a graze where graze is not counted.

If you specify 0, the laser object can be grazed only once.\
The default value is 20 frames (3 graze/second).

## ObjLaser_SetInvalidLength
<pre>
    Arguments:
        1) real: objectID
        2) real: ratioBase
        3) real: ratioTip
</pre>
Sets the portion of the laser object where there is no collision, in relation to the base and the tip of the laser.

By default, the values are 10 (10%).

## ObjLaser_SetItemDistance
<pre>
    Arguments:
        1) real: objectID
        2) real: interval
</pre>
Sets the item occurrence interval when the laser object is deleted and changed into items.

## ObjLaser_GetLength
<pre>
    Arguments:
        1) real: objectID
</pre>
Returns the length of the laser object.

## ObjStLaser_SetAngle
<pre>
    Arguments:
        1) real: objectID
        2) real: angle
</pre>
Sets the angle at which the straight laser object will point at (different from movement angle).

## ObjStLaser_GetAngle
<pre>
    Arguments:
        1) real: objectID
</pre>
Returns the angle at which the straight laser object is pointing (different from movement angle).

## ObjStLaser_SetSource
<pre>
    Arguments:
        1) real: objectID
        2) bool: bDrawSource
</pre>
Sets whether the light source at the base of the straight laser object is drawn.

## ObjCrLaser_SetTipDecrement
<pre>
    Arguments:
        1) real: objectID
        2) real: reductionRate
</pre>
Sets the transparency reduction rate at the tip of the curved laser object.

Default is 1.0 (tip of laser is invisible).