# Time Functions

[Return to Functions](../functions.html)

## GetCurrentDateTimeS
```
    Return Type:
        string
```
Returns a string containing the current date and time.\
For example, if the current date is 2012/09/16 12:34:56, then "20120916123456" will be returned.\
To convert this to a number, you may use the atoi function like so:
```let year = atoi(GetCurrentDateTimeS[0..4]);</pre>

## GetSystemTimeMicros
```
    Return Type:
        real
```
Returns the current system time in microseconds.

_**Note**: This is an arbitrary timestamp based on some moment in the past, so only the delta between two calls of this function make sense._

## GetSystemTimeMillis
```
    Return Type:
        real
```
Returns the current system time in milliseconds.

_**Note**: This is an arbitrary timestamp based on some moment in the past, so only the delta between two calls of this function make sense._

## GetSystemTimeSecs
```
    Return Type:
        real
```
Returns the current system time in seconds.

_**Note**: This is an arbitrary timestamp based on some moment in the past, so only the delta between two calls of this function make sense._

## GetStageTime
```
    Return Type:
        real
```
Returns the amount of time that has elapsed since the start of the main script in milliseconds.

## GetStageTimeF
```
    Return Type:
        real
```
Returns the amount of frames that have elapsed since the start of the main script.

## GetPackageTime
```
    Return Type:
        real
```
Returns the amount of time that has elapsed since the start of the main package in milliseconds.

## GetCurrentFps
```
    Return Type:
        real
```
Returns the current FPS.

## GetReplayFps
```
    Return Type:
        real
```
Returns the FPS of the replay at the current time.\
Note that this value refreshes at a much slower rate than [GetCurrentFps](#getcurrentfps).