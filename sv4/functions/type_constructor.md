# Type Constructor Functions

[Return to Functions](../functions.html)

## bool
<pre>
    Arguments:
        1) any: value
    Return Type:
        bool
</pre>
Returns a bool constructed from the given value.

## real
<pre>
    Arguments:
        1) any: value
    Return Type:
        real
</pre>
Returns a real constructed from the given value.

## char
<pre>
    Arguments:
        1) any: value
    Return Type:
        char
</pre>
Returns a char constructed from the given value.

## string
<pre>
    Arguments:
        1) any: value
    Return Type:
        string
</pre>
Returns a string constructed from the given value.

This function is faster than ToString.

## array
<pre>
    Arguments:
        1) array|string|table: value
    Return Type:
        array
</pre>
Returns a array constructed from the given value.

This behaves differently depending on the type of the value passed:
- array: constructs a shallow copy of the array
- string: constructs an array containing the characters in the string
- table: constructs an array containing all the keys of the table

## table
<pre>
    Arguments:
        1) table: value
    Return Type:
        table
</pre>
Returns a table constructed from a shallow copy of the given table.