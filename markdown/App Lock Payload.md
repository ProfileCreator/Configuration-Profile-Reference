# App Lock Payload  

 [Configuration Profile Reference - App Lock Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW35)  

The App Lock payload is designated by specifying `com.apple.app.lock` as the `PayloadType` value. Only one of this payload type can be installed at any time. This payload can be installed only on a Supervised device.  

By installing an app lock payload, the device is locked to a single application until the payload is removed. The home button is disabled, and the device returns to the specified application automatically upon wake or reboot.  


> **Note:** 
You can’t update any app while the device is locked in Single App Mode. You need to exit Single App Mode long enough to update apps as needed. During that time you should restrict the visible apps as much as possible, except for Settings and Phone and any other apps that cannot be blacklisted.  
  

This payload is supported only in iOS 6.0 and later.  

The payload contains the following key:  

|Key|Type|Value|
|-|-|-|
|`App`|Dictionary|A dictionary containing information about the app.|
  

The `App` dictionary, in turn, contains the following key:  

|Key|Type|Value|
|-|-|-|
|`Identifier`|String|The bundle identifier of the application.|
|`Options`|Dictionary|Optional. Described below.</br>**Availability:** Available only in iOS 7.0 and later.|
|`UserEnabledOptions`|Dictionary|Optional. Described below.</br>**Availability:** Available only in iOS 7.0 and later.|
  

The `Options` dictionary, if present, can contain the following keys (in iOS 7.0 and later):  

|Key|Type|Value|
|-|-|-|
|`DisableTouch`|Boolean|Optional. If `true`, the touch screen is disabled. Default is `false`. Available in tvOS 10.2 and later.|
|`DisableDeviceRotation`|Boolean|Optional. If `true`, device rotation sensing is disabled. Default is `false`.|
|`DisableVolumeButtons`|Boolean|Optional. If `true`, the volume buttons are disabled. Default to `false`.|
|`DisableRingerSwitch`|Boolean|Optional. If `true`, the ringer switch is disabled. Default is `false`.</br>When disabled, the ringer behavior depends on what position the switch was in when it was first disabled.|
|`DisableSleepWakeButton`|Boolean|Optional. If `true`, the sleep/wake button is disabled. Default is `false`.|
|`DisableAutoLock`|Boolean|Optional. If `true`, the device will not automatically go to sleep after an idle period. Available in tvOS 10.2 and later.|
|`EnableVoiceOver`|Boolean|Optional. If `true`, VoiceOver is turned on. Default is `false`. Available in tvOS 10.2 and later.|
|`EnableZoom`|Boolean|Optional. If `true`, Zoom is turned on. Default is `false`. Available in tvOS 10.2 and later.|
|`EnableInvertColors`|Boolean|Optional. If `true`, Invert Colors is turned on. Default is `false`. Available in tvOS 10.2 and later.|
|`EnableAssistiveTouch`|Boolean|Optional. If `true`, AssistiveTouch is turned on. Default is `false`.|
|`EnableSpeakSelection`|Boolean|Optional. If `true`, Speak Selection is turned on. Default is `false`.|
|`EnableMonoAudio`|Boolean|Optional. If `true`, Mono Audio is turned on. Default is `false`.|
  

The `UserEnabledOptions` dictionary, if present, can contain the following keys (in iOS 7.0 and later):  

|Key|Type|Value|
|-|-|-|
|`VoiceOver`|Boolean|Optional. If `true`, allow VoiceOver adjustment. Default is `false`.|
|`Zoom`|Boolean|Optional. If `true`, allow Zoom adjustment. Default is `false`.|
|`InvertColors`|Boolean|Optional. If `true`, allow Invert Colors adjustment. Default is `false`.|
|`AssistiveTouch`|Boolean|Optional. If `true`, allow AssistiveTouch adjustment. Default is `false`.|
  
