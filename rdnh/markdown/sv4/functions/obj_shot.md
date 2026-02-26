# Shot Object Functions

[Return to Functions](../functions.html)

## ObjEnemy_Create
```
    Arguments:
        1) real const: objectType
    Return Type:
        real
```
Creates a shot object of the specified type and returns its ID.

Object types are:
```
OBJ_SHOT
OBJ_LOOSE_LASER
OBJ_STRAIGHT_LASER
OBJ_CURVE_LASER
```
In order to draw and fire the shot object and have it listed as an existing bullet, you have to register it using [ObjShot_Regist](objshot_regist).

## ObjShot_Regist
```
    Arguments:
        1) real: objectID
```
Activates the specified shot object.

Shot objects cannot be utilized until this functions is called.

## ObjShot_SetAutoDelete
```
    Arguments:
        1) real: objectID
        2) bool: bAutoDelete
```
Enables or disables auto-deletion of the shot object when outside of the screen boundaries.

Defaults to true.

## ObjShot_FadeDelete
```
    Arguments:
        1) real: objectID
```
Fades out the shot object and deletes it.

## ObjShot_SetDeleteFrame
```
    Arguments:
        1) real: objectID
        2) real: frames
```
Deletes the shot object after the specified number of frames.

## ObjShot_SetDelay
```
    Arguments:
        1) real: objectID
        2) real: frames
```
Delays the shot object, firing it after the specified number of frames.

Bullets will glow to announce delay; lasers will be shown very thin.

## ObjShot_SetSpellResist
```
    Arguments:
        1) real: objectID
        2) bool: bSpellResist
```
When set to true, the shot object will not be deleted by the player's spell.

Defaults to false.

## ObjShot_SetAutoDeleteDisableFrame
```
    Arguments:
        1) real: objectID
        2) real: time
```
Disables auto-deletion of the shot object when outside of the screen boundaries for the given amount of frames.

_**Note**: Manual calls to ObjShot_SetAutoDelete will interfere with/override this function's behavior._

## ObjShot_SetSpellResistFrame
```
    Arguments:
        1) real: objectID
        2) real: time
```
Prevents the shot object from being deleted by player spells for the given amount of frames.

_**Note**: Manual calls to ObjShot_SetSpellResist will interfere with/override this function's behavior._

## ObjShot_SetGraphic
```
    Arguments:
        1) real: objectID
        2) real: graphicID
```
Gives the shot object the specified graphic.

## ObjShot_SetCenterRotationEnable
```
    Arguments:
        1) real: objectID
        2) bool: enable
```
Enables or disables center rotation when rendering normal shot objects, which may improve the quality for some shots that spin using angular velocity.

This will override the shotdata center_rotation property.

## ObjShot_SetSourceBlendType
```
    Arguments:
        1) real: objectID
        2) real const: blendType
```
Gives the shot object's delay graphic the specified [blend type](./blend_types.html).

Note: This is an obsolete alias for ObjShot_SetDelayBlendType

## ObjShot_SetDelayBlendType
```
    Arguments:
        1) real: objectID
        2) real const: blendType
```
Gives the shot object's delay graphic the specified [blend type](./blend_types.html).

## ObjShot_SetDelayGraphic
```
    Arguments:
        1) real: objectID
        2) real: graphicID
```
Sets a graphicID from the shotdata to use as the shot object's delay cloud.

Set to -1 to reset this to the default delay associated with shot graphic.

## ObjShot_SetDelayMotionEnable
```
    Arguments:
        1) real: objectID
        2) bool: enable
```
Enables or disables motion during the shot object's delay period.

Only works with regular shots.\
Default is false.

## ObjShot_SetRenderOffsetX
```
    Arguments:
        1) real: objectID
        2) real: offsetX
```
Sets the x rendering position offset for the given shot object.

When rendering the shot, this offset value will be added to its final position.

_**Note**: This function does not work on curvy lasers._

## ObjShot_SetRenderOffsetY
```
    Arguments:
        1) real: objectID
        2) real: offsetY
```
Sets the y rendering position offset for the given shot object.

When rendering the shot, this offset value will be added to its final position.

_**Note**: This function does not work on curvy lasers._

## ObjShot_SetRenderOffsetXY
```
    Arguments:
        1) real: objectID
        2) real: offsetX
        3) real: offsetY
```
Sets the x and y rendering position offset for the given shot object.

When rendering the shot, this offset value will be added to its final position.

_**Note**: This function does not work on curvy lasers._

## ObjShot_GetRenderOffsetX
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the x render offset of the given shot object.

## ObjShot_GetRenderOffsetY
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the y render offset of the given shot object.

## ObjShot_SetDamage
```
    Arguments:
        1) real: objectID
        2) real: damage
```
Sets the damage of the specified shot object.

For player shots only.

