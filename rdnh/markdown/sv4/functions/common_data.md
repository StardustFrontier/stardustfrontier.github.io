# Common Data Functions

[Return to Functions](../functions.html)

## SetDefaultCommonDataArea
```
    Arguments:
        1) string: str
```
Sets the name of the default common data area to the specified string.

## SetCommonData
```
    Arguments:
        1) string: key
        2) any: value
```
Maps the given key to the given value in the default common data area.\
The value can be returned by using [GetCommonData](getcommondata) with the corresponding key.

## GetCommonData
```
    Arguments:
        1) string: key
        2) any: defaultValue = nil
    Return Type:
        any
```
Returns the value associated with the given key in the default common data area, or defaultValue if no mapping exists.

If defaultValue is not provided, it will be nil.

## ClearCommonData
Removes all of the common data in the default common data area.

## DeleteCommonData
```
    Arguments:
        1) string: key
```
Removes the common data mapping with the specified key from the default common data area.

## SetAreaCommonData
```
    Arguments:
        1) string: area
        2) string: key
        3) any: value
```
Maps the given key to the given value in the specified common data area.\
The value can be returned by using [GetAreaCommonData](getareacommondata) with the corresponding area and key.

## GetAreaCommonData
```
    Arguments:
        1) string: area
        2) string: key
        3) any?: defaultValue
    Return Type:
        any
```
Returns the value associated with the given key in the specified common data area, or defaultValue if no mapping exists.

If defaultValue is not provided, it will be nil.

## ClearAreaCommonData
```
    Arguments:
        1) string: area
```
Removes all of the common data in the specified area.

## DeleteAreaCommonData
```
    Arguments:
        1) string: area
        2) string: key
```
Removes the common data mapping with the specified key from the specified common data area.

## DeleteWholeCommonDataArea
```
    Arguments:
        1) string: area
```
Deletes the whole area common data, not just the key-value list.

To use the area common data again, it must be recreated with CreateCommonDataArea.

## CreateCommonDataArea
```
    Arguments:
        1) string: area
```
Creates a common data area with the provided area name, in which various common data can be stored.

## CopyCommonDataArea
```
    Arguments:
        1) string: destArea
        2) string: srcArea
```
Copies the common data in the source area to the destination area.

## IsCommonDataAreaExists
```
    Arguments:
        1) string: area
    Return Type:
        bool
```
Returns true if the area name corresponds to an existing common data area, otherwise returns false.

## GetCommonDataAreaKeyList
```
    Return Type:
        string array
```
Returns an array of all common data area names.

## GetCommonDataAreaKeyList
```
    Arguments:
        1) string: area
    Return Type:
        string array
```
Returns an array of the keys in the specified area.

## SaveCommonDataAreaA1
```
    Arguments:
        1) string: area
    Return Type:
        bool
```
Saves everything in the specified common data area to a data file.\
Returns true if successful and false if the operation failed.

## LoadCommonDataAreaA1
```
    Arguments:
        1) string: area
    Return Type:
        bool
```
Loads everything in the specified common data area from the saved data file.\
Returns true if successful and false if the operation failed.

## SaveCommonDataAreaA2
```
    Arguments:
        1) string: area
        2) string: path
    Return Type:
        bool
```
Saves everything in the specified common data area to a data file at the specified path.\
Returns true if successful and false if the operation failed.

## LoadCommonDataAreaA2
```
    Arguments:
        1) string: area
        2) string: path
    Return Type:
        bool
```
Loads everything in the specified common data area from the saved data file at the specified path.\
Returns true if successful and false if the operation failed.

## SaveCommonDataAreaToReplayFile
```
    Arguments:
        1) string: area
    Return Type:
        bool
```
Saves the specified common data area to the replay file.\
Returns true if successful and false if the operation failed.\
***Note**: This function should not be called during a replay.*

## LoadCommonDataAreaFromReplayFile
```
    Arguments:
        1) string: area
    Return Type:
        bool
```
Loads everything in the specified common data area from the replay file.\
Returns true if successful and false if the operation failed.\
***Note**: This function should not be called during gameplay.*

## LoadCommonDataValuePointer
```
    Arguments:
        1) string: key
        2) any: defaultValue = nil
    Returns:
        cdata: valuePointer
```
Returns a pointer to the common data value with the given key in the default area.

If the key doesn't exist, it will be created and initialized with defaultValue, which is nil if not provided.

## LoadAreaCommonDataValuePointer
```
    Arguments:
        1) string: area
        2) string: key
        3) any: defaultValue = nil
    Returns:
        cdata: valuePointer
```
Returns a pointer to the common data value with the given key in the given area.

If the key doesn't exist, it will be created and initialized with defaultValue, which is nil if not provided.

## IsValidCommonDataValuePointer
```
    Arguments:
        1) cdata: valuePointer
    Returns:
        bool: bValid
```
Returns true if the given value is a valid common data value pointer, otherwise returns false.

## SetCommonDataPtr
```
    Arguments:
        1) cdata: valuePointer
        2) any: value
    Returns:
        any: storedValue
```
Sets the common data value that valuePointer points to.

_**Note:** Passing an invalid pointer may cause a memory access violation (the game will crash). Avoid using this function if an area may be deleted._

## GetCommonDataPtr
```
    Arguments:
        1) cdata: valuePointer
        2) any: defaultValue
    Returns:
        any: storedValue
```
Returns the common data value that valuePointer points to, or defaultValue if no mapping exists.

_**Note:** Passing an invalid pointer may cause a memory access violation (the game will crash). Avoid using this function if an area may be deleted._