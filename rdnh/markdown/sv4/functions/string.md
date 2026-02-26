# String Functions

[Return to Functions](../functions.html)

## string_find
```
    Arguments:
        1) string: str
        2) char|string: toFind
        3) real: startIndex = 0
    Return Type:
        real
```
Finds the character or substring in str and returns the index it starts at or -1 if it was not found.

Optionally, the index to start the operation at can be specified. This is 0 by default.

## string_replace
```
    Arguments:
        1) string: str
        2) char|string: toFind
        3) char|string: replacement
        4) real: count?
    Return Type:
        string
```
Returns a new string with the given number of occurrences of toFind replaced with replacement.

If count is not given, all occurrences will be replaced.

## string_split
```
    Arguments:
        1) string: str
        2) string: delimiter
        3) real: maxSplits?
    Return Type:
        array[string]
```
Splits the string using the given delimiter and returns the result as an array of strings.

If maxSplits is given, only that number of splits will be performed.

_**Note**: Unlike SplitString, if the split results in an empty string it will still be included in the returned array._

## string_starts_with
```
    Arguments:
        1) string: str
        2) string: prefix
    Return Type:
        bool
```
Returns true if the string begins with the given prefix, otherwise returns false.

## string_ends_with
```
    Arguments:
        1) string: str
        2) string: suffix
    Return Type:
        bool
```
Returns true if the string ends with the given suffix, otherwise returns false.

## string_count_char
```
    Arguments:
        1) string: str
        2) char: character
    Return Type:
        string
```
Returns the total occurrences of the given character in str.

## string_join
```
    Arguments:
        1) string: str
        2) array|string|table: collection
    Return Type:
        string
```
Returns a string with all the elements of the collection concatenated together as strings.

## string_lower
```
    Arguments:
        1) string: str
    Return Type:
        string
```
Returns a copy of the string with all characters converted to lowercase.

## string_upper
```
    Arguments:
        1) string: str
    Return Type:
        string
```
Returns a copy of the string with all characters converted to uppercase.

## repr
```
    Arguments:
        1) any: value
    Return Type:
        string
```
Returns a printable string representation describing the value.

This may be identical to string(value) or ToString(value), but in other cases, it's slightly different. For example, string values will retain their double quotes.

## ToString
```
    Arguments:
        1) any: value
    Return Type:
        string
```
Returns the value as a string.

## IntToString
```
    Arguments:
        1) real: value
    Return Type:
        string
```
Returns the value as a string, omits any decimal places.

## IntToCommaString
```
    Arguments:
        1) real: value
    Return Type:
        string
```
Returns the value as an integer string formatted with commas.

## itoa
```
    Arguments:
        1) real: value
    Return Type:
        string
```
Returns the value as a string, omits any decimal places.

This function is identical to IntToString.

## rtoa
```
    Arguments:
        1) real: value
    Return Type:
        string
```
Returns the real value as a string.

## rtos
```
    Arguments:
        1) string: format
        2) real: value
    Return Type:
        string
```
Returns the value as a string, with some filtering options.

The format is presented as a string that determines how many digits will be shown.\
It can contain any combination of the following three characters: "0", ".", "\#".\
"0" is a slot for a digit.
\"." represents the decimal place in the string.\
"\#" creates a space in the string.
Example: rtos("000.000", 1.23) = "001.230", and rtos("#00", 1.23) = " 01".

## vtos
```
    Arguments:
        1) string: format
        2) any: value
    Return Type:
        string
```
Returns the value as a string, with some more filtering options.

The format string is different from rtos in that it's more of a code than directly defining the digits that will be shown.\
First, the number of digits on each side of the decimal are specified (000.00 is 3.2 in the format string).\
Unused digits will be filled with spaces.\
If preceded by a "-", the digits will be right-justified, adding blank spaces to the right instead of the left.\
If preceded by a "0", all digits not occupied by the value will be filled by zeroes.\
If ended with a "d", the value will be presented as an integer.\
If ended with an "f", the value will be presented as a real number.\
If ended with an "s", this indicates the value given was in the form of a string.\
Example: vtos("03d", 1.23) = "001", vtos("3d", 1.23) = "　1", vtos("-3d", 1.23) = "1　", and vtos("03.5f", 1.23) = "001.23000"

## atoi
```
    Arguments:
        1) string: value
    Return Type:
        real
```
Converts a string to an integer.

If the string does not represent a valid number, then 0 will be returned.

## ator
```
    Arguments:
        1) string: value
    Return Type:
        real
```
Converts a string to a real number.

If the string does not represent a valid number, then 0 will be returned.

## TrimString
```
    Arguments:
        1) string: str
    Return Type:
        string
```
Returns the string with spaces removed from the beginning and ending of the text.

For example, TrimString(" ABC ") will return "ABC".

## SplitString
```
    Arguments:
        1) string: str
        2) string: delimiter
    Return Type:
        string array
```
Returns an array containing the split strings.

For example, SplitString("A/123/BCD", "/") will return ["A", "123", "BCD"].

## StringReplace
```
    Arguments:
        1) string: str
        2) string: substring
        3) string: replacement
        4) real: count
    Return Type:
        string
```
Replaces the given number of occurrences of substring in str with a replacement string and returns it.

If count is `NULL`, it will replace all matches.

## StringEraseAllChar
```
    Arguments:
        1) string: str
        2) string: charList
    Return Type:
        string
```
Erases all occurrences of the given chars in the list from the string and returns it.

*Note: charList is passed as a **string**.*

## StringFormat
```
    Arguments:
        1) string: str
        2+) any: values...
    Return Type:
        string
```
Returns a string formatted in the same way as C's printf family of functions.

## sprintf
```
    Arguments:
        1) string: str
        2+) any: values...
    Return Type:
        string
```
Returns a string formatted in the same way as C's printf family of functions.

This is just an alias for [StringFormat](#stringformat).