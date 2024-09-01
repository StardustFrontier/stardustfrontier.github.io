# Path Functions

[Return to Functions](./../rednh_functions.html)

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
        string array
</pre>
Returns a list of files in the folder of the specified file path (or folder path).

## GetDirectoryList
<pre>
    Arguments:
        1) string: path
    Return Type:
        string array
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

## GetCurrentScriptDirectory
<pre>
    Return Type:
        string
</pre>
Returns the directory of the file in which this function was called.

## GetScriptPathList
<pre>
    Arguments:
        1) string: path
        2) const real: scriptType
    Return Type:
        string array
</pre>
Returns an array of available (selectable at selection screen) scripts of the specified type within the directory of the specified path. Script types are:
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