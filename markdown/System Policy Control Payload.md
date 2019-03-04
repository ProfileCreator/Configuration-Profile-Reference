# System Policy Control Payload  

 [Configuration Profile Reference - System Policy Control Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW21)  

The System Policy Control payload is designated by specifying `com.apple.systempolicy.control` as the `PayloadType`.  

This payload allows control over configuring the “Allowed applications downloaded from:” option in the “General” tab of “Security & Privacy” in System Preferences.  

This payload must only exist in a device profile. If the payload is present in a user profile, an error will be generated during installation and the profile will fail to install.  

This payload is supported only on macOS v10.8 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`EnableAssessment`|Boolean|Optional. If the key is present and has a value of `YES`, Gatekeeper is enabled. If the key is present and has a value of `NO`, Gatekeeper is disabled.|
|`AllowIdentifiedDevelopers`|Boolean|Optional. If the key is present and has a value of `YES`, Gatekeeper’s “Mac App Store and identified developers” option is chosen. If the key is present and has a value of `NO`, Gatekeeper’s “Mac App Store” option is chosen.</br>If `EnableAssessment` is not `true`, this key has no effect.|
  
