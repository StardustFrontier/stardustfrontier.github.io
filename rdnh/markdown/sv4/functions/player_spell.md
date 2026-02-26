# Player Spell Functions

[Return to Functions](../functions.html)

## ObjSpell_Create
```
    Return Type:
        real
```
Creates a spell object and returns its ID.

## ObjSpell_Regist
```
    Arguments:
        1) real: objectID
```
Invokes the spell card object.

## ObjSpell_SetDamage
```
    Arguments:
        1) real: objectID
        2) real: damage
```
Sets the damage of the spell object.

## ObjSpell_SetEraseShot
```
    Arguments:
        1) real: objectID
        2) real: bEraseShot
```
Determines whether the specified spell object can delete enemy bullets.

Defaults to true.

## ObjSpell_SetIntersectionCircle
```
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: radius
```
Sets the hit circle for the spell object.

## ObjSpell_SetIntersectionLine
```
    Arguments:
        1) real: objectID
        2) real: x1
        3) real: y1
        4) real: x2
        5) real: y2
        6) real: width
```
Sets the hit line for the spell object.