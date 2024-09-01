# Player Functions

[Return to Functions](./docs.html)

## GetPlayerObjectID
<pre>
    Return Type:
        real
</pre>
Returns the player object ID.

## GetPlayerScriptID
<pre>
    Return Type:
        real
</pre>
Returns the player script ID.

## SetPlayerSpeed
<pre>
    Arguments:
        1) real: speedNormal
        2) real: speedFocus
</pre>
Sets the normal speed and focus speed of the player.

## SetPlayerClip
<pre>
    Arguments:
        1) real: left
        2) real: top
        3) real: right
        4) real: bottom
</pre>
Sets the area within which the player can move.

## SetPlayerLife
<pre>
    Arguments:
        1) real: value
</pre>
Sets number of lives for the player.

Note: Can be a non-integer value.

## SetPlayerSpell
<pre>
    Arguments:
        1) real: value
</pre>
Sets number of spells/bombs for the player.

Note: Can be a non-integer value.

## SetPlayerPower
<pre>
    Arguments:
        1) real: value
</pre>
Sets power value for the player.

Note: Can be a non-integer value.

## SetPlayerInvincibilityFrame
<pre>
    Arguments:
        1) real: frames
</pre>
Sets the number of frames for player invincibility.

## SetPlayerDownStateFrame
<pre>
    Arguments:
        1) real: frames
</pre>
Sets the number of frames before respawning the player after player death.

## SetPlayerRebirthFrame
<pre>
    Arguments:
        1) real: frames
</pre>
Sets the number of frames the player can deathbomb for after being hit.

Default is 15 frames.

## SetPlayerRebirthLossFrame
<pre>
    Arguments:
        1) real: frames
</pre>
Sets the number of deathbomb frames the player loses per deathbomb.

Default is 3 frames.

## SetPlayerAutoItemCollectLine
<pre>
    Arguments:
        1) real: y
</pre>
Sets the y coordinate of the auto collect line.

A negative value removes the line.\
Default is no autocollect line.

## SetForbidPlayerShot
<pre>
    Arguments:
        1) bool: forbid
</pre>
When set to true, the player cannot use normal shots.

## SetForbidPlayerSpell
<pre>
    Arguments:
        1) bool: forbid
</pre>
When set to true, the player cannot use spells/bombs.

## SetPlayerItemIntersectionRadius
<pre>
    Arguments:
        1) real: radius
</pre>
Sets the intersection radius between the player and items.

If the item is within this radius, it will be collected instantly.\
Defaults to 24.

## SetPlayerItemAbsorbRadius
<pre>
    Arguments:
        1) real: radius
</pre>
Sets the absorb radius between the player and items.

If the item is within this radius, it will begin to move towards the player.\
Defaults to 0 (no effect).

*Note: This will be cancelled by [CancelCollectItems](./docs_item.html#cancelcollectitems).*

## GetPlayerX
<pre>
    Return Type:
        real
</pre>
Returns the x-coordinate of the player.

## GetPlayerY
<pre>
    Return Type:
        real
</pre>
Returns the y-coordinate of the player.

## GetPlayerState
<pre>
    Return Type:
        real const
</pre>
Returns the player state.

State is one of:
<pre>
STATE_NORMAL (player is alive)
STATE_HIT (after being hit, during counter bomb frames)
STATE_DOWN (after being hit, before reappearing)
STATE_END (game over)
</pre>

## GetPlayerSpeed
<pre>
    Return Type:
        real array
</pre>
Returns the player movement speed as an array [unfocusedSpeed, focusedSpeed].

## GetPlayerClip
<pre>
    Return Type:
        real array
</pre>
Returns the player's clip as an array [left, top, right, bottom].

## GetPlayerLife
<pre>
    Return Type:
        real
</pre>
Returns the number of player lives.

## GetPlayerSpell
<pre>
    Return Type:
        real
</pre>
Returns the number of player spells/bombs.

## GetPlayerPower
<pre>
    Return Type:
        real
</pre>
Returns the amount of player power

## GetPlayerInvincibilityFrame
<pre>
    Return Type:
        real
</pre>
Returns the number of frames during which the player is invincible.

## GetPlayerDownStateFrame
<pre>
    Return Type:
        real
</pre>
Returns the number of frames during which the player is respawning.

## GetPlayerRebirthFrame
<pre>
    Return Type:
        real
</pre>
Returns the number of frames during which the player can deathbomb.

## GetAngleToPlayer
<pre>
    Arguments:
        real: obj
    Return Type:
        real
</pre>
Returns the angle from the given object to the player.

## IsPermitPlayerShot
<pre>
    Return Type:
        bool
</pre>
Returns true if the player can use normal shots, false otherwise.

## IsPermitPlayerSpell
<pre>
    Return Type:
        bool
</pre>
Returns true if the player can use spells/bombs, false otherwise.

Note: The returned value may differ from a previously set SetForbidPlayerSpell. For instance, it is forced to false during a LastSpell.

## IsPlayerLastSpellWait
<pre>
    Return Type:
        bool
</pre>
Returns true if the player is deathbombing, false otherwise.

## IsPlayerSpellActive
<pre>
    Return Type:
        bool
</pre>
Returns true if the player is utilizing a bomb, false otherwise.

## GetPlayerID
<pre>
    Return Type:
        bool
</pre>
Returns the system ID of the player script.

This value is defined inside the player script in the #ID header.

## GetPlayerReplayName
<pre>
    Return Type:
        bool
</pre>
Returns the replay ID of the player.

This value is defined inside the player script in the #ReplayName header.