# Debug Functions

[Return to Functions](../functions.html)

## WriteLog
<pre>
    Arguments:
        1+) string: str
</pre>
Outputs the given string(s) to the log window.

When more than one string is passed, they will be separated by spaces.

## WriteLogF
<pre>
    Arguments:
        1) string: str
        2+) any: values...
</pre>
Outputs the given string to the log window, formatting it in the same way as C's printf family of functions.

This is equivalent to:\
`WriteLog(StringFormat(str, values...));`

## printf
<pre>
    Arguments:
        1) string: str
        2+) any: values...
</pre>
Outputs the given string to the log window, formatting it in the same way as C's printf family of functions.

This is an alias for WriteLogF.

## RaiseError
<pre>
    Arguments:
        1+) string: str
</pre>
Creates an error box with the specified string.\
Execution of the script is stopped, closing the script.

When more than one string is passed, they will _not_ be separated by spaces.

## assert
<pre>
    Arguments:
        1) bool: condition
        2) any: value
</pre>
If the condition is false, raise an error with the specified value and terminate the script.

## get_interned_strings
<pre>
    Return Type:
        array[string]
</pre>
Returns an array of all strings that have been internalized by the running scripts.

## get_ref_count
<pre>
    Arguments:
        1) any: value
    Return Type:
        real
</pre>
Returns the internal reference count of the given value if it's a collection type, otherwise always returns 0.\
The count returned will be one higher than the actual count, because it includes the temporary reference created when calling this function.

Collection types are: _array_, _string_, and _table_.

## GetCurrentMemoryUsage
<pre>
    Return Type:
        real
</pre>
Returns the current amount of memory used by the rdnh process in bytes.

## GetDnhBuildInfo
<pre>
    Return Type:
        string
</pre>
Returns a string that identifies the build of rdnh (currently, the date as yy.mm.dd)

## GetDnhScriptVersion
<pre>
    Return Type:
        string
</pre>
Returns the version of the rdnh scripting language as a string in the format: MajorVersion.MinorVersion