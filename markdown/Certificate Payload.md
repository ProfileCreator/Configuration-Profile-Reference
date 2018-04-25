# Certificate Payload  

 [Configuration Profile Reference - Certificate Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW248)  

The `PayloadType` of a certificate payload must be one of the following:  

|Payload type|Container format|Certificate type|
|-|-|-|
|`com.apple.security.root`|PKCS#1(.cer)|Alias for `com.apple.security.pkcs1`.|
|`com.apple.security.pkcs1`|PKCS#1(.cer)|DER-encoded certificate without private key. May contain root certificates.|
|`com.apple.security.pem`|PKCS#1(.cer)|PEM-encoded certificate without private key. May contain root certificates.|
|`com.apple.security.pkcs12`|PKCS#12(.p12)|Password-protected identity certificate. Only one certificate may be included.|
  

In addition to the settings common to all payloads, all Certificate payloads define the following keys:  

|Key|Type|Value|
|-|-|-|
|`PayloadCertificateFileName`|String|Optional. The file name of the enclosed certificate.|
|`PayloadContent`|Data|Mandatory. The base64 representation of the payload with a line length of 52.|
|`Password`|String|Optional. For PKCS#12 certificates, contains the password to the identity.|
  


> **Caution:** 
Because the password string is stored in the clear in the profile, it is recommended that the profile be encrypted for the device.  
  
