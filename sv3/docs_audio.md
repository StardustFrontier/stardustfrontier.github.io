# Audio Functions

[Return to Functions](./docs.html)

## LoadSound
<pre>
    Arguments:
        1) string: path
    Return Type:
        bool
</pre>
Loads the specified sound file.\
Returns true if successful, otherwise returns false.\
*Note: Required before using PlayBGM or PlaySE in the same script as these two functions are called on the respective paths.*

## RemoveSound
<pre>
    Arguments:
        1) string: path
</pre>
Unloads the specified sound file.

## PlayBGM
<pre>
    Arguments:
        1) string: path
        2) real: loopStart
        3) real: loopEnd
</pre>
Plays the specified sound file as a looping BGM.\
You can be more precise by using decimals.

## PlaySE
<pre>
    Arguments:
        1) string: path
</pre>
Plays specified sound file as a sound effect.

## StopSound
<pre>
    Arguments:
        1) string: path
</pre>
Stops playing the specified sound file.

## SetSoundDivisionVolumeRate
<pre>
    Arguments:
        1) real const: soundDivision
        2) real: volumeRate
</pre>
Sets the volume rate for the specified sound division.

## GetSoundDivisionVolumeRate
<pre>
    Arguments:
        1) real const: soundDivision
</pre>
Returns the volume rate of the specified sound division.