# AirPlay Security Payload  

 [Configuration Profile Reference - AirPlay Security Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW56)  

The AirPlay Security payload locks the Apple TV to a particular style of AirPlay Security. The AirPlay Security payload is designated by specifying `com.apple.airplay.security` as the `PayloadType` vaue.  

This payload is supported on tvOS 11.0 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`SecurityType`|String|Required. Must be one of the defined values: `NONE`, `PASSCODE_ONCE`, `PASSCODE_ALWAYS`, or `PASSWORD`.</br>`NONE` will allow any incoming AirPlay connection without challenge. Only allowed if `AccessType` is `WIFI_ONLY`.</br>`PASSCODE_ONCE` will require an on-screen passcode to be entered upon the first connection.</br>`PASSCODE_ALWAYS` will require an on-screen passcode to be entered upon every AirPlay connection.</br>`PASSWORD` will require a passphrase to be entered as specified in the Password key. The Password key is required if this `SecurityType` is selected.|
|`AccessType`|String|Required. Must be one of the defined values: `ANY` or `WIFI_ONLY`.</br>`ANY` allows connections from both Ethernet/WiFi and AWDL.</br>`WIFI_ONLY` allows connections only from devices on the same Ethernet/WiFi network as the Apple TV.|
|`Password`|String|Optional. The AirPlay password. Required if `SecurityType` is `PASSWORD`.|
  
