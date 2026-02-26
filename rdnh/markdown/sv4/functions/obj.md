# Obj Functions

[Return to Functions](../functions.html)

## Obj_Delete
```
    Arguments:
        1) real: objectIDs...
```
Deletes the object(s) associated with the given ID(s).

## Obj_DeleteArray
```
    Arguments:
        1) array[real]: objectIDs
```
Deletes the objects with the IDs in the given array.

## Obj_IsDeleted
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if the object mapped to the given objectID is deleted, otherwise false.

## Obj_Exists
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if the object mapped to the given objectID *exists* (is not deleted), otherwise false.

*Note: This function is the inverse of [Obj_IsDeleted](obj_isdeleted).*

## Obj_SetVisible
```
    Arguments:
        1) real: objectID
        2) bool: isVisible
```
Sets whether the specified object is visible.

If this is set to false, the object will not be drawn.

## Obj_IsVisible
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if the object is set to be visible.

## Obj_SetRenderPriority
```
    Arguments:
        1) real: objectID
        2) real: priority
```
Sets the object's render priority.

*Note: Render priorities for this function are on a 0.0-1.0 scale.*

## Obj_SetRenderPriorityI
```
    Arguments:
        1) real: objectID
        2) real: priorityI
```
Sets the object's (integer) render priority.

*Note: Render priorities for this function are on a 0-100 scale.*

## Obj_GetRenderPriority
```
    Arguments:
        1) real: objectID
        2) real: priority
    Return Type:
        real
```
Returns the object's render priority.

*Note: Render priorities for this function are on a 0.0-1.0 scale.*

## Obj_GetRenderPriorityI
```
    Arguments:
        1) real: objectID
        2) real: priorityI
    Return Type:
        real
```
Returns the object's (integer) render priority.

*Note: Render priorities for this function are on a 0-100 scale.*

## Obj_SetRenderUpdateEnable
```
    Arguments:
        1) real: objectID
        2) bool: enable
```
Enables or disables render updates for the object.

This stops processing of all automated ObjRender functions (such as the tween and speed ones).

## Obj_IsRenderUpdateEnable
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if render updates for this object are enabled, otherwise returns false.

## Obj_SetForceRenderUpdate
```
    Arguments:
        1) real: objectID
        2) bool: enable
```
Enabling this flag stops the object from having its render updates disabled by the global SetRenderUpdateEnable function.

*Note: This will not prevent Obj_IsRenderUpdateEnable from enabling/disabling render updates.*

## Obj_IsForceRenderUpdate
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if the force render update flag for this object is enabled, otherwise returns false.

## Obj_GetValue
```
    Arguments:
        1) real: objectID
        2) string: key
    Return Type:
        any
```
Returns the value associated with the given key for the given object, previously set by [Obj_SetValue](#obj_setvalue).

***Warning**: If the key-value pair does not exist or was deleted, attempting to access it will crash the program.*

## Obj_GetValueD
```
    Arguments:
        1) real: objectID
        2) string: key
        3) any: defaultValue
    Return Type:
        any
```
Returns the value associated with the given key for the given object, previously set by [Obj_SetValue](#obj_setvalue).

If the key-value pair doesn't exist, the default value is returned instead.

## Obj_SetValue
```
    Arguments:
        1) real: objectID
        2) string: key
        3) any: value
```
For the given object, maps the given key to the given value.

The value can be returned by using [Obj_GetValue](#obj_getvalue) with the corresponding key.

## Obj_DeleteValue
```
    Arguments:
        1) real: objectID
        2) string: key
```
Deletes the key-value pair previously set by [Obj_SetValue](#obj_setvalue).

## Obj_IsValueExists
```
    Arguments:
        1) real: objectID
        2) string: key
```
Checks whether the object has a key-value pair for the given key and returns true if it does.

## Obj_GetValueInt
```
    Arguments:
        1) real: objectID
        2) real: key
    Return Type:
        any
```
Returns the value associated with the given (int) key for the given object, previously set by [Obj_SetValueInt](#obj_setvalueint).

***Warning**: If the key-value pair does not exist or was deleted, attempting to access it will crash the program.*

## Obj_GetValueIntD
```
    Arguments:
        1) real: objectID
        2) real: key
        3) any: defaultValue
    Return Type:
        any
```
Returns the value associated with the given (int) key for the given object, previously set by [Obj_SetValueInt](#obj_setvalueint).

If the key-value pair doesn't exist, the default value is returned instead.

## Obj_SetValueInt
```
    Arguments:
        1) real: objectID
        2) real: key
        3) any: value
```
For the given object, maps the given (int) key to the given value.

The value can be returned by using [Obj_GetValueInt](#obj_getvalueint) with the corresponding key.

## Obj_DeleteValueInt
```
    Arguments:
        1) real: objectID
        2) real: key
```
Deletes the (int) key-value pair previously set by [Obj_SetValueInt](#obj_setvalueint).

## Obj_IsValueIntExists
```
    Arguments:
        1) real: objectID
        2) real: key
```
Checks whether the object has a (int) key-value pair for the given key and returns true if it does.

## Obj_SetFlag
```
    Arguments:
        1) real: objectID
        2) real: flag
```
Sets a bit flag for an object.

Multiple flags may be set in one call using bitwise OR (`|`)\
*Note: To work properly, flag must be in the form:* `1 << x`

## Obj_ClearFlag
```
    Arguments:
        1) real: objectID
        2) real: flag
```
Clears (unsets) the specified bit flag for an object.

Multiple flags may be cleared in one call using bitwise OR (`|`)\
*Note: To work properly, flag must be in the form:* `1 << x`

## Obj_HasFlag
```
    Arguments:
        1) real: objectID
        2) real: flag
    Return Type:
        boool
```
Returns true if the specified bit flag for the object is set, otherwise false.

Multiple flags may be checked in one call using bitwise OR (`|`)\
*Note: To work properly, flag must be in the form:* `1 << x`

## Obj_GetFlag
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns **all** of the flags currently set for the specified object.

A single flag can be checked by using bitwise AND (`&`) on the result.

## Obj_GetType
```
    Arguments:
        1) real: objectID
    Return Type:
        real const
```
Returns the [object's type](./docs_object_types.html). as a constant real value.