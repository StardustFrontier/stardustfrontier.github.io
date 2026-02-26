# Array Functions

[Return to Functions](../functions.html)

## array_create
```
    Arguments:
        1) real: size
        2) any: initValue = nil
```
Creates a new array of the given size and fills it with the given value.

## array_append
```
    Arguments:
        1) array: arr
        2+) any: values...
```
Appends the given values to the array.

## array_insert
```
    Arguments:
        1) array: arr
        2) real: index
        3) any: value
```
Inserts the value into the array at the given index.

## array_pop
```
    Arguments:
        1) array: arr
```
Removes the last element from the array.

## array_erase
```
    Arguments:
        1) array: arr
        2) real: index
```
Erases the element at the given index from the array.

## array_reserve
```
    Arguments:
        1) array: arr
        2) real: n
```
Pre-allocates memory for n elements without resizing the actual array.

For example:\
if this is called on an empty array like array_reserve(arr, 100), the length will still be 0, but it will be faster to append to because the space is already reserved.

## array_resize
```
    Arguments:
        1) array: arr
        2) real: n
        3) any: initValue = nil
```
Resizes the array so that it contains n elements.

If n < length(arr): removes the excess elements\
If n > length(arr): expands the container, setting each new element to initValue (nil if not provided)

## array_clear
```
    Arguments:
        1) array: arr
```
Removes all elements from the array.

## array_find
```
    Arguments:
        1) array: arr
        2) any: toFind
        3) real: startIndex = 0
    Return Type:
        real
```
Finds the value in arr and returns the index it starts at or -1 if it was not found.

Optionally, the index to start the operation at can be specified. This is 0 by default.

## array_sort
```
    Arguments:
        1) array: arr
        2) function: comp?
    Return Type:
        real
```
Sorts the elements in the given array in non-descending order.

A user-defined comparator function may be passed to compare the elements:
```
function Compare(a, b, res) { res[0] = a > b; }
```

If comp is not provided, the elements will be compared using the < operator.

_**Note**: The order of equal elements is not guaranteed to be preserved._

## array_bisect_left
```
    Arguments:
        1) array: arr
        2) any: x
        3) any: low?
        4) any: high?
    Return:
        real: index
```
Returns the index in the sorted array where x should be inserted to maintain the array's order.

If x already exists in the list, the index of its first occurrence is returned.\
_low_ and _high_ can optionally be passed to specify the bounds within the array to search (defaults to the 0 and length(arr)).

## array_bisect_right
```
    Arguments:
        1) array: arr
        2) any: x
        3) any: low?
        4) any: high?
    Return:
        real: index
```
Returns the rightmost index in the sorted array where x should be inserted to maintain the array's order.

If x already exists in the list, the next index after the last occurrence is returned.
_low_ and _high_ can optionally be passed to specify the bounds within the array to search (defaults to the 0 and length(arr)).

## array_bisect
```
    Arguments:
        1) array: arr
        2) any: x
        3) any: low?
        4) any: high?
    Return:
        real: index
```
This function is an alias for array_bisect_right and works in the exact same way.

## array_count
```
    Arguments:
        1) array: arr
        2) any: value
    Return Type:
        real
```
Returns the number of times the given value appears in the array.

## array_contains
```
    Arguments:
        1) array: arr
        2) any: value
    Return Type:
        bool
```
Returns true if the array contains the given value at least once, otherwise returns false.