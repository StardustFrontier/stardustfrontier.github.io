# Enemy Object Functions

[Return to Functions](./docs.html)

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

## ObjEnemy_SetLife
<pre>
    Arguments:
        1) real: objectID
        2) real: life
</pre>
Sets the amount of life points for the enemy object.

## ObjEnemy_AddLife
<pre>
    Arguments:
        1) real: objectID
        2) real: lifeToAdd
</pre>
Adds the amount of life points to the enemy object's current life.

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