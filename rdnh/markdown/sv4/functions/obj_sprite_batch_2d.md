# ObjSpriteBatch2D Functions

[Return to Functions](../functions.html)

## ObjSpriteBatch2D_Create
```
    Arguments:
        1) real: maxSpriteCount
    Returns:
        real: objectID
```
Creates a sprite batch 2d object with the ability to render up to maxSpriteCount sprites and returns its ID.

## ObjSpriteBatch2D_CreateRenderer
```
    Arguments:
        1)  real: objectID
        2+) real const: blendTypes...
```
Creates a renderer for the specified blend type(s).

*Note: each renderer allocates memory for enough vertices to draw the sprite count set in ObjSpriteBatch2D_Create.*

## ObjSpriteBatch2D_CreateRendererAll
```
    Arguments:
        1) real: objectID
```
Creates renderers for all blend types.

*Note: each renderer allocates memory for enough vertices to draw the sprite count set in ObjSpriteBatch2D_Create.*

## ObjSpriteBatch2D_SetTexture
```
    Arguments:
        1) real: objectID
        2) string: texture
```
Sets the texture for the sprite batch to use.

All objects added to the batch are rendered using this texture.

## ObjSpriteBatch2D_AddSprite
```
    Arguments:
        1) real: objectID
        2) real: spriteObjectID
```
Adds a sprite to the batch, which must be an ObjBatchSprite2D.

## ObjSpriteBatch2D_RemoveSprite
```
    Arguments:
        1) real: objectID
        2) real: spriteObjectID
```
Removes a sprite from the sprite batch.

*Note: This is a slow operation and shouldn't be used often.*

## ObjBatchSprite2D_Create
```
    Returns:
        real: objectID
```
Creates a 2D sprite object capable of being batch rendered and returns its ID.

This object is actually of the type OBJ_BATCH_SPRITE_2D, but it can use all ObjSprite2D functions and most ObjRender functions.

*Note: These objects cannot use ObjPrim functions.*