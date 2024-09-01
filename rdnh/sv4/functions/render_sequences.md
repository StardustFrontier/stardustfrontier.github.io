# Using Render Sequences

[Return to Functions](../functions.html)

&nbsp;

Related Pages:
- [ObjRender Sequence Functions](./obj_render_sequence.html)
- [RenderSequenceData Functions](./render_sequence_data.html)
- [Render Sequence Constants](./render_sequence_constants.html)

---

## Render Sequences

Render sequences are a new way to control render objects over time. They allow you to build a timeline of commands that set various properties of objects.

A command can be as simple as "instantly set the x-coordinate to 123" to as complex as "smoothly interpolate from the current color values to new ones over 60 frames". Deleting the object is even possible with a command.

All render objects when created have an empty render sequence. This sequence can be added to as soon as the object is created using:
<pre>ObjRender_AddSequenceCommand(obj, renderCommandType, args...)</pre>
While this function is defined as varargs, any extra arguments passed beyond the allowed amount for a type of command will be discarded. If not enough arguments are passed, a default value of 0 will be used.

After adding commands to the render object's sequence, you can begin playing the sequence using:
<pre>ObjRender_PlaySequence(obj)</pre>
and stop it with:
<pre>ObjRender_StopSequence(obj, bCancelTweens)</pre>
When stopping a sequence, if bCancelTweens is true, any commands that change values over time in the sequence that were currently in progress will be forcibly stopped.

Once the sequence is finished playing, if an OnFinish function was set, this will now be called. This function must have 1 parameter so that it can be passed the object ID. The OnFinish function can be set with:
<pre>ObjRender_SetSequenceOnFinish(obj, $func)</pre>
Note that the OnFinish function must be globally accessible in the script and can't be nested inside another function.

Other notes:
- Sequences have a set of 4 writable variables which can be set in a few ways, such as with RC_SET_VAR and RC_RAND
- Variables are used by passing the constant representing the variable as an argument instead of a value
- Variables can be used for performing math or other complex behavior within a sequence

## RenderSequenceData
There is a new data-object type called [RenderSequenceData](./render_sequence_data.html).

RenderSequenceData is a new type of internal value called a DataObject. They are similar to objects, but only hold data.\
Render commands are added to RenderSequenceData using RenderSequenceData_AddCommand.

This is used to create reusable "templates" of render sequences. For example, if you have some kind of effect that always uses the same render sequence, instead of creating the render sequence many times for each object, you can create one RenderSequenceData and assign it to the render object using:
<pre>ObjRender_SetSequence(dataSequence)</pre>
Render sequence command lists are shared. If you later use ObjRender_AddSequenceCommand, it will update _all_ shared command lists.

If you want to create a copy of a render sequence with its own unique command list, use:
<pre>ObjRender_CopySequenceFromObject(objDest, objSource)</pre>

**_Note_**: While command lists are shared, the actual _state_ (progress within the sequence, etc.) is unique to each render object.