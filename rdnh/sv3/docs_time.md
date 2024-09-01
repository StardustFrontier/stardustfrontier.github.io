# Time Functions

[Return to Functions](./docs.html)

## GetCurrentDateTimeS
<pre>
    Return Type:
        string
</pre>
Returns a string containing the current date and time.\
For example, if the current date is 2012/09/16 12:34:56, then "20120916123456" will be returned.\
To convert this to a number, you may use the atoi function like so: `let year = atoi(GetCurrentDateTimeS[0..4]);`

## GetStageTime
<pre>
    Return Type:
        real
</pre>
Returns the amount of time that has elapsed since the start of the main script in milliseconds.

## GetStageTimeF
<pre>
    Return Type:
        real
</pre>
Returns the amount of frames that have elapsed since the start of the main script.

## GetPackageTime
<pre>
    Return Type:
        real
</pre>
Returns the amount of time that has elapsed since the start of the main package in milliseconds.

## GetCurrentFps
<pre>
    Return Type:
        real
</pre>
Returns the current FPS.

## GetReplayFps
<pre>
    Return Type:
        real
</pre>
Returns the FPS of the replay at the current time.\
Note that this value refreshes at a much slower rate than [GetCurrentFps](#getcurrentfps).