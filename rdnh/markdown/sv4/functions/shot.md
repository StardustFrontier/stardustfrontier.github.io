# Shot Functions

[Return to Functions](../functions.html)

## DeleteShotAll
```
    Arguments:
        1) real const: type
        2) real const: deleteType
```
Deletes all shot objects on screen matching the criteria, utilizing the selected deletion type.

type can be:
```
TYPE_ALL (all shot objects)
TYPE_SHOT (shot objects without spell resistance)
TYPE_CHILD (shot objects fired from the currently running script)
```
deleteType can be:
```
TYPE_IMMEDIATE (immediately delete the bullets)
TYPE_FADE (slowly fade out the bullets)
TYPE_ITEM (turn the bullets into items according to the running item script)
Note: With TYPE_FADE, bullets will still be visible while fading out, but they will not have any collision.
```

## DeleteShotInCircle
```
    Arguments:
        1) real const: type
        2) real const: deleteType
        3) real: x
        4) real: y
        5) real: radius
```
Deletes all shot objects matching the criteria in the designated circle centered at (x, y) with provided radius, utilizing the selected deletion type.

type can be:
```
TYPE_ALL (all shot objects)
TYPE_SHOT (shot objects without spell resistance)
TYPE_CHILD (shot objects fired from the currently running script)
```
deleteType can be:
```
TYPE_IMMEDIATE (immediately delete the bullets)
TYPE_FADE (slowly fade out the bullets)
TYPE_ITEM (turn the bullets into items according to the running item script)
Note: With TYPE_FADE, bullets will still be visible while fading out, but they will not have any collision.
```

## CreateShotA1
```
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: graphic
        6) real: delay
    Return Type:
        real
```
Creates a basic bullet that will move at the angle and speed defined. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotA2
```
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: acceleration
        6) real: maxSpeed
        7) real: graphic
        8) real: delay
    Return Type:
        real
```
Creates a bullet that will move at the angle and speed defined, incrementing its speed by acceleration every frame, capping at maxspeed. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotOA1
```
    Arguments:
        1) real: parentObjectID
        2) real: speed
        3) real: angle
        4) real: graphic
        5) real: delay
    Return Type:
        real
```
Creates a bullet that will spawn on the coordinates of the given object id and will move at the angle and speed defined. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotB1
```
    Arguments:
        1) real: x
        2) real: y
        3) real: xSpeed
        4) real: ySpeed
        5) real: graphic
        6) real: delay
    Return Type:
        real
```
Creates a bullet that will move at the specified x and y speeds. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotB2
```
    Arguments:
        1) real: x
        2) real: y
        3) real: xSpeed
        4) real: ySpeed
        5) real: xAcceleration
        6) real: yAcceleration
        7) real: xMaxSpeed
        8) real: yMaxSpeed
        9) real: graphic
        10) real: delay
    Return Type:
        real
```
Creates a bullet that will move at the specified x and y speeds, incrementing its speed components by the respective acceleration component every frame, capping at the maxspeed for each component. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotOB1
```
    Arguments:
        1) real: parentObjectID
        2) real: xSpeed
        3) real: ySpeed
        4) real: graphic
        5) real: delay
    Return Type:
        real
```
Creates a bullet that will spawn on the coordinates of the given object id and will move at the specified x and y speeds. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateLooseLaserA1
```
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: length
        6) real: width
        7) real: graphic
        8) real: delay
    Return Type:
        real
```
Creates a loose (moving) laser that will move at the angle and speed defined, with its size defined by the length (in direction of travel) and width. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the laser will appear.\
During it's delay, there will be a collisionless cloud that appears where the laser will spawn.\
Returns a void value in a player script if the player is unable to shoot.\
This function can be used to create larger bullets.

## CreateStraightLaserA1
```
    Arguments:
        1) real: x
        2) real: y
        3) real: angle
        4) real: length
        5) real: width
        6) real: deleteTime
        7) real: graphic
        8) real: delay
    Return Type:
        real
```
Creates a straight laser mounted at the position provided, with its size defined by the length (in direction of travel) and width. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the laser will appear.\
The <scode>deleteTime</scode> argument determines how many frames until the laser disappears.\
During the delay, the laser will appear as a very thin laser that has no collision (AKA delay laser) in order to give the player a warning.\
Having no delay while using this function is not advisable, as the laser will spawn at full size the moment the delay is over.\
Returns a void value in a player script if the player is unable to shoot.

