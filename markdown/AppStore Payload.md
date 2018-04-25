# AppStore Payload  

 [Configuration Profile Reference - AppStore Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW197)  

The AppStore payload is designated by specifying `com.apple.app.appstore` as the `PayloadType` value.   

It establishes macOS AppStore restrictions and is supported on the User channel.  

The payload contains the following keys:  

|Key|Type|Value|
|-|-|-|
|`restrict-store-require-admin-to-install`|Boolean|Optional. Restrict app installations to admin users. Available on macOS 10.9 and later.|
|`restrict-store-softwareupdate-only`|Boolean|Optional. Restrict app installations to software updates only. Available on macOS 10.10 and later.|
|`restrict-store-disable-app-adoption`|Boolean|Optional. Disable App Adoption by users. Available on macOS 10.10 and later.|
|`DisableSoftwareUpdateNotifications`|Boolean|Optional. Disable software update notifications. Available on macOS 10.10 and later.|
|`restrict-store-mdm-install -softwareupdate-only`|Boolean|Optional. Restrict app installations to MDM-installed apps and software updates. Available on macOS 10.11 and later.|
  
