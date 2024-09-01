# Table Functions

[Return to Functions](../functions.html)

## table_insert
<pre>
    Arguments:
        1) table: tab
        2) string: key
        3) any: value
</pre>
Inserts a new entry into the table.

## table_remove
<pre>
    Arguments:
        1) table: tab
        2) string: key
</pre>
Removes the entry with the given key from the table.

## table_set
<pre>
    Arguments:
        1) table: tab
        2) string: key
        3) any: value
</pre>
Sets the value associated with the given key in the table to value.

## table_get
<pre>
    Arguments:
        1) table: tab
        2) string: key
    Return Type:
        any
</pre>
Gets the value associated with the given key in the table.

## table_get_keys
<pre>
    Arguments:
        1) table: tab
    Return Type:
        array[string]
</pre>
Returns an array containing all the keys in the table.

## table_get_values
<pre>
    Arguments:
        1) table: tab
    Return Type:
        array[any]
</pre>
Returns an array containing all the values in the table.