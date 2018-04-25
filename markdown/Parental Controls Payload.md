# Parental Controls Payload  

 [Configuration Profile Reference - Parental Controls Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

Parental Control on macOS consists of many different payloads which are set individually depending on the type of control required. Parental control payloads are supported on the user channel. Each payload and its respective keys are described in the sections below.  

### Parental Control Web Content Filter Payload  

 [Configuration Profile Reference - Parental Control Web Content Filter Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

The Parental Control Web Content Filter payload is designated by specifying `com.apple.familycontrols.contentfilter` as the `PayloadType` value.  

In addition to the settings common to all payloads, this payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`restrictWeb`|Boolean|Required. Set to `true` to enable Web content filters.|
|`useContentFilter`|Boolean|Optional. Set to `true` to try to automatically filter content.|
|`whiteListEnabled`|Boolean|Optional. Set to `true` to use the filterWhiteList and filterBlackList lists.|
|`siteWhiteList`|Array of Dictionaries|Required if `whiteListEnabled` is `true`. If specified, this key contains an array of dictionaries (see below) that define additional allowed sites besides those in the automated list of allowed and unallowed sites, including disallowed adult sites.|
|`filterWhiteList`|Array of URL Strings|Optional. If specified and `restrictWeb` is `true`, qn array of URLs designating the only allowed Websites.|
|`filterBlackList`|Array of URL Strings|Optional. If specified and `restrictWeb` is `true`, an array of URLs of Websites never to be allowed.|
  

Each `siteWhiteList` dictionary contains these keys:  

|Key|Type|Value|
|-|-|-|
|`address`|String|Required. Site prefix, including `http(s)` scheme.|
|`pageTitle`|String|Optional. Site page title.|
  
  

### Parental Control Time Limits Payload  

 [Configuration Profile Reference - Parental Control Time Limits Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

The Parental Control Time Limits payload is designated by specifying `com.apple.familycontrols.timelimits.v2` as the `PayloadType` value.  

It consists of a dictionary containing a master enabled flag plus a dictionary of time limit specification keys.  

In addition to the settings common to all payloads, this payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`familyControlsEnabled`|Boolean|Required. Set to `true` to use time limits.|
|`time-limits`|Dictionary|Required if `familyControlsEnabled` is `true`. Time limits settings.|
  

Each `time-limits` dictionary contains these keys:  

|Key|Type|Value|
|-|-|-|
|`weekday-allowance`|Dictionary|Optional. Weekday allowance settings.|
|`weekday-curfew`|Dictionary|Optional. Weekday curfew settings.|
|`weekend-allowance`|Dictionary|Optional. Weekend allowance settings.|
|`weekend-curfew`|Dictionary|Optional. Weekend curfew settings.|
  

Each `allowance` or `curfew` dictionary contains these keys:  

|Key|Type|Value|
|-|-|-|
|`enabled`|Boolean|Required. Set to `true` to enable these settings.|
|`rangeType`|Number|Required. Type of day range: 0 = weekday, 1 = weekend.|
|`start`|String|Optional. Curfew start time in the format %d:%d:%d.|
|`end`|String|Optional. Curfew end time in the format %d:%d:%d.|
|`secondsPerDay`|Number|Optional. Seconds for that day for allowance.|
  
  

### Parental Control Application Access Payload  

 [Configuration Profile Reference - Parental Control Application Access Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

The Parental Control Application Access payload is designated by specifying `com.apple.applicationaccess.new` as the `PayloadType` value.  

It enables application access restrictions on macOS.  

In addition to the settings common to all payloads, this payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`familyControlsEnabled`|Boolean|Required. Set to `true` to enable application access restrictions.|
|`whiteList`|Array of Dictionaries|Optional. Allowed processes.|
|`pathBlackList`|Array of Strings|Optional. Paths to disallowed processes.|
|`pathWhiteList`|Array of Strings|Optional. Paths to allowed processes.|
  

Each `whiteList` dictionary contains these keys:  

|Key|Type|Value|
|-|-|-|
|`bundleID`|String|Optional. Bundle ID of application.|
|`displayName`|String|Optional. Display name.|
|`displayName`|String|Optional. Path to application.|
  
  

### Parental Control Dashboard Payload  

 [Configuration Profile Reference - Parental Control Dashboard Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

The Parental Control Dashboard payload is designated by specifying `com.apple.dashboard` as the `PayloadType` value.  

It is used to define a white list of dashboard widgets.  

In addition to the settings common to all payloads, this payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`whiteListEnabled`|Boolean|Required. Set to `true` to enable the widget white list items.|
|`whiteList`|Array of Dictionaries|Required. List that defines Dashboard widgets.|
  

Each widget `whiteList` dictionary contains these keys:  

|Key|Type|Value|
|-|-|-|
|`Type`|String|Required. Set to `bundleID` to use a widget’s bundle ID as its ID.|
|`ID`|String|Required. The bundle ID of a widget.|
  
  

### Parental Control Dictionary Payload  

 [Configuration Profile Reference - Parental Control Dictionary Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

The Parental Control Dictionary payload is designated by specifying `com.apple.Dictionary` as the `PayloadType` value.  

It enables the restrictions defined in the device’s Parental Controls Dictionary.  

In addition to the settings common to all payloads, this payload defines this key:  

|Key|Type|Value|
|-|-|-|
|`parentalControl`|Boolean|Required. Set to `true` to enable parental controls dictionary restrictions.|
  
  

### Parental Control Dictation and Profanity Payload  

 [Configuration Profile Reference - Parental Control Dictation and Profanity Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

The Parental Control Dictation and Profanity payload is designated by specifying `com.apple.ironwood.support` as the `PayloadType` value.  

It disables dictation and suppresses profanity on the device.  

In addition to the settings common to all payloads, this payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`IronwoodAllowed`|Boolean|Optional. Set to `false` to disable dictation.|
|`ProfanityAllowed`|Boolean|Optional. Set to `false` to suppress profanity.|
  
  

### Parental Control Game Center Payload  

 [Configuration Profile Reference - Parental Control Game Center Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

The Parental Control Game Center payload is designated by specifying `com.apple.gamed` as the `PayloadType` value.  

It restricts Game Center options on the device.  

In addition to the settings common to all payloads, this payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`GKFeatureGameCenterAllowed`|Boolean|Optional. Set to `false` to disable Game Center.|
|`GKFeatureAccountModificationAllowed`|Boolean|Optional. Set to `false` to disable account modifications.|
|`GKFeatureAddingGameCenterFriendsAllowed`|Boolean|Optional. Set to `false` to disable adding Game Center friends.|
|`GKFeatureMultiplayerGamingAllowed`|Boolean|Optional. Set to `false` to disable multiplayer gaming.|
  
  

### Additional Parental Controls  

 [Configuration Profile Reference - Additional Parental Controls](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW103)  

Additional parental control functions can be found in the following payloads:  


* [System Policy Control Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW21)  

* [Email Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW11)  

* [Media Management](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW104)  

* [AppStore Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW197)  

* [Dock Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW327)  
  
  
