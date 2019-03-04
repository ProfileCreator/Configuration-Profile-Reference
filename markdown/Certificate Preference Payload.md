# Certificate Preference Payload  

 [Configuration Profile Reference - Certificate Preference Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW143)  

Certificate Preference payloads are designated by specifying `com.apple.security.certificatepreference` as the `PayloadType` value. See also [Identity Preference Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW243) for setting up identity preferences.  

A Certificate Preference payload lets you identify a Certificate Preference item in the user's keychain that references a certificate payload included in the same profile. It can only appear in a user profile, not a device profile. You can include multiple Certificate Preference payloads as needed.   

Available in MacOS 10.12 and later.   

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`Name`|String|Required. An email address (RFC822) or other name for which a preferred certificate is requested.|
|`PayloadCertificateUUID`|String|The UUID of another payload within the same profile that installed the certificate; for example, a 'com.apple.security.root' payload.|
  
