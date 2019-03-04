# TV Remote Payload  

 [Configuration Profile Reference - TV Remote Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW69)  

The TV Remote payload is designated by specifying `com.apple.tvremote` as the `PayloadType` value.   

This payload allows restricting the connections from the Apple TV Remote app to an Apple TV and restricting the available Apple TV devices in the Apple TV Remote app.  

To lock specific Apple TVs to specific devices running Apple TV Remote app, both the Apple TVs and remote devices can be specified in the same payload.  

In addition to the settings common to all payload types, the TV Remote payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`AllowedRemotes`|Array of Dictionaries|If present, the Apple TV will only connect with the Apple TV Remote app from the devices specified.</br>If not present, or the list is empty, any device will be allowed to connect.</br>**Availability:** Available in tvOS 11.3 and later.|
|`AllowedTVs`|Array of Dictionaries|If present, the Apple TV Remote app will only connect to the specified Apple TVs.</br>If not present, or the list is empty, the device will be able to connect to any Apple TV.</br>**Availability:** Available in iOS 11.3 and later.|
  

Each entry in the `AllowedRemotes` array is a dictionary that can contain the following key:  

|Key|Type|Value|
|-|-|-|
|`RemoteDeviceID`|String|The MAC address of a permitted iOS device that can control this Apple TV. </br>Use the format “xx:xx:xx:xx:xx:xx”. The field is not case sensitive.</br>**Availability:** Available in tvOS 11.3 and later.|
  

Each entry in the `AllowedTVs` array is a dictionary that can contain the following key:  

|Key|Type|Value|
|-|-|-|
|`TVDeviceID`|String|The MAC address of an Apple TV device that this iOS device is permitted to control. </br>Use the format “xx:xx:xx:xx:xx:xx”. The field is not case sensitive.</br>**Availability:** Available in iOS 11.3 and later.|
  
