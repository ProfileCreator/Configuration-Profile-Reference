# Google Account Payload  

 [Configuration Profile Reference - Google Account Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW610)  

The Google account payload is designated by specifying `com.apple.google-oauth` as the `PayloadType` value. You can install multiple Google payloads.  

Each Google payload sets up a Google email address as well as any other Google services the user enables after authentication. Google accounts must be installed via MDM or by Apple Configurator 2 (if the device is supervised). The payload never contains credentials; the user will be prompted to enter credentials shortly after the payload has been successfully installed.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`AccountDescription`|String|Optional. A user-visible description of the Google account, shown in the Mail and Settings apps.|
|`AccountName`|String|Optional. The user’s full name for the Google account. This name will appear in sent messages.|
|`EmailAddress`|String|Required. The full Google email address for the account.|
|`CommunicationServiceRules`|Dictionary|Optional. The communication service handler rules for this account. The `CommunicationServiceRules` dictionary currently contains only a `DefaultServiceHandlers` key; its value is a dictionary which contains an `AudioCall` key whose value is a string containing the bundle identifier for the default application that handles audio calls made to contacts from this account.|
  
