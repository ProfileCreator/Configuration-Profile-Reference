# Desktop Payload  

 [Configuration Profile Reference - Desktop Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW326)  

The Desktop payload is designated by specifying `com.apple.desktop` as the `PayloadType`.  

This payload sets up macOS Desktop settings and restrictions. It is supported on the user channel and on macOS 10.10 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`locked`|Boolean|Optional. If `true`, the desktop picture is locked. Default is `false`.|
|`override-picture-path`|String|Optional. If supplied, it sets the path to the desktop picture.|
  
