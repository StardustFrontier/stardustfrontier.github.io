# Enemy Functions

[Return to Functions](./docs.html)

## GetEnemyBossSceneObjectID
<pre>
    Return Type:
        real
</pre>
Returns the boss scene object ID or ID_INVALID when not in a boss scene.

## GetEnemyBossObjectID
<pre>
    Return Type:
        real array
</pre>
Returns an array consisting of the object ID of the boss present on the screen.

## GetAllEnemyID
<pre>
    Return Type:
        real array
</pre>
Returns an array consisting of the object ID of every enemy present on the screen.

## GetIntersectionRegistedEnemyID
<pre>
    Return Type:
        real array
</pre>
Returns an array consisting of the object ID of all enemies with a registered hitbox to player shots (via ObjEnemy_SetIntersectionCircleToShot()).

## GetAllEnemyIntersectionPosition
<pre>
    Return Type:
        2D real array
</pre>
Returns the position of all enemies for which collision detection is true (currently intersecting) as a 2D array.

Return format is [index][<x coordinate, y coordinate>].

## GetEnemyIntersectionPosition
<pre>
    Arguments:
        1) x
        2) y
        3) acquisitionValue
    Return Type:
        2D real array
</pre>
Returns the enemy intersection position around the given position with acquisitionValue priority as a 2D array.

Return format is [index][<x coordinate, y coordinate>].\
The first possible acquisition value (index 0) corresponds to the nearest enemy to the provided x and y coordinates.

## GetEnemyIntersectionPositionByIdA1
<pre>
    Arguments:
        1) real: enemyObjectID
    Return Type:
        2D real array
</pre>
Returns all collision detection positions of the specified enemy as a 2D array.

Return format is [index][<x coordinate, y coordinate>].

## GetEnemyIntersectionPositionByIdA2
<pre>
    Arguments:
        1) real: enemyObjectID
        2) real: x
        3) real: y
    Return Type:
        2D real array
</pre>
Returns all collision detection positions of the specified enemy closest to the given coordinates as a 2D array.

Return format is [index][<x coordinate, y coordinate>].\
The first index (index 0) corresponds to the nearest intersection position from the provided x and y coordinates.

## GetNearestEnemyIntersectionIdA1
<pre>
    Arguments:
        1) real: x
        2) real: y
    Return Type:
        real
</pre>
Returns the nearest enemy object ID to the given coordinates with intersection enabled.

## LoadEnemyShotData
<pre>
    Arguments:
        1) string: path
    Return Type:
        bool
</pre>
Loads specified shot data file and returns true if successful.

Files with the same name can only be loaded once.

## ReloadEnemyShotData
<pre>
    Arguments:
        1) string: path
    Return Type:
        bool
</pre>
Reloads specified shot data file.

Unlike LoadEnemyShotData, this function can load the same file several times.\
You can also (re)load a file that has not been loaded by LoadEnemyShotData.