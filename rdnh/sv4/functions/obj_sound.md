# ObjSound Functions

[Return to Functions](../functions.html)

## ObjSound_Create
<pre>
    Return Type:
        real
</pre>
Creates a sound object and returns its ID.

## ObjSound_Load
<pre>
    Arguments:
        1) real: objectID
        2) string: pathSound
</pre>
Loads the specified sound file.

## ObjSound_Play
<pre>
    Arguments:
        1) real: objectID
</pre>
Plays the sound file associated with the object.

## ObjSound_Stop
<pre>
    Arguments:
        1) real: objectID
</pre>
Stops the sound file associated with the object.

## ObjSound_SetVolumeRate
<pre>
    Arguments:
        1) real: objectID
        2) real: volumeRate
</pre>
Sets the volume of the sound object (0-100).

## ObjSound_SetVolumeDecibel
<pre>
    Arguments:
        1) real: objectID
        2) real: dB
</pre>
Sets the volume rate for the sound object in decibels subtracted from the source sound.

Example: ObjSound_SetVolumeDecibel(obj, -8.5);\
The above would set a volume rate that reduces the volume by 8.5 dB.

## ObjSound_SetPanRate
<pre>
    Arguments:
        1) real: objectID
        2) real: panRate
</pre>
Sets the pan volume of the sound object (-100-100).

0 is neutral, -100 is left-side only, 100 is right-side only.

## ObjSound_SetFrequency
<pre>
    Arguments:
        1) real: objectID
        2) real: frequency
</pre>
Sets the frequency of the sound object in samples.

Pass 0 to reset the frequency to its default value.

## ObjSound_SetFade
<pre>
    Arguments:
        1) real: objectID
        2) real: fadeTime
</pre>
Sets the fade time of the sound object.

Fade value is how much the volume will increase per second; accepts negative values for fadeouts.

## ObjSound_SetLoopEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
When set to true, the sound object will be allowed to loop.

## ObjSound_SetLoopTime
<pre>
    Arguments:
        1) real: objectID
        2) real: loopStart
        3) real: loopEnd
</pre>
Sets the timing of the loop, in seconds.

## ObjSound_SetLoopSampleCount
<pre>
    Arguments:
        1) real: objectID
        2) real: loopStart
        3) real: loopEnd
</pre>
Sets the timing of the loop based on the sample count.

## ObjSound_SetRestartEnable
<pre>
    Arguments:
        1) real: objectID
        2) bool: bEnable
</pre>
When set to true, allows the sound object to continue where it left off instead of restarting every time ObjSound_Play is called.

## ObjSound_SetSoundDivision
<pre>
    Arguments:
        1) real: objectID
        2) real const: soundDivision
</pre>
Specifies whether a sound is a BGM, sound effect, or "voice".

Each sound division has its own separate global volume setting.\
Available sound divisions are:
<pre>
SOUND_BGM
SOUND_SE
SOUND_VOICE
</pre>

## ObjSound_SetStartTime
<pre>
    Arguments:
        1) real: objectID
        2) real: startTime
</pre>
Sets the time for the sound file to start playing at in seconds.

## ObjSound_SetStartTimeSampleCount
<pre>
    Arguments:
        1) real: objectID
        2) real: startTime
</pre>
Sets the time for the sound file to start playing at in samples.

## ObjSound_Seek
<pre>
    Arguments:
        1) real: objectID
        2) real: seekPosition
</pre>
Seeks to the specified position (in seconds) in the playing the sound file.

## ObjSound_SeekSampleCount
<pre>
    Arguments:
        1) real: objectID
        2) real: seekPosition
</pre>
Seeks to the specified position (in samples) in the playing the sound file.

## ObjSound_IsPlaying
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        bool
</pre>
Returns true if the sound file is playing.

## ObjSound_GetVolumeRate
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Returns the volume (0-100) of the sound file.

## ObjSound_GetPosition
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Gets the current playback position of the song in seconds.

***Warning**: This function can only be used to get an average idea of where the position is, because this will only update every few seconds.*

## ObjSound_GetPositionSampleCount
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Gets the current playback position of the song in samples.

***Warning**: This function can only be used to get an average idea of where the position is, because this will only update every few seconds.*