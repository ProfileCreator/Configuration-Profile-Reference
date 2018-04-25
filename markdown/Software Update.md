# Software Update  

 [Configuration Profile Reference - Software Update](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW68)  

The Software Update payload is designated by specifying `com.apple.SoftwareUpdate` as the `PayloadType`.  

This payload controls software update catalog options on macOS v10.13 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`CatalogURL`|String|Optional. The URL of the software update catalog.|
|`forceDelayedSoftwareUpdates`|Boolean|Optional. If `true`, software updates will be delayed by the duration defined by `ManagedDeferredInstallDelay`. Default is `false`.|
|`ManagedDeferredInstallDelay`|Integer|Optional. The duration, in days, that software updates will be delayed, if `forcedDelayedSoftwareUpdates` is set to `true`.  Default is `30`.</br>**Availability:** Available in macOS 10.13.4 and later.|
  
