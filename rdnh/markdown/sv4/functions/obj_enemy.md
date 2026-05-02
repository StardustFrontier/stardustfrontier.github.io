# ObjEnemy Functions

[Return to Functions](../functions.html)

## ObjEnemy_Create
```
    Arguments:
        1) real const: objectType
    Return Type:
        real
```
Creates an enemy object of the specified type and returns its ID.

Object types are:
```
OBJ_ENEMY
OBJ_ENEMY_BOSS
```
In order to draw the enemy object and have it listed as an existing enemy, you have to register it using ObjEnemy_Regist.\
If you want to create a boss enemy object, you have to create a boss scene object first.

## ObjEnemy_Regist
```
    Arguments:
        1) real: objectID
```
Activates the specified enemy object.

Enemy objects cannot be utilized until this functions is called.

## ObjEnemy_SetAutoDelete
```
    Arguments:
        1) real: objectID
        2) bool: bAutoDelete
```
Enables or disables auto-deletion of the enemy object when outside of horizontal and vertical boundaries set by SetEnemyAutoDeleteClip.

Equivalent to setting ObjEnemy_SetAutoDeleteHorizontal and ObjEnemy_SetAutoDeleteVertical to true.

Defaults to _false_ (unlike shot objects).

## ObjEnemy_SetAutoDeleteHorizontal
```
    Arguments:
        1) real: objectID
        2) bool: bAutoDelete
```
Enables or disables auto-deletion of the enemy object when outside of the left and right boundaries set by SetEnemyAutoDeleteClip.

Defaults to _false_.

## ObjEnemy_SetAutoDeleteVertical
```
    Arguments:
        1) real: objectID
        2) bool: bAutoDelete
```
Enables or disables auto-deletion of the enemy object when outside of the top and bottom boundaries set by SetEnemyAutoDeleteClip.

Defaults to _false_.

## ObjEnemy_SetDeleteFrame
```
    Arguments:
        1) real: objectID
        2) real: frames
```
Deletes the enemy object after the specified number of frames.

## ObjEnemy_SetInvincibilityFrame
```
    Arguments:
        1) real: objectID
        2) real: frames
```
Sets the number of frames for enemy invincibility.

Intersections will still be processed, but no damage will be dealt. (ObjEnemy_GetShotHitCount can return non-zero during invincibility)

## ObjEnemy_GetInvincibilityFrame
```
    Arguments:
        1) real: objectID
    Returns:
        real: invincibilityFrames
```
Returns the number of frames during which the enemy is invincible.

## ObjEnemy_GetInfo
```
    Arguments:
        1) real: objectID
        2) real const: infoType
    Return Type:
        varies
```
Returns info about the enemy object based on the given infoType constant.

Info types are:
```
INFO_LIFE - Returns the life points of the enemy (real)
INFO_DAMAGE_RATE_SHOT - Returns the damage rate percentage of normal player shots set by ObjEnemy_SetDamageRate (real: 1-100)
INFO_DAMAGE_RATE_SPELL - Returns the damage rate percentage of player bombs set by ObjEnemy_SetDamageRate (real: 1-100)
INFO_SHOT_HIT_COUNT - Returns the amount of times the enemy was hit by player bullets in the previous frame (real)
```

## ObjEnemy_GetLife
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the life of the enemy object.

## ObjEnemy_GetMaxLife
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the maximum life of the enemy object.

## ObjEnemy_GetPreviousFrameLife
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the previous frame life of the enemy object.

## ObjEnemy_GetShotDamageRate
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the damage rate percentage of normal player shots set by ObjEnemy_SetDamageRate.

## ObjEnemy_GetSpellDamageRate
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the damage rate percentage of player bombs set by ObjEnemy_SetDamageRate.

## ObjEnemy_GetMaximumDamage
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the maximum damage per frame set by ObjEnemy_SetMaximumDamage.

## ObjEnemy_GetShotHitCount
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the amount of times the enemy was hit by player bullets in the previous frame.

## ObjEnemy_GetExistTime
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the amount of frames the enemy object has existed for.

## ObjEnemy_SetLife
```
    Arguments:
        1) real: objectID
        2) real: life
```
Sets the amount of life for the enemy object.

## ObjEnemy_AddLife
```
    Arguments:
        1) real: objectID
        2) real: lifeToAdd
```
Adds the amount of life points to the enemy object's current life.

## ObjEnemy_AddLifeEx
```
    Arguments:
        1) real: objectID
        2) real: lifeToAdd
```
Adds life to the enemy object with respect to the enemy object's maximum damage.

Negative value (damaging) will count towards the maximum damage as if getting hit by a player shot.\
Positive value (healing) will reduce the damage count and allow more damage to be dealt in the frame equal to how much the healing was.