## ObjShot_SetPenetration
```
    Arguments:
        1) real: objectID
        2) real: penetration
```
Sets the penetration of the shot object.

The shot object can hit enemies as many times as the penetration value before being deleted.\
For player shots only.

## ObjShot_SetEraseShot
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
Enables/disables the ability to erase enemy shots when the specified shot object comes into contact with it.

Each time a shot is erased, the penetration of the shot object will go down by 1.\
For player shots only.

## ObjShot_SetSpellFactor
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
Sets whether or not to use the spell damage factor for the shot object.

For player shots only.

## ObjShot_SetGrazeInvalidFrame
```
    Arguments:
        1) real: objectID
        2) real: frames
```
Sets the amount of frames that must pass before the specified shot can be grazed again.

Use GRAZE_INVALID_NONE to reset this value to normal.\
Default value is GRAZE_INVALID_NONE

Note: This is for normal shot objects only. Use [ObjLaser_SetGrazeInvalidFrame](#objlaser_setgrazeinvalidframe) for lasers.

## ObjShot_ToItem
```
    Arguments:
        1) real: objectID
```
Turns the bullet into an item.

## ObjShot_AddShotA1
```
    Arguments:
        1) real: sourceObjectID
        2) real: targetObjectID
        3) real: frame
```
At the specified frame, spawns the added shot object at the source shot object's position.

## ObjShot_AddShotA2
```
    Arguments:
        1) real: sourceObjectID
        2) real: targetObjectID
        3) real: frame
        4) real: distance
        5) real: angle
```
At the specified frame, spawns the added shot object at the specified distance and angle from the source shot object's position.

## ObjShot_SetIntersectionCircleA1
```
    Arguments:
        1) real: objectID
        2) real: radius
```
Creates a hitbox of specified radius for collision detection of the shot object.

In order to maintain the hitbox, it must be set every frame.\
There can be multiple hitboxes set for one shot object.\
At the specified frame, spawns the added shot object at the source shot object's position.

## ObjShot_SetIntersectionCircleA2
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: radius
```
Creates a hitbox of specified radius for collision detection of the shot object.

In order to maintain the hitbox, it must be set every frame.\
There can be multiple hitboxes set for one shot object.

## ObjShot_SetIntersectionLine
```
    Arguments:
        1) real: objectID
        2) real: x1
        3) real: y1
        4) real: x2
        5) real: y2
        6) real: width
```
Creates a line segment hitbox between the specified coordinates for collision detection of the shot object.

In order to maintain the hitbox, it must be set every frame.\
There can be multiple hitboxes set for one shot object.

## ObjShot_SetIntersectionEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
Sets whether collision detection of the shot object will be checked.

If set to false, the shot object will have no collision detection.

## ObjShot_GetIntersectionEnable
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns whether ObjShot_SetIntersectionEnable was set to true or false on the shot object.

## ObjShot_SetIntersectionScaleXY
```
    Arguments:
        1) real: objectID
        2) real: scaleX
        3) real: scaleY
```
_This function was ported from ph3sx._


Sets the shot object's X and Y hitbox scales.\
For normal shots, the true scale is the half-point between the X and Y scales.\
Currently this only works for normal shots.

Note: Ellipse hitboxes aren't possible with this feature.

## ObjShot_SetItemChange
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
Sets whether the shot object will turn into an item when deleted.

If set to false, the shot object will not turn into an item.

## ObjShot_GetDamage
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the damage of the specified shot object.

## ObjShot_GetPenetration
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the penetration of the specified shot object.

## ObjShot_GetDelay
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the number of frames remaining in the shot's delay.

## ObjShot_IsSpellResist
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns whether the shot object can be deleted by a player spell.

Shot object spell resistance can be set with ObjShot_SetSpellResist.

## ObjShot_GetGrazeStatus
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if the player is colliding with the specified shot's graze hitbox

## ObjShot_GetImageID
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the graphic ID of the shot object.

## ObjShot_GetIntersectionScaleX
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the intersection x scale set by ObjShot_SetIntersectionScaleXY.

## ObjShot_GetIntersectionScaleY
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the intersection y scale set by ObjShot_SetIntersectionScaleXY.

## ObjShot_AddTransform
```
    Arguments:
        1) real: objectID
        2) bool: bAsync
        3) real const: typeTransform
        4+) real: args...
    Return Type:
        real
```
Adds a transformation of the given [transformation type](./shot_transformation_types.html) to the shot object or pattern object and returns its index.

If bAsync is true, then this transform will execute at the same time as the previous one if supported,\
otherwise it will wait for the previous transform to finish first.

## ObjShot_SetTransform
```
    Arguments:
        1) real: objectID
        2) real: index
        3) bool: bAsync
        4) real const: typeTransform
        5+) real: args...
    Return Type:
        real
