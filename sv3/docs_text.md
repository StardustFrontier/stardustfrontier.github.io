# Text Functions

[Return to Functions](./../rednh_functions.html)

## InstallFont
<pre>
    Arguments:
        1) string: path
    Return Type:
        bool
</pre>
Loads the given font, which can be used with ObjText_SetFontType, allowing for usage of fonts that are not standard to Windows.

Returns true if successful.

## ToString
<pre>
    Arguments:
        1) any: value
    Return Type:
        string
</pre>
Returns the value as a string.

## IntToString
<pre>
    Arguments:
        1) real: value
    Return Type:
        string
</pre>
Returns the value as a string, omits any decimal places.

## itoa
<pre>
    Arguments:
        1) real: value
    Return Type:
        string
</pre>
Returns the value as a string, omits any decimal places.

This function is identical to IntToString.

## rtoa
<pre>
    Arguments:
        1) real: value
    Return Type:
        string
</pre>
Returns the real value as a string.

## rtos
<pre>
    Arguments:
        1) string: format
        2) real: value
    Return Type:
        string
</pre>
Returns the value as a string, with some filtering options.

The format is presented as a string that determines how many digits will be shown.\
It can contain any combination of the following three characters: "0", ".", "\#".\
"0" is a slot for a digit.
\"." represents the decimal place in the string.\
"\#" creates a space in the string.
Example: rtos("000.000", 1.23) = "001.230", and rtos("#00", 1.23) = " 01".

## vtos
<pre>
    Arguments:
        1) string: format
        2) any: value
    Return Type:
        string
</pre>
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
<pre>
    Arguments:
        1) string: value
    Return Type:
        real
</pre>
Converts a string to an integer.

If the string does not represent a valid number, then 0 will be returned.

## ator
<pre>
    Arguments:
        1) string: value
    Return Type:
        real
</pre>
Converts a string to a real number.

If the string does not represent a valid number, then 0 will be returned.

## TrimString
<pre>
    Arguments:
        1) string: str
    Return Type:
        string
</pre>
Returns the string with spaces removed from the beginning and ending of the text.

For example, TrimString(" ABC ") will return "ABC".

## SplitString
<pre>
    Arguments:
        1) string: str
        2) string: delimiter
    Return Type:
        string array
</pre>
Returns an array containing the split strings.

For example, SplitString("A/123/BCD", "/") will return ["A", "123", "BCD"].

## StringReplace
<pre>
    Arguments:
        1) string: str
        2) string: substring
        3) string: replacement
        4) real: count
    Return Type:
        string
</pre>
Replaces the given number of occurrences of substring in str with a replacement string and returns it.

If count is `NULL`, it will replace all matches.

## StringEraseAllChar
<pre>
    Arguments:
        1) string: str
        2) string: charList
    Return Type:
        string
</pre>
Erases all occurrences of the given chars in the list from the string and returns it.

*Note: charList is passed as a **string**.*