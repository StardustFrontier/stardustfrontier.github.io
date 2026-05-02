# Text Functions

[Return to Functions](../functions.html)

## InstallFont
```
    Arguments:
        1) string: path
    Return Type:
        bool
```
Loads the given font, which can be used with ObjText_SetFontType, allowing for usage of fonts that are not standard to Windows.

Returns true if successful.

## ClearFontCache
```
    Return Type:
        nil
```
Clears the font character cache and texture atlas.