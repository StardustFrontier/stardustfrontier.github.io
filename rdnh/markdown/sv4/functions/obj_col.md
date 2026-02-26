# ObjCol Functions

[Return to Functions](../functions.html)

## ObjCol_IsIntersected
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if the specified object is currently intersecting with another object.

## ObjCol_GetListOfIntersectedEnemyID
```
    Arguments:
        1) real: objectID
    Return Type:
        array[real]
```
Returns an array of all enemy object IDs that the specified object is currently intersecting with.

## ObjCol_StoreListOfIntersectedEnemyID
```
    Arguments:
        1) real: objectID
        2) array: storageArray
```
Stores all enemy object IDs that the specified object is currently intersecting with in storageArray.

## ObjCol_StoreListOfIntersectedShotID
```
    Arguments:
        1) real: objectID
        2) array: storageArray
        3) real const: owner
```
Stores all shot object IDs of the specified owner type currently intersecting with the object in storageArray.

owner can be:
```
OWNER_ENEMY
OWNER_PLAYER
```

## ObjCol_StoreListOfIntersectedItemID
```
    Arguments:
        1) real: objectID
        2) array: storageArray
```
Stores all item object IDs that the specified object is currently intersecting with in storageArray.

## ObjCol_GetIntersectedCount
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the number of times the specified object intersected with other objects during the previous frame.

For example, this can be used to determine how many player shots have collided with an enemy.