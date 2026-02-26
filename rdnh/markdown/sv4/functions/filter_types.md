# Filter Types

[Return to Functions](../functions.html)

#
The available texture filtering types are as follows, with the descriptions coming from the official Direct3D 9 documentation:

- **FILTER_NONE**\
When used as a Mip filter type, disables mipmapping. This causes the rasterizer to use the magnification filter instead.

<br />

- **FILTER_POINT**\
When used as a Mag or Min filter type, point filtering (nearest neighbor) is used.\
When used as a Mip filter type, enables mipmapping and specifies that the rasterizer chooses the color from the texel of the nearest mip level.

<br />

- **FILTER_LINEAR**\
When used as a Mag or Min filter type, bilinear interpolation filtering is used.\
When used as a Mip filter type, enables mipmapping and trilinear filtering; it specifies that the rasterizer interpolates between the two nearest mip levels.

<br />

- **FILTER_ANISOTROPIC**\
When used as a Mag or Min filter type, specifies that anisotropic texture filtering is used. Compensates for distortion caused by the difference in angle between the texture polygon and the plane of the screen.\
\
_**Warning**: Do not use as a Mip filter type._

<br />

- **FILTER_PYRAMIDAL_QUAD**\
A 4-sample tent filter used as a Mag or Min filter.\
\
_**Warning**: Do not use as a Mip filter type._

<br />

- **FILTER_GAUSSIAN_QUAD**\
A 4-sample Gaussian filter used as a Mag or Min filter.\
\
_**Warning**: Do not use as a Mip filter type._

<br />