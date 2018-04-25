# Shared Device Configuration Payload  

 [Configuration Profile Reference - Shared Device Configuration Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW602)  

The Shared Device Configuration Payload is designated by specifying `com.apple.shareddeviceconfiguration` as the `PayloadType` value. It can contain only one payload, which must be supervised. It is not supported on the User Channel.  

The Shared Device Configuration Payload allows admins to specify optional text displayed on the login window and lock screen (i.e. a "If Lost, Return To" message and Asset Tag Information). It is supported on iOS 9.3 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`AssetTagInformation`|String|Optional. Asset tag information for the device, displayed on the login window and lock screen.|
|`LockScreenFootnote`|String|Optional. A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.|
|`IfLostReturnToMessage`|String|**Deprecated.** Use `LockScreenFootnote` instead.|
  
