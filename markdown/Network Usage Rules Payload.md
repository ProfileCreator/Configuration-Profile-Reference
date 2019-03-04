# Network Usage Rules Payload  

 [Configuration Profile Reference - Network Usage Rules Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW9a)  

The Network Usage Rules payload is designated by specifying `com.apple.networkusagerules` as the `PayloadType` value.  

Network Usage Rules allow enterprises to specify how managed apps use networks, such as cellular data networks. These rules only apply to managed apps.  

In addition to the settings common to all payloads, this payload defines this key:  

|Key|Type|Value|
|-|-|-|
|`ApplicationRules`|Array of Dictionaries|Required.|
  

Each entry in the `ApplicationRules` array must be a dictionary containing these keys:  

|Key|Type|Value|
|-|-|-|
|`AppIdentifierMatches`|Array|Optional. A list of managed app identifiers, as strings, that must follow the associated rules. If this key is missing, the rules will apply to all managed apps on the device.</br>Each string in the `AppIdentifierMatches` array may either be an exact app identifier match, e.g. `com.mycompany.myapp`, or it may specify a prefix match for the Bundle ID by using the * wildcard character. The wildcard character, if used, must appear after a period character (.), and may only appear once, at the end of the string, e.g. `com.mycompany.*`.|
|`AllowRoamingCellularData`|Boolean|Optional. Default `true`. If set to `false`, matching managed apps will not be allowed to use cellular data when roaming.|
|`AllowCellularData`|Boolean|Optional. Default `true`. If set to `false`, matching managed apps will not be allowed to use cellular data at any time.|
  
