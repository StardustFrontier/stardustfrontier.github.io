# Type Constructor Functions

[Return to Functions](../functions.html)

## bool
```
    Arguments:
        1) any: value
    Return Type:
        bool
```
Returns a bool constructed from the given value.

## real
```
    Arguments:
        1) any: value
    Return Type:
        real
```
Returns a real constructed from the given value.

## char
```
    Arguments:
        1) any: value
    Return Type:
        char
```
Returns a char constructed from the given value.

## string
```
    Arguments:
        1) any: value
    Return Type:
        string
```
Returns a string constructed from the given value.

This function is faster than ToString.

## array
```
    Arguments:
        1) array|string|table: value
    Return Type:
        array
```
Returns an array constructed from the given value.

This behaves differently depending on the type of the value passed:
- array: constructs a shallow copy of the array
- string: constructs an array containing the characters in the string
- table: constructs an array containing all the keys of the table

## table
```
    Arguments:
        1) table: value
    Return Type:
        table
```
Returns a table constructed from a shallow copy of the given table.