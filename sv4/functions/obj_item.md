# ObjItem Functions

[Return to Functions](../functions.html)

## ObjItem_Create
<pre>
    Arguments:
        1) real: itemID
    Return Type:
        real
</pre>
Creates an item object of the specified itemID and returns its object ID.

In order to draw the item object and have it listed as an existing item, you have to register it using [ObjItem_Regist](objitem_regist).\

## ObjItem_Regist
<pre>
    Arguments:
        1) real: objectID
</pre>
Activates the specified item object.

Item objects created with [ObjItem_Create](objitem_create) cannot be utilized until this functions is called.

## ObjItem_SetItemID
<pre>
    Arguments:
        1) real: objectID
        2) real: itemID
</pre>
Sets the ID of the item object, as defined in the item definition script.

## ObjItem_SetRenderScoreEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether a score indicator will be displayed when the item object is collected.

This is the score given as argument to the CreateItem() functions.

## ObjItem_SetPlayerAbsorbEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether the item will be pulled towards the player when it is within the player's item absorb radius.

## ObjItem_SetAutoCollectEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether the item will be pulled towards the player when the player moves past the point of auto-collection.

## ObjItem_SetAutoCollectSpeed
<pre>
    Arguments:
        1) real: objectID
        2) real: autoCollectSpeed
</pre>
Sets the speed at which the items are pulled towards the player during auto-collection.

## ObjItem_SetAutoCollectAcceleration
<pre>
    Arguments:
        1) real: objectID
        2) real: acceleration
</pre>
Sets the acceleration for auto-collection, which is added to its speed every frame.

If non-zero, auto-collection will begin at the item's current speed, accelerating to the auto-collection speed.\
In other words, auto-collection speed will be considered the max speed instead of instantly being set.\
Defaults to 0.

## ObjItem_SetDefinedMovePatternA1
<pre>
    Arguments:
        1) real: objectID
        2) real const: movementType
</pre>
Sets the movement type of the item object.

Available movement types are:
<pre>
ITEM_MOVE_DOWN - immediately drops down
ITEM_MOVE_TOPLAYER - automatically flies towards the player
</pre>

## ObjItem_SetMoveToPlayer
<pre>
    Arguments:
        1) real: objectID
        2) bool: enable
</pre>
Instantly enables or disables the object flying towards the player's position.

## ObjItem_SetWeight
<pre>
    Arguments:
        1) real: objectID
        2) real: weight
</pre>
Sets the weight for the item object's movement, used when calculating the slowing down of the item spawn.

This is similar to the weight in ObjMove_SetDestAtWeight.\
Note: For items created with CreateItemU3, this function has no effect.

## ObjItem_SetAcceleration
<pre>
    Arguments:
        1) real: objectID
        2) real: acceleration
</pre>
Sets the acceleration for the item object's movement, which is added to its speed every frame.

For CreateItemU3, this is the overall acceleration.\
For all other types, this is the acceleration used for the fall speed once the item object begins moving down.

## ObjItem_SetMaxSpeed
<pre>
    Arguments:
        1) real: objectID
        2) real: maxSpeed
</pre>
Sets the max speed that can be reached by acceleration for the object's movement.

For CreateItemU3, this is the max speed the item object can reach from acceleration overall.\
For all other types, this is the max speed of the item object falling once it begins moving down.

## ObjItem_SetIntersectionEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
Sets whether collision detection of the item object will be checked.

If set to false, the item object will have no collision detection.

## ObjItem_GetIntersectionEnable
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns whether ObjItem_SetIntersectionEnable was set to true or false on the item object.

## ObjItem_GetItemID
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the item object's itemID.

## ObjItem_GetMoveType
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real const
</pre>
Returns the item object's move type.

## ObjItem_GetInfo
<pre>
    Arguments:
        1) real: objectID
        2) real const: infoType
    Return Type:
        varies
</pre>
Returns info about the item object based on the given info type constant.

Available info types are:
<pre>
INFO_ITEM_SCORE - Returns the score value of the item object (real)
</pre>