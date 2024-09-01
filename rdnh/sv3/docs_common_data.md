# Common Data Functions

[Return to Functions](./docs.html)

## SetDefaultCommonDataArea
<pre>
    Arguments:
        1) string: str
</pre>
Sets the name of the default common data area to the specified string.

## SetCommonData
<pre>
    Arguments:
        1) string: key
        2) any: value
</pre>
Maps the given key to the given value in the default common data area.\
The value can be returned by using [GetCommonData](getcommondata) with the corresponding key.

## GetCommonData
<pre>
    Arguments:
        1) string: key
        2) any: defaultValue
    Return Type:
        any
</pre>
Returns the value associated with the given key in the default common data area, or defaultValue if no mapping exists.

## ClearCommonData
Removes all of the common data in the default common data area.

## DeleteCommonData
<pre>
    Arguments:
        1) string: key
</pre>
Removes the common data mapping with the specified key from the default common data area.

## SetAreaCommonData
<pre>
    Arguments:
        1) string: area
        2) string: key
        3) any: value
</pre>
Maps the given key to the given value in the specified common data area.\
The value can be returned by using [GetAreaCommonData](getareacommondata) with the corresponding area and key.

## GetAreaCommonData
<pre>
    Arguments:
        1) string: area
        2) string: key
        3) any: defaultValue
    Return Type:
        any
</pre>
Returns the value associated with the given key in the specified common data area, or defaultValue if no mapping exists.

## ClearAreaCommonData
<pre>
    Arguments:
        1) string: area
</pre>
Removes all of the common data in the specified area.

## DeleteAreaCommonData
<pre>
    Arguments:
        1) string: area
        2) string: key
</pre>
Removes the common data mapping with the specified key from the specified common data area.

## CreateCommonDataArea
<pre>
    Arguments:
        1) string: area
</pre>
Creates a common data area with the provided area name, in which various common data can be stored.

## CopyCommonDataArea
<pre>
    Arguments:
        1) string: destArea
        2) string: srcArea
</pre>
Copies the common data in the source area to the destination area.

## IsCommonDataAreaExists
<pre>
    Arguments:
        1) string: area
    Return Type:
        bool
</pre>
Returns true if the area name corresponds to an existing common data area, otherwise returns false.

## GetCommonDataAreaKeyList
<pre>
    Return Type:
        string array
</pre>
Returns an array of all common data area names.

## GetCommonDataAreaKeyList
<pre>
    Arguments:
        1) string: area
    Return Type:
        string array
</pre>
Returns an array of the keys in the specified area.

## SaveCommonDataAreaA1
<pre>
    Arguments:
        1) string: area
    Return Type:
        bool
</pre>
Saves everything in the specified common data area to a data file.\
Returns true if successful and false if the operation failed.

## LoadCommonDataAreaA1
<pre>
    Arguments:
        1) string: area
    Return Type:
        bool
</pre>
Loads everything in the specified common data area from the saved data file.\
Returns true if successful and false if the operation failed.

## SaveCommonDataAreaA2
<pre>
    Arguments:
        1) string: area
        2) string: path
    Return Type:
        bool
</pre>
Saves everything in the specified common data area to a data file at the specified path.\
Returns true if successful and false if the operation failed.

## LoadCommonDataAreaA2
<pre>
    Arguments:
        1) string: area
        2) string: path
    Return Type:
        bool
</pre>
Loads everything in the specified common data area from the saved data file at the specified path.\
Returns true if successful and false if the operation failed.

## SaveCommonDataAreaToReplayFile
<pre>
    Arguments:
        1) string: area
    Return Type:
        bool
</pre>
Saves the specified common data area to the replay file.\
Returns true if successful and false if the operation failed.\
***Note**: This function should not be called during a replay.*

## LoadCommonDataAreaFromReplayFile
<pre>
    Arguments:
        1) string: area
    Return Type:
        bool
</pre>
Loads everything in the specified common data area from the replay file.\
Returns true if successful and false if the operation failed.\
***Note**: This function should not be called during gameplay.*