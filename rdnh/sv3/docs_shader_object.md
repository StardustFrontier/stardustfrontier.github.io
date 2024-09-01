# Shader Object Functions

[Return to Functions](./docs.html)

## ObjShader_Create
<pre>
    Return Type:
        real
</pre>
Creates a shader object and returns its ID.

## ObjShader_SetShaderF
<pre>
    Arguments:
        1) real: objectID
        2) string: pathShader
</pre>
Sets the path to the HLSL source for the shader.

## ObjShader_SetShaderO
<pre>
    Arguments:
        1) real: objectID
        2) real: shaderObjectID
</pre>
Starts applying the shader to a render object.

Does not work with text objects, but you can render one to a render target.

## ObjShader_ResetShader
<pre>
    Arguments:
        1) real: objectID
</pre>
Terminates application of all shaders to the render object.

## ObjShader_SetTechnique
<pre>
    Arguments:
        1) real: objectID
        2) string: technique
</pre>
Sets the technique that you want to run on the shader object.

## ObjShader_SetVector
<pre>
    Arguments:
        1) real: objectID
        2) string: parameterID
        3) real: float4x
        4) real: float4y
        5) real: float4z
        6) real: float4w
</pre>
Sets a float4 parameter in the shader.

## ObjShader_SetFloat
<pre>
    Arguments:
        1) real: objectID
        2) string: parameterID
        3) real: floatValue
</pre>
Sets a float parameter in the shader.

## ObjShader_SetFloatArray
<pre>
    Arguments:
        1) real: objectID
        2) string: parameterID
        3) real array: floatArray
</pre>
Sets a float[] parameter in the shader.

## ObjShader_SetTexture
<pre>
    Arguments:
        1) real: objectID
        2) string: parameterID
        3) string: pathTexture
</pre>
Sets a texture parameter using the path to the appropriate image in the shader.

You can call multiple textures.