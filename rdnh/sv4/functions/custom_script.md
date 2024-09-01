# Custom Script Functions

[Return to Functions](../functions.html)

## SetShotDeleteEventEnable
<pre>
    Arguments:
        1) real: eventType
        2) bool: bEventEnable
</pre>
Sets whether the specified bullet deletion event is allowed to occur.

Default is false for both event types.
Available event types are:
<pre>
EV_DELETE_SHOT_IMMEDIATE - event will delete the shot immediately
EV_DELETE_SHOT_FADE - event will fade out the shot
</pre>