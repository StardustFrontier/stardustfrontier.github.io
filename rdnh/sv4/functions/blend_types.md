# Blend Types

[Return to Functions](../functions.html)

#
Blend types affect the way an object is rendered.\
The available blend types are:

- **BLEND_ALPHA**\
Overlays the image on top of the background, using the image's alpha values to determine transparency of individual pixels.\
\
Formula: `(r1, g1, b1) * a1/255 + (r2, g2, b2) * (1 - (a1/255))`

<br />

- **BLEND_ADD_RGB**\
Adds the image's pixel values to those of the background, resulting in a brighter image.\
\
Formula: `(r1, g1, b1) + (r2, g2, b2)`

<br />

- **BLEND_MULTIPLY**\
Multiplies the image's pixel values with those of the background, as a ratio from 0 to 255.\
For example, an image multiplied by solid white will result in the same image, and an image multiplied by solid gray (127, 127, 127) will result in an image with half the brightness.\
\
Formula: `(r1, g1, b1) * (r2, g2, b2) / 255`

<br />

- **BLEND_SUBTRACT**\
Subtracts the image's pixel values from those of the background, resulting in a darker image.\
\
Formula: `(r2, g2, b2) - (r1, g1, b1)`

<br />

- **BLEND_ADD_ARGB**\
Adds the image's pixel values to those of the background, using the image's alpha values to determine transparency of individual pixels.\
\
Formula: `(r1, g1, b1) * a1/255 + (r2, g2, b2)`

<br />

- **BLEND_INV_DESTRGB**\
Inverts the color of the background in relation to the intensity of the image's pixel values. Also known as exclusion blending.\
\
The closer the image's pixel values are to 255, the more the background is inverted in that color.\
The closer the image's pixel values are to 0, the less it is inverted in that color.\
What this results in is a linear scale between the inverted background, half-intensity (127), and the original background color.\
\
For example, a solid white image will invert the background pixels exactly. A solid red image (255, 0, 0) will invert only the background pixels' red values, but not affect the green or blue values.\
\
Formula: `(r1, g1, b1) + (r2, g2, b2) - 2 * (r1, g1, b1) * (r2, g2, b2) / 255`

<br />

- **BLEND_SHADOW**\
Inverts the image's pixel values, then applies multiply-blend with the background.\
\
Formula: `((255, 255, 255) - (r1, g1, b1)) * (r2, g2, b2) / 255`

<br />