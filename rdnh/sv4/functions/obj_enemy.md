# ObjEnemy Functions

[Return to Functions](../functions.html)

## ObjEnemy_Create
<pre>
    Arguments:
        1) real const: objectType
    Return Type:
        real
</pre>
Creates an enemy object of the specified type and returns its ID.

Object types are:
<pre>
OBJ_ENEMY
OBJ_ENEMY_BOSS
</pre>
In order to draw the enemy object and have it listed as an existing enemy, you have to register it using ObjEnemy_Regist.\
If you want to create a boss enemy object, you have to create a boss scene object first.

## ObjEnemy_Regist
<pre>
    Arguments:
        1) real: objectID
</pre>
Activates the specified enemy object.

Enemy objects cannot be utilized until this functions is called.

## ObjEnemy_SetAutoDelete
<pre>
    Arguments:
        1) real: objectID
        2) bool: bAutoDelete
</pre>
Enables or disables auto-deletion of the enemy object when outside of horizontal and vertical boundaries set by SetEnemyAutoDeleteClip.

Equivalent to setting ObjEnemy_SetAutoDeleteHorizontal and ObjEnemy_SetAutoDeleteVertical to true.

Defaults to _false_ (unlike shot objects).

## ObjEnemy_SetAutoDeleteHorizontal
<pre>
    Arguments:
        1) real: objectID
        2) bool: bAutoDelete
</pre>
Enables or disables auto-deletion of the enemy object when outside of the left and right boundaries set by SetEnemyAutoDeleteClip.

Defaults to _false_.

## ObjEnemy_SetAutoDeleteVertical
<pre>
    Arguments:
        1) real: objectID
        2) bool: bAutoDelete
</pre>
Enables or disables auto-deletion of the enemy object when outside of the top and bottom boundaries set by SetEnemyAutoDeleteClip.

Defaults to _false_.

## ObjEnemy_SetDeleteFrame
<pre>
    Arguments:
        1) real: objectID
        2) real: frames
</pre>
Deletes the enemy object after the specified number of frames.

## ObjEnemy_SetInvincibilityFrame
<pre>
    Arguments:
        1) real: objectID
        2) real: frames
</pre>
Sets the number of frames for enemy invincibility.

Intersections will still be processed, but no damage will be dealt. (ObjEnemy_GetShotHitCount can return non-zero during invincibility)

## ObjEnemy_GetInvincibilityFrame
<pre>
    Arguments:
        1) real: objectID
    Returns:
        real: invincibilityFrames
</pre>
Returns the number of frames during which the enemy is invincible.

## ObjEnemy_GetInfo
<pre>
    Arguments:
        1) real: objectID
        2) real const: infoType
    Return Type:
        varies
</pre>
Returns info about the enemy object based on the given infoType constant.

Info types are:
<pre>
INFO_LIFE - Returns the life points of the enemy (real)
INFO_DAMAGE_RATE_SHOT - Returns the damage rate percentage of normal player shots set by ObjEnemy_SetDamageRate (real: 1-100)
INFO_DAMAGE_RATE_SPELL - Returns the damage rate percentage of player bombs set by ObjEnemy_SetDamageRate (real: 1-100)
INFO_SHOT_HIT_COUNT - Returns the amount of times the enemy was hit by player bullets in the previous frame (real)
</pre>

## ObjEnemy_GetLife
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the life of the enemy object.

## ObjEnemy_GetMaxLife
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the maximum life of the enemy object.

## ObjEnemy_GetPreviousFrameLife
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the previous frame life of the enemy object.

## ObjEnemy_GetShotDamageRate
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the damage rate percentage of normal player shots set by ObjEnemy_SetDamageRate.

## ObjEnemy_GetSpellDamageRate
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the damage rate percentage of player bombs set by ObjEnemy_SetDamageRate.

## ObjEnemy_GetMaximumDamage
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the maximum damage per frame set by ObjEnemy_SetMaximumDamage.

## ObjEnemy_GetShotHitCount
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the amount of times the enemy was hit by player bullets in the previous frame.

## ObjEnemy_GetExistTime
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the amount of frames the enemy object has existed for.

## ObjEnemy_SetLife
<pre>
    Arguments:
        1) real: objectID
        2) real: life
</pre>
Sets the amount of life for the enemy object.

## ObjEnemy_AddLife
<pre>
    Arguments:
        1) real: objectID
        2) real: lifeToAdd
</pre>
Adds the amount of life points to the enemy object's current life.

## ObjEnemy_AddLifeEx
<pre>
    Arguments:
        1) real: objectID
        2) real: lifeToAdd
</pre>
Adds life to the enemy object with respect to the enemy object's maximum damage.

Negative value (damaging) will count towards the maximum damage as if getting hit by a player shot.\
Positive value (healing) will reduce the damage count and allow more damage to be dealt in the frame equal to how much the healing was.

## ObjEnemy_SetDamageRate
<pre>
    Arguments:
        1) real: objectID
        2) real: shotDamageRate
        3) real: spellDamageRate
</pre>
Sets the damage rate of the player's attacks against the specified enemy.

Setting to 0 will cause the enemy to take no damage, 100 is the default (100%) value.\
Values above 100 are possible.\
Values below 0 are also possible, but may cause the boss health to overflow.

## ObjEnemy_SetMaximumDamage
<pre>
    Arguments:
        1) real: objectID
        2) real: maximumDamage
</pre>
Sets the maximum amount of damage that the enemy object can receive through normal means in a single frame.

Default value is uncapped.

## ObjEnemy_SetIntersectionCircleToShot
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: radius
</pre>
Sets the position and size of the enemy hitbox.

Any collision with player shots or spells with the circle will damage the enemy.\
*Note: This function must be called every frame to maintain the collision.*

## ObjEnemy_SetIntersectionCircleToPlayer
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: radius
</pre>
Sets the enemy hitbox for player collision.

Any collision with the circle will kill the player.\
*Note: This function must be called every frame to maintain the collision.*

## ObjEnemy_SetAutoIntersectionCircleToShot
<pre>
    Arguments:
        1) real: objectID
        2) real: radius
</pre>
Automatically sets the radius of the enemy-to-shot intersection circle each frame.

The position of the circle will be the enemy's current position.

## ObjEnemy_SetAutoIntersectionCircleToPlayer
<pre>
    Arguments:
        1) real: objectID
        2) real: radius
</pre>
Automatically sets the radius of the enemy-to-player intersection circle each frame.

The position of the circle will be the enemy's current position.

## ObjEnemy_SetEnableIntersectionPositionFetching
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
If set to false, the following functions will not include the specified enemy object's hitboxes:
<pre>
- GetEnemyIntersectionPosition
- GetEnemyIntersectionPositionByIdA1
- GetEnemyIntersectionPositionByIdA2
- GetAllEnemyIntersectionPosition
- GetNearestEnemyIntersectionIdA1
- GetNearestEnemyIntersectionIdA2
</pre>

## ObjEnemy_SetDeathFunc
<pre>
    Arguments:
        1) real: objectID
        2) function: deathFunc
</pre>
Calls the given function when the enemy reaches zero life.