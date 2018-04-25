# System Policy Managed Payload  

 [Configuration Profile Reference - System Policy Managed Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW23)  

The System Policy Managed payload is designated by specifying `com.apple.systempolicy.managed` as the `PayloadType`. This is one of three payloads that allows control of various GateKeeper settings.  

This payload allows control to disable the Finder’s contextual menu that allows bypass of System Policy restrictions.  

This payload is supported only on macOS v10.8 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`DisableOverride`|Boolean|Optional. If YES, the Finder’s contextual menu item will be disabled.|
  
