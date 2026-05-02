# Math Functions

[Return to Functions](../functions.html)

## add
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the sum of two values.

## subtract
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the difference of two values.

## multiply
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the product of two values.

## divide
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the quotient of two values.

## remainder
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the modulo operation (the remainder of a quotient) of two values.\
**Note**: remainder or % will always return a value with the same sign as the divisor.\
**Example**: remainder(10, 3) or 10 % 3 will return 1 because 10 / 3 equals 3 with a remainder of 1.

## power
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns value1 raised to the power of value2.\
Equivalent to ** operator.

## bit_lshift
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns value1 shifted left by value2 bits.\
Equivalent to << operator.

## bit_rshift
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns value1 shifted right by value2 bits.\
Equivalent to >> operator.

## bit_and
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the bitwise AND of two values.\
Equivalent to & operator.

## bit_xor
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the bitwise XOR of two values.\
Equivalent to ^ operator.

## bit_or
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the bitwise OR of two values.\
Equivalent to | operator.

## bit_not
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the bitwise NOT of the value.\
Equivalent to ~~ operator.

## min
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the lesser of the two values.

## max
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the greater of the two values.

## clamp
```
    Arguments:
        1) real: value
        2) real: minValue
        3) real: maxValue
    Return Type:
        real
```
Returns the value clamped between the given minimum and maximum values.\
Equivalent to min(max(value, minValue), maxValue)

