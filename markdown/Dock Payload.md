# Dock Payload  

 [Configuration Profile Reference - Dock Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW327)  

The Dock payload is designated by specifying `com.apple.dock` as the `PayloadType`.  

The Dock payload is supported on the user channel and, except for `AllowDockFixupOverride`, on all version of macOS. The key `AllowDockFixupOverride` is supported on macOS 10.12 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`orientation`|String|Optional. Orientation of the dock. Values may be `bottom`, `left`, or `right`.|
|`position-immutable`|Boolean|Optional. If `true`, the position is locked.|
|`autohide`|Boolean|Optional. If `true`, automatically hide and show the dock.	|
|`autohide-immutable`|Boolean|Optional. If `true`, the Automatically Hide checkbox is disabled.|
|`minimize-to-application`|Boolean|Optional. If `true`, enable the minimize-to-application feature.|
|`minimize-to-application-immutable`|Boolean|Optional. If `true`, the minimize-to-application checkbox is disabled.|
|`magnification`|Boolean|Optional. If `true`, magnification is active.|
|`magnify-immutable`|Boolean|Optional. If `true`, the magnification checkbox is disabled.|
|`largesize`|Integer|Optional. The size of the largest magnification. Values must be in range 16 to 128.|
|`magsize-immutable`|Boolean|Optional. If `true`, the magnify slider is disabled.|
|`show-process-indicators`|Boolean|Optional. If `true`, show the process indicator.|
|`launchanim`|Boolean|Optional. If `true`, animate opening applications.|
|`launchanim-immutable`|Boolean|Optional. If `true`, the Animate Opening Applications checkbox is disabled.|
|`mineffect`|String|Optional. Set minimize effect. Values may be `genie` or `scale`.|
|`mineffect-immutable`|Boolean|Optional. If `true`, the Minimize Using popup is disabled.|
|`tilesize`|Integer|Optional. The tile size. Values must be in range 16 to 128.|
|`size-immutable`|Boolean|Optional. If `true`, the size slider will be disabled.|
|`MCXDockSpecialFolders`|Array of Strings|Optional. One or more special folders that may be created at user login time and placed in the dock. Values may be `AddDockMCXMyApplicationsFolder`,  `AddDockMCXDocumentsFolder`,  `AddDockMCXSharedFolder`,  or  `AddDockMCXOriginalNetworkHomeFolder`. The "My Applications" item is only used for Simple Finder environments. The "Original Network Home" item is only used for mobile account users.|
|`AllowDockFixupOverride`|Boolean|Optional. If `true`, use the file in `/Library/Preferences/ com.apple.dockfixup.plist` when a new user or migrated user logs in. The format of this file currently has no documentation. This option has no effect for existing users.|
|`static-only`|Boolean|Optional. If `true`, the device will use the static-apps and static-others dictionaries for the dock and ignore any items in the persistent-apps and persistent-others dictionaries. If `false`, the contents will be merged with the `static` items listed first.|
|`static-others`|Array of Dictionaries|Optional. Dock items in the Documents side that cannot be removed from the dock.|
|`static-apps`|Array of Dictionaries|Optional. Dock items in the Applications side that cannot be removed from the dock.|
|`contents-immutable`|Boolean|Optional. If `true`,  the user cannot remove any item from or add any item to the dock.|
  

The `static-others` and `static-apps` dictionaries define the following keys:  

|Key|Type|Value|
|-|-|-|
|`tile-data`|Dictionary|Required. Information about a dock item.|
|`tile-type`|String|Required. The type of the tile. Values may be `file-tile`, `directory-tile`, or `url-tile`. If you are unsure whether the file item is a file or a directory, set this key to `file-tile`.|
  

The `tile-data` dictionary defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`label`|String|Required. Label of a dock item.|
|`url`|String|Optional. For URL tiles, the URL string.|
|`file-type`|Integer|Required. The type of the tile expressed as a number. 3 = `directory`, 0 = `URL`, 1 = `file`.|
  