## CreateCurveLaserA1
```
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: length
        6) real: width
        7) real: graphic
        8) real: delay
    Return Type:
        real
```
Creates a curve laser that will move at the angle and speed defined, with its size defined by the length (in direction of travel) and width. Also returns its object ID.

<scode>graphic</scode> is the image the bullet will have, while <scode>delay</scode> is the time in frames before the laser will appear.\
During it's delay, there will be a collisionless cloud that appears where the laser will spawn.\
Returns a void value in a player script if the player is unable to shoot.\
Use ObjMove_SetAngularVelocity to adjust the curve of this laser.\
This function is heavy to process, so having many curve lasers on-screen at the same time is not recommended.

## SetShotIntersectionCircle
```
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
```
Adds a circular player hitbox at the specified position with the provided radius.

Note: Lasts one frame.

## SetShotIntersectionLine
```
    Arguments:
        1) real: x1
        2) real: y1
        3) real: x2
        4) real: y2
        5) real: width
```
Adds a linear player hitbox between the two specified positions with the provided width.

Note: Lasts one frame.

## GetShotIdInCircleA1
```
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
    Return Type
        array[real]
```
Returns the object IDs of the bullets inside the given circle in an array.

Inside a player script, it will only return enemy bullet IDs, and vice versa.

## GetShotIdInCircleA2
```
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
        4) real const: target
    Return Type
        array[real]
```
Returns the object IDs of the bullets inside the given circle with the specified target type in an array.

target can be:
```
TARGET_ALL (all shots)
TARGET_ENEMY (enemy shots only)
TARGET_PLAYER (player shots only)
```

## GetAllShotID
```
    Arguments:
        1) real const: target
    Return Type
        array[real]
```
Returns the object IDs of all bullets with the specified target type in an array.

target can be:
```
TARGET_ALL (all shots)
TARGET_ENEMY (enemy shots only)
TARGET_PLAYER (player shots only)
```

## StoreShotIdInCircleA1
```
    Arguments:
        1) array: storageArray
        2) real: x
        3) real: y
        4) real: radius
```
Stores the object IDs of the bullets inside the given circle in storageArray.\
This is faster than the _Get_ version if the array has been pre-reserved to an adequate size with array_reserve.

Inside a player script, it will only return enemy bullet IDs, and vice versa.

## StoreShotIdInCircleA2
```
    Arguments:
        1) array: storageArray
        2) real: x
        3) real: y
        4) real: radius
        5) real const: target
```
Stores the object IDs of the bullets inside the given circle with the specified target type in storageArray.\
This is faster than the _Get_ version if the array has been pre-reserved to an adequate size with array_reserve.

target can be:
```
TARGET_ALL (all shots)
TARGET_ENEMY (enemy shots only)
TARGET_PLAYER (player shots only)
```

## StoreAllShotID
```
    Arguments:
        1) array: storageArray
        2) real const: target
```
Stores the object IDs of all bullets with the specified target type in an array.\
This is faster than the _Get_ version if the array has been pre-reserved to an adequate size with array_reserve.

target can be:
```
TARGET_ALL (all shots)
TARGET_ENEMY (enemy shots only)
TARGET_PLAYER (player shots only)
```

## GetShotCount
```
    Arguments:
        1) real const: target
    Return Type
        real
```
Returns the number of bullets with the specified target type.

target can be:
```
TARGET_ALL (all shots)
TARGET_ENEMY (enemy shots only)
TARGET_PLAYER (player shots only)
```

## SetShotAutoDeleteClip
```
    Arguments:
        1) real: left
        2) real: top
        3) real: right
        4) real: bottom
```
Sets at what point bullets will be automatically deleted when leaving the STG screen.

To override this auto deletion, use ObjShot_SetAutoDelete on the bullet you want to prevent from auto deleting.\
Defaults to (64, 64, 64, 64).

