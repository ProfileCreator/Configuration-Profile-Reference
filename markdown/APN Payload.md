# APN Payload  

 [Configuration Profile Reference - APN Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW24)  

The APN (Access Point Name) payload is designated by specifying `com.apple.apn.managed` as the `PayloadType` value.  

In iOS 7 and later, the APN payload is deprecated in favor of the Cellular payload.  

The APN Payload is not supported in macOS.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`DefaultsData`|Dictionary|This dictionary contains two key/value pairs.|
|`DefaultsDomainName`|String|The only allowed value is `com.apple.managedCarrier`.|
|`apns`|Array|This array contains an arbitrary number of dictionaries, each describing an APN configuration, with the key/value pairs below.|
|`apn`|String|This string specifies the Access Point Name.|
|`username`|String|This string specifies the user name for this APN. If it is missing, the device prompts for it during profile installation.|
|`password`|Data|Optional. This data represents the password for the user for this APN. For obfuscation purposes, the password is encoded. If it is missing from the payload, the device prompts for the password during profile installation.|
|`Proxy`|String|Optional. The IP address or URL of the APN proxy.|
|`ProxyPort`|Number|Optional. The port number of the APN proxy.|
  
