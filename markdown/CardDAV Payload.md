# CardDAV Payload  

 [Configuration Profile Reference - CardDAV Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW15)  

The CardDAV payload is designated by specifying `com.apple.carddav.account` as the `PayloadType` value.  

As of macOS v10.8 and later, this payload type supports obtaining `CardDAVUsername` and `CardDAVPassword` from an Identification Payload, if present.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`CardDAVAccountDescription`|String|Optional. The description of the account.|
|`CardDAVHostName`|String|The server address.|
|`CardDAVUsername`|String|The user's login name.|
|`CardDAVPassword`|String|Optional. The user's password.|
|`CardDAVUseSSL`|Boolean|Optional. Whether or not to use SSL.|
|`CardDAVPort`|Integer|Optional. The port on which to connect to the server.|
|`CardDAVPrincipalURL`|String|Optional. Not supported on macOS. The base URL to the user’s address book.|
  
