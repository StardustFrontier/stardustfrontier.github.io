# Player Functions

[Return to Functions](../functions.html)

## GetPlayerObjectID
```
    Return Type:
        real
```
Returns the player object ID.

## GetPlayerScriptID
```
    Return Type:
        real
```
Returns the player script ID.

## SetPlayerSpeed
```
    Arguments:
        1) real: speedNormal
        2) real: speedFocus
```
Sets the normal speed and focus speed of the player.

## SetPlayerClip
```
    Arguments:
        1) real: left
        2) real: top
        3) real: right
        4) real: bottom
```
Sets the area within which the player can move.

## SetPlayerMovePriority
```
    Arguments:
        1) real const: keyPriorityHorizontal
        2) real const: keyPriorityVertical
```
Sets the virtual key to prioritize when moving horizontally and vertically.

KEY_INVALID can be passed to reset to the default behavior.

Example: To prioritize left when both VK_LEFT and VK_RIGHT are pressed and down when both VK_UP and VK_DOWN are pressed:

<scode>SetPlayerMovePriority(VK_LEFT, VK_DOWN);</scode>

## SetPlayerLife
```
    Arguments:
        1) real: value
```
Sets number of lives for the player.

Note: Can be a non-integer value.

## SetPlayerSpell
```
    Arguments:
        1) real: value
```
Sets number of spells/bombs for the player.

Note: Can be a non-integer value.

## SetPlayerPower
```
    Arguments:
        1) real: value
```
Sets power value for the player.

Note: Can be a non-integer value.

## SetPlayerInvincibilityFrame
```
    Arguments:
        1) real: frames
```
Sets the number of frames for player invincibility.

## SetPlayerDownStateFrame
```
    Arguments:
        1) real: frames
```
Sets the number of frames before respawning the player after player death.

## SetPlayerRebirthFrame
```
    Arguments:
        1) real: frames
```
Sets the number of frames the player can deathbomb for after being hit.

Default is 15 frames.

## SetPlayerRebirthLossFrame
```
    Arguments:
        1) real: frames
```
Sets the number of deathbomb frames the player loses per deathbomb.

Default is 3 frames.

## SetPlayerAutoItemCollectLine
```
    Arguments:
        1) real: y
```
Sets the y coordinate of the auto collect line.

A negative value removes the line.\
Default is no autocollect line.

## SetForbidPlayerShot
```
    Arguments:
        1) bool: forbid
```
When set to true, the player cannot use normal shots.

## SetForbidPlayerSpell
```
    Arguments:
        1) bool: forbid
```
When set to true, the player cannot use spells/bombs.

## SetForbidPlayerMovement
```
    Arguments:
        1) bool: forbid
```
When set to true, the player cannot move.

## SetPlayerItemIntersectionRadius
```
    Arguments:
        1) real: radius
```
Sets the intersection radius between the player and items.

If the item is within this radius, it will be collected instantly.\
Defaults to 24.

## SetPlayerItemAbsorbRadius
```
    Arguments:
        1) real: radius
```
Sets the absorb radius between the player and items.

If the item is within this radius, it will begin to move towards the player.\
Defaults to 0 (no effect).

*Note: This will be cancelled by [CancelCollectItems](./docs_item.html#cancelcollectitems).*

## SetPlayerRebirthPosition
```
    Arguments:
        1) real: x
        2) real: y
```
Sets the respawn point of the player.

Pass REBIRTH_DEFAULT as either coordinate to reset it to its default value.\
The default value is (GetStgFrameWidth() / 2, GetStgFrameHeight() - 48)

## GetPlayerX
```
    Return Type:
        real
```
Returns the x-coordinate of the player.

## GetPlayerY
```
    Return Type:
        real
```
Returns the y-coordinate of the player.

## GetPlayerState
```
    Return Type:
        real const
```
Returns the player state.

State is one of:
```
STATE_NORMAL (player is alive)
STATE_HIT (after being hit, during counter bomb frames)
STATE_DOWN (after being hit, before reappearing)
STATE_END (game over)
```

## GetPlayerSpeed
```
    Return Type:
        real array
```
Returns the player movement speed as an array [unfocusedSpeed, focusedSpeed].

## GetPlayerClip
```
    Return Type:
        real array
```
Returns the player's clip as an array [left, top, right, bottom].

## GetPlayerLife
```
    Return Type:
        real
```
Returns the number of player lives.

## GetPlayerSpell
```
    Return Type:
        real
```
Returns the number of player spells/bombs.

## GetPlayerPower
```
    Return Type:
        real
```
Returns the amount of player power

## GetPlayerInvincibilityFrame
```
    Return Type:
        real
```
Returns the number of frames during which the player is invincible.

## GetPlayerDownStateFrame
```
    Return Type:
        real
```
Returns the number of frames during which the player is respawning.

## GetPlayerRebirthFrame
```
    Return Type:
        real
```
Returns the number of frames during which the player can deathbomb.

## GetAngleToPlayer
```
    Arguments:
        real: obj
    Return Type:
        real
```
Returns the angle from the given object to the player.

## GetAngleToPlayerXY
```
    Arguments:
        real: obj
    Return Type:
        real
```
Returns the angle from (x, y) to the player object.

Equivalent to <scode>atan2(GetPlayerY() - y, GetPlayerX() - x)</scode>

## IsPermitPlayerShot
```
    Return Type:
        bool
```
Returns true if the player can use normal shots, false otherwise.

## IsPermitPlayerSpell
```
    Return Type:
        bool
```
Returns true if the player can use spells/bombs, false otherwise.

Note: The returned value may differ from a previously set SetForbidPlayerSpell. For instance, it is forced to false during a LastSpell.

## IsPermitPlayerMovement
```
    Return Type:
        bool
```
Returns true if the player is allowed to move, false otherwise.

## IsPlayerLastSpellWait
```
    Return Type:
        bool
```
Returns true if the player is deathbombing, false otherwise.

## IsPlayerSpellActive
```
    Return Type:
        bool
```
Returns true if the player is utilizing a bomb, false otherwise.

## SetPlayerInvincibleGraze
```
    Arguments:
        1) bool: bEnable
```
Sets whether the player can graze during the invincibility period.

False by default (unlike ph3sx).

## SetPlayerIntersectionEraseShot
```
    Arguments:
        1) bool: bEnable
```
Sets whether shots colliding with the player would get automatically deleted.

False by default (unlike ph3sx).

## SetPlayerStateEndEnable
```
    Arguments:
        1) bool: bEnable
```
Sets whether STATE_END is permitted to activate.

If set to false, player life will continue below 0 upon each death without limit.

True by default.

_**Note:** In ph3sx, this defaults to false when the main script is a package script, which is not the case in rdnh._

## SetPlayerShootdownEventEnable
```
    Arguments:
        1) bool: bEnable
```
Sets whether EV_PLAYER_SHOOTDOWN will be notified upon the player's death.

Setting it to false would also disable STATE_DOWN and STATE_END from ever occuring.

True by default.

## GetPlayerID
```
    Return Type:
        bool
```
Returns the system ID of the player script.

This value is defined inside the player script in the #ID header.

## GetPlayerReplayName
```
    Return Type:
        bool
```
Returns the replay ID of the player.

This value is defined inside the player script in the #ReplayName header.