## ObjEnemy_SetDamageRate
```
    Arguments:
        1) real: objectID
        2) real: shotDamageRate
        3) real: spellDamageRate
```
Sets the damage rate of the player's attacks against the specified enemy.

Setting to 0 will cause the enemy to take no damage, 100 is the default (100%) value.\
Values above 100 are possible.\
Values below 0 are also possible, but may cause the boss health to overflow.

## ObjEnemy_SetMaximumDamage
```
    Arguments:
        1) real: objectID
        2) real: maximumDamage
```
Sets the maximum amount of damage that the enemy object can receive through normal means in a single frame.

Default value is uncapped.

## ObjEnemy_SetSharedLifeTarget
```
    Arguments:
        1) real: objectID
        2) real: targetObjectID
```
Makes it so the enemy object shares life with the target enemy object.

Whenever the enemy would have taken damage in any way, it will be redirected to the target object.

## ObjEnemy_GetSharedLifeTarget
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the target object that this enemy is sharing life with.

## ObjEnemy_SetTotalDamage
```
    Arguments:
        1) real: objectID
        2) real: totalDamage
```
Sets the total direct damage dealt to the enemy object since creation.

This should only be called to reset the value to 0 if needed.

## ObjEnemy_GetTotalDamage
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the total "intended" direct damage dealt to the enemy object since creation.

This always returns the amount of damage the enemy would have received even if it is taking no direct damage as a result of ObjEnemy_SetSharedLifeTarget\
If the enemy is a _target_ of another enemy object's shared life, then it will not include the damage done to the other enemy

## ObjEnemy_SetIntersectionCircleToShot
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: radius
```
Sets the position and size of the enemy hitbox.

Any collision with player shots or spells with the circle will damage the enemy.\
*Note: This function must be called every frame to maintain the collision.*

## ObjEnemy_SetIntersectionCircleToPlayer
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: radius
```
Sets the enemy hitbox for player collision.

Any collision with the circle will kill the player.\
*Note: This function must be called every frame to maintain the collision.*

## ObjEnemy_SetAutoIntersectionCircleToShot
```
    Arguments:
        1) real: objectID
        2) real: radius
```
Automatically sets the radius of the enemy-to-shot intersection circle each frame.

The position of the circle will be the enemy's current position.

## ObjEnemy_SetAutoIntersectionCircleToPlayer
```
    Arguments:
        1) real: objectID
        2) real: radius
```
Automatically sets the radius of the enemy-to-player intersection circle each frame.

The position of the circle will be the enemy's current position.

## ObjEnemy_SetEnableIntersectionPositionFetching
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
If set to false, the following functions will not include the specified enemy object's hitboxes:
```
- GetEnemyIntersectionPosition
- GetEnemyIntersectionPositionByIdA1
- GetEnemyIntersectionPositionByIdA2
- GetAllEnemyIntersectionPosition
- GetNearestEnemyIntersectionIdA1
- GetNearestEnemyIntersectionIdA2
```

## ObjEnemy_SetPreferredHomingTarget
```
    Arguments:
        1) real: objectID
        2) bool: bPreferred
```
Marks or unmarks an enemy object as a preferred target for homing player shots.

## ObjEnemy_IsPreferredHomingTarget
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if the enemy is marked as a preferred target for homing player shots, otherwise returns false.

## ObjEnemy_SetMovementBoundsEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
Sets whether or not the enemy's movement should be clamped to its movement bounds.

## ObjEnemy_IsMovementBoundsEnable
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns whether or not the enemy movement is currently set to be clamped to its movement bounds.

## ObjEnemy_SetMovementBounds
```
    Arguments:
        1) real: objectID
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
```
Sets the movement bounds for the enemy object relative to (0, 0) within the STG frame area.

## ObjEnemy_GetMovementBounds
```
    Arguments:
        1) real: objectID
    Return Type:
        real[]
```
Returns the movement bounds for the enemy object.

## ObjEnemy_SetHitEffectEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
Sets whether the engine should handle hit effects for the enemy object.

## ObjEnemy_SetHitEffectParam
```
    Arguments:
        1) real: objectID
        2) real: colorHex
        3) real: indexSoundHigh
        4) real: indexSoundLow
```
Sets the hit effect color, sound at high life, and sound at low life for the enemy object.

-1 can be passed for either sound argument to disable the sound.

_**Note**: Sound playback relies on using PlayStageSound internally. If the script has not been set up to use that, no sound will be played._

## ObjEnemy_SetHitEffectSoundOverride
```
    Arguments:
        1) real: objectID
        2) real: indexSound
```
ets a hit sound effect that overrides all other hit sounds for the enemy object.

-1 can be passed as the sound argument to disable overriding.

## ObjEnemy_SetDeathFunc
```
    Arguments:
        1) real: objectID
        2) function: deathFunc
```
Calls the given function when the enemy reaches zero life.