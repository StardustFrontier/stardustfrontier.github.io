# ObjRender Sequence Functions

[Return to Functions](../functions.html)

&nbsp;

Related Pages:
- [Using Render Sequences](./render_sequences.html)
- [RenderSequenceData Functions](./render_sequence_data.html)
- [Render Sequence Constants](./render_sequence_constants.html)

---

## ObjRender_AddSequenceCommand
```
    Arguments:
        1) real: objID
        2) real const: renderCommandType
        3+) real: args...
    Returns:
        real: index
```
Adds a [render command](./render_sequence_constants.html) to the object's render sequence and returns its index.

Required arguments for each type vary, see the list of commands for more details.

## ObjRender_RemoveSequenceCommand
```
    Arguments:
        1) real: objID
```
Removes the last render command from the object's render sequence.

## ObjRender_InitializeSequence
```
    Arguments:
        1) real: objID
        2) real: size
```
Initializes the object's render sequence, optionally reserving space (0 or NULL to ignore) for size commands.

## ObjRender_SetSequence
```
    Arguments:
        1) real: objID
        2) real: dataSeqID
```
Sets the object's render sequence to dataSeqID, which must be a RenderSequenceData.

## ObjRender_CopySequence
```
    Arguments:
        1) real: objID
        2) real: objID2
```
Copies objID2's render sequence to objID.

## ObjRender_PlaySequence
```
    Arguments:
        1) real: objID
```
Starts playing the object's render sequence from the beginning.

## ObjRender_StartSequence
```
    Arguments:
        1) real: objID
```
Starts playing the object's render sequence from the beginning.

This is an alias for ObjRender_PlaySequence.

## ObjRender_StopSequence
```
    Arguments:
        1) real: objID
        2) bool: bCancelTweens
```
Stops playing the object's render sequence.

if bCancelTweens is true, cancels any _TWEEN_ type commands.

## ObjRender_PauseSequence
```
    Arguments:
        1) real: objID
        2) bool: bCancelTweens
```
Pauses the object's render sequence without resetting its state.

if bCancelTweens is true, cancels any _TWEEN_ type commands.

## ObjRender_ResumeSequence
```
    Arguments:
        1) real: objID
```
Resumes playing a previously paused object's render sequence.

## ObjRender_PatchSequenceJump
```
    Arguments:
        1) real: objID
        2) real: jumpIndex
```
Patches the jump at jumpIndex in the render sequence to point to the next added render command.

## ObjRender_GetSequenceTimer
```
    Arguments:
        1) real: objID
    Returns:
        real: timer
```
Returns the render sequence's current timer value. This is set by RC_WAIT and counts down to 0.

## ObjRender_SetSequenceTimer
```
    Arguments:
        1) real: objID
        2) real: timer
```
Sets the render sequence's timer value directly. A command of type RC_WAIT should be used instead for most cases.

## ObjRender_GetSequenceIndex
```
    Arguments:
        1) real: objID
    Returns:
        real: index
```
Returns the render sequence's current instruction index.

This may be inaccurate during execution, since render sequences run ahead of scripts.

## ObjRender_SetSequenceIndex
```
    Arguments:
        1) real: objID
        2) real: index
```
Sets the render sequence's instruction index directly.

This can be useful for setting the initial index to start at.

## ObjRender_SetSequenceVar
```
    Arguments:
        1) real: objID
        2) real: varID
        3) real: value
```
Sets the render sequence variable with the given ID to the given value.

## ObjRender_SetSequenceVars
```
    Arguments:
        1) real: objID
        2+) real: values...
```
Sets the values of each render sequence variable in order.

_**Note**: If only a few variables need to be set and they are in order, then only that amount of values needs to be passed._

## ObjRender_SequenceIsStopped
```
    Arguments:
        1) real: objID
    Returns:
        bool: bStopped
```
Returns true if the sequence is stopped or finished, otherwise returns false.

## ObjRender_SequenceIsPaused
```
    Arguments:
        1) real: objID
    Returns:
        bool: bPaused
```
Returns true if the sequence is paused, otherwise returns false.

## ObjRender_SequenceIsRunning
```
    Arguments:
        1) real: objID
    Returns:
        bool: bRunning
```
Returns true if the sequence is running, otherwise returns false.