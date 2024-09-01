# ObjFile Functions

[Return to Functions](../functions.html)

## ObjFile_Create
<pre>
    Arguments:
        1) real const: objectType
    Return Type:
        real
</pre>
Creates a file object of the specified type and returns its ID.

Object types are:
<pre>
OBJ_FILE_TEXT: (a text file)
OBJ_FILE_BINARY: (a binary file)
</pre>

## ObjFile_Open
<pre>
    Arguments:
        1) real: objectID
        2) string: pathFile
    Return Type:
        bool
</pre>
Opens a file for reading with the specified path and binds the specified file object to the opened file.

Returns true if the file was opened successfully, otherwise false.

## ObjFile_OpenNW
<pre>
    Arguments:
        1) real: objectID
        2) string: pathFile
    Return Type:
        bool
</pre>
Opens a file for both reading and writing with the specified path and binds the specified file object to the opened file.

Returns true if the file was opened successfully, otherwise false.

## ObjFile_Store
<pre>
    Arguments:
        1) real: objectID
        2) string: pathFile
</pre>
Saves a file previously opened with ObjFile_OpenNW.

Must be called once after writing the data.

## ObjFile_GetSize
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the file size of the file object.

## ObjFile_GetLastWriteTimeMS
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns a timestamp representing the last time the file was written to in milliseconds.