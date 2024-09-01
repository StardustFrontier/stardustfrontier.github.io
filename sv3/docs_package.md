# Package Functions

[Return to Functions](./docs.html)

## ClosePackage
Ends the package script.

## InitializeStageScene
Called only once before the start of a stage.

Calling performs the initial processing for the stage.

## FinalizeStageScene
Called only once at the end of a stage.

Calling ends the stage processing and defines the end point of replays.\
*Note: throws an error if the stage script is not yet closed.*

## StartStageScene
Starts the stage script.

## SetStageIndex
<pre>
    Arguments:
        1) real: stageIndex
</pre>
Defines the index of the stage to be started next.

The value does not need to be sequential.\
Specifying an already specified index results in an error.

## SetStageMainScript
<pre>
    Arguments:
        1) string: pathScript
</pre>
Defines the stage script to be started next.

## SetStagePlayerScript
<pre>
    Arguments:
        1) string: pathScript
</pre>
Defines the player script to be used in the stage.

This player must have been declared in the #Player header.

## SetStageReplayFile
<pre>
    Arguments:
        1) string: pathReplay
</pre>
Runs the stage script once with the replay replaying all virtual key presses (including player shots, movement, etc).

Can only be called after InitializeStageScene.\
Since the replay file holds information for each stage, in a multi-stage replay, you can begin playback from a middle stage without having to start from the first stage.

## GetStageSceneState
<pre>
    Return Type:
        const real
</pre>
Returns status information about the currently running stage script.

Defaults to -1 if there is no status information to report.\
Possible return values:
<pre>
STAGE_STATE_FINISHED - whether the stage is finished or not
</pre>

## GetStageSceneResult
<pre>
    Return Type:
        real const
</pre>
Returns a constant value representing the reason the stage was finished.

Possible return values:
<pre>
0 - This is the default return value if none of the others are returned (unsure if safe to expect)
STAGE_RESULT_CLEARED - Stage was cleared
STAGE_RESULT_PLAYER_DOWN - Ran out of lives
STAGE_RESULT_BREAK_OFF - Ended prematurely; was terminated by the player
</pre>

## PauseStageScene
<pre>
    Arguments:
        1) bool: bPause
</pre>
Pauses or resumes the stage script.

This function also notifies either the `EV_PAUSE_ENTER` or `EV_PAUSE_LEAVE` event for every running script.

## TerminateStageScene
Exits out of the currently running stage.

This function will additionally set the stage result to `RESULT_BREAK_OFF`

#

## GetLoadFreePlayerScriptList
<pre>
    Return Type:
        string array
</pre>
Returns an array of the player scripts available in the /script/player/ folder.

## GetFreePlayerScriptCount
<pre>
    Return Type:
        real
</pre>
Returns the number of player scripts available in the /script/player/ folder.

## GetFreePlayerScriptInfo
<pre>
    Arguments:
        1) real: playerScriptIndex
        2) real const: infoType
    Return Type:
        varies
</pre>
Returns various information about the player script based on the given info type constant.

Available info types are:
<pre>
INFO_SCRIPT_PATH        (string): Script path
INFO_SCRIPT_ID          (string): The player script's #ID
INFO_SCRIPT_TITLE       (string): The player script's #Title
INFO_SCRIPT_TEXT        (string): The player script's #Text
INFO_SCRIPT_IMAGE       (string): The player script's #Image
INFO_SCRIPT_REPLAY_NAME (string): The player script's #ReplayName
</pre>

#

## LoadReplayList
Loads a list of the available replays for the current script.

## GetValidReplayIndices
Loads a list of indices for the current script's available replays.

## IsValidReplayIndex
<pre>
    Arguments:
        1) real: replayIndex
    Return Type:
        bool
</pre>
Returns true or false depending on the index chosen is valid to be used in [GetReplayInfo](GetReplayInfo).

## GetReplayInfo
<pre>
    Arguments:
        1) real: replayIndex
        2) real const: infoType
    Return Type:
        varies
</pre>
Returns various information about the replay with the given index based on the given info type constant.

Available info types are:
<pre>
REPLAY_FILE_PATH              - string: (replay file path)
REPLAY_DATE_TIME              - string: (date and time at which the replay was saved)
REPLAY_USER_NAME              - string: (player's name)
REPLAY_TOTAL_SCORE            - real: (final score)
REPLAY_FPS_AVERAGE            - real: (average framerate)
REPLAY_PLAYER_NAME            - string: (player script name)
REPLAY_STAGE_INDEX_LIST       - real array: (list of stage indices that the replay used)
REPLAY_STAGE_START_SCORE_LIST - real array: (List of score indices at the start of each stage (the order of the stage indices is from REPLAY_STAGE_INDEX_LIST))
REPLAY_STAGE_LAST_SCORE_LIST  - real array: (List of score indices at the end of each stage (the order of the stage indices is from REPLAY_STAGE_INDEX_LIST))
REPLAY_COMMENT                - string: (comment set arbitrarily using SetReplayInfo)
</pre>

## SetReplayInfo
<pre>
    Arguments:
        1) real const: infoType
        2) any: data
    Return Type:
        varies
</pre>
Sets the replay information.

Available info types are:
<pre>
REPLAY_COMMENT - string: an arbitrary comment held by the replay.
</pre>

## GetReplayUserData
<pre>
    Arguments:
        1) real: replayIndex
        2) string: key
    Return Type:
        varies
</pre>
Returns the replay data associated with the given replay index and key.

This is an undocumented vanilla dnh function and has not been tested.\
*Note: Might crash if the key does not exist.*

## SetReplayUserData
<pre>
    Arguments:
        1) string: key
        2) any: value
</pre>
Maps the given key to the given value for the replay data.

This is an undocumented vanilla dnh function and has not been tested.

## IsReplayUserDataExists
<pre>
    Arguments:
        1) real: replayIndex
        2) string: key
    Return Type:
        bool
</pre>
Checks whether the given replay index has a key-value pair for the given key and returns true if it does.

This is an undocumented vanilla dnh function and has not been tested.

## SaveReplay
<pre>
    Arguments:
        1) real: replayIndex
    Return Type:
        bool
</pre>
Saves a replay to the specified replay index.

Returns true if successful, otherwise false.