# Shot Functions

[Return to Functions](./docs.html)

## DeleteShotAll
<pre>
    Arguments:
        1) real const: type
        2) real const: deleteType
</pre>
Deletes all shot objects on screen matching the criteria, utilizing the selected deletion type.

type can be:
<pre>
TYPE_ALL (all shot objects)
TYPE_SHOT (shot objects without spell resistance)
TYPE_CHILD (shot objects fired from the currently running script)
</pre>
deleteType can be:
<pre>
TYPE_IMMEDIATE (immediately delete the bullets)
TYPE_FADE (slowly fade out the bullets)
TYPE_ITEM (turn the bullets into items according to the running item script)
Note: With TYPE_FADE, bullets will still be visible while fading out, but they will not have any collision.
</pre>

## DeleteShotInCircle
<pre>
    Arguments:
        1) real const: type
        2) real const: deleteType
        3) real: x
        4) real: y
        5) real: radius
</pre>
Deletes all shot objects matching the criteria in the designated circle centered at (x, y) with provided radius, utilizing the selected deletion type.

type can be:
<pre>
TYPE_ALL (all shot objects)
TYPE_SHOT (shot objects without spell resistance)
TYPE_CHILD (shot objects fired from the currently running script)
</pre>
deleteType can be:
<pre>
TYPE_IMMEDIATE (immediately delete the bullets)
TYPE_FADE (slowly fade out the bullets)
TYPE_ITEM (turn the bullets into items according to the running item script)
Note: With TYPE_FADE, bullets will still be visible while fading out, but they will not have any collision.
</pre>

## CreateShotA1
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: graphic
        6) real: delay
    Return Type:
        real
</pre>
Creates a basic bullet that will move at the angle and speed defined. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotA2
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: acceleration
        6) real: maxSpeed
        7) real: graphic
        8) real: delay
    Return Type:
        real
</pre>
Creates a bullet that will move at the angle and speed defined, incrementing its speed by acceleration every frame, capping at maxspeed. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotOA1
<pre>
    Arguments:
        1) real: parentObjectID
        2) real: speed
        3) real: angle
        4) real: graphic
        5) real: delay
    Return Type:
        real
</pre>
Creates a bullet that will spawn on the coordinates of the given object id and will move at the angle and speed defined. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotB1
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: xSpeed
        4) real: ySpeed
        5) real: graphic
        6) real: delay
    Return Type:
        real
</pre>
Creates a bullet that will move at the specified x and y speeds. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotB2
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: xSpeed
        4) real: ySpeed
        5) real: xAcceleration
        6) real: yAcceleration
        7) real: xMaxSpeed
        8) real: yMaxSpeed
        9) real: graphic
        10) real: delay
    Return Type:
        real
</pre>
Creates a bullet that will move at the specified x and y speeds, incrementing its speed components by the respective acceleration component every frame, capping at the maxspeed for each component. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateShotOB1
<pre>
    Arguments:
        1) real: parentObjectID
        2) real: xSpeed
        3) real: ySpeed
        4) real: graphic
        5) real: delay
    Return Type:
        real
</pre>
Creates a bullet that will spawn on the coordinates of the given object id and will move at the specified x and y speeds. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the bullet will appear.\
During it's delay, there will be a collisionless cloud that appears where the bullet will spawn.\
Returns a void value in a player script if the player is unable to shoot.

## CreateLooseLaserA1
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: length
        6) real: width
        7) real: graphic
        8) real: delay
    Return Type:
        real
</pre>
Creates a loose (moving) laser that will move at the angle and speed defined, with its size defined by the length (in direction of travel) and width. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the laser will appear.\
During it's delay, there will be a collisionless cloud that appears where the laser will spawn.\
Returns a void value in a player script if the player is unable to shoot.\
This function can be used to create larger bullets.

## CreateStraightLaserA1
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: angle
        4) real: length
        5) real: width
        6) real: deleteTime
        7) real: graphic
        8) real: delay
    Return Type:
        real
</pre>
Creates a straight laser mounted at the position provided, with its size defined by the length (in direction of travel) and width. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the laser will appear.\
The 'deletetime' argument determines how many frames until the laser disappears.\
During the delay, the laser will appear as a very thin laser that has no collision (AKA delay laser) in order to give the player a warning.\
Having no delay while using this function is not advisable, as the laser will spawn at full size the moment the delay is over.\
Returns a void value in a player script if the player is unable to shoot.

