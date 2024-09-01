# Debug Functions

[Return to Functions](./docs.html)

## WriteLog
<pre>
    Arguments:
        1) string: str
</pre>
Outputs the given string to the log window.

## RaiseError
<pre>
    Arguments:
        1) string: str
</pre>
Creates an error box with the specified string.\
Execution of the script is stopped, closing the script.

## assert
<pre>
    Arguments:
        1) bool: condition
        2) any: value
</pre>
If the condition is false, raise an error with the specified value and terminate the script.