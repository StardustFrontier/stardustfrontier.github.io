# ObjFIleB Functions

[Return to Functions](../functions.html)

## ObjFileB_SetByteOrder
<pre>
    Arguments:
        1) real: objectID
        2) real const: byteOrder
</pre>
Sets the Byte Order of the file.

Defaults to ENDIAN_LITTLE.
Available byte orders are:
<pre>
ENDIAN_LITTLE: (Little endian)
ENDIAN_BIG: (Big endian)
</pre>

## ObjFileB_SetCharacterCode
<pre>
    Arguments:
        1) real: objectID
        2) real const: characterCode
</pre>
Sets the Character Code of the file.

This is necessary for reading strings with [ObjFileB_ReadString](objfileb_readstring).\
Defaults to CODE_ACP.\
Available character codes are:
<pre>
CODE_ACP: ANSI/Shift-JIS
CODE_UTF8: UTF8
CODE_UTF16LE: UTF16 LE
CODE_UTF16BE: UTF16 BE
</pre>

## ObjFileB_GetPointer
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the position of the current file pointer.

## ObjFileB_Seek
<pre>
    Arguments:
        1) real: objectID
        2) real: position
</pre>
Sets the position of the current file pointer.

## ObjFileB_ReadBoolean
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Reads a byte from the file and returns a boolean value.

This will also advance the file pointer by 1 byte.

## ObjFileB_ReadByte
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Reads a signed byte from the file and returns it (1-byte integer).

This will also advance the file pointer by 1 byte.

## ObjFileB_ReadShort
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Reads a signed short from the file and returns it (2-byte integer).

This will also advance the file pointer by 2 bytes.

## ObjFileB_ReadInteger
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Reads a signed integer from the file and returns it (4-byte integer).

This will also advance the file pointer by 4 bytes.

## ObjFileB_ReadLong
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Reads a signed long from the file and returns it (8-byte integer).

This will also advance the file pointer by 8 bytes.

## ObjFileB_ReadFloat
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Reads a float from the file and returns it (4-byte floating point).

This will also advance the file pointer by 4 bytes.

## ObjFileB_ReadDouble
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Reads a double from the file and returns it (8-byte floating point).

## ObjFileB_ReadString
<pre>
    Arguments:
        1) real: objectID
        2) real: size
    Return Type:
        string
</pre>
Reads a string of the given size in bytes from the file and returns it.

This will also advance the file pointer by 8 bytes.

## ObjFileB_ReadAllBytes
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real array
</pre>
Reads the entire file and returns it as an array of individual bytes.

This will also advance the file pointer to the end of the file.

## ObjFileB_WriteBoolean
<pre>
    Arguments:
        1) real: objectID
        2) bool: value
</pre>
Adds a boolean value to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteByte
<pre>
    Arguments:
        1) real: objectID
        2) real: value
</pre>
Adds a 1-byte integer to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteShort
<pre>
    Arguments:
        1) real: objectID
        2) real: value
</pre>
Adds a 2-byte integer to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteInteger
<pre>
    Arguments:
        1) real: objectID
        2) real: value
</pre>
Adds a 4-byte integer to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteLong
<pre>
    Arguments:
        1) real: objectID
        2) real: value
</pre>
Adds an 8-byte integer to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteFloat
<pre>
    Arguments:
        1) real: objectID
        2) real: value
</pre>
Adds a 4-byte floating point number to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteDouble
<pre>
    Arguments:
        1) real: objectID
        2) real: value
</pre>
Adds an 8-byte floating point number to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteString
<pre>
    Arguments:
        1) real: objectID
</pre>
Adds a string to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteAllBytes
<pre>
    Arguments:
        1) real: objectID
</pre>
Adds an array of bytes to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.