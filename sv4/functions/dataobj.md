# DataObj Functions

[Return to Functions](../functions.html)

&nbsp;

DataObjects are lightweight, persistent values similar to objects that only contain data and have no processing overhead. The engine stores them in a separate array from standard objects and Obj functions will not work on them.

**Note:** SetAutoDeleteObject(true) _will_ result in DataObjects being deleted.

&nbsp;

## DataObj_Delete
<pre>
    Arguments:
        1) real: dataIDs...
</pre>
Deletes the data-object(s) associated with the given ID(s).

## DataObj_DeleteArray
<pre>
    Arguments:
        1) array[real]: dataIDs
</pre>
Deletes the data-objects with the IDs in the given array.

## DataObj_IsDeleted
<pre>
    Arguments:
        1) real: dataID
    Returns:
        bool: bDeleted
</pre>
Returns true if the data-object mapped to the given dataID is deleted, otherwise false.

## DataObj_Exists
<pre>
    Arguments:
        1) real: dataID
    Returns:
        bool: bExists
</pre>
Returns true if the data-object mapped to the given dataID *exists* (is not deleted), otherwise false.

*Note: This function is the inverse of [DataObj_IsDeleted](dataobj_isdeleted).*

## DataObj_GetType
<pre>
    Arguments:
        1) real: dataID
    Returns:
        real const: dataType
</pre>
Returns the type of the data-object.

This can be, for example: DATA_OBJ_RENDER_SEQUENCE