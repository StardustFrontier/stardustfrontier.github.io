# RenderSequenceData Functions

[Return to Functions](../functions.html)

&nbsp;

Related Pages:
- [Using Render Sequences](./render_sequences.html)
- [ObjRender Sequence Functions](./obj_render_sequence.html)
- [Render Sequence Constants](./render_sequence_constants.html)

---

## RenderSequenceData_Create
<pre>
    Arguments:
        1) real?: sizeReserve
    Returns:
        real: dataID
</pre>
Creates a render sequence data-object and returns its ID.

sizeReserve is the amount of memory to pre-allocate for the render sequence's command list.\
This argument may be omitted to use the default value.

_**Note:** This is a data-object, which is NOT a standard object. Only DataObj functions and other RenderSequenceData functions will work on it._

## RenderSequenceData_Delete
<pre>
    Arguments:
        1) real: dataIDs...
</pre>
Deletes the render sequence data-object(s) associated with the given ID(s).

_**Note:** This is an alias for DataObj_Delete._

## RenderSequenceData_CopyCommands
<pre>
    Arguments:
        1) real: dataID
        2) real: sourceDataID
</pre>
Copies the render sequence command list from sourceDataID.

## RenderSequenceData_AddCommand
<pre>
    Arguments:
        1) real: dataID
        2) real const: renderCommandType
        3+) real: args...
    Returns:
        real: index
</pre>
Adds a [render command](./render_sequence_constants.html) to the data's render sequence and returns its index.

## RenderSequenceData_GetCommandCount
<pre>
    Arguments:
        1) real: dataID
    Returns:
        real: commandCount
</pre>
Returns the total number of commands that were added to this data's render sequence.

## RenderSequenceData_SetJumpDest
<pre>
    Arguments:
        1) real: dataID
        2) real: index
        3) real: dest
</pre>
Sets the jump destination of the command at the given index in the sequence to dest.