# Setup Assistant  

 [Configuration Profile Reference - Setup Assistant](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW67)  

The Setup Assistant Payload is designated by specifying `com.apple.SetupAssistant.managed` as the `PayloadType`.  

On macOS, this payload specifies Setup Assistant options for either the system or particular users.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`SkipCloudSetup`|Boolean|Optional. If `true`, skip the Apple ID setup window.</br>**Availability:** Available in macOS 10.12 and later. |
|`SkipSiriSetup`|Boolean|Optional. If `true`, skip the Siri setup window.</br>**Availability:** Available in macOS 10.12 and later. |
|`SkipPrivacySetup`|Boolean|Optional. If `true`, skip the Privacy consent window.</br>**Availability:** Available in macOS 10.13.4 and later. |
|`SkipiCloudStorageSetup`|Boolean|Optional. If `true`, skip the iCloud Storage window.</br>**Availability:** Available in macOS 10.13.4 and later. |
  
