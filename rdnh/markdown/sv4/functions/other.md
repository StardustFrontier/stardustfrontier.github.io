# Other Functions

[Return to Functions](../functions.html)

## StartSlow
```
    Arguments:
        1) real: slowTarget
        2) real: fpsValue
```
Creates a pseudo slow effect by forcing Danmakufu to run at the specified FPS value.

There is currently only one target available, TARGET_ALL.\
Use StopSlow to stop this effect.

## StopSlow
```
    Arguments:
        1) real: slowTarget
```
Removes the pseudo slow from StartSlow, and restores Danmakufu to normal FPS.

There is currently only one target available, TARGET_ALL.

## IsIntersected_Obj_Obj
```
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        bool
```
Returns true if any of both object's hitboxes intersect at least once.

Note: This function is currently only available on bullet and laser objects.

## IsIntersected_Obj_Obj_All
```
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        bool
```
Returns true if all of both object's hitboxes intersect with any of each other's at least once.

Note: This function is currently only available on bullet and laser objects.

## GetObjectDistance
```
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        real
```
Returns the distance between the two objects.

If one of the objects' ID is invalid, -1 will be returned.

## GetObjectDistanceSq
```
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        real
```
Returns the square of the distance between the two objects.

If one of the objects' ID is invalid, -1 will be returned.

## GetObjectDistance2D
```
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        real
```
Returns the distance between the two 2D objects.

If one of the objects' ID is invalid, -1 will be returned.

## GetObjectDistanceSq2D
```
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        real
```
Returns the square of the distance between the two 2D objects.

If one of the objects' ID is invalid, -1 will be returned.

## GetObject2dPosition
```
    Arguments:
        1) real: objID
    Return Type:
        real array
```
Returns the 2D coordinates of a 3D object projected onto the 2D window.

The array is returned as [X, Y].

## Get2dPosition
```
    Arguments:
        1) real: x
        2) real: y
        3) real: z
    Return Type:
        real array
```
Returns the 2D coordinates of the given 3D coordinates projected onto the 2D window.

The array is returned as [X, Y].

## wait
```
    Arguments:
        1) real: frames
```
Pauses execution for the given amount of frames.

This is functionally equivalent to:
```
loop (frames) yield;
```

## copy
```
    Arguments:
        1) any: collection
    Return Type:
        any
```
Returns a deep copy of the value.

A deep copy creates a new collection and recursively inserts copies of each element found in the original collection.\
In other words, each value in the new collection will be a unique reference instead of referring to the value in the original collection.

## erase
```
    Arguments:
        1) any array: arr
        2) real: index
    Return Type:
        any array
```
Returns a new array with the element at the given index in the provided array removed.

## length
```
    Arguments:
        1) any array: arr
    Return Type:
        real
```
Returns the size of an array.

## concatenate
```
    Arguments:
        1) any array: arr1
        2) any array: arr2
    Return Type:
        any array
```
Concatenates the two provided arrays (of same type) and returns the new array.

Function version of ~.\
Works on strings, as they are character arrays.

## slice
```
    Arguments:
        1) any array: arr
        2) real: start
        3) real: end
    Return Type:
        any array
```
Cuts out a specific portion of an array.

Function version of array[start..end].
Sliced portion includes start but not end.

## CreateArray
```
    Arguments:
        1) real or any: array length or element1
        2) any: ... (varargs elements)
    Return Type:
        any array
```
Creates an array of the specified length if argument count is 1, otherwise create an array with the given elements.

Note: This function has a variable number of arguments.

## find_func
```
    Arguments:
        1) string: name
    Return Type:
        function
```
Searches the global scope for a function with the given name and returns it.

If the function was not found, then an error is raised.

## not
```
    Arguments:
        1) any array: arr
    Return Type:
        real
```
Returns the logical negation of the provided boolean expression.

Function version of !.

## PickValue
```
    Arguments:
        1) real: index
        2) any varargs: args
    Return Type:
        real
```
Returns the value at the given argument index.\
Can pass as many values as needed.

Note: This function will raise an error if the index is out of bounds.

## Interpolate
```
    Arguments:
        1) real const: interpolationType
        2) real: startValue
        3) real: endValue
        4) real: timeRatio
    Return Type:
        real
```
Interpolates between startValue and endValue by timeRatio using the given [interpolation type](./interpolation_types.html).

Note: timeRatio must be a value between 0 and 1.