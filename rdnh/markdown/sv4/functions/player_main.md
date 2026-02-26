# Player Main Functions

[Return to Functions](../functions.html)

## CreatePlayerShotA1
```
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: damage
        6) real: penetration
        7) real: shotGraphicID
    Return Type:
        real or void
```
Fires a player shot with the specified position, speed, angle, damage, penetration, and graphic from the player shotsheet.

If the player is not permitted to shoot, then this function returns void, otherwise it returns a shot object ID.

## CallSpell
If the conditions to use a spell card are met, uses the spell card.

## LoadPlayerShotData
```
    Arguments:
        1) real: pathShotData
    Return Type:
        bool
```
Loads the player shot data file, allowing its IDs to be used in the player script.

Returns true on success, otherwise false.\
If called several times, loads each file in succession as long as the IDs are different.\
A file cannot be loaded multiple times in a row.

## ReloadPlayerShotData
```
    Arguments:
        1) real: pathShotData
    Return Type:
        bool
```
Reloads the player shot data file, allowing its IDs to be used in the player script.

Returns true on success, otherwise false.\
A file can be loaded several times with this function.\
Can be used without loading through LoadPlayerShotData first.

## GetSpellManageObject
```
    Return Type:
        real
```
Returns the spell card management object ID.

It is necessary to delete this object using ObjDelete once the spell is over.