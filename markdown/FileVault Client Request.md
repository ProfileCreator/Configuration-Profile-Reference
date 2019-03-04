# FileVault Client Request  

 [Configuration Profile Reference - FileVault Client Request](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW843)  

The client issues a HTTPS POST request to the server with XML data containing the following:  

|Key|Type|Value|
|-|-|-|
|`VersionNumber`|String|Currently set to '1.0'.|
|`SerialNumber`|String|The serial number of the client computer. The server must include this value in its response back to the client (see below).|
|`RecoveryKeyCMS64`|String|The recovery key encrypted using the encryption certificate provided in the configuration profile (referenced by the `EncryptCertPayloadUUID` key). The encrypted payload contains only the recovery key string without any XML wrapper. The encrypted data is wrapped in a CMS envelope and is then Base-64 encoded.|
  

These tags are enclosed within a parent `FDECaptureRequest` tag. An example of an XML message body is:  

```
<FDECaptureRequest>
<VersionNumber>1.0</VersionNumber>
<SerialNumber>A02FE08UCC8X</SerialNumber>
<RecoveryKeyCMS64>MIAGCSqGSIb3DQEHA ... AAAAAAAAA==</RecoveryKeyCMS64>
</FDECaptureRequest>
```  
