# ObjRender Sequence Functions

[Return to Functions](../functions.html)

&nbsp;

Related Pages:
- [Using Render Sequences](./render_sequences.html)
- [RenderSequenceData Functions](./render_sequence_data.html)
- [Render Sequence Constants](./render_sequence_constants.html)

---

## ObjRender_AddSequenceCommand
<pre>
    Arguments:
        1) real: objID
        2) real const: renderCommandType
        3+) real: args...
    Returns:
        real: index
</pre>
Adds a [render command](./render_sequence_constants.html) to the object's render sequence and returns its index.

Required arguments for each type vary, see the list of commands for more details.

## ObjRender_RemoveSequenceCommand
<pre>
    Arguments:
        1) real: objID
</pre>
Removes the last render command from the object's render sequence.

## ObjRender_InitializeSequence
<pre>
    Arguments:
        1) real: objID
        2) real: size
</pre>
Initializes the object's render sequence, optionally reserving space (0 or NULL to ignore) for size commands.

## ObjRender_SetSequence
<pre>
    Arguments:
        1) real: objID
        2) real: dataSeqID
</pre>
Sets the object's render sequence to dataSeqID, which must be a RenderSequenceData.

## ObjRender_CopySequence
<pre>
    Arguments:
        1) real: objID
        2) real: objID2
</pre>
Copies objID2's render sequence to objID.

## ObjRender_PlaySequence
<pre>
    Arguments:
        1) real: objID
</pre>
Starts playing the object's render sequence from the beginning.

## ObjRender_StartSequence
<pre>
    Arguments:
        1) real: objID
</pre>
Starts playing the object's render sequence from the beginning.

This is an alias for ObjRender_PlaySequence.

## ObjRender_StopSequence
<pre>
    Arguments:
        1) real: objID
        2) bool: bCancelTweens
</pre>
Stops playing the object's render sequence.

if bCancelTweens is true, cancels any _TWEEN_ type commands.

## ObjRender_PauseSequence
<pre>
    Arguments:
        1) real: objID
        2) bool: bCancelTweens
</pre>
Pauses the object's render sequence without resetting its state.

if bCancelTweens is true, cancels any _TWEEN_ type commands.

## ObjRender_ResumeSequence
<pre>
    Arguments:
        1) real: objID
</pre>
Resumes playing a previously paused object's render sequence.

## ObjRender_PatchSequenceJump
<pre>
    Arguments:
        1) real: objID
        2) real: jumpIndex
</pre>
Patches the jump at jumpIndex in the render sequence to point to the next added render command.

## ObjRender_SetSequenceOnFinish
<pre>
    Arguments:
        1) real: objID
        2) function: funcOnFinish
</pre>
Sets the function to call after the render sequence finishes executing.

funcOnFinish cannot be task or sub and must take 1 parameter.

## ObjRender_GetSequenceTimer
<pre>
    Arguments:
        1) real: objID
    Returns:
        real: timer
</pre>
Returns the render sequence's current timer value. This is set by RC_WAIT and counts down to 0.

## ObjRender_SetSequenceTimer
<pre>
    Arguments:
        1) real: objID
        2) real: timer
</pre>
Sets the render sequence's timer value directly. A command of type RC_WAIT should be used instead for most cases.

## ObjRender_GetSequenceIndex
<pre>
    Arguments:
        1) real: objID
    Returns:
        real: index
</pre>
Returns the render sequence's current instruction index.

This may be inaccurate during execution, since render sequences run ahead of scripts.

## ObjRender_SetSequenceIndex
<pre>
    Arguments:
        1) real: objID
        2) real: index
</pre>
Sets the render sequence's instruction index directly.

This can be useful for setting the initial index to start at.

## ObjRender_SequenceIsStopped
<pre>
    Arguments:
        1) real: objID
    Returns:
        bool: bStopped
</pre>
Returns true if the sequence is stopped or finished, otherwise returns false.

## ObjRender_SequenceIsPaused
<pre>
    Arguments:
        1) real: objID
    Returns:
        bool: bPaused
</pre>
Returns true if the sequence is paused, otherwise returns false.

## ObjRender_SequenceIsRunning
<pre>
    Arguments:
        1) real: objID
    Returns:
        bool: bRunning
</pre>
Returns true if the sequence is running, otherwise returns false.