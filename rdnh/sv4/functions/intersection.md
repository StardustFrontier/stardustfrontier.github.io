# Intersection Functions

[Return to Functions](../functions.html)

## IsIntersected_Point_Polygon
<pre>
    Arguments:
        1) real: point - x
        2) real: point - y
        3) (real[2][]): polygon vertices
    Returns:
        bool: intersection
</pre>
Returns true if the given point intersects with the polygon.

The polygon can be convex, concave, or complex (self-intersecting).

## IsIntersected_Point_Circle
<pre>
    Arguments:
        1) real: point  - x
        2) real: point  - y
        3) real: circle - x
        4) real: circle - y
        5) real: circle - radius
    Returns:
        bool: intersection
</pre>
Returns true if the given point intersects with the circle.

## IsIntersected_Point_Ellipse
<pre>
    Arguments:
        1) real: point   - x
        2) real: point   - y
        3) real: ellipse - x
        4) real: ellipse - y
        5) real: ellipse - x radius
        6) real: ellipse - y radius
    Returns:
        bool: intersection
</pre>
Returns true if the given point intersects with the ellipse.

## IsIntersected_Point_Line
<pre>
    Arguments:
        1) real: point - x
        2) real: point - y
        3) real: line - start x
        4) real: line - start y
        5) real: line - end x
        6) real: line - end y
        7) real: line - width
    Returns:
        bool: intersection
</pre>
Returns true if the given point intersects with the line.

## IsIntersected_Point_RegularPolygon
<pre>
    Arguments:
        1) real: point   - x
        2) real: point   - y
        3) real: polygon - x
        4) real: polygon - y
        5) real: polygon - radius
        6) real: polygon - edge count
        7) real: polygon - angle (degrees)
    Returns:
        bool: intersection
</pre>
Returns true if the given point intersects with the regular polygon.

## IsIntersected_Circle_Polygon
<pre>
    Arguments:
        1) real: circle - x
        2) real: circle - y
        3) real: circle - radius
        4) real[2][]: polygon vertices
    Returns:
        bool: intersection
</pre>
Returns true if the given circle intersects with the polygon.

The polygon can be convex, concave, or complex (self-intersecting).

## IsIntersected_Circle_Circle
<pre>
    Arguments:
        1) real: circle 1 - x
        2) real: circle 1 - y
        3) real: circle 1 - radius
        4) real: circle 2 - x
        5) real: circle 2 - y
        6) real: circle 2 - radius
    Returns:
        bool: intersection
</pre>
Returns true if the given circles intersect.

## IsIntersected_Circle_Ellipse
<pre>
    Arguments:
        1) real: circle  - x
        2) real: circle  - y
        3) real: circle  - radius
        4) real: ellipse - x
        5) real: ellipse - y
        6) real: ellipse - x radius
        7) real: ellipse - y radius
    Returns:
        bool: intersection
</pre>
Returns true if the given circle intersects with the ellipse.

## IsIntersected_Circle_RegularPolygon
<pre>
    Arguments:
        1) real: circle  - x
        2) real: circle  - y
        3) real: circle  - radius
        4) real: polygon - x
        5) real: polygon - y
        6) real: polygon - radius
        7) real: polygon - edge count
        8) real: polygon - angle (degrees)
    Returns:
        bool: intersection
</pre>
Returns true if the given circle intersects with the regular polygon.

## IsIntersected_Line_Polygon
<pre>
    Arguments:
        1) real: line - start x
        2) real: line - start y
        3) real: line - end x
        4) real: line - end y
        5) real: line - width
        6) real[2][]: polygon vertices
    Returns:
        bool: intersection
</pre>
Returns true if the given line intersects with the polygon.

The polygon can be convex, concave, or complex (self-intersecting).

## IsIntersected_Line_Circle
<pre>
    Arguments:
        1) real: line   - start x
        2) real: line   - start y
        3) real: line   - end x
        4) real: line   - end y
        5) real: line   - width
        6) real: circle - x
        7) real: circle - y
        8) real: circle - radius
    Returns:
        bool: intersection
</pre>
Returns true if the given line intersects with the circle.

## IsIntersected_Line_Ellipse
<pre>
    Arguments:
        1) real: line    - start x
        2) real: line    - start y
        3) real: line    - end x
        4) real: line    - end y
        5) real: line    - width
        6) real: ellipse - x
        7) real: ellipse - y
        8) real: ellipse - x radius
        9) real: ellipse - y radius
    Returns:
        bool: intersection
</pre>
Returns true if the given line intersects with the ellipse.

## IsIntersected_Line_Line
<pre>
    Arguments:
        1)  real: line 1 - start x
        2)  real: line 1 - start y
        3)  real: line 1 - end x
        4)  real: line 1 - end y
        5)  real: line 1 - width
        6)  real: line 2 - start x
        7)  real: line 2 - start y
        8)  real: line 2 - end x
        9)  real: line 2 - end y
        10) real: line 2 - width
    Returns:
        bool: intersection
</pre>
Returns true if the given lines intersect.

## IsIntersected_Line_RegularPolygon
<pre>
    Arguments:
        1)  real: line    - start x
        2)  real: line    - start y
        3)  real: line    - end x
        4)  real: line    - end y
        5)  real: line    - width
        6)  real: polygon - x
        7)  real: polygon - y
        8)  real: polygon - radius
        9)  real: polygon - edge count
        10) real: polygon - angle (degrees)
    Returns:
        bool: intersection
</pre>
Returns true if the given line intersects with the regular polygon.

## IsIntersected_Polygon_Polygon
<pre>
    Arguments:
        1) real[2][]: polygon 1 vertices
        2) real[2][]: polygon 2 vertices
    Returns:
        bool: intersection
</pre>
Returns true if the given polygons intersect.

The polygons can be convex, concave, or complex (self-intersecting).

## IsIntersected_Polygon_Ellipse
<pre>
    Arguments:
        1) real[2][]: polygon vertices
        2) real: ellipse - x
        3) real: ellipse - y
        4) real: ellipse - x radius
        5) real: ellipse - y radius
    Returns:
        bool: intersection
</pre>
Returns true if the given polygon intersects with the ellipse.

The polygon can be convex, concave, or complex (self-intersecting).

## IsIntersected_Polygon_RegularPolygon
<pre>
    Arguments:
        1) real[2][]: polygon 1 vertices
        2) real: polygon 2 - x
        3) real: polygon 2 - y
        4) real: polygon 2 - radius
        5) real: polygon 2 - edge count
        6) real: polygon 2 - angle (degrees)
    Returns:
        bool: intersection
</pre>
Returns true if the given polygon intersects with the regular polygon.

The polygon can be convex, concave, or complex (self-intersecting).