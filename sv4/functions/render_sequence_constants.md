# ObjRender Sequence Constants

[Return to Functions](../functions.html)

&nbsp;

Related Pages:
- [Using Render Sequences](./render_sequences.html)
- [ObjRender Sequence Functions](./obj_render_sequence.html)
- [RenderSequenceData Functions](./render_sequence_data.html)

---

## Introduction

In the following sections, arguments listed after the constant name like **RC_SOMETHING(arg1, arg2)** refer to the arguments passed after the constant in the ObjRender_AddSequenceCommand or RenderSequenceData_AddCommand functions.

_**Note**: Argument values must not exceed 9,007,199,254,740,959 (2^53-33)._

## Variables

These are not actually commands. They can be used in the same places as value arguments, but behave as variables.

### Writable
These variables can be set arbitrarily.
<pre>
RC_V0:    variable at index 0
RC_VAR_0: variable at index 0 (alias)

RC_V1:    variable at index 1
RC_VAR_1: variable at index 1 (alias)

RC_V2:    variable at index 2
RC_VAR_2: variable at index 2 (alias)

RC_V3:    variable at index 3
RC_VAR_3: variable at index 3 (alias)
</pre>

### Read-only
These are pseudo-variables and can only be read from, as they actually become function calls internally. Attempting to use them as a destination (such as for RC_SET_VAR) may cause a crash.
<pre>
RC_VAR_RAND: random real value in the range set by RC_SET_RAND_VAR_RANGE

RC_VAR_RAND_INT: random integer value in the range set by RC_SET_RAND_VAR_RANGE

RC_VAR_RAND_ANGLE: random real value in the range [0, 360)

RC_VAR_POS_X: the object's current x position

RC_VAR_POS_Y: the object's current y position

RC_VAR_POS_Z: the object's current z position

RC_VAR_ANGLE_X: the object's current x angle

RC_VAR_ANGLE_Y: the object's current y angle

RC_VAR_ANGLE_Z: the object's current z angle

RC_VAR_SCALE_X: the object's current x scale

RC_VAR_SCALE_Y: the object's current y scale

RC_VAR_SCALE_Z: the object's current z scale
</pre>

## Sequence-related/General Purpose
<pre>
RC_WAIT(frames):
    Delays execution of the next command by the given frames.

RC_PAUSE_HIDE(bForbidUpdates):
    Pauses the sequence and makes the object invisible.
    If bForbidUpdates is true, active tweens will be cancelled and interrupts cannot be triggered anymore.
    Interrupt triggering will be re-enabled when ObjRender_ResumeSequence is called.
	
RC_PAUSE(bForbidUpdates):
    Pauses the sequence.
    If bForbidUpdates is true, active tweens will be cancelled and interrupts cannot be triggered anymore.
    Interrupt triggering will be re-enabled when ObjRender_ResumeSequence is called.

RC_INTERRUPT_LABEL():
    Acts as a label/marker for an interrupt triggered externally.
    This command doesn't actually do anything directly.

RC_NOTIFY_EVENT(scriptId, eventType, args...):
    Calls NotifyEvent.

RC_NOTIFY_EVENT_OWN(eventType, args...):
    Calls NotifyEventOwn.
    The script that is notified will be the one that created the object.

RC_NOTIFY_EVENT_ALL(eventType, args...):
    Calls NotifyEventAll.
</pre>

## Variables and Math
<pre>
RC_SET_VAR(var&, value):
    var = value

RC_ADD(var&, value):
    var += value

RC_SUB(var&, value):
    var -= value

RC_MUL(var&, value):
    var *= value

RC_DIV(var&, value):
    var /= value

RC_MOD(var&, value):
    var %= value

RC_SIN(var&, value):
    var = sin(value)

RC_COS(var&, value):
    var = cos(value)

RC_TAN(var&, value):
    var = tan(value)

RC_ASIN(var&, value):
    var = asin(value)

RC_ACOS(var&, value):
    var = acos(value)

RC_ATAN(var&, value):
    var = atan(value)
	
RC_ATAN2(var&, y, x):
    var = atan2(y, x)

RC_CIRCLE_POS((varResX&, varResY&, angle, radius)):
    varResX = radius * cos(angle)
    varResY = radius * sin(angle)

RC_RAND(var&, minValue, maxValue):
    var = prand(minValue, maxValue)
    Note: This is separate from the RC_VAR_RAND variables.

RC_SET_RAND_VAR_RANGE(var&, minValue, maxValue):
    Sets the range for RC_VAR_RAND* variables.
</pre>

## Jumps
All jumps use absolute offsets.

<pre>
RC_JUMP(jumpDest):
    Unconditional jump to jumpDest

RC_JUMP_DEC(varCounter&, jumpDest):
    Decrement varCounter, if varCounter > 0: jump to jumpDest

RC_JUMP_E(a, b, jumpDest):
    if a == b: jump to jumpDest

RC_JUMP_NE(a, b, jumpDest):
    if a != b: jump to jumpDest

RC_JUMP_L(a, b, jumpDest):
    if a < b: jump to jumpDest

RC_JUMP_LE(a, b, jumpDest):
    if a <= b: jump to jumpDest

RC_JUMP_G(a, b, jumpDest):
    if a > b: jump to jumpDest

