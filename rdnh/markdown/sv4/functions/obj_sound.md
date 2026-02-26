# ObjSound Functions

[Return to Functions](../functions.html)

## ObjSound_Create
```
    Return Type:
        real
```
Creates a sound object and returns its ID.

## ObjSound_Load
```
    Arguments:
        1) real: objectID
        2) string: pathSound
```
Loads the specified sound file.

## ObjSound_Play
```
    Arguments:
        1) real: objectID
```
Plays the sound file associated with the object.

## ObjSound_Stop
```
    Arguments:
        1) real: objectID
```
Stops the sound file associated with the object.

## ObjSound_SetVolumeRate
```
    Arguments:
        1) real: objectID
        2) real: volumeRate
```
Sets the volume of the sound object (0-100).

## ObjSound_SetVolumeDecibel
```
    Arguments:
        1) real: objectID
        2) real: dB
```
Sets the volume rate for the sound object in decibels subtracted from the source sound.

Example: ObjSound_SetVolumeDecibel(obj, -8.5);\
The above would set a volume rate that reduces the volume by 8.5 dB.

## ObjSound_SetPanRate
```
    Arguments:
        1) real: objectID
        2) real: panRate
```
Sets the pan volume of the sound object (-100-100).

0 is neutral, -100 is left-side only, 100 is right-side only.

## ObjSound_SetFrequency
```
    Arguments:
        1) real: objectID
        2) real: frequency
```
Sets the frequency of the sound object in samples.

Pass 0 to reset the frequency to its default value.

## ObjSound_SetFade
```
    Arguments:
        1) real: objectID
        2) real: fadeTime
```
Sets the fade time of the sound object.

Fade value is how much the volume will increase per second; accepts negative values for fadeouts.

## ObjSound_SetLoopEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
When set to true, the sound object will be allowed to loop.

## ObjSound_SetLoopTime
```
    Arguments:
        1) real: objectID
        2) real: loopStart
        3) real: loopEnd
```
Sets the timing of the loop, in seconds.

## ObjSound_SetLoopSampleCount
```
    Arguments:
        1) real: objectID
        2) real: loopStart
        3) real: loopEnd
```
Sets the timing of the loop based on the sample count.

## ObjSound_SetRestartEnable
```
    Arguments:
        1) real: objectID
        2) bool: bEnable
```
When set to true, allows the sound object to continue where it left off instead of restarting every time ObjSound_Play is called.

## ObjSound_SetSoundDivision
```
    Arguments:
        1) real: objectID
        2) real const: soundDivision
```
Specifies whether a sound is a BGM, sound effect, or "voice".

Each sound division has its own separate global volume setting.\
Available sound divisions are:
```
SOUND_BGM
SOUND_SE
SOUND_VOICE
```

## ObjSound_SetStartTime
```
    Arguments:
        1) real: objectID
        2) real: startTime
```
Sets the time for the sound file to start playing at in seconds.

## ObjSound_SetStartTimeSampleCount
```
    Arguments:
        1) real: objectID
        2) real: startTime
```
Sets the time for the sound file to start playing at in samples.

## ObjSound_Seek
```
    Arguments:
        1) real: objectID
        2) real: seekPosition
```
Seeks to the specified position (in seconds) in the playing the sound file.

## ObjSound_SeekSampleCount
```
    Arguments:
        1) real: objectID
        2) real: seekPosition
```
Seeks to the specified position (in samples) in the playing the sound file.

## ObjSound_IsPlaying
```
    Arguments:
        1) real: objectID
    Return Type:
        bool
```
Returns true if the sound file is playing.

## ObjSound_GetVolumeRate
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Returns the volume (0-100) of the sound file.

## ObjSound_GetPosition
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Gets the current playback position of the song in seconds.

***Warning**: This function can only be used to get an average idea of where the position is, because this will only update every few seconds.*

## ObjSound_GetPositionSampleCount
```
    Arguments:
        1) real: objectID
    Return Type:
        real
```
Gets the current playback position of the song in samples.

***Warning**: This function can only be used to get an average idea of where the position is, because this will only update every few seconds.*