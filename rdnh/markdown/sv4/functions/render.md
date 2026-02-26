# Render Functions

[Return to Functions](../functions.html)

## LoadTexture
```
    Arguments:
        1) string: path
    Return Type:
        bool
```
Loads the specified image file as a texture.

Returns true if loading was successful, otherwise returns false.

## LoadTextureMipmap
```
    Arguments:
        1) string: path
    Return Type:
        bool
```
Loads the specified image file as a texture and generates a mipmap chain for it.

Returns true if loading was successful, otherwise returns false.

## LoadTextureInLoadThread
```
    Arguments:
        1) string: path
    Return Type:
        bool
```
Loads specified image file as a texture in a separate thread.

Returns true if loading was successful, otherwise returns false.\
Using this function inside @Loading is the same as using LoadTexture.\
When using large images, the script will freeze until the image has finished loading.

## LoadTextureMipmapInLoadThread
```
    Arguments:
        1) string: path
    Return Type:
        bool
```
Loads specified image file as a texture and generates a mipmap chain for it in a separate thread.

Returns true if loading was successful, otherwise returns false.\
Using this function inside @Loading is the same as using LoadTexture.\
When using large images, the script will freeze until the image has finished loading.

## RemoveTexture
```
    Arguments:
        1) string: path
```
Unloads the specified texture file.

## GetTextureWidth
```
    Arguments:
        1) string: path
    Return Type:
        real
```
Returns the width of the specified image file.

## GetTextureHeight
```
    Arguments:
        1) string: path
    Return Type:
        real
```
Returns the height of the specified image file.

## GetMaxTextureAnisotropy
```
    Returns:
        real
```
Returns the max texture anisotropy level supported by the device.

## IsAnisotropicTextureFilterSupported
```
    Returns:
        bool
```
Returns true if anisotropic texture filtering is supported by the device, otherwise returns false.

## SetFogEnable
```
    Arguments:
        1) bool: enable
```
Enables or disables fog.

## SetFogParam
```
    Arguments:
        1) real: start
        2) real: end
        3) real: red
        4) real: green
        5) real: blue
```
Sets the fog parameters with the start and end distances from the player and the rgb values.

To turn the screen dark, you can use SetFogParam(250, 700, 0, 0, 0).

## SetFogBoundaryParam
```
    Arguments:
        1) real: start
        2) real: end
```
Sets the fog boundary (distance) parameters to the given start and end values.

## SetFogColorParam
```
    Arguments:
        1) real: red
        2) real: green
        3) real: blue
```
Sets the fog color parameters to the given RGB values.

## SetFogColorHexParam
```
    Arguments:
        1) real: colorHex
```
Sets the fog color parameters using RGB in hexadecimal format (0xRRGGBB).

## IsFogEnable
```
    Returns:
        bool: bEnable
```
Returns true if fog is enabled, otherwise returns false.

## GetFogParam
```
    Returns:
        array[real]: params
```
Returns the current fog parameters as an array with the format [start, end, red, green, blue]

## GetFogBoundaryParam
```
    Returns:
        array[real]: boundary
```
Returns the current fog boundary parameters as an array with the format [start, end]

## GetFogColorParam
```
    Returns:
        array[real]: color
```
Returns the current fog color parameters as an array with the format [red, green, blue]

## GetFogColorHexParam
```
    Returns:
        real: color
```
Returns the current fog color parameters as a real XRGB value.

## TweenFogBoundaryParam
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: start
        4) real: end
```
Changes the fog boundary parameters to (start, end) over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve any of the current values.

## TweenFogColorParam
```
    Arguments:
        1) real: duration
        2) real: interpType
        3) real: red
        4) real: green
        5) real: blue
```
Changes the fog color parameters to (red, green, blue) over _duration_ frames with the given interpolation type.

NO_CHANGE can be used to preserve any of the current values.

## CancelFogTweens
Cancels all of the active fog tweens.

## SetRenderUpdateEnable
```
    Arguments:
        1) bool: enable
```
Enables or disables render updates for all objects.

This stops processing of all automated ObjRender functions (such as the tween and speed ones).\
Objects with Obj_SetForceRenderUpdate set to true are unaffected.\
This can also be set per object with Obj_SetRenderUpdateEnable.

## IsRenderUpdateEnable
```
    Return Type:
        bool
```
Returns true if render updates are globally enabled, otherwise returns false.

## ClearInvalidRenderPriority
Clear invalid render priorities set with [SetInvalidRenderPriorityA1](#setinvalidrenderprioritya1).


## SetInvalidRenderPriorityA1
```
    Arguments:
        1) real: start
        2) real: end
```
Sets invalid render priority between start and end render priorities.

Drawing within the specified range is disabled by this function.

## GetReservedRenderTargetName
```
    Arguments:
        1) real: index
    Return Type:
        real
```
Returns the render target name reserved at Danmakufu's startup.

Index in range: 0-2\
There is always a texture that can be obtained with this function.

## CreateRenderTarget
```
    Arguments:
        1) string: targetName
    Return Type:
        bool
```
Creates a custom render target outside of the reserved ones.

To use, ObjPrim_SetTexture must have the name of the render target as a string.\
Textures created with this function can be used for [RenderToTextureA1](#rendertotexturea1) and other similar functions.

## CreateRenderTargetB
```
    Arguments:
        1) string: targetName
        2) real: width
        3) real: height
    Return Type:
        bool
