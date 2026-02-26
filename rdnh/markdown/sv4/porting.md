# Porting from RDNH SV3 to SV4

[Return to Index](./docs.html)

#

This page documents the steps to port a script from ScriptVersion 3 to ScriptVersion 4.

If I missed anything, please let me know.\
-- Mana

## General
The save file formats have changed, any .dat files saved by the engine should be deleted manually (including LogWindow.dat if you want it to start with all filters on by default)

## Arrays
Arrays are now _references_, ensure all array usage now takes this into account:
- When passing arrays to a function, if you want to work with a copy of the array instead of directly modifying the original array, you must make a local copy like: `let arrCopy = copy(arr);`
- The above point is also true for assigning an existing array to a variable, `let arr2 = arr1;` is a reference to the _same array_
- `arr[index] = value;` will modify all references to the array
- `~` and `~=` operators do not modify the array, they create a new array leaving the original array untouched

## Strings
Strings are now references to immutable sequences of characters, _not_ arrays. The engine will attempt to de-duplicate simple strings (alphanumeric, underscores, dots, and slashes) during compilation to make comparison between strings faster.

Important points:
- The `~` and `~=` operators still work as expected
- `str[index] = value;` will no longer work and will raise a clear error message
- `array(str);` can be used to construct a modifiable array containing all of the characters of `str`
- `string(value)` can be used to construct a new string from any type

## Collection Type Warning
All collection types (array, string, table) are references and use simple reference counting garbage collection. This means that if you create a reference cycle, **the memory can leak**.\
Strings, despite being a collection type, cannot create reference cycles because they are immutable sequences of _char_ (a non-collection type).

_**Note**: The [copy(collection)](./functions/other.html#copy) function can be used to safely store a copy of a collection within itself._

The following are examples of reference cycles that can cause a leak and how to avoid them:
- arr[index] = arr
  - use arr[index] = copy(arr) instead
- tab.property = tab;
  - use tab.property = copy(tab) instead
- tab["property"] = tab;
  - use tab["property"] = copy(tab) instead
- any array_ or table_ function that adds an element
  - pass a copy as the element to add instead
  
The concatenation operators ~ and ~= _always_ create a deep copy automatically and are therefore always safe to use.

## Operators
- The absolute value operator has been removed, the _abs_ or _absolute_ function should be used instead
- The exponentiation operator ^ has been changed to ** (and its assignment version is **=)
  - ^ is now the bitwise xor operator

## Functions
Some new functions are known to have the same names as functions in existing scripts:
- SetDifficulty
- GetDifficulty

## Keywords
Some new keywords that were introduced are likely to potentially have the same names as variables in existing scripts, ensure that no variables are named the following:
- vdif
- const
- nil
- bool
- real
- char
- array
- string
- table