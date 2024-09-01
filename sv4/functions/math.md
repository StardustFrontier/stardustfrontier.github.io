# Math Functions

[Return to Functions](../functions.html)

## add
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the sum of two values.

## subtract
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the difference of two values.

## multiply
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the product of two values.

## divide
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the quotient of two values.

## remainder
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the modulo operation (the remainder of a quotient) of two values.\
**Note**: remainder or % will always return a value with the same sign as the divisor.\
**Example**: remainder(10, 3) or 10 % 3 will return 1 because 10 / 3 equals 3 with a remainder of 1.

## power
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns value1 raised to the power of value2.\
Equivalent to ** operator.

## bit_lshift
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns value1 shifted left by value2 bits.\
Equivalent to << operator.

## bit_rshift
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns value1 shifted right by value2 bits.\
Equivalent to >> operator.

## bit_and
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the bitwise AND of two values.\
Equivalent to & operator.

## bit_xor
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the bitwise XOR of two values.\
Equivalent to ^ operator.

## bit_or
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the bitwise OR of two values.\
Equivalent to | operator.

## bit_not
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the bitwise NOT of the value.\
Equivalent to ~~ operator.

## min
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the lesser of the two values.

## max
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the greater of the two values.

## log
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the natural (base e) [logarithm](https://en.wikipedia.org/wiki/Logarithm) of the value.

## log10
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the common (base 10) [logarithm](https://en.wikipedia.org/wiki/Logarithm) of the value.

## cos
<pre>
    Arguments:
        1) real: angle
    Return Type:
        real
</pre>
Returns the cosine of the angle.\
Cosine is a value between -1 and 1 that corresponds to the x-value in a coordinate plane.

## sin
<pre>
    Arguments:
        1) real: angle
    Return Type:
        real
</pre>
Returns the sine of the angle.\
Sine is a value between -1 and 1 that corresponds to the y-value in a coordinate plane.

## tan
<pre>
    Arguments:
        1) real: angle
    Return Type:
        real
</pre>
Returns the tangent of the angle.\
Tangent is the slope of the line created by the angle (x/y).

## acos
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the arccosine of the angle.\
acos(cos(x)) = x, if x is between 0 and 180.

## asin
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the arcsine of the value.\
asin(sin(x)) = x, if x is between -90 and 90.

## atan
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the arctangent of the value.\
atan(tan(x)) = x, if x is between -90 and 90.

## atan2
<pre>
    Arguments:
        1) real: y
        2) real: x
    Return Type:
        real
</pre>
Returns the arctangent of y/x, which is the angle from (0, 0) to (x, y).\
The angle will be in the range -180 < a <= 180, where a is the returned value.\
Useful for getting the angle from one point to another point.\
For example, the angle from the boss to the player is atan2(player y - boss y, player x - boss x).

## sqrt
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the square root of the value.

## cbrt
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the cubic root of the value.

## hypot
<pre>
    Arguments:
        1) real: value1
        2) real: value2
    Return Type:
        real
</pre>
Returns the hypotenuse of a right-angled triangle whose legs are value1 and value2.

## cot
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the cotangent of the value.

## csc
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the cosecant of the value.

## sec
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the secant of the value.

## cosh
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the hyperbolic cosine of the value.

## sinh
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the hyperbolic sine of the value.

## tanh
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the hyperbolic tangent of the value.

## acosh
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the area hyperbolic cosine of the value.

## asinh
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the area hyperbolic sine of the value.

## atanh
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the area hyperbolic tangent of the value.

## coth
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the hyperbolic cotangent of the value.

## csch
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the hyperbolic cosecant of the value.

## sech
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the hyperbolic secant of the value.

## rand
<pre>
    Arguments:
        1) real: min
        2) real: max
    Return Type:
        real
</pre>
Returns a random real value between the two values.

## rand_int
<pre>
    Arguments:
        1) real: min
        2) real: max
    Return Type:
        real
</pre>
Returns a random integer value between the two values.

## prand
<pre>
    Arguments:
        1) real: min
        2) real: max
    Return Type:
        real
</pre>
Returns a predetermined random real value between min and max, of which the seed is set with psrand

## prand_int
<pre>
    Arguments:
        1) real: min
        2) real: max
    Return Type:
        real
</pre>
Returns a predetermined random integer value between min and max, of which the seed is set with psrand

## psrand
<pre>
    Arguments:
        1) real: seed
</pre>
Initialize the random number sequence for the prand and prand_int functions.\
If not set, it will be 1 by default.

## round
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the value as an integer.\
Values of 0.5 or greater are rounded up; otherwise they are rounded down.

## truncate
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the value with no decimal places.\
For instance, 1.123 becomes 1.\
The shortened name trunc can also be used to refer to this function.

## ceil
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the value rounded up to the next integer.

## floor
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the value rounded down to the next integer.

## absolute
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the value as an absolute number (if it is negative, it will be changed to a positive).\
The shortened name abs can also be used to refer to this function.

## modc
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns a modulus of the first value. Modulus provides the remainder of the division (7 modulo 5 would be 2).\
**Note:** unlike remainder, modc returns a value with the same sign as the dividend: modc(-7, 4) equals -3 and modc(7, -4) equals 3.

## pi
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Returns the value of pi.

Note: Use the constant PI instead of this function, it only exists for compatibility reasons.

## successor
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Adds 1 to the value, then returns it.

## predecessor
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Subtracts 1 from the value, then returns it.

## negative
<pre>
    Arguments:
        1) real: value
    Return Type:
        real
</pre>
Negates the value, then returns it.\
This changes positive values to negative and vice-versa.\
Equivalent to unary - operator.

## ToDegrees
<pre>
    Arguments:
        1) real: x
    Returns:
        real: result
</pre>
Convert angle _x_ from radians to degrees.

## ToRadians
<pre>
    Arguments:
        1) real: x
    Returns:
        real: result
</pre>
Convert angle _x_ from degrees to radians.

## AngleNormalize
<pre>
    Arguments:
        1) real: angle (degrees)
    Returns:
        real: result
</pre>
Returns the angle (provided in degrees) normalized to the range [0, 360)

## AngleNormalizeR
<pre>
    Arguments:
        1) real: angle (radians)
    Returns:
        real: result
</pre>
Returns the angle (provided in radians) normalized to the range [0, 2pi)

## AngularDistance
<pre>
    Arguments:
        1) real: angleFrom (degrees)
        2) real: angleTo (degrees)
    Returns:
        real: result
</pre>
Calculates the shortest angular distance between the given angles (provided in degrees).

The returned value will be in the range [-180, 180)

## AngularDistanceR
<pre>
    Arguments:
        1) real: angleFrom (radians)
        2) real: angleTo (radians)
    Returns:
        real: result
</pre>
Calculates the shortest angular distance between the given angles (provided in radians).

The returned value will be in the range [-pi, pi)

## AngleReflect
<pre>
    Arguments:
        1) real: angleRay (degrees)
        2) real: angleSurface (degrees)
    Returns:
        real: result
</pre>
Calculates the given ray's angle of reflection upon a surface of the given angle.

The returned value will be in the range [0, 360)

## AngleReflectR
<pre>
    Arguments:
        1) real: angleRay (radians)
        2) real: angleSurface (radians)
    Returns:
        real: result
</pre>
Calculates the given ray's angle of reflection upon a surface of the given angle.

The returned value will be in the range [0, 2pi)