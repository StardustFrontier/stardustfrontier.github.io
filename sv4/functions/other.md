# Other Functions

[Return to Functions](../functions.html)

## StartSlow
<pre>
    Arguments:
        1) real: slowTarget
        2) real: fpsValue
</pre>
Creates a pseudo slow effect by forcing Danmakufu to run at the specified FPS value.

There is currently only one target available, TARGET_ALL.\
Use StopSlow to stop this effect.

## StopSlow
<pre>
    Arguments:
        1) real: slowTarget
</pre>
Removes the pseudo slow from StartSlow, and restores Danmakufu to normal FPS.

There is currently only one target available, TARGET_ALL.

## IsIntersected_Obj_Obj
<pre>
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        bool
</pre>
Returns true if any of both object's hitboxes intersect at least once.

Note: This function is currently only available on bullet and laser objects.

## IsIntersected_Obj_Obj_All
<pre>
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        bool
</pre>
Returns true if all of both object's hitboxes intersect with any of each other's at least once.

Note: This function is currently only available on bullet and laser objects.

## GetObjectDistance
<pre>
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        real
</pre>
Returns the distance between the two objects.

If one of the objects' ID is invalid, -1 will be returned.

## GetObjectDistanceSq
<pre>
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        real
</pre>
Returns the square of the distance between the two objects.

If one of the objects' ID is invalid, -1 will be returned.

## GetObjectDistance2D
<pre>
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        real
</pre>
Returns the distance between the two 2D objects.

If one of the objects' ID is invalid, -1 will be returned.

## GetObjectDistanceSq2D
<pre>
    Arguments:
        1) real: objID1
        2) real: objID2
    Return Type:
        real
</pre>
Returns the square of the distance between the two 2D objects.

If one of the objects' ID is invalid, -1 will be returned.

## GetObject2dPosition
<pre>
    Arguments:
        1) real: objID
    Return Type:
        real array
</pre>
Returns the 2D coordinates of a 3D object projected onto the 2D window.

The array is returned as [X, Y].

## Get2dPosition
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: z
    Return Type:
        real array
</pre>
Returns the 2D coordinates of the given 3D coordinates projected onto the 2D window.

The array is returned as [X, Y].

## wait
<pre>
    Arguments:
        1) real: frames
</pre>
Pauses execution for the given amount of frames.

This is functionally equivalent to:
<pre>
loop (frames) yield;
</pre>

## copy
<pre>
    Arguments:
        1) any: collection
    Return Type:
        any
</pre>
Returns a deep copy of the value.

A deep copy creates a new collection and recursively inserts copies of each element found in the original collection.\
In other words, each value in the new collection will be a unique reference instead of referring to the value in the original collection.

## erase
<pre>
    Arguments:
        1) any array: arr
        2) real: index
    Return Type:
        any array
</pre>
Returns a new array with the element at the given index in the provided array removed.

## length
<pre>
    Arguments:
        1) any array: arr
    Return Type:
        real
</pre>
Returns the size of an array.

## concatenate
<pre>
    Arguments:
        1) any array: arr1
        2) any array: arr2
    Return Type:
        any array
</pre>
Concatenates the two provided arrays (of same type) and returns the new array.

Function version of ~.\
Works on strings, as they are character arrays.

## slice
<pre>
    Arguments:
        1) any array: arr
        2) real: start
        3) real: end
    Return Type:
        any array
</pre>
Cuts out a specific portion of an array.

Function version of array[start..end].
Sliced portion includes start but not end.

## CreateArray
<pre>
    Arguments:
        1) real or any: array length or element1
        2) any: ... (varargs elements)
    Return Type:
        any array
</pre>
Creates an array of the specified length if argument count is 1, otherwise create an array with the given elements.

Note: This function has a variable number of arguments.

## find_func
<pre>
    Arguments:
        1) string: name
    Return Type:
        function
</pre>
Searches the global scope for a function with the given name and returns it.

If the function was not found, then an error is raised.

## not
<pre>
    Arguments:
        1) any array: arr
    Return Type:
        real
</pre>
Returns the logical negation of the provided boolean expression.

Function version of !.

## PickValue
<pre>
    Arguments:
        1) real: index
        2) any varargs: args
    Return Type:
        real
</pre>
Returns the value at the given argument index.\
Can pass as many values as needed.

Note: This function will raise an error if the index is out of bounds.

## Interpolate
<pre>
    Arguments:
        1) real const: interpolationType
        2) real: startValue
        3) real: endValue
        4) real: timeRatio
    Return Type:
        real
</pre>
Interpolates between startValue and endValue by timeRatio using the given [interpolation type](./interpolation_types.html).

Note: timeRatio must be a value between 0 and 1.