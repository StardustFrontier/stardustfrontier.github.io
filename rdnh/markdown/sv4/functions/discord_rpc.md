# Discord RPC Functions

[Return to Functions](../functions.html)

## DiscordRPC_Initialize
```
    Arguments:
        1) string: appID
        2) array[string]: allowList = nil
```
Initializes Discord RPC with the given application ID (string) and an optional allow list.

An allow list is a string array of Discord user IDs that are allowed to connect.\
If an allow list is not provided, all connections will be allowed.

_**Note**: Discord RPC will not work unless discord-rpc.dll is placed in the module directory._

## DiscordRPC_Shutdown
```
    Return Type:
        nil
```
Shuts down Discord RPC, closing any existing connection.

This is only needed if you want to be able to reinitialize Discord RPC, such as to toggle it on or off in an options menu.

## DiscordRPC_IsConnected
```
    Return Type:
        bool
```
Returns true if connected to a Discord user, otherwise returns false.

## DiscordRPC_ClearPresence
```
    Return Type:
        nil
```
Fully clears the current rich presence, including the "Playing: (App Name)" text.

## DiscordRPC_ForcePresenceUpdate
```
    Return Type:
        nil
```
Immediately forces rich presence to update.

_**Note**: Discord's update rate limit is not formally documented, but some sources say to avoid updating more than a few times per 15 seconds._

## DiscordRPC_SetPresenceStartTime
```
    Arguments:
        1) real: timestamp
```
Sets the rich presence start timestamp in seconds since the epoch format.

Should be used with `GetTimeSinceEpoch()`.

## DiscordRPC_SetPresenceEndTime
```
    Arguments:
        1) real: timestamp
```
Sets the rich presence end timestamp in seconds since the epoch format.

Should be used with `GetTimeSinceEpoch()`.

## DiscordRPC_SetPresenceDetails
```
    Arguments:
        1) string: details
```
Sets the rich presence details (primary description) text.

This is the first description line in the activity interface.

## DiscordRPC_SetPresenceState
```
    Arguments:
        1) string: state
```
Sets the rich presence state (secondary description) text.

This is the second description line in the activity interface.

## DiscordRPC_SetPresenceLargeImage
```
    Arguments:
        1) string: imageName
```
Sets the name of the large (primary) image to use.

## DiscordRPC_SetPresenceLargeImageText
```
    Arguments:
        1) string: text
```
Sets the text shown when hovering over the large (primary) image.

## DiscordRPC_SetPresenceSmallImage
```
    Arguments:
        1) string: imageName
```
Sets the name of the small (secondary) image to use.

## DiscordRPC_SetPresenceSmallImageText
```
    Arguments:
        1) string: text
```
Sets the text shown when hovering over the small (secondary) image.