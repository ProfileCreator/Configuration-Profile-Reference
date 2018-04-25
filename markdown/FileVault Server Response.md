# FileVault Server Response  

 [Configuration Profile Reference - FileVault Server Response](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW844)  

Upon receiving the client’s request, the server must respond to the client with XML data containing:  

|Key|Type|Value|
|-|-|-|
|`SerialNumber`|String|The serial number of the client computer. This value must be the same as the one sent in the request.|
|`RecordNumber`|Short string|This value must be nonempty but otherwise is up to the site to define it. This value will be displayed to the user along with the serial number on the EFI login screen when the user is asked to enter the recovery key. As an example, this could be a value to assist the site administrator in locating or verifying the user's recovery key in a database.|
  
