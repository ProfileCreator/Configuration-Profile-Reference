# CalDAV Payload  

 [Configuration Profile Reference - CalDAV Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW16)  

The payload is designated by specifying `com.apple.caldav.account` as the `PayloadType`.  

This payload configures a CalDAV account.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`CalDAVAccountDescription`|String|Optional. The description of the account.|
|`CalDAVHostName`|String|The server address.</br>In macOS, this key is required.|
|`CalDAVUsername`|String|The user's login name.</br>In macOS, this key is required.|
|`CalDAVPassword`|String|Optional. The user's password.|
|`CalDAVUseSSL`|Boolean|Whether or not to use SSL.</br>In macOS, this key is optional.|
|`CalDAVPort`|Integer|Optional. The port on which to connect to the server.|
|`CalDAVPrincipalURL`|String|Optional. The base URL to the user’s calendar. In macOS this URL is required if the user doesn’t provide a password, because auto-discovery of the service will fail and the account won’t be created.|
  
