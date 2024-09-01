# Collision Object Functions

[Return to Functions](./docs.html)

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
        real
</pre>
Returns an array of all enemy object IDs that the specified object is currently intersecting with.

## ObjCol_GetIntersectedCount
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the number of times the specified object intersected with other objects during the previous frame.

For example, this can be used to determine how many player shots have collided with an enemy.