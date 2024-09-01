# Render Functions

[Return to Functions](./docs.html)

## LoadTexture
<pre>
    Arguments:
        1) string: path
    Return Type:
        bool
</pre>
Loads the specified image file as a texture.

Returns true if loading was successful, otherwise returns false.

## LoadTextureInLoadThread
<pre>
    Arguments:
        1) string: path
    Return Type:
        bool
</pre>
Loads specified image file as a texture in a separate thread.

Returns true if loading was successful, otherwise returns false.\
Using this function inside @Loading is the same as using LoadTexture.\
When using large images, the script will freeze until the image has finished loading.

## RemoveTexture
<pre>
    Arguments:
        1) string: path
</pre>
Unloads the specified texture file.

## GetTextureWidth
<pre>
    Arguments:
        1) string: path
    Return Type:
        real
</pre>
Returns the width of the specified image file.

## GetTextureHeight
<pre>
    Arguments:
        1) string: path
    Return Type:
        real
</pre>
Returns the height of the specified image file.

## SetFogEnable
<pre>
    Arguments:
        1) bool: enable
</pre>
Enables or disables fog.

## SetFogParam
<pre>
    Arguments:
        1) real: start
        2) real: end
        3) real: red
        4) real: green
        5) real: blue
</pre>
Sets the fog parameters with the start and end distances from the player and the rgb values.

To turn the screen dark, you can use SetFogParam(250, 700, 0, 0, 0).

## ClearInvalidRenderPriority
Clear invalid render priorities set with [SetInvalidRenderPriorityA1](setinvalidrenderprioritya1).


## SetInvalidRenderPriorityA1
<pre>
    Arguments:
        1) real: start
        2) real: end
</pre>
Sets invalid render priority between start and end render priorities.

Drawing within the specified range is disabled by this function.

## GetReservedRenderTargetName
<pre>
    Arguments:
        1) real: index
    Return Type:
        real
</pre>
Returns the render target name reserved at Danmakufu's startup.

Index in range: 0-2\
There is always a texture that can be obtained with this function.

## CreateRenderTarget
<pre>
    Arguments:
        1) string: targetName
    Return Type:
        bool
</pre>
Creates a custom render target outside of the reserved ones.

To use, ObjPrim_SetTexture must have the name of the render target as a string.\
Textures created with this function can be used for [RenderToTextureA1](rendertotexturea1) and other similar functions.

## RenderToTextureA1
<pre>
    Arguments:
        1) string: targetName
        2) real: start
        3) real: end
        4) bool: clearRenderTarget
</pre>
Renders the specified range of invalid render priority drawings to a texture.

Set clearRenderTarget to true in order to clear the render target after each frame. If set to false, the render target will remain into the next frame.

## RenderToTextureB1
<pre>
    Arguments:
        1) string: targetName
        2) real: objectId
        3) bool: clearRenderTarget
</pre>
Renders the specified object to a texture.

Set clearRenderTarget to true in order to clear the render target after each frame. If set to false, the render target will remain into the next frame.

## SaveRenderedTextureA1
<pre>
    Arguments:
        1) string: targetName
        2) string: fileName
</pre>
Saves rendered texture to a file.

In Re:Dnh, the image will be saved as PNG regardless of extension. In vanilla Dnh, it will be BMP.\
The image file created by this function can be used immediately after its execution.

## SaveRenderedTextureA2
<pre>
    Arguments:
        1) string: targetName
        2) string: fileName
        3) real: left
        4) real: top
        5) real: right
        6) real: bottom
</pre>
Saves rendered texture to a file, given left/top/right/bottom bounds of the region to capture.

In Re:Dnh, the image will be saved as PNG regardless of extension. In vanilla Dnh, it will be BMP.\
The image file created by this function can be used immediately after its execution.

## SaveSnapShotA1
<pre>
    Arguments:
        1) string: fileName
</pre>
Saves a picture of the game to a file.

The image file created by this function can be used immediately after its execution.

## SaveSnapShotA2
<pre>
    Arguments:
        1) string: fileName
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
</pre>
Saves a picture of the game to a file, given left/top/right/bottom bounds of the region to capture.

The image file created by this function can be used immediately after its execution.

## SetGraphicsSettings
<pre>
    Arguments:
        1) real: windowSizeIndex
        2) real: bFullscreen
        3) real: bBorderless
        4) real: bIntegerScale
        5) real: bVsync
</pre>
Sets some graphics-related settings.

<pre>
windowSizeIndex : The index of the window size to use, as defined in the .def
bFullscreen     : Whether or not to change to fullscreen mode
bBorderless     : Whether or not to use a borderless window when in fullscreen mode
bIntegerScale   : Whether or not to use integer scaling in borderless fullscreen mode
bVsync          : Whether or not to enable vsync</pre>

*Note: All arguments may be set to NO_CHANGE to retain their current state*

## GetGraphicsSettings
<pre>
    Return Type:
        any array
</pre>
Returns a multi-type array of the current graphics settings.

The array is in the following format: [windowSizeIndex, bFullscreen, bBorderless. bIntegerScale, bVsync]

## GetAspectRatio
<pre>
    Arguments:
        1) real: windowSizeIndex
    Return Type:
        real const
</pre>
Returns a constant representing the aspect ratio of the given window size index.

Current possible values are:
- ASPECT_RATIO_4_3
- ASPECT_RATIO_16_9
- ASPECT_RATIO_16_10

## IsPixelShaderSupported
<pre>
    Arguments:
        1) real: majorVersion
        2) real: minorVersion
    Return Type:
        bool
</pre>
Returns true if the user's GPU supports the specified pixel shader version.

Example: `IsPixelShaderSupported(3, 0);` checks for Pixel Shader version 3.0

## SetShader
<pre>
    Arguments:
        1) real: objShader
        2) real: start
        3) real: end
</pre>
Sets the shader object associated with objShader to affect render priorities between start and end.

*Note: Render priorities are on a 0-1 scale.*

## SetShaderI
<pre>
    Arguments:
        1) real: objShader
        2) real: start
        3) real: end
</pre>
Sets the shader object associated with objShader to affect (integer) render priorities between start and end.

*Note: Render priorities are on a 0-100 scale.*

## ResetShader
<pre>
    Arguments:
        1) real: start
        2) real: end
</pre>
Stops rendering textures within the specified render priority range to the shader object.

*Note: Render priorities are on a 0-1 scale.*

## ResetShaderI
<pre>
    Arguments:
        1) real: start
        2) real: end
</pre>
Stops rendering textures within the specified (integer) render priority range to the shader object.

*Note: Render priorities are on a 0-100 scale.*