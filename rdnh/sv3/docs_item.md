# Item Functions

[Return to Functions](./docs.html)

## CreateItemA1
<pre>
    Arguments:
        1) real const: itemType
        2) real: x
        3) real: y
        4) real: score
    Return Type:
        real
</pre>
Creates an item of the provided itemType and score value at the specified x and y coordinates. Also returns its object ID.

Falling speeds can be tuned with the following functions:
- [ObjItem_SetWeight](./docs_item_object.html#objitem_setweight)
- [ObjItem_SetAcceleration](./docs_item_object.html#objitem_setacceleration)
- [ObjItem_SetMaxSpeed](./docs_item_object.html#objitem_setmaxspeed)

itemType can be one of the following:
<pre>
DS_ITEM_1UP and DS_ITEM_1UP_S (lives)
DS_ITEM_SPELL and DS_ITEM_SPELL_S (bombs)
DS_ITEM_POINT and DS_ITEM_POINT_S (points)
DS_ITEM_POWER and DS_ITEM_POWER_S (power)
DS_ITEM_USER (user-defined).
</pre>
The types ending in '_S' will create a smaller version of the specified item.

*Note: If either of the given coordinates are NULL_POS, the item will not be created.*

## CreateItemA2
<pre>
    Arguments:
        1) real const: itemType
        2) real: x
        3) real: y
        4) real: xDest
        5) real: yDest
        6) real: score
    Return Type:
        real
</pre>
Creates an item of the provided itemType and score value at the specified x and y coordinates that moves to the provided x and y destination coordinates before falling down. Also returns its object ID.

Falling speeds can be tuned with the following functions:
- [ObjItem_SetWeight](./docs_item_object.html#objitem_setweight)
- [ObjItem_SetAcceleration](./docs_item_object.html#objitem_setacceleration)
- [ObjItem_SetMaxSpeed](./docs_item_object.html#objitem_setmaxspeed)

itemType can be one of the following:
<pre>
DS_ITEM_1UP and DS_ITEM_1UP_S (lives)
DS_ITEM_SPELL and DS_ITEM_SPELL_S (bombs)
DS_ITEM_POINT and DS_ITEM_POINT_S (points)
DS_ITEM_POWER and DS_ITEM_POWER_S (power)
DS_ITEM_USER (user-defined).
</pre>
The types ending in '_S' will create a smaller version of the specified item.

*Note: If either of the given coordinates are NULL_POS, the item will not be created.*

## CreateItemU1
<pre>
    Arguments:
        1) real: itemID
        2) real: x
        3) real: y
        4) real: score
    Return Type:
        real
</pre>
Creates a user-defined item with the provided item ID and score value at the specified x and y coordinates. Also returns its object ID.

Falling speeds can be tuned with the following functions:
- [ObjItem_SetWeight](./docs_item_object.html#objitem_setweight)
- [ObjItem_SetAcceleration](./docs_item_object.html#objitem_setacceleration)
- [ObjItem_SetMaxSpeed](./docs_item_object.html#objitem_setmaxspeed)

*Note: If either of the given coordinates are NULL_POS, the item will not be created.*

## CreateItemU2
<pre>
    Arguments:
        1) real: itemID
        2) real: x
        3) real: y
        4) real: xDest
        5) real: yDest
        6) real: score
    Return Type:
        real
</pre>
Creates a user-defined item with the provided item ID and score value at the specified x and y coordinates that moves to the provided x and y destination coordinates before falling. Also returns its object ID.

Falling speeds can be tuned with the following functions:
- [ObjItem_SetWeight](./docs_item_object.html#objitem_setweight)
- [ObjItem_SetAcceleration](./docs_item_object.html#objitem_setacceleration)
- [ObjItem_SetMaxSpeed](./docs_item_object.html#objitem_setmaxspeed)

*Note: If either of the given coordinates are NULL_POS, the item will not be created.*

## CreateItemU3
<pre>
    Arguments:
        1) real: itemID
        2) real: x
        3) real: y
        4) real: xDest
        5) real: yDest
        6) real: score
    Return Type:
        real
</pre>
Creates a user-defined item at the specified point.

Uses official Touhou-style item movement (acceleration-based).\
Falling speeds can be tuned with the following functions:
- [ObjItem_SetAcceleration](./docs_item_object.html#objitem_setacceleration)
- [ObjItem_SetMaxSpeed](./docs_item_object.html#objitem_setmaxspeed)

*Note: If either of the given coordinates are NULL_POS, the item will not be created.*

## GetItemIdInCircleA1
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
    Return Type:
        real array
</pre>
Returns the object IDs of the items inside the given circle in an array.

## GetItemIdInCircleA2
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
        4) real: itemType
    Return Type:
        real array
</pre>
Returns the object IDs of the items inside the given circle with the specified itemType in an array.

## CollectAllItems
Makes all items fly towards the player.

## CollectItemsByType
<pre>
    Arguments:
        1) real: itemType
    Return Type:
</pre>
Makes all items of the specified type fly toward the player.

itemType can be one of the following:
<pre>
ITEM_1UP and ITEM_1UP_S (lives)
ITEM_SPELL and ITEM_SPELL_S (bombs)
ITEM_POINT and ITEM_POINT_S (points)
ITEM_POWER and ITEM_POWER_S (power)
ITEM_USER (user-defined).
</pre>
The types ending in '_S' will create a smaller version of the specified item.

## CollectItemsInCircle
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
</pre>
Makes all items within the circle fly toward the player.

## CancelCollectItems
Cancels any items that were currently moving to the player for collection.

Note: This function only works for items collected by the player auto item collection line (SetPlayerAutoItemCollectLine).

## StartItemScript
<pre>
    Arguments:
        1) string: path
</pre>
Starts the script at the provided path for processing user-defined items.

## SetDefaultBonusItemEnable
<pre>
    Arguments:
        1) bool: enable
</pre>
Sets whether or not to create the default autocollected bullet delete items when bullets are deleted to items.

True will create the items, false will not.\
The default value is true.

## LoadItemData
<pre>
    Arguments:
        1) string: path
    Return Type:
        bool
</pre>
Loads the specified item data and returns true if successful.

Can be called any amount of times, but currently existing IDs will be replaced by new ones of the same value.\
You may not use the same file twice in this function; to do so, see ReloadItemData.

## ReloadItemData
<pre>
    Arguments:
        1) string: path
    Return Type:
        bool
</pre>
Reloads the specified item data and returns true if successful.

Can be called any amount of times, but currently existing IDs will be replaced by new ones of the same value.\
You do not need to use LoadItemData before using this function.