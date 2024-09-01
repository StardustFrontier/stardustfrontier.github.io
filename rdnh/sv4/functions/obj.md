# Obj Functions

[Return to Functions](../functions.html)

## Obj_Delete
<pre>
    Arguments:
        1) real: objectIDs...
</pre>
Deletes the object(s) associated with the given ID(s).

## Obj_DeleteArray
<pre>
    Arguments:
        1) array[real]: objectIDs
</pre>
Deletes the objects with the IDs in the given array.

## Obj_IsDeleted
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Returns true if the object mapped to the given objectID is deleted, otherwise false.

## Obj_Exists
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Returns true if the object mapped to the given objectID *exists* (is not deleted), otherwise false.

*Note: This function is the inverse of [Obj_IsDeleted](obj_isdeleted).*

## Obj_SetVisible
<pre>
    Arguments:
        1) real: objectID
        2) bool: isVisible
</pre>
Sets whether the specified object is visible.

If this is set to false, the object will not be drawn.

## Obj_IsVisible
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Returns true if the object is set to be visible.

## Obj_SetRenderPriority
<pre>
    Arguments:
        1) real: objectID
        2) real: priority
</pre>
Sets the object's render priority.

*Note: Render priorities for this function are on a 0.0-1.0 scale.*

## Obj_SetRenderPriorityI
<pre>
    Arguments:
        1) real: objectID
        2) real: priorityI
</pre>
Sets the object's (integer) render priority.

*Note: Render priorities for this function are on a 0-100 scale.*

## Obj_GetRenderPriority
<pre>
    Arguments:
        1) real: objectID
        2) real: priority
    Return Type:
        real
</pre>
Returns the object's render priority.

*Note: Render priorities for this function are on a 0.0-1.0 scale.*

## Obj_GetRenderPriorityI
<pre>
    Arguments:
        1) real: objectID
        2) real: priorityI
    Return Type:
        real
</pre>
Returns the object's (integer) render priority.

*Note: Render priorities for this function are on a 0-100 scale.*

## Obj_SetRenderUpdateEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: enable
</pre>
Enables or disables render updates for the object.

This stops processing of all automated ObjRender functions (such as the tween and speed ones).

## Obj_IsRenderUpdateEnable
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Returns true if render updates for this object are enabled, otherwise returns false.

## Obj_SetForceRenderUpdate
<pre>
    Arguments:
        1) real: objectID
        2) bool: enable
</pre>
Enabling this flag stops the object from having its render updates disabled by the global SetRenderUpdateEnable function.

*Note: This will not prevent Obj_IsRenderUpdateEnable from enabling/disabling render updates.*

## Obj_IsForceRenderUpdate
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Returns true if the force render update flag for this object is enabled, otherwise returns false.

## Obj_GetValue
<pre>
    Arguments:
        1) real: objectID
        2) string: key
    Return Type:
        any
</pre>
Returns the value associated with the given key for the given object, previously set by [Obj_SetValue](obj_setvalue).

***Warning**: If the key-value pair does not exist or was deleted, attempting to access it will crash the program.*

## Obj_GetValueD
<pre>
    Arguments:
        1) real: objectID
        2) string: key
        3) any: defaultValue
    Return Type:
        any
</pre>
Returns the value associated with the given key for the given object, previously set by [Obj_SetValue](obj_setvalue).

If the key-value pair doesn't exist, the default value is returned instead.

## Obj_SetValue
<pre>
    Arguments:
        1) real: objectID
        2) string: key
        3) any: value
</pre>
For the given object, maps the given key to the given value.

The value can be returned by using [Obj_GetValue](obj_getvalue) with the corresponding key.

## Obj_DeleteValue
<pre>
    Arguments:
        1) real: objectID
        2) string: key
</pre>
Deletes the key-value pair previously set by [Obj_SetValue](obj_setvalue).

## Obj_IsValueExists
<pre>
    Arguments:
        1) real: objectID
        2) string: key
</pre>
Checks whether the object has a key-value pair for the given key and returns true if it does.

## Obj_GetValueInt
<pre>
    Arguments:
        1) real: objectID
        2) real: key
    Return Type:
        any
</pre>
Returns the value associated with the given (int) key for the given object, previously set by [Obj_SetValueInt](obj_setvalueint).

***Warning**: If the key-value pair does not exist or was deleted, attempting to access it will crash the program.*

## Obj_GetValueIntD
<pre>
    Arguments:
        1) real: objectID
        2) real: key
        3) any: defaultValue
    Return Type:
        any
</pre>
Returns the value associated with the given (int) key for the given object, previously set by [Obj_SetValueInt](obj_setvalueint).

If the key-value pair doesn't exist, the default value is returned instead.

## Obj_SetValueInt
<pre>
    Arguments:
        1) real: objectID
        2) real: key
        3) any: value
</pre>
For the given object, maps the given (int) key to the given value.

The value can be returned by using [Obj_GetValueInt](obj_getvalueint) with the corresponding key.

## Obj_DeleteValueInt
<pre>
    Arguments:
        1) real: objectID
        2) real: key
</pre>
Deletes the (int) key-value pair previously set by [Obj_SetValueInt](obj_setvalueint).

## Obj_IsValueIntExists
<pre>
    Arguments:
        1) real: objectID
        2) real: key
</pre>
Checks whether the object has a (int) key-value pair for the given key and returns true if it does.

## Obj_SetFlag
<pre>
    Arguments:
        1) real: objectID
        2) real: flag
</pre>
Sets a bit flag for an object.

Multiple flags may be set in one call using bitwise OR (`|`)\
*Note: To work properly, flag must be in the form:* `1 << x`

## Obj_ClearFlag
<pre>
    Arguments:
        1) real: objectID
        2) real: flag
</pre>
Clears (unsets) the specified bit flag for an object.

Multiple flags may be cleared in one call using bitwise OR (`|`)\
*Note: To work properly, flag must be in the form:* `1 << x`

## Obj_HasFlag
<pre>
    Arguments:
        1) real: objectID
        2) real: flag
    Return Type:
        boool
</pre>
Returns true if the specified bit flag for the object is set, otherwise false.

Multiple flags may be checked in one call using bitwise OR (`|`)\
*Note: To work properly, flag must be in the form:* `1 << x`

## Obj_GetFlag
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns **all** of the flags currently set for the specified object.

A single flag can be checked by using bitwise AND (`&`) on the result.

## Obj_GetType
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real const
</pre>
Returns the [object's type](./docs_object_types.html). as a constant real value.