# Home Screen Layout Payload  

 [Configuration Profile Reference - Home Screen Layout Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW603)  

The Home Screen Layout Payload is designated by specifying `com.apple.homescreenlayout` as the `PayloadType` value. It can contain only one payload, which must be supervised. It is supported on the User Channel.  

This payload defines a layout of apps, folders, and web clips for the Home screen. It is supported on iOS 9.3 and later.  


> **Note:** 
If a home screen layout puts more than six items in the iPad dock the location of the seventh and succeeding items may be undefined but they will not be omitted.  
  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`Dock`|Array|Optional. An array of dictionaries, each of which must conform to the icon dictionary format.|
|`Pages`|Array|Required. An array of dictionaries, each of which must conform to the icon dictionary format.|
  

Icon format dictionaries are defined as follows:  

|Key|Type|Value|
|-|-|-|
|`Type`|String|Required. Must be one of the following:</br></br>* Application  </br></br>* Folder  </br></br>|
|`DisplayName`|String|Optional. Human-readable string to be shown to the user.|
|`BundleID`|String|Required if App type. The bundle identifier of the app.|
|`Pages`|Array|Optional. Array of arrays of dictionaries. Each of the dictionaries complies to the icon dictionary format.|
  
