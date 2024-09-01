# Boss Scene Object Functions

[Return to Functions](./docs.html)

## ObjEnemyBossScene_Create
<pre>
    Return Type:
        real
</pre>
Creates a Boss Scene object and returns its ID.

## ObjEnemyBossScene_Regist
<pre>
    Arguments:
        1) real: objectID
</pre>
Starts the specified boss scene.

## ObjEnemyBossScene_Add
<pre>
    Arguments:
        1) real: objectID
        2) real: phaseStep
        3) string: pathScript
</pre>
Adds the specified script to the boss scene at the specified phase.

## ObjEnemyBossScene_LoadInThread
<pre>
    Arguments:
        1) real: objectID
    Return Type:
        real
</pre>
Compiles all the enemy scripts in the boss scene and initializes global variables.

As the length of compile time cannot be guaranteed, initialize all global variables besides constants in @Initialize.

## ObjEnemyBossScene_GetInfo
<pre>
    Arguments:
        1) real: objectID
        2) real const: infoType
    Return Type:
        varies
</pre>
Returns info about the boss scene object based on the given info type constant.

Available info types are:
<pre>
INFO_IS_SPELL - Returns true if a spell card is active
INFO_IS_LAST_SPELL - Returns true if the Last Spell is active
INFO_IS_DURABLE_SPELL - Returns true in the case of a survival spell
INFO_IS_LAST_STEP - Returns true when the last spell is active
INFO_TIMER - Returns the timer value in seconds
INFO_TIMERF - Returns the timer value in frames (returns -1 if unlimited)
INFO_ORGTIMERF - Returns the original timer value in frames (returns -1 if unlimited)
INFO_SPELL_SCORE - Returns the score of the spell card
INFO_REMAIN_STEP_COUNT - Returns the number of steps remaining in the active boss scene
INFO_ACTIVE_STEP_LIFE_COUNT - Returns the amount of attacks of the enemy for the active step
INFO_ACTIVE_STEP_TOTAL_MAX_LIFE - Returns the initial life of the enemy for the active step
INFO_ACTIVE_STEP_TOTAL_LIFE - Returns the total remaining life for the active step
INFO_PLAYER_SHOOTDOWN_COUNT - Returns the amount of times the player died during the spell
INFO_PLAYER_SPELL_COUNT - Returns the amount of times the player bombed during the spell
INFO_ACTIVE_STEP_LIFE_RATE_LIST - Returns an array containing the proportion (0-1) of each attacks's amount of life in the active step
INFO_CURRENT_LIFE - Returns the current life of the enemy in the current attack
INFO_CURRENT_LIFE_MAX - Returns the maximum life of the enemy in the current attack
With regards to the step info types, step refers to the individual sections specified in the ObjEnemyBossScene_Add function's second argument.
For each script (referred to as an attack here) you load into the step, you increase the step life count of that specific step by 1.
</pre>

## ObjEnemyBossScene_SetSpellTimer
<pre>
    Arguments:
        1) real: objectID
        2) real: timer
</pre>
Sets the timer (in frames) of the current boss scene.

## ObjEnemyBossScene_StartSpell
<pre>
    Arguments:
        1) real: objectID
        2) real: timer
</pre>
Starts the boss spell card of the current boss scene.