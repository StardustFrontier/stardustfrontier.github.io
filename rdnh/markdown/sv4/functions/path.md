# Path Functions

[Return to Functions](../functions.html)

## GetModuleDirectory
```
    Return Type:
        string
```
Returns the directory containing the running th_dnh.exe file.

## GetMainStgScriptPath
```
    Return Type:
        string
```
Returns the path of the currently running stage script.

## GetMainPackageScriptPath
```
    Return Type:
        string
```
Returns the path of the currently running package script.

## GetMainStgScriptDirectory
```
    Return Type:
        string
```
Returns the directory of the currently running stage script.

## GetUserScriptDirectory
```
    Return Type:
        string
```
Returns the user-defined script directory.

This is set in the rdnh.def file with the *UserScriptDir* property.

## GetMainScriptDirectory
```
    Return Type:
        string
```
Returns the directory of the running script, ignoring included files.

## GetMainScriptPath
```
    Return Type:
        string
```
Returns the path of the running script, ignoring included files.

## GetCurrentScriptDirectory
```
    Return Type:
        string
```
Returns the directory of the file in which this function was called.

## GetCurrentScriptPath
```
    Return Type:
        string
```
Returns the path of the file in which this function was called.

## GetDirectoryList
```
    Arguments:
        1) string: path
    Return Type:
        array[string]
```
Returns an array of the directories available within the directory of the specified path.

## GetFilePathList
```
    Arguments:
        1) string: path
    Return Type:
        array[string]
```
Returns a list of files in the folder of the specified file path (or folder path).

This function will not list any files within an archive (.dat) file. In that case, use [GetArchiveFilePathList](#getarchivefilepathlist) instead.

## GetArchiveFilePathList
```
    Arguments:
        1) string: archivePath
        2) bool: bFullPath
    Return Type:
        array[string]
```
Returns an array of all file paths within the given archive file.\
If bFullPath is true, the paths will be full absolute paths. Otherwise, they will be relative to the archive's directory. 

Note: The archive file must already be loaded before calling this function.

## GetFileDirectory
```
    Arguments:
        1) string: path
    Return Type:
        string
```
Returns the directory of the specified file path. Specifically, returns the input string up to the rightmost forward slash, with backslashes removed.

## GetDirectoryName
```
    Arguments:
        1) string: path
    Return Type:
        string
```
Returns the name of the directory for the given path.

## GetFileName
```
    Arguments:
        1) string: path
    Return Type:
        string
```
Returns the name of the file for the given path.

## GetFileNameWithoutExtension
```
    Arguments:
        1) string: path
    Return Type:
        string
```
Returns the name of the file for the given path with its extension.

## GetFileExtension
```
    Arguments:
        1) string: path
    Return Type:
        string
```
Returns the file extension from the given filename.

## GetFileLastWriteTimeMillis
```
    Arguments:
        1) string: path
    Returns:
        real: timestamp
```
Returns a timestamp representing the time this file was last written to in milliseconds.

This is useful for comparing to other timestamps of the same file to see if its contents have changed.

## IsFileExists
```
    Arguments:
        1) string: path
    Returns:
        bool: bExists
```
Returns true if the file exists, otherwise returns false.

## DeleteFile
```
    Arguments:
        1) string: path
    Returns:
        bool: bSucceeded
```
Deletes the file at the given path and returns whether or not the deletion succeeded.

For safety reasons, currently this function only works on full paths that contain the module directory.

## CopyFile
```
    Arguments:
        1) string: pathSource
        2) string: pathDest
        3) bool: bOverwrite = false
    Returns:
        bool: bSucceeded
```
Copies the file from pathSource to pathDest.

If a file already exists at pathDest and bOverwrite is true, it will be overwritten. Otherwise, the function will fail.

## RenameFile
```
    Arguments:
        1) string: pathSource
        2) string: pathDest
        3) bool: bOverwrite = false
    Returns:
        bool: bSucceeded
```
Renames the file at pathSource to pathDest.

If a file already exists at pathDest and bOverwrite is true, it will be overwritten. Otherwise, the function will fail.\
This function will also fail if the source and destination are in different directories.

## GetScriptPathList
```
    Arguments:
        1) string: path
        2) const real: scriptType
    Return Type:
        array[string]
```
Returns an array of available (selectable at selection screen) scripts of the specified type within the directory of the specified path.

Script types are:
- <scode>TYPE_SCRIPT_ALL</scode>
- <scode>TYPE_SCRIPT_PLAYER</scode>
- <scode>TYPE_SCRIPT_SINGLE</scode>
- <scode>TYPE_SCRIPT_PLURAL</scode>
- <scode>TYPE_SCRIPT_STAGE</scode>
- <scode>TYPE_SCRIPT_PACKAGE</scode>