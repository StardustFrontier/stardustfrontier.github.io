# ObjCol Functions

[Return to Functions](../functions.html)

## ObjCol_IsIntersected
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Returns true if the specified object is currently intersecting with another object.

## ObjCol_GetListOfIntersectedEnemyID
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        array[real]
</pre>
Returns an array of all enemy object IDs that the specified object is currently intersecting with.

## ObjCol_StoreListOfIntersectedEnemyID
<pre>
    Arguments:
        1) real: objectID
        2) array: storageArray
</pre>
Stores all enemy object IDs that the specified object is currently intersecting with in storageArray.

## ObjCol_StoreListOfIntersectedShotID
<pre>
    Arguments:
        1) real: objectID
        2) array: storageArray
        3) real const: owner
</pre>
Stores all shot object IDs of the specified owner type currently intersecting with the object in storageArray.

owner can be:
<pre>
OWNER_ENEMY
OWNER_PLAYER
</pre>

## ObjCol_StoreListOfIntersectedItemID
<pre>
    Arguments:
        1) real: objectID
        2) array: storageArray
</pre>
Stores all item object IDs that the specified object is currently intersecting with in storageArray.

## ObjCol_GetIntersectedCount
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the number of times the specified object intersected with other objects during the previous frame.

For example, this can be used to determine how many player shots have collided with an enemy.