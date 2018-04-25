# Calendar Subscription Payload  

 [Configuration Profile Reference - Calendar Subscription Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW17)  

The calendar subscription payload is designated by specifying `com.apple.subscribedcalendar.account` as the `PayloadType` value.  

A calendar subscription payload adds a subscribed calendar to the user’s calendars list.  

The calendar subscription payload is not supported in macOS.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`SubCalAccountDescription`|String|Optional. Description of the account.|
|`SubCalAccountHostName`|String|The server address.|
|`SubCalAccountUsername`|String|The user's login name.|
|`SubCalAccountPassword`|String|The user's password.|
|`SubCalAccountUseSSL`|Boolean|Whether or not to use SSL.|
  