## SetShotTextureFilter
```
    Arguments:
        1) real const: filterMin
        2) real const: filterMag
```
Sets the min and mag texture filtering modes for rendering all shot objects.

Defaults to FILTER_LINEAR for both.

## SetShotGrazeInvalidFrame
```
    Arguments:
        1) real: frames
```
Sets the default amount of frames that must pass before the shot can be grazed again.

Use GRAZE_INVALID_NONE to reset this value to normal.\
Defaults to GRAZE_INVALID_NONE.

## SetShotIntersectionActiveRadius
```
    Arguments:
        1) real: radius
```
Sets the radius from the player in which shot intersection is enabled.

When shots are within this radius, intersection will automatically be enabled, otherwise it will be disabled.\
Defaults to 0, which disables this feature.

## GetShotIntersectionActiveRadius
```
    Return Type:
        real
```
Returns the active intersection radius for shots.

Defaults to 0.

## SetShotMovementEnable
```
    Arguments:
        1) bool: bEnable
```
Enables or disables movement processing for all shot objects.

## IsShotMovementEnable
```
    Return Type:
        bool
```
Returns whether or not shot movement processing is enabled.

## GetShotDataInfoA1
```
    Arguments:
        1) real: graphic
        2) real const: targetShotData
        3) real const: infoType
    Return Type:
        varies
```
Returns information from the shotdata depending on the information requested.

targetShotData can be `TARGET_PLAYER` or `TARGET_ENEMY`.\
infotype can be:
```
INFO_RECT (returns [left, top, right, bottom] for the graphic)
INFO_DELAY_COLOR (returns [red, green, blue] for the graphic)
INFO_BLEND (returns blend type for the graphic)
INFO_COLLISION (returns radius of collision detection)
INFO_COLLISION_LIST (returns 2D array of collision hitbox radii and coordinates [radius, x, y])
INFO_FIXED_ANGLE (returns the value of fixed_angle)
```

## GetEnemyShotDataRect
```
    Arguments:
        1) real: graphic
    Return Type:
        array[real]
```
Returns the rect ([left, top, right, bottom]) for the graphic from the enemy shotdata.

## GetEnemyShotDataLayer
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the render layer for the graphic from the enemy shotdata.

## GetEnemyShotDataBlend
```
    Arguments:
        1) real: graphic
    Return Type:
        real const
```
Returns the blend type for the graphic from the enemy shotdata.

## GetEnemyShotDataAlpha
```
    Arguments:
        1) real: graphic
    Return Type:
        real const
```
Returns the alpha for the graphic from the enemy shotdata.

## GetEnemyShotDataDelayRect
```
    Arguments:
        1) real: graphic
    Return Type:
        array[real]
```
Returns the delay rect ([left, top, right, bottom]) for the graphic from the enemy shotdata.

## GetEnemyShotDataDelayColor
```
    Arguments:
        1) real: graphic
    Return Type:
        array[real]
```
Returns the delay color ([red, green, blue]) for the graphic from the enemy shotdata.

## GetEnemyShotDataDelayColorHex
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the delay color as a single integer value for the graphic from the enemy shotdata.

## GetEnemyShotDataDelayBlend
```
    Arguments:
        1) real: graphic
    Return Type:
        real const
```
Returns the delay blend type for the graphic from the enemy shotdata.

## GetEnemyShotDataAngularVelocity
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of angular_velocity for the graphic from the enemy shotdata.

## GetEnemyShotDataFixedAngle
```
    Arguments:
        1) real: graphic
    Return Type:
        bool
```
Returns the value of fixed_angle for the graphic from the enemy shotdata.

## GetEnemyShotDataCenterRotation
```
    Arguments:
        1) real: graphic
    Return Type:
        bool
```
Returns the value of center_rotation for the graphic from the enemy shotdata.

## GetEnemyShotDataRoundPosition
```
    Arguments:
        1) real: graphic
    Return Type:
        bool
```
Returns the value of round_position for the graphic from the enemy shotdata.

## GetEnemyShotDataAngleRounding
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of angle_rounding for the graphic from the enemy shotdata.

## GetEnemyShotDataUserValue0
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of user_0 for the graphic from the enemy shotdata.

