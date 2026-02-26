# DataObj Functions

[Return to Functions](../functions.html)

&nbsp;

DataObjects are lightweight, persistent values similar to objects that only contain data and have no processing overhead. The engine stores them in a separate array from standard objects and Obj functions will not work on them.

**Note:** SetAutoDeleteObject(true) _will_ result in DataObjects being deleted.

&nbsp;

## DataObj_Delete
```
    Arguments:
        1) real: dataIDs...
```
Deletes the data-object(s) associated with the given ID(s).

## DataObj_DeleteArray
```
    Arguments:
        1) array[real]: dataIDs
```
Deletes the data-objects with the IDs in the given array.

## DataObj_IsDeleted
```
    Arguments:
        1) real: dataID
    Returns:
        bool: bDeleted
```
Returns true if the data-object mapped to the given dataID is deleted, otherwise false.

## DataObj_Exists
```
    Arguments:
        1) real: dataID
    Returns:
        bool: bExists
```
Returns true if the data-object mapped to the given dataID *exists* (is not deleted), otherwise false.

*Note: This function is the inverse of [DataObj_IsDeleted](dataobj_isdeleted).*

## DataObj_GetType
```
    Arguments:
        1) real: dataID
    Returns:
        real const: dataType
```
Returns the type of the data-object.

This can be, for example: DATA_OBJ_RENDER_SEQUENCE