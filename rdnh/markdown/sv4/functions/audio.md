# Audio Functions

[Return to Functions](../functions.html)

## LoadSound
```
    Arguments:
        1) string: path
    Return Type:
        bool
```
Loads the specified sound file.\
Returns true if successful, otherwise returns false.\
*Note: Required before using PlayBGM or PlaySE in the same script as these two functions are called on the respective paths.*

## RemoveSound
```
    Arguments:
        1) string: path
```
Unloads the specified sound file.

## PlayBGM
```
    Arguments:
        1) string: path
        2) real: loopStart
        3) real: loopEnd
```
Plays the specified sound file as a looping BGM.\
You can be more precise by using decimals.

## PlaySE
```
    Arguments:
        1) string: path
```
Plays specified sound file as a sound effect.

## StopSound
```
    Arguments:
        1) string: path
```
Stops playing the specified sound file.

## SetSoundDivisionVolumeRate
```
    Arguments:
        1) real const: soundDivision
        2) real: volumeRate
```
Sets the volume rate for the specified sound division.

## GetSoundDivisionVolumeRate
```
    Arguments:
        1) real const: soundDivision
```
Returns the volume rate of the specified sound division.