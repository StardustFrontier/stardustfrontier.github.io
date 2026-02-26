# ObjShader Functions

[Return to Functions](../functions.html)

## ObjShader_Create
```
    Return Type:
        real
```
Creates a shader object and returns its ID.

## ObjShader_SetShaderF
```
    Arguments:
        1) real: objectID
        2) string: pathShader
```
Sets the path to the HLSL source for the shader.

## ObjShader_SetShaderO
```
    Arguments:
        1) real: objectID
        2) real: shaderObjectID
```
Starts applying the shader to a render object.

Does not work with text objects, but you can render one to a render target.

## ObjShader_ResetShader
```
    Arguments:
        1) real: objectID
```
Terminates application of all shaders to the render object.

## ObjShader_SetTechnique
```
    Arguments:
        1) real: objectID
        2) string: technique
```
Sets the technique that you want to run on the shader object.

## ObjShader_SetVector
```
    Arguments:
        1) real: objectID
        2) string: parameterID
        3) real: float4x
        4) real: float4y
        5) real: float4z
        6) real: float4w
```
Sets a float4 parameter in the shader.

## ObjShader_SetFloat
```
    Arguments:
        1) real: objectID
        2) string: parameterID
        3) real: floatValue
```
Sets a float parameter in the shader.

## ObjShader_SetFloatArray
```
    Arguments:
        1) real: objectID
        2) string: parameterID
        3) real array: floatArray
```
Sets a float[] parameter in the shader.

## ObjShader_SetTexture
```
    Arguments:
        1) real: objectID
        2) string: parameterID
        3) string: pathTexture
```
Sets a texture parameter using the path to the appropriate image in the shader.

You can call multiple textures.