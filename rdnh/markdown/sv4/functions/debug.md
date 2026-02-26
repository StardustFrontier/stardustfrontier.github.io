# Debug Functions

[Return to Functions](../functions.html)

## WriteLog
```
    Arguments:
        1+) string: str
```
Outputs the given string(s) to the log window.

When more than one string is passed, they will be separated by spaces.

## WriteLogF
```
    Arguments:
        1) string: str
        2+) any: values...
```
Outputs the given string to the log window, formatting it in the same way as C's printf family of functions.

This is equivalent to:\
`WriteLog(StringFormat(str, values...));`

## printf
```
    Arguments:
        1) string: str
        2+) any: values...
```
Outputs the given string to the log window, formatting it in the same way as C's printf family of functions.

This is an alias for WriteLogF.

## RaiseError
```
    Arguments:
        1+) string: str
```
Creates an error box with the specified string.\
Execution of the script is stopped, closing the script.

When more than one string is passed, they will _not_ be separated by spaces.

## assert
```
    Arguments:
        1) bool: condition
        2) any: value
```
If the condition is false, raise an error with the specified value and terminate the script.

## get_interned_strings
```
    Return Type:
        array[string]
```
Returns an array of all strings that have been internalized by the running scripts.

## get_ref_count
```
    Arguments:
        1) any: value
    Return Type:
        real
```
Returns the internal reference count of the given value if it's a collection type, otherwise always returns 0.\
The count returned will be one higher than the actual count, because it includes the temporary reference created when calling this function.

Collection types are: _array_, _string_, and _table_.

## GetCurrentMemoryUsage
```
    Return Type:
        real
```
Returns the current amount of memory used by the rdnh process in bytes.

## GetDnhBuildInfo
```
    Return Type:
        string
```
Returns a string that identifies the build of rdnh (currently, the date as yy.mm.dd)

## GetDnhScriptVersion
```
    Return Type:
        string
```
Returns the version of the rdnh scripting language as a string in the format: MajorVersion.MinorVersion