## CreateCurveLaserA1
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: speed
        4) real: angle
        5) real: length
        6) real: width
        7) real: graphic
        8) real: delay
    Return Type:
        real
</pre>
Creates a curve laser that will move at the angle and speed defined, with its size defined by the length (in direction of travel) and width. Also returns its object ID.

graphic is the image the bullet will have, while delay is the time in frames before the laser will appear.\
During it's delay, there will be a collisionless cloud that appears where the laser will spawn.\
Returns a void value in a player script if the player is unable to shoot.\
Use ObjMove_SetAngularVelocity to adjust the curve of this laser.\
This function is heavy to process, so having many curve lasers on-screen at the same time is not recommended.

## SetShotIntersectionCircle
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
</pre>
Adds a circular player hitbox at the specified position with the provided radius.

Note: Lasts one frame.

## SetShotIntersectionLine
<pre>
    Arguments:
        1) real: x1
        2) real: y1
        3) real: x2
        4) real: y2
        5) real: width
</pre>
Adds a linear player hitbox between the two specified positions with the provided width.

Note: Lasts one frame.

## GetShotIdInCircleA1
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
    Return Type
        real array
</pre>
Returns the object IDs of the bullets inside the given circle in an array.

Inside a player script, it will only return enemy bullet IDs, and vice versa.

## GetShotIdInCircleA2
<pre>
    Arguments:
        1) real: x
        2) real: y
        3) real: radius
        4) real const: target
    Return Type
        real array
</pre>
Returns the object IDs of the bullets inside the given circle with the specified target type in an array.

Inside a player script, it will only return enemy bullet IDs, and vice versa.\
target can be:
<pre>
TARGET_ALL (all shots)
TARGET_ENEMY (enemy shots only)
TARGET_PLAYER (player shots only)
</pre>

## GetShotCount
<pre>
    Arguments:
        1) real const: target
    Return Type
        real
</pre>
Returns the number of bullets with the specified target type.

target can be:
<pre>
TARGET_ALL (all shots)
TARGET_ENEMY (enemy shots only)
TARGET_PLAYER (player shots only)
</pre>

## SetShotAutoDeleteClip
<pre>
    Arguments:
        1) real: left
        2) real: top
        3) real: right
        4) real: bottom
</pre>
Sets at what point bullets will be automatically deleted when leaving the STG screen.

To override this auto deletion, use ObjShot_SetAutoDelete on the bullet you want to prevent from auto deleting.\
Defaults to (64, 64, 64, 64).

## SetShotGrazeInvalidFrame
<pre>
    Arguments:
        1) real: frames
</pre>
Sets the default amount of frames that must pass before the shot can be grazed again.

Use GRAZE_INVALID_NONE to reset this value to normal.\
Defaults to GRAZE_INVALID_NONE.

## SetShotIntersectionActiveRadius
<pre>
    Arguments:
        1) real: radius
</pre>
Sets the radius from the player in which shot intersection is enabled.

When shots are within this radius, intersection will automatically be enabled, otherwise it will be disabled.\
Defaults to 0, which disables this feature.

## GetShotIntersectionActiveRadius
<pre>
    Arguments:
        1) real: radius
</pre>
Returns the active intersection radius for shots.

Defaults to 0.

## GetShotDataInfoA1
<pre>
    Arguments:
        1) real: graphic
        2) real const: targetShotData
        3) real const: infoType
    Return Type:
        varies
</pre>
Returns information from the shotdata depending on the information requested.

targetShotData can be `TARGET_PLAYER` or `TARGET_ENEMY`.\
infotype can be:
<pre>
INFO_RECT (returns [left, top, right, bottom] for the graphic)
INFO_DELAY_COLOR (returns [red, green, blue] for the graphic)
INFO_BLEND (returns blend type for the graphic)
INFO_COLLISION (returns radius of collision detection)
INFO_COLLISION_LIST (returns 2D array of collision hitbox radii and coordinates [radius, x, y])
</pre>

## StartShotScript
<pre>
    Arguments:
        1) string: path
</pre>
Starts the specified shot script.