RC_JUMP_GE(a, b, jumpDest):
    if a >= b: jump to jumpDest
	
RC_JUMP_FLAG(flag, jumpDest):
    if Obj_HasFlag(obj, flag): jump to jumpDest

RC_JUMP_NOT_FLAG(flag, jumpDest):
    if !Obj_HasFlag(obj, flag): jump to jumpDest
</pre>

## Obj Manipulation
<pre>
RC_DELETE():
    Calls Obj_Delete.

RC_SET_PRIORITY(priorityI):
    Calls Obj_SetRenderPriorityI.

RC_SET_VISIBLE(bVisible):
    Calls Obj_SetVisible.

RC_SET_FLAG(flag):
    Calls Obj_SetFlag.

RC_CLEAR_FLAG(flag):
    Calls Obj_ClearFlag.
</pre>

## ObjRender Manipulation
<pre>
RC_SET_X(x):
    Calls ObjRender_SetX.

RC_SET_Y(y):
    Calls ObjRender_SetY.

RC_SET_Z(z):
    Calls ObjRender_SetZ.

RC_SET_POSITION(x, y, z):
    Calls ObjRender_SetPosition.

RC_SET_ANGLE_X(x):
    Calls ObjRender_SetAngleX.

RC_SET_ANGLE_Y(y):
    Calls ObjRender_SetAngleY.

RC_SET_ANGLE_Z(z):
    Calls ObjRender_SetAngleZ.

RC_SET_ANGLE(x, y, z):
    Calls ObjRender_SetAngleXYZ.

RC_SET_SCALE_X(x):
    Calls ObjRender_SetScaleX.

RC_SET_SCALE_Y(y):
    Calls ObjRender_SetScaleY.

RC_SET_SCALE_Z(z):
    Calls ObjRender_SetScaleZ.

RC_SET_SCALE(x, y, z):
    Calls ObjRender_SetScaleXYZ.

RC_SET_COLOR(r, g, b):
    Calls ObjRender_SetColor.

RC_SET_COLOR_HEX(color):
    Calls ObjRender_SetColorHex.

RC_SET_COLOR_HSV(h, s, v):
    Calls ObjRender_SetColorHSV.

RC_SET_ALPHA(alpha):
    Calls ObjRender_SetAlpha.

RC_SET_BLEND_TYPE(blendType):
    Calls ObjRender_SetBlendType.

RC_SET_MOVE_SPEED(speedX, speedY, speedZ):
    Calls ObjRender_SetMoveSpeed.

RC_SET_ROTATION_SPEED(speedX, speedY, speedZ):
    Calls ObjRender_SetRotationSpeed.

RC_SET_SCALE_SPEED(speedX, speedY, speedZ):
    Calls ObjRender_SetScaleSpeed.

RC_CANCEL_TWEENS():
    Calls ObjRender_CancelTweens.

RC_TWEEN_POSITION(duration, interpType, endValueX, endValueY, endValueZ):
    Calls ObjRender_TweenPosition.

RC_TWEEN_ANGLE(duration, interpType, endValueX, endValueY, endValueZ):
    Calls ObjRender_TweenAngle.

RC_TWEEN_SCALE(duration, interpType, endValueX, endValueY, endValueZ):
    Calls ObjRender_TweenScale.

RC_TWEEN_COLOR(duration, interpType, endValueR, endValueG, endValueB):
    Calls ObjRender_TweenColor.

RC_TWEEN_ALPHA(duration, interpType, endValueA):
    Calls ObjRender_TweenAlpha.
</pre>

## ObjSprite2D Manipulation
<pre>
RC_SPRITE2D_SET_SOURCE_RECT(left, top, right, bottom):
    Calls ObjSprite2D_SetSourceRect.

RC_SPRITE2D_SET_SOURCE_RECTB(x, y, width, height):
    Calls ObjSprite2D_SetSourceRectB.

RC_SPRITE2D_SET_DEST(typeDest):
    Calls ObjSprite2D_SetDest.

RC_SPRITE2D_SET_DEST_RECT(left, top, right, bottom):
    Calls ObjSprite2D_SetDestRect.

RC_SPRITE2D_SET_DEST_CENTER():
    Calls ObjSprite2D_SetDestCenter.
	
RC_TWEEN_SPRITE2D_DEST_RECT(duration, interpType, left, top, right, bottom):
    Changes the object's destination rect over duration frames with the given interpolation type.
</pre>

## ObjSprite3D Manipulation
<pre>
RC_SPRITE3D_SET_SOURCE_RECT(left, top, right, bottom):
    Calls ObjSprite3D_SetSourceRect.

RC_SPRITE3D_SET_SOURCE_RECTB(x, y, width, height):
    Calls ObjSprite3D_SetSourceRectB.

RC_SPRITE3D_SET_DEST(typeDest):
    Calls ObjSprite3D_SetDest.

RC_SPRITE3D_SET_DEST_RECT(left, top, right, bottom):
    Calls ObjSprit3D_SetDestRect.

RC_SPRITE3D_SET_SOURCE_DEST_RECT(left, top, right, bottom):
    Calls ObjSprit3D_SetSourceDestRect.
</pre>

## Debug
<pre>
RC_PRINT(level = LOG_USER):
    Prints debug info about the sequence to the log window at the given log level (defaults to LOG_USER).
</pre>