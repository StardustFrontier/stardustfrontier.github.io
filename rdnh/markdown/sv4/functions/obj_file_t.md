# ObjFileT Functions

[Return to Functions](../functions.html)

## ObjFileT_GetLineCount
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns number of lines in the text file.

## ObjFileT_GetLineText
```
    Arguments:
        1) real: objectID
        2) real: lineNumber
    Return Type:
        string
```
Returns the string of the specified line in the text file.

Lines are 1-indexed (the first line is 1) rather than 0-indexed.

## ObjFileT_SplitLineText
```
    Arguments:
        1) real: objectID
        2) real: lineNumber
        3) string: delimiter
    Return Type:
        string array
```
Returns a string array obtained by splitting the specified line of the text file by the specified delimiter character.

## ObjFileT_AddLine
```
    Arguments:
        1) real: objectID
        2) string: lineToAdd
```
Appends a line of text to the end of the list of lines to output.

The line will actually be added to the file once [ObjFile_Store](./docs_file_object.html#objfile_store) has been called.

## ObjFileT_ClearLine
```
    Arguments:
        1) real: objectID
```
Clears all of the lines added with [ObjFileT_AddLine](objfilet_addline)