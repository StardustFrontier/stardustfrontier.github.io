# Table Functions

[Return to Functions](../functions.html)

## table_create
```
    Arguments:
        1+) any: keyValuePairs...
```
Returns a table constructed from the given key-value pair(s).

For example: `table_create("x", 123, "y", 456)`\
Would create the table: `{"x": 123, "y": 456}`

## table_insert
```
    Arguments:
        1) table: tab
        2) string: key
        3) any: value
```
Inserts a new entry into the table.

## table_remove
```
    Arguments:
        1) table: tab
        2) string: key
```
Removes the entry with the given key from the table.

## table_set
```
    Arguments:
        1) table: tab
        2) string: key
        3) any: value
```
Sets the value associated with the given key in the table to value.

## table_get
```
    Arguments:
        1) table: tab
        2) string: key
    Return Type:
        any
```
Gets the value associated with the given key in the table.

## table_get_keys
```
    Arguments:
        1) table: tab
    Return Type:
        array[string]
```
Returns an array containing all the keys in the table.

## table_get_values
```
    Arguments:
        1) table: tab
    Return Type:
        array[any]
```
Returns an array containing all the values in the table.