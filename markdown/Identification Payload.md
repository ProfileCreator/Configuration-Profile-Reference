# Identification Payload  

 [Configuration Profile Reference - Identification Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW10)  

The Identification payload is designated by specifying `com.apple.configurationprofile.identification` value as the `PayloadType` value.  

This payload allows you to save names of the account user and prompt text. If left blank, the user has to provide this information when he or she installs the profile.  

The Identification payload is not supported in iOS.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`FullName`|String|The full name of the designated accounts.|
|`EmailAddress`|String|The address for the accounts.|
|`UserName`|String|The UNIX user name for the accounts.|
|`Password`|String|You can provide the password or choose to have the user provide it when he or she installs the profile.|
|`Prompt`|String|Custom instruction for the user, if needed.|
  
