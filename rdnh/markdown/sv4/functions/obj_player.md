# ObjPlayer Functions

[Return to Functions](../functions.html)

## ObjPlayer_AddIntersectionCircleA1
```
    Arguments:
        1) real: objectID
        2) real: collisionX
        3) real: collisionY
        4) real: collisionRadius
        5) real: grazeRadius
```
Creates a hitbox of specified radius for collision detection of the player object.

The graze area extends the specified radius around the hitbox (the true graze radius is the sum of the two).\
The hitbox will remain valid for every frame once created.

## ObjPlayer_AddIntersectionCircleA2
```
    Arguments:
        1) real: objectID
        2) real: grazeX
        3) real: grazeY
        4) real: grazeRadius
```
Creates a grazebox of specified radius for the player object.

The grazebox will remain valid for every frame once created.

## ObjPlayer_ClearIntersection
```
    Arguments:
        1) real: objectID
```
Deletes all hitboxes of the player object.