## GetEnemyShotDataUserValue1
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of user_1 for the graphic from the enemy shotdata.

## GetEnemyShotDataUserValue2
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of user_2 for the graphic from the enemy shotdata.

## GetEnemyShotDataUserValue3
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of user_3 for the graphic from the enemy shotdata.

## GetEnemyShotDataCollision
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the radius of collision detection for the graphic from the enemy shotdata.

## GetEnemyShotDataCollisionList
```
    Arguments:
        1) real: graphic
    Return Type:
        array[array[real]]
```
Returns a 2D array of collision hitbox radii and coordinates [radius, x, y] for the graphic from the enemy shotdata.

## GetEnemyShotDataAnimationData
```
    Arguments:
        1) real: graphic
    Return Type:
        array[array[real]]
```
Returns a 2D array of animation_data [frame, left, top, right, bottom] for the graphic from the enemy shotdata.

## GetPlayerShotDataRect
```
    Arguments:
        1) real: graphic
    Return Type:
        array[real]
```
Returns the rect ([left, top, right, bottom]) for the graphic from the player shotdata.

## GetPlayerShotDataLayer
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the render layer for the graphic from the player shotdata.

## GetPlayerShotDataBlend
```
    Arguments:
        1) real: graphic
    Return Type:
        real const
```
Returns the blend type for the graphic from the player shotdata.

## GetPlayerShotDataAlpha
```
    Arguments:
        1) real: graphic
    Return Type:
        real const
```
Returns the alpha for the graphic from the player shotdata.

## GetPlayerShotDataDelayRect
```
    Arguments:
        1) real: graphic
    Return Type:
        array[real]
```
Returns the delay rect ([left, top, right, bottom]) for the graphic from the player shotdata.

## GetPlayerShotDataDelayColor
```
    Arguments:
        1) real: graphic
    Return Type:
        array[real]
```
Returns the delay color ([red, green, blue]) for the graphic from the player shotdata.

## GetPlayerShotDataDelayColorHex
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the delay color as a single integer value for the graphic from the player shotdata.

## GetPlayerShotDataDelayBlend
```
    Arguments:
        1) real: graphic
    Return Type:
        real const
```
Returns the delay blend type for the graphic from the player shotdata.

## GetPlayerShotDataAngularVelocity
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of angular_velocity for the graphic from the player shotdata.

## GetPlayerShotDataFixedAngle
```
    Arguments:
        1) real: graphic
    Return Type:
        bool
```
Returns the value of fixed_angle for the graphic from the player shotdata.

## GetPlayerShotDataCenterRotation
```
    Arguments:
        1) real: graphic
    Return Type:
        bool
```
Returns the value of center_rotation for the graphic from the player shotdata.

## GetPlayerShotDataRoundPosition
```
    Arguments:
        1) real: graphic
    Return Type:
        bool
```
Returns the value of round_position for the graphic from the player shotdata.

## GetPlayerShotDataAngleRounding
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of angle_rounding for the graphic from the player shotdata.

## GetPlayerShotDataUserValue0
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of user_0 for the graphic from the player shotdata.

## GetPlayerShotDataUserValue1
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of user_1 for the graphic from the player shotdata.

## GetPlayerShotDataUserValue2
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of user_2 for the graphic from the player shotdata.

## GetPlayerShotDataUserValue3
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the value of user_3 for the graphic from the player shotdata.

## GetPlayerShotDataCollision
```
    Arguments:
        1) real: graphic
    Return Type:
        real
```
Returns the radius of collision detection for the graphic from the player shotdata.

## GetPlayerShotDataCollisionList
```
    Arguments:
        1) real: graphic
    Return Type:
        array[array[real]]
```
Returns a 2D array of collision hitbox radii and coordinates [radius, x, y] for the graphic from the player shotdata.


## GetPlayerShotDataAnimationData
```
    Arguments:
        1) real: graphic
    Return Type:
        array[array[real]]
```
Returns a 2D array of animation_data [frame, left, top, right, bottom] for the graphic from the player shotdata.

## StartShotScript
```
    Arguments:
        1) string: path
```
Starts the specified shot script.