# AirPlay Payload  

 [Configuration Profile Reference - AirPlay Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW38)  

The AirPlay payload is designated by specifying `com.apple.airplay` as the `PayloadType` value.  

This payload is supported on iOS 7.0 and later and on macOS 10.10 and later.  

|Key|Type|Value|
|-|-|-|
|`Whitelist`|Array of dictionaries|Optional. Supervised only (ignored otherwise). If present, only AirPlay destinations present in this list are available to the device.</br>The dictionary format is described below.|
|`Passwords`|Array of dictionaries|Optional. If present, sets passwords for known AirPlay destinations. The dictionary format is described below.|
  

Each entry in the `Whitelist` array is a dictionary that can contain the following fields:  

|Key|Type|Value|
|-|-|-|
|`DeviceID`|String|The Device ID of the AirPlay destination, in the format `xx:xx:xx:xx:xx:xx`. This field is not case sensitive.|
  

Each entry in the `Passwords` array is a dictionary that contains the following fields:  

|Key|Type|Value|
|-|-|-|
|`DeviceName`|String|The name of the AirPlay destination (used on iOS).|
|`DeviceID`|String|The `DeviceID` of the AirPlay destination (used on macOS).|
|`Password`|String|The password for the AirPlay destination.|
  
