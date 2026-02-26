# ObjFIleB Functions

[Return to Functions](../functions.html)

## ObjFileB_SetByteOrder
```
    Arguments:
        1) real: objectID
        2) real const: byteOrder
```
Sets the Byte Order of the file.

Defaults to ENDIAN_LITTLE.
Available byte orders are:
```
ENDIAN_LITTLE: (Little endian)
ENDIAN_BIG: (Big endian)
```

## ObjFileB_SetCharacterCode
```
    Arguments:
        1) real: objectID
        2) real const: characterCode
```
Sets the Character Code of the file.

This is necessary for reading strings with [ObjFileB_ReadString](objfileb_readstring).\
Defaults to CODE_ACP.\
Available character codes are:
```
CODE_ACP: ANSI/Shift-JIS
CODE_UTF8: UTF8
CODE_UTF16LE: UTF16 LE
CODE_UTF16BE: UTF16 BE
```

## ObjFileB_GetPointer
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the position of the current file pointer.

## ObjFileB_Seek
```
    Arguments:
        1) real: objectID
        2) real: position
```
Sets the position of the current file pointer.

## ObjFileB_ReadBoolean
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Reads a byte from the file and returns a boolean value.

This will also advance the file pointer by 1 byte.

## ObjFileB_ReadByte
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Reads a signed byte from the file and returns it (1-byte integer).

This will also advance the file pointer by 1 byte.

## ObjFileB_ReadShort
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Reads a signed short from the file and returns it (2-byte integer).

This will also advance the file pointer by 2 bytes.

## ObjFileB_ReadInteger
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Reads a signed integer from the file and returns it (4-byte integer).

This will also advance the file pointer by 4 bytes.

## ObjFileB_ReadLong
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Reads a signed long from the file and returns it (8-byte integer).

This will also advance the file pointer by 8 bytes.

## ObjFileB_ReadFloat
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Reads a float from the file and returns it (4-byte floating point).

This will also advance the file pointer by 4 bytes.

## ObjFileB_ReadDouble
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Reads a double from the file and returns it (8-byte floating point).

## ObjFileB_ReadString
```
    Arguments:
        1) real: objectID
        2) real: size
    Return Type:
        string
```
Reads a string of the given size in bytes from the file and returns it.

This will also advance the file pointer by 8 bytes.

## ObjFileB_ReadAllBytes
```
    Arguments:
        1) real: objectID
    Return Type:
        real array
```
Reads the entire file and returns it as an array of individual bytes.

This will also advance the file pointer to the end of the file.

## ObjFileB_WriteBoolean
```
    Arguments:
        1) real: objectID
        2) bool: value
```
Adds a boolean value to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteByte
```
    Arguments:
        1) real: objectID
        2) real: value
```
Adds a 1-byte integer to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteShort
```
    Arguments:
        1) real: objectID
        2) real: value
```
Adds a 2-byte integer to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteInteger
```
    Arguments:
        1) real: objectID
        2) real: value
```
Adds a 4-byte integer to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteLong
```
    Arguments:
        1) real: objectID
        2) real: value
```
Adds an 8-byte integer to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteFloat
```
    Arguments:
        1) real: objectID
        2) real: value
```
Adds a 4-byte floating point number to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteDouble
```
    Arguments:
        1) real: objectID
        2) real: value
```
Adds an 8-byte floating point number to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteString
```
    Arguments:
        1) real: objectID
```
Adds a string to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.

## ObjFileB_WriteAllBytes
```
    Arguments:
        1) real: objectID
```
Adds an array of bytes to the list of bytes to be output to the file.

This will be actually written to the file when [ObjFile_Store](./docs_file_object.html#objfile_store) is called.