```
Sets a transformation of the given [transformation type](./shot_transformation_types.html) at the given index on the shot object or pattern object and returns the same index that was passed.

If the index is larger than the transformation list, empty slots before it will be filled with blank transforms that are skipped when executed.

If bAsync is true, then this transform will execute at the same time as the previous one if supported,\
otherwise it will wait for the previous transform to finish first.

## ObjShot_AddTransformFunc
```
    Arguments:
        1) real: objectID
        2) bool: bAsync
        3) real const: typeTransform
        4) function: argFunc
        5+) real: args...
    Return Type:
        real
```
Identical to ObjShot_AddTransform, but allows passing a function value as the first transform argument.

The `EX_FUNCTION` transform type must use this version of the function.

## ObjShot_SetTransformFunc
```
    Arguments:
        1) real: objectID
        2) real: index
        3) bool: bAsync
        4) real const: typeTransform
        5) function: argFunc
        6+) real: args...
    Return Type:
        real
```
Identical to ObjShot_SetTransform, but allows passing a function value as the first transform argument.

The `EX_FUNCTION` transform type must use this version of the function.

## ObjShot_FinishTransformFunction
```
    Arguments:
        1) real: objectID
```
Marks the shot object as being done with an `EX_FUNCTION` transform.

This disables the `EX_FUNCTION` transform and advances the transformation list.

## ObjShot_DisableTransform
```
    Arguments:
        1) real: objectID
        2) real const: typeTransform
```
Instantly disables a currently active transform of the given type on the shot object regardless of its progress.

## ObjLaser_SetLength
```
    Arguments:
        1) real: objectID
        2) real: length
```
Sets the length of the laser object.

## ObjLaser_SetRenderWidth
```
    Arguments:
        1) real: objectID
        2) real: renderWidth
```
Sets the visible width of the laser object (not the same as the laser object's collision width).

## ObjLaser_SetIntersectionWidth
```
    Arguments:
        1) real: objectID
        2) real: collisionWidth
```
Sets the collision width of the laser object.

This can be set to be larger than the laser object's render width, so take caution.

## ObjLaser_SetGrazeInvalidFrame
```
    Arguments:
        1) real: objectID
        2) real: grazeInvalidFrames
```
Specify the number of frames after a graze where graze is not counted.

If you specify 0, the laser object can be grazed only once.\
The default value is 20 frames (3 graze/second).

## ObjLaser_SetItemDistance
```
    Arguments:
        1) real: objectID
        2) real: interval
```
Sets the item occurrence interval when the laser object associated with objID is deleted and changed into items.

Defaults to 24.

## ObjLaser_TweenLength
```
    Arguments:
        1) real: objectID
        2) real: duration
        3) real const: interpType
        4) real: lengthEnd
```
Changes the laser object's length to lengthEnd over duration frames with the given interpolation type.

## ObjLaser_SetInvalidLength
```
    Arguments:
        1) real: objectID
        2) real: ratioBase
        3) real: ratioTip
```
Sets the portion of the laser object where there is no collision, in relation to the base and the tip of the laser.

By default, the values are 10 (10%).

## ObjLaser_SetItemDistance
```
    Arguments:
        1) real: objectID
        2) real: interval
```
Sets the item occurrence interval when the laser object is deleted and changed into items.

## ObjLaser_GetLength
```
    Arguments:
        1) real: objectID
```
Returns the length of the laser object.

## ObjStLaser_SetAngle
```
    Arguments:
        1) real: objectID
        2) real: angle
```
Sets the angle at which the straight laser object will point at (different from movement angle).

## ObjStLaser_GetAngle
```
    Arguments:
        1) real: objectID
```
Returns the angle at which the straight laser object is pointing (different from movement angle).

## ObjStLaser_SetSource
```
    Arguments:
        1) real: objectID
        2) bool: bDrawSource
```
Sets whether the light source at the base of the straight laser object is drawn.

## ObjStLaser_SetFadeType
```
    Arguments:
        1) real: objectID
        2) real const: fadeType
```
Sets the fade deletion type for the straight laser object.

Can be `FADE_LASER_SCALE`, `FADE_LASER_ALPHA`, or `FADE_LASER_NONE`.\
Defaults to `FADE_LASER_SCALE`.

## ObjStLaser_SetFadeTime
```
    Arguments:
        1) real: objectID
        2) real: time
```
Sets the duration of the straight laser's fade delete effect.

Defaults to 30 frames.

## ObjStLaser_DisableSpawnGrowth
```
    Arguments:
        1) real: objectID
```
Disables the initial "growth" effect on the straight laser object, resulting in it being spawned at the final size.

## ObjCrLaser_SetTipDecrement
```
    Arguments:
        1) real: objectID
        2) real: reductionRate
```
Sets the transparency reduction rate at the tip of the curved laser object.

Default is 1.0 (tip of laser is invisible).