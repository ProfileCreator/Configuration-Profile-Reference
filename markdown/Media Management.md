# Media Management  

 [Configuration Profile Reference - Media Management](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW104)  

The profile configuration keys for media management are of two kinds: those that restrict disc burning and those that restrict media mounting and ejection. All keys are available on all versions of macOS and are supported on the user channel.  

### Disc Burning Payloads  

 [Configuration Profile Reference - Disc Burning Payloads](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW104)  

Disc burning restrictions require both Disc Burning and Finder payloads.  

The Disc Burning payload is designated by specifying `com.apple.DiscRecording` as the `PayloadType` value.  

In addition to the settings common to all payloads, this payload defines this key:  

|Key|Type|Value|
|-|-|-|
|`BurnSupport`|String|Required. Set to `off` to disable disc burning. Set to `on` for normal default operation. Set to `authenticate` to require authentication. Setting this key to `on` will not enable disc burn support if it has already been disabled by other mechanisms or preferences.|
  

The Finder payload is designated by specifying `com.apple.finder` as the `PayloadType` value.  

In addition to the settings common to all payloads, this payload defines this key:  

|Key|Type|Value|
|-|-|-|
|`ProhibitBurn`|Boolean|Required. Set to `false` to enable the Finder’s burn support. Set to `true` to disable the Finder’s burn support.|
  
  

### Allowed Media Payload  

 [Configuration Profile Reference - Allowed Media Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW104)  

The Allowed Media payload is designated by specifying `com.apple.systemuiserver` as the `PayloadType` value.  

This payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`logout-eject`|Dictionary|Optional. Media type dictionary to define volumes to eject when the user logs out.|
|`mount-controls`|Dictionary|Optional. Media type dictionary to control volume mounting.|
|`unmount-controls`|Dictionary|Optional. Media type dictionary to control volume unmounting.|
  

The Media type dictionaries can contain the following keys. Not all dictionaries use all keys. Values for media action strings are given in the next table.  

|Key (media type)|Type|Value|
|-|-|-|
|`all-media`|String|Optional. Unused; set to empty string.|
|`cd`|String or Array of Strings|Optional. Media action string(s).|
|`dvd`|String or Array of Strings|Optional. Media action string(s).|
|`bd`|String or Array of Strings|Optional. Media action string(s).|
|`blankcd`|String or Array of Strings|Optional. Media action string(s).|
|`blankdvd`|String or Array of Strings|Optional. Media action string(s).|
|`blankbd`|String or Array of Strings|Optional. Media action string(s).|
|`dvdram`|String or Array of Strings|Optional. Media action string(s).|
|`disk-image`|String or Array of Strings|Optional. Media action string(s).|
|`harddisk-internal`|String or Array of Strings|Optional. Media action string(s).|
|`networkdisk`|String or Array of Strings|Optional. Media action string(s).|
|`harddisk-external`|String or Array of Strings|Optional. Media action string(s). Internally installed SD-Cards and USB flash drives are included in the `harddisk-external` category. This key is the default for media types that don’t fall into other categories.|
  

Media action strings are described below. You can combine some strings in arrays to create custom actions.  

|Key|Type|Value|
|-|-|-|
|`authenticate`|Boolean|Optional. The user will be authenticated before the media is mounted.|
|`read-only`|Boolean|Optional. The media will be mounted as read-only; this action cannot be combined with unmount controls.|
|`deny`|Boolean|Optional. The media will not be mounted.|
|`eject`|Boolean|Optional. The media will not be mounted and it will be ejected if possible. Note that some volumes are not defined as ejectable, so using the deny key may be the best solution. This action cannot be combined with unmount controls.|
  
  
