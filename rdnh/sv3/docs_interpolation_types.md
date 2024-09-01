# Interpolation Types

[Return to Functions](./docs.html)

#
Interpolation type constants are in the form: `IP_<EQUATION>_<EASING>`\
The equation type can be any of the following:
<pre>
2X  - Quadratic
3X  - Cubic
4X  - Quartic
5X  - Quintic
SIN - Sine
</pre>
The easing type can be any of the following:
<pre>
LINEAR     - Linear from start to end.
ACCEL      - Start slow, speed up.
DECEL      - Start fast, slow to stop.
SMOOTH     - Start slow, accelerate, decelerate, slow to stop. Combination of ACCEL and DECEL.
SMOOTH_INV - Start slow, speed up, stop halfway, start fast, slow to stop. Inverted SMOOTH (DECEL then ACCEL)
</pre>


List of all valid combinations:
<pre>
IP_LINEAR
IP_2X_ACCEL
IP_3X_ACCEL
IP_4X_ACCEL
IP_5X_ACCEL
IP_2X_DECEL
IP_3X_DECEL
IP_4X_DECEL
IP_5X_DECEL
IP_2X_SMOOTH
IP_3X_SMOOTH
IP_4X_SMOOTH
IP_5X_SMOOTH
IP_2X_SMOOTH_INV
IP_3X_SMOOTH_INV
IP_4X_SMOOTH_INV
IP_5X_SMOOTH_INV
IP_SIN_ACCEL
IP_SIN_DECEL
IP_SIN_SMOOTH
IP_SIN_SMOOTH_INV
</pre>