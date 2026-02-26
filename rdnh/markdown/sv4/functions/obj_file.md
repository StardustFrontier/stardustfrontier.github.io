# ObjFile Functions

[Return to Functions](../functions.html)

## ObjFile_Create
```
    Arguments:
        1) real const: objectType
    Return Type:
        real
```
Creates a file object of the specified type and returns its ID.

Object types are:
```
OBJ_FILE_TEXT: (a text file)
OBJ_FILE_BINARY: (a binary file)
```

## ObjFile_Open
```
    Arguments:
        1) real: objectID
        2) string: pathFile
    Return Type:
        bool
```
Opens a file for reading with the specified path and binds the specified file object to the opened file.

Returns true if the file was opened successfully, otherwise false.

## ObjFile_OpenNW
```
    Arguments:
        1) real: objectID
        2) string: pathFile
    Return Type:
        bool
```
Opens a file for both reading and writing with the specified path and binds the specified file object to the opened file.

Returns true if the file was opened successfully, otherwise false.

## ObjFile_Store
```
    Arguments:
        1) real: objectID
        2) string: pathFile
```
Saves a file previously opened with ObjFile_OpenNW.

Must be called once after writing the data.

## ObjFile_GetSize
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the file size of the file object.

## ObjFile_GetLastWriteTimeMS
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns a timestamp representing the last time the file was written to in milliseconds.