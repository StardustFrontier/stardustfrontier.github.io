# Path Functions

[Return to Functions](../functions.html)

## GetFileDirectory
<pre>
    Arguments:
        1) string: path
    Return Type:
        string
</pre>
Returns the directory of the specified file path. Specifically, returns the input string up to the rightmost forward slash, with backslashes removed.

## GetFilePathList
<pre>
    Arguments:
        1) string: path
    Return Type:
        array[string]
</pre>
Returns a list of files in the folder of the specified file path (or folder path).

This function will not list any files within an archive (.dat) file. In that case, use [GetArchiveFilePathList](#getarchivefilepathlist) instead.

## GetArchiveFilePathList
<pre>
    Arguments:
        1) string: archivePath
        2) bool: bFullPath
    Return Type:
        array[string]
</pre>
Returns an array of all file paths within the given archive file.\
If bFullPath is true, the paths will be full absolute paths. Otherwise, they will be relative to the archive's directory. 

Note: The archive file must already be loaded before calling this function.

## GetDirectoryList
<pre>
    Arguments:
        1) string: path
    Return Type:
        array[string]
</pre>
Returns an array of the directories available within the directory of the specified path.

## GetModuleDirectory
<pre>
    Return Type:
        string
</pre>
Returns the directory containing the running th_dnh.exe file.

## GetMainStgScriptPath
<pre>
    Return Type:
        string
</pre>
Returns the path of the currently running stage script.

## GetMainPackageScriptPath
<pre>
    Return Type:
        string
</pre>
Returns the path of the currently running package script.

## GetMainStgScriptDirectory
<pre>
    Return Type:
        string
</pre>
Returns the directory of the currently running stage script.

## GetUserScriptDirectory
<pre>
    Return Type:
        string
</pre>
Returns the user-defined script directory.

This is set in the rdnh.def file with the *UserScriptDir* property.

## GetMainScriptDirectory
<pre>
    Return Type:
        string
</pre>
Returns the directory of the running script, ignoring included files.

## GetCurrentScriptDirectory
<pre>
    Return Type:
        string
</pre>
Returns the directory of the file in which this function was called.

## GetCurrentScriptPath
<pre>
    Return Type:
        string
</pre>
Returns the path of the file in which this function was called.

## GetScriptPathList
<pre>
    Arguments:
        1) string: path
        2) const real: scriptType
    Return Type:
        array[string]
</pre>
Returns an array of available (selectable at selection screen) scripts of the specified type within the directory of the specified path.

Script types are:
- TYPE_SCRIPT_ALL: All scripts
- TYPE_SCRIPT_PLAYER: Player scripts
- TYPE_SCRIPT_SINGLE: Single scripts
- TYPE_SCRIPT_PLURAL: Plural scripts
- TYPE_SCRIPT_STAGE: Stage scripts
- TYPE_SCRIPT_PACKAGE: Package scripts

## GetFileExtension
<pre>
    Arguments:
        1) string: path
    Return Type:
        string
</pre>
Returns the file extension from the given filename.

## GetFileLastWriteTimeMillis
<pre>
    Arguments:
        1) string: path
    Returns:
        real: timestamp
</pre>
Returns a timestamp representing the time this file was last written to in milliseconds.

This is useful for comparing to other timestamps of the same file to see if its contents have changed.

## IsFileExists
<pre>
    Arguments:
        1) string: path
    Returns:
        bool: bExists
</pre>
Returns true if the file exists, otherwise returns false.

## DeleteFile
<pre>
    Arguments:
        1) string: path
    Returns:
        bool: bSucceeded
</pre>
Deletes the file at the given path and returns whether or not the deletion succeeded.

For safety reasons, currently this function only works on full paths that contain the module directory.

## CopyFile
<pre>
    Arguments:
        1) string: pathSource
        2) string: pathDest
        3) bool: bOverwrite = false
    Returns:
        bool: bSucceeded
</pre>
Copies the file from pathSource to pathDest.

If a file already exists at pathDest and bOverwrite is true, it will be overwritten. Otherwise, the function will fail.

## RenameFile
<pre>
    Arguments:
        1) string: pathSource
        2) string: pathDest
        3) bool: bOverwrite = false
    Returns:
        bool: bSucceeded
</pre>
Renames the file at pathSource to pathDest.

If a file already exists at pathDest and bOverwrite is true, it will be overwritten. Otherwise, the function will fail.\
This function will also fail if the source and destination are in different directories.