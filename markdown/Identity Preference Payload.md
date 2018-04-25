# Identity Preference Payload  

 [Configuration Profile Reference - Identity Preference Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW243)  

Available in macOS 10.12 and later. An Identity Preference payload lets you identify an Identity Preference item in the user's keychain that references a identity payload included in the same profile. It can only appear in a user profile, not a device profile. See also [Certificate Preference Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW143) for setting up certificate preferences.  

You can include multiple Identity Preference payloads as needed. Identity Preference payloads are designated by specifying `com.apple.security.identitypreference` as the `PayloadType` value.  

An Identity Preference payload contains the following keys:  

|Key|Type|Value|
|-|-|-|
|`Name`|String|Required. An email address (RFC822), DNS hostname, or other name that uniquely identifies a service requiring this identity.|
|`PayloadCertificateUUID`|String|The UUID of another payload within the same profile that installed the identity; for example, a 'com.apple.security.pkcs12' or 'com.apple.security.scep' payload.|
  
