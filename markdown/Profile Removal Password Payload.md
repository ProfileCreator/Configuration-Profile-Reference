# Profile Removal Password Payload  

 [Configuration Profile Reference - Profile Removal Password Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW8)  

The Removal Password payload is designated by specifying `com.apple.profileRemovalPassword` value as the `PayloadType` value.  

A password removal policy payload provides a password to allow users to remove a locked configuration profile from the device. If this payload is present and has a password value set, the device asks for the password when the user taps a profile's Remove button. This payload is encrypted with the rest of the profile.  

|Key|Type|Value|
|-|-|-|
|`RemovalPassword`|String|Optional. Supervised only. Specifies the removal password for the profile.|
  
