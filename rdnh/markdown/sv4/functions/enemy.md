# Enemy Functions

[Return to Functions](../functions.html)

## GetEnemyBossSceneObjectID
```
    Return Type:
        real
```
Returns the boss scene object ID or ID_INVALID when not in a boss scene.

## GetEnemyBossObjectID
```
    Return Type:
        real array
```
Returns an array consisting of the object ID of the boss present on the screen.

## GetEnemyIdInCircle
```
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
        4) real: enemyObjectType
    Return Type
        array[real]
```
Returns the object IDs of the enemies inside the given circle with the specified enemy object type in an array.

enemyObjectType can be:
```
OBJ_ENEMY
OBJ_ENEMY_BOSS
```

## StoreEnemyIdInCircle
```
    Arguments:
        1) array: storageArray
        2) real: x
        3) real: y
        4) real: radius
        5) real: enemyObjectType
```
Stores the object IDs of the enemies inside the given circle with the specified enemy object type in storageArray.\
This is faster than the _Get_ version if the array has been pre-reserved to an adequate size with array_reserve.

enemyObjectType can be:
```
OBJ_ENEMY
OBJ_ENEMY_BOSS
```

## GetAllEnemyID
```
    Return Type:
        real array
```
Returns an array consisting of the object ID of every enemy present on the screen.

## GetIntersectionRegistedEnemyID
```
    Return Type:
        real array
```
Returns an array consisting of the object ID of all enemies with a registered hitbox to player shots (via ObjEnemy_SetIntersectionCircleToShot()).

## GetAllEnemyIntersectionPosition
```
    Return Type:
        2D real array
```
Returns the position of all enemies for which collision detection is true (currently intersecting) as a 2D array.

Return format is [index][<x coordinate, y coordinate>].

## GetEnemyIntersectionPosition
```
    Arguments:
        1) x
        2) y
        3) acquisitionValue
    Return Type:
        2D real array
```
Returns the enemy intersection position around the given position with acquisitionValue priority as a 2D array.

Return format is [index][<x coordinate, y coordinate>].\
The first possible acquisition value (index 0) corresponds to the nearest enemy to the provided x and y coordinates.

## GetEnemyIntersectionPositionByIdA1
```
    Arguments:
        1) real: enemyObjectID
    Return Type:
        2D real array
```
Returns all collision detection positions of the specified enemy as a 2D array.

Return format is [index][<x coordinate, y coordinate>].

## GetEnemyIntersectionPositionByIdA2
```
    Arguments:
        1) real: enemyObjectID
        2) real: x
        3) real: y
    Return Type:
        2D real array
```
Returns all collision detection positions of the specified enemy closest to the given coordinates as a 2D array.

Return format is [index][<x coordinate, y coordinate>].\
The first index (index 0) corresponds to the nearest intersection position from the provided x and y coordinates.

## GetNearestEnemyIntersectionIdA1
```
    Arguments:
        1) real: x
        2) real: y
    Return Type:
        real
```
Returns the nearest enemy object ID to the given coordinates with intersection enabled.

## GetNearestEnemyIntersectionIdA2
```
    Arguments:
        1) real: x
        2) real: y
        3) real: minDist
    Return Type:
        real
```
Returns the nearest enemy object ID to the given coordinates with the given minimum distance with intersection enabled.

## SetEnemyAutoDeleteClip
```
    Arguments:
        1) real: left
        2) real: right
        3) real: top
        4) real: bottom
```
Sets the margin that enemy objects are allowed to traverse past the edges of the STG field before getting automatically deleted.

Defaults to (64, 64, 64, 64).

## LoadEnemyShotData
```
    Arguments:
        1) string: path
    Return Type:
        bool
```
Loads specified shot data file and returns true if successful.

Files with the same name can only be loaded once.

## ReloadEnemyShotData
```
    Arguments:
        1) string: path
    Return Type:
        bool
```
Reloads specified shot data file.

Unlike LoadEnemyShotData, this function can load the same file several times.\
You can also (re)load a file that has not been loaded by LoadEnemyShotData.