# macOS Server Payload  

 [Configuration Profile Reference - macOS Server Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW152)  

This payload defines an macOS Server account. This payload is designated by the `com.apple.osxserver.account` PayloadType value.  

|Key|Type|Value|
|-|-|-|
|`HostName`|String|Mandatory. The server address.|
|`UserName`|String|Mandatory. The user's login name.|
|`Password`|String|Optional. The user’s password.|
|`AccountDescription`|String|Optional. Description of the account.|
|`ConfiguredAccounts`|Array|Mandatory. An array of dictionaries containing configured account types and relevant settings. Each dictionary consists of a `Type` field plus additional settings specific to the `Type`.|
  

The following `ConfiguredAccounts` dictionary is currently supported:  

### Documents Dictionary  

 [Configuration Profile Reference - Documents Dictionary](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW152)  

|Key|Type|Value|
|-|-|-|
|`Type`|String|Mandatory. The Documents account type: `com.apple.osxserver.documents`.|
|`Port`|Number|Optional. Designates the port number to use when contacting the server. If no port number is specified, the default port is used.|
  
  
