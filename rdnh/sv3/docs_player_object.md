# Player Object Functions

[Return to Functions](./docs.html)

## ObjPlayer_AddIntersectionCircleA1
<pre>
    Arguments:
        1) real: objectID
        2) real: collisionX
        3) real: collisionY
        4) real: collisionRadius
        5) real: grazeRadius
</pre>
Creates a hitbox of specified radius for collision detection of the player object.

The graze area extends the specified radius around the hitbox (the true graze radius is the sum of the two).\
The hitbox will remain valid for every frame once created.

## ObjPlayer_AddIntersectionCircleA2
<pre>
    Arguments:
        1) real: objectID
        2) real: grazeX
        3) real: grazeY
        4) real: grazeRadius
</pre>
Creates a grazebox of specified radius for the player object.

The grazebox will remain valid for every frame once created.

## ObjPlayer_ClearIntersection
<pre>
    Arguments:
        1) real: objectID
</pre>
Deletes all hitboxes of the player object.