## log
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the natural (base e) [logarithm](https://en.wikipedia.org/wiki/Logarithm) of the value.

## log10
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the common (base 10) [logarithm](https://en.wikipedia.org/wiki/Logarithm) of the value.

## cos
```
    Arguments:
        1) real: angle
    Return Type:
        real
```
Returns the cosine of the angle.\
Cosine is a value between -1 and 1 that corresponds to the x-value in a coordinate plane.

## sin
```
    Arguments:
        1) real: angle
    Return Type:
        real
```
Returns the sine of the angle.\
Sine is a value between -1 and 1 that corresponds to the y-value in a coordinate plane.

## tan
```
    Arguments:
        1) real: angle
    Return Type:
        real
```
Returns the tangent of the angle.\
Tangent is the slope of the line created by the angle (x/y).

## acos
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the arccosine of the angle.\
acos(cos(x)) = x, if x is between 0 and 180.

## asin
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the arcsine of the value.\
asin(sin(x)) = x, if x is between -90 and 90.

## atan
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the arctangent of the value.\
atan(tan(x)) = x, if x is between -90 and 90.

## atan2
```
    Arguments:
        1) real: y
        2) real: x
    Return Type:
        real
```
Returns the arctangent of y/x, which is the angle from (0, 0) to (x, y).\
The angle will be in the range -180 < a <= 180, where a is the returned value.\
Useful for getting the angle from one point to another point.\
For example, the angle from the boss to the player is atan2(player y - boss y, player x - boss x).

## sqrt
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the square root of the value.

## cbrt
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the cubic root of the value.

## hypot
```
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
```
Returns the hypotenuse of a right-angled triangle whose legs are value1 and value2.

## cot
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the cotangent of the value.

## csc
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the cosecant of the value.

## sec
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the secant of the value.

## cosh
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the hyperbolic cosine of the value.

## sinh
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the hyperbolic sine of the value.

## tanh
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the hyperbolic tangent of the value.

## acosh
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the area hyperbolic cosine of the value.

## asinh
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the area hyperbolic sine of the value.

## atanh
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the area hyperbolic tangent of the value.

## coth
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the hyperbolic cotangent of the value.

## csch
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the hyperbolic cosecant of the value.

## sech
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the hyperbolic secant of the value.

## rand
```
    Arguments:
        1) real: min
        2) real: max
    Return Type:
        real
```
Returns a random real value between the two values.

## rand_int
```
    Arguments:
        1) real: min
        2) real: max
    Return Type:
        real
```
Returns a random integer value between the two values.

## prand
```
    Arguments:
        1) real: min
        2) real: max
    Return Type:
        real
```
Returns a predetermined random real value between min and max, of which the seed is set with psrand

## prand_int
```
    Arguments:
        1) real: min
        2) real: max
    Return Type:
        real
```
Returns a predetermined random integer value between min and max, of which the seed is set with psrand

## psrand
```
    Arguments:
        1) real: seed
```
Initialize the random number sequence for the prand and prand_int functions.\
If not set, it will be 1 by default.

## round
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the value as an integer.\
Values of 0.5 or greater are rounded up; otherwise they are rounded down.

## truncate
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the value with no decimal places.\
For instance, 1.123 becomes 1.\
The shortened name trunc can also be used to refer to this function.

## ceil
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the value rounded up to the next integer.

## floor
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the value rounded down to the next integer.

## absolute
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the value as an absolute number (if it is negative, it will be changed to a positive).\
The shortened name abs can also be used to refer to this function.

## modc
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns a modulus of the first value. Modulus provides the remainder of the division (7 modulo 5 would be 2).\
**Note:** unlike remainder, modc returns a value with the same sign as the dividend: modc(-7, 4) equals -3 and modc(7, -4) equals 3.

## pi
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Returns the value of pi.

Note: Use the constant PI instead of this function, it only exists for compatibility reasons.

## successor
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Adds 1 to the value, then returns it.

## predecessor
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Subtracts 1 from the value, then returns it.

## negative
```
    Arguments:
        1) real: value
    Return Type:
        real
```
Negates the value, then returns it.\
This changes positive values to negative and vice-versa.\
Equivalent to unary - operator.

## ToDegrees
```
    Arguments:
        1) real: x
    Returns:
        real: result
```
Convert angle _x_ from radians to degrees.

## ToRadians
```
    Arguments:
        1) real: x
    Returns:
        real: result
```
Convert angle _x_ from degrees to radians.

## AngleNormalize
```
    Arguments:
        1) real: angle (degrees)
    Returns:
        real: result
```
Returns the angle (provided in degrees) normalized to the range [0, 360)

## AngleNormalizeR
```
    Arguments:
        1) real: angle (radians)
    Returns:
        real: result
```
Returns the angle (provided in radians) normalized to the range [0, 2pi)

## AngularDistance
```
    Arguments:
        1) real: angleFrom (degrees)
        2) real: angleTo (degrees)
    Returns:
        real: result
```
Calculates the shortest angular distance between the given angles (provided in degrees).

The returned value will be in the range [-180, 180)

## AngularDistanceR
```
    Arguments:
        1) real: angleFrom (radians)
        2) real: angleTo (radians)
    Returns:
        real: result
```
Calculates the shortest angular distance between the given angles (provided in radians).

The returned value will be in the range [-pi, pi)

## AngleReflect
```
    Arguments:
        1) real: angleRay (degrees)
        2) real: angleSurface (degrees)
    Returns:
        real: result
```
Calculates the given ray's angle of reflection upon a surface of the given angle.

The returned value will be in the range [0, 360)

## AngleReflectR
```
    Arguments:
        1) real: angleRay (radians)
        2) real: angleSurface (radians)
    Returns:
        real: result
```
Calculates the given ray's angle of reflection upon a surface of the given angle.

The returned value will be in the range [0, 2pi)

## GetRotatedX
```
    Arguments:
        1) real: x1
        2) real: y1
        3) real: x2
        4) real: y2
        5) real: angle
    Return Type:
        array[real, real]
```
Returns the x-coordinate after rotating the point (x1, y1) around point (x2, y2) by the specified angle in degrees.

## GetRotatedY
```
    Arguments:
        1) real: x1
        2) real: y1
        3) real: x2
        4) real: y2
        5) real: angle
    Return Type:
        array[real, real]
```
Returns the y-coordinate after rotating the point (x1, y1) around point (x2, y2) by the specified angle in degrees.

## GetRotatedPoint
```
    Arguments:
        1) real: x1
        2) real: y1
        3) real: x2
        4) real: y2
        5) real: angle
    Return Type:
        array[real, real]
```
Returns the coordinates [x, y] after rotating the point (x1, y1) around point (x2, y2) by the specified angle in degrees.