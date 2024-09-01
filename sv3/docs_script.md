# Script Functions

[Return to Functions](./docs.html)

## LoadScript
<pre>
    Arguments:
        1) string: scriptPath
    Return Type:
        real
</pre>
Loads and compiles the specified script, and returns its script ID.\
Also calls @Loading and initializes global variables in the script.

## LoadScriptInThread
<pre>
    Arguments:
        1) string: scriptPath
    Return Type:
        real
</pre>
Loads and compiles the specified script in a different thread, and returns its script ID.\
Also calls @Loading and initializes global variables in the script.

## StartScript
<pre>
    Arguments:
        1) real: scriptID
    Return Type:
        real
</pre>
Starts the specified script.\
Calls @Initialize and starts @MainLoop in the script.

## CloseScript
<pre>
    Arguments:
        1) real: scriptID
</pre>
Stops the specified script.

Until this function is called, the script will continue to run.

## IsCloseScript
<pre>
    Arguments:
        1) real: scriptID
    Return Type:
        bool
</pre>
Returns whether the specified script has been stopped.\
Returns true if the script is not running.

## SetScriptArgument
<pre>
    Arguments:
        1) real: scriptID
        2) real: argumentIndex
        3) any: value
</pre>
Before starting the given script with StartScript, sets a value that is to be passed to the given script upon starting.

This value can be retrieved in the started script with [GetScriptArgument](#getscriptargument).

## GetScriptArgument
<pre>
    Arguments:
        1) real: argumentIndex
    Return Type:
        any
</pre>
Returns the value of the specified argument, previously set by SetScriptArgument before the script was started.

## GetScriptArgumentCount
<pre>
    Return Type:
        real
</pre>
Returns the number of arguments set by SetScriptArgument before the script was started.

## CloseStgScene
Ends the current scene (returns to script selection screen).

## GetOwnScriptID
<pre>
    Return Type:
        real
</pre>
Returns the script's own ID.

## GetEventType
<pre>
    Return Type:
        real const
</pre>
Returns the event type currently triggered in @Event.

## GetEventArgument
<pre>
    Arguments:
        1) real: argumentIndex
    Return Type:
        any
</pre>
Returns the argument of the event currently triggered in @Event.

Note: Can be an arbitrary value.

## SetScriptResult
<pre>
    Arguments:
        1) any: eventResult
</pre>
Sets the result of the event in @Event, which can then be retrieved by [GetScriptResult](#getscriptresult).

## GetScriptResult
<pre>
    Arguments:
        1) real: scriptID
    Return Type:
        any
</pre>
Returns the event result from [SetScriptResult](#setscriptresult).

Note: Can be an arbitrary value.

## SetAutoDeleteObject
<pre>
    Arguments:
        1) bool: enable
</pre>
Sets whether to delete all existing objects that were created in the current script at its termination.

If set to true, the current script's objects will be deleted.\
The default value is false.

## NotifyEvent
<pre>
    Arguments:
        1) real: scriptID
        2) real const: eventType
        3+) any: arguments...
</pre>
Calls the @Event of the script with the specified ID, triggering the specified event.

An arbitrary amount of arguments may be passed to the event, but there must be at least one.\
The event type may use a value greater than EV_USER.

## NotifyEventAll
<pre>
    Arguments:
        1) real const: eventType
        2) any: arguments...
</pre>
Calls the @Event of all scripts, triggering the specified event in all scripts listening for it.

An arbitrary amount of arguments may be passed to the event, but there must be at least one.\
The event type may use a value greater than EV_USER.

## GetScriptInfoA1
<pre>
    Arguments:
        1) string: scriptPath
        1) real const: infoType
    Return Type:
        varies
</pre>
Parses and returns information from the script file's header.

Constants for infotype are as follows:
<pre>
INFO_SCRIPT_TYPE: Returns the script type (const): one of TYPE_SCRIPT_PLAYER: Player script, TYPE_SCRIPT_SINGLE: Single script, TYPE_SCRIPT_PLURAL: Plural script, TYPE_SCRIPT_STAGE: Stage script, or TYPE_SCRIPT_PACKAGE: Package script.
INFO_SCRIPT_PATH: Returns the script path (string).
INFO_SCRIPT_ID: Returns the script #ID (int).
INFO_SCRIPT_TITLE: Returns the script #Title (string).
INFO_SCRIPT_TEXT: Returns the script #Text (string).
INFO_SCRIPT_IMAGE: Returns the script #Image (string).
INFO_SCRIPT_REPLAY_NAME: Returns the script #ReplayName (string).
</pre>

## SetScriptDifficulty
<pre>
    Arguments:
        1) real: difficulty
</pre>
Sets the difficulty level of all scripts, affecting both currently running scripts and future started ones.

This is used mainly for the difficulty (colon) operator: `let value = easyVal: normalVal: hardVal: lunaticVal;` and `!ENHL` statements.\
0 = Easy, 1 = Normal, 2 = Hard, 3 = Lunatic, 4 = ArbitraryW, 5 = ArbitraryX, 6 = ArbitraryY, 7 = ArbitraryZ, 8 = ArbitraryO

## GetScriptDifficulty
<pre>
    Return Type:
        real
</pre>
Gets the difficulty level of all running scripts.