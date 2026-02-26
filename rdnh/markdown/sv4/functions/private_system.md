# Private System Functions

[Return to Functions](../functions.html)

## SetPauseScriptPath
```
    Arguments:
        1) string: pathScript
```
Defines a script to be executed when the game is paused.

## SetEndSceneScriptPath
```
    Arguments:
        1) string: pathScript
```
Defines a script to be executed when the game (Single/Plural/Stage) finishes.

## SetReplaySaveSceneScriptPath
```
    Arguments:
        1) string: pathScript
```
Defines a script to be executed when the player chooses to save a replay of the game.

## GetTransitionRenderTargetName
```
    Return Type:
        string
```
Gets the name of the render target from the frame before a menu script was executed.

Specifically to be used by menu scripts such as the pause script.\
This can be used to create a texture of the previous frame just before the game is paused.\
This allows for effects to be applied such as fading to a blur.