```
Creates a custom render target outside of the reserved ones with a specific width and height.

To use, ObjPrim_SetTexture must have the name of the render target as a string.\
Textures created with this function can be used for [RenderToTextureA1](#rendertotexturea1) and other similar functions.

## CopyRenderTargetToBackupSurface
```
    Arguments:
        1) string: targetName
```
Creates a backup surface for the render target and copies the render target's contents to it.

If the Direct3D device is lost, the render target will be restored using this attached backup surface.

_**Note:** This is an expensive operation and should only be used for render targets that are not rendered to every frame, such as the transition target for pause scenes._

## ClearRenderTargetBackupSurface
```
    Arguments:
        1) string: targetName
```
Clears and deletes the render target's backup surface.

It is recommended to call this after you are done using the render target, so that an old frame isn't held within the backup surface.

## RenderToTextureA1
```
    Arguments:
        1) string: targetName
        2) real: start
        3) real: end
        4) bool: clearRenderTarget
```
Renders the specified range of invalid render priority drawings to a texture.

Set clearRenderTarget to true in order to clear the render target after each frame. If set to false, the render target will remain into the next frame.

## RenderToTextureB1
```
    Arguments:
        1) string: targetName
        2) real: objectId
        3) bool: clearRenderTarget
```
Renders the specified object to a texture.

Set clearRenderTarget to true in order to clear the render target after each frame. If set to false, the render target will remain into the next frame.

## RenderToTextureBA1
```
    Arguments:
        1) string: targetName
        2) array[real]: objIdArray
        3) bool: clearRenderTarget
```
Renders the objects in the specified array to a texture.

Set clearRenderTarget to true in order to clear the render target after each frame. If set to false, the render target will remain into the next frame.

## SaveRenderedTextureA1
```
    Arguments:
        1) string: targetName
        2) string: fileName
```
Saves rendered texture to a file.

In Re:Dnh, the image will be saved as PNG regardless of extension. In vanilla Dnh, it will be BMP.\
The image file created by this function can be used immediately after its execution.

## SaveRenderedTextureA2
```
    Arguments:
        1) string: targetName
        2) string: fileName
        3) real: left
        4) real: top
        5) real: right
        6) real: bottom
```
Saves rendered texture to a file, given left/top/right/bottom bounds of the region to capture.

In Re:Dnh, the image will be saved as PNG regardless of extension. In vanilla Dnh, it will be BMP.\
The image file created by this function can be used immediately after its execution.

## SaveSnapShotA1
```
    Arguments:
        1) string: fileName
```
Saves a picture of the game to a file.

The image file created by this function can be used immediately after its execution.

## SaveSnapShotA2
```
    Arguments:
        1) string: fileName
        2) real: left
        3) real: top
        4) real: right
        5) real: bottom
```
Saves a picture of the game to a file, given left/top/right/bottom bounds of the region to capture.

The image file created by this function can be used immediately after its execution.

## SetGraphicsSettings
```
    Arguments:
        1) real: windowSizeIndex
        2) real: bFullscreen
        3) real: bBorderless
        4) real: bIntegerScale
        5) real: bVsync
```
Sets some graphics-related settings.

```
windowSizeIndex : The index of the window size to use, as defined in the .def
bFullscreen     : Whether or not to change to fullscreen mode
bBorderless     : Whether or not to use a borderless window when in fullscreen mode
bIntegerScale   : Whether or not to use integer scaling in borderless fullscreen mode
bVsync          : Whether or not to enable vsync```

*Note: All arguments may be set to NO_CHANGE to retain their current state*

## GetGraphicsSettings
```
    Return Type:
        any array
```
Returns a multi-type array of the current graphics settings.

The array is in the following format: [windowSizeIndex, bFullscreen, bBorderless. bIntegerScale, bVsync]

## GetAspectRatio
```
    Arguments:
        1) real: windowSizeIndex
    Return Type:
        real const
```
Returns a constant representing the aspect ratio of the given window size index.

Current possible values are:
- ASPECT_RATIO_4_3
- ASPECT_RATIO_16_9
- ASPECT_RATIO_16_10

## IsPixelShaderSupported
```
    Arguments:
        1) real: majorVersion
        2) real: minorVersion
    Return Type:
        bool
```
Returns true if the user's GPU supports the specified pixel shader version.

Example: `IsPixelShaderSupported(3, 0);` checks for Pixel Shader version 3.0

## SetShader
```
    Arguments:
        1) real: objShader
        2) real: start
        3) real: end
```
Sets the shader object associated with objShader to affect render priorities between start and end.

*Note: Render priorities are on a 0-1 scale.*

## SetShaderI
```
    Arguments:
        1) real: objShader
        2) real: start
        3) real: end
```
Sets the shader object associated with objShader to affect (integer) render priorities between start and end.

*Note: Render priorities are on a 0-100 scale.*

## ResetShader
```
    Arguments:
        1) real: start
        2) real: end
```
Stops rendering textures within the specified render priority range to the shader object.

*Note: Render priorities are on a 0-1 scale.*

## ResetShaderI
```
    Arguments:
        1) real: start
        2) real: end
```
Stops rendering textures within the specified (integer) render priority range to the shader object.

*Note: Render priorities are on a 0-100 scale.*