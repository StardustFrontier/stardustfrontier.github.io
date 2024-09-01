# Player Spell Functions

[Return to Functions](../functions.html)

## ObjSpell_Create
<pre>
    Return Type:
        real
</pre>
Creates a spell object and returns its ID.

## ObjSpell_Regist
<pre>
    Arguments:
        1) real: objectID
</pre>
Invokes the spell card object.

## ObjSpell_SetDamage
<pre>
    Arguments:
        1) real: objectID
        2) real: damage
</pre>
Sets the damage of the spell object.

## ObjSpell_SetEraseShot
<pre>
    Arguments:
        1) real: objectID
        2) real: bEraseShot
</pre>
Determines whether the specified spell object can delete enemy bullets.

Defaults to true.

## ObjSpell_SetIntersectionCircle
<pre>
    Arguments:
        1) real: objectID
        2) real: x
        3) real: y
        4) real: radius
</pre>
Sets the hit circle for the spell object.

## ObjSpell_SetIntersectionLine
<pre>
    Arguments:
        1) real: objectID
        2) real: x1
        3) real: y1
        4) real: x2
        5) real: y2
        6) real: width
</pre>
Sets the hit line for the spell object.