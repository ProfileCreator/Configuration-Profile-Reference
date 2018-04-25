# Screensaver  

 [Configuration Profile Reference - Screensaver](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW60)  

The device level screensaver payload can be used to enable or disable the screen lock password function and one of the ways of disabling the option. Screensaver payloads are designated by specifying `com.apple.screensaver` as the `PayloadType`.  

The Screensaver payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`askForPassword`|Boolean|Optional. If set to `true`, the user will be prompted for a password when the screensaver is unlocked or stopped.</br>**Availability:** Available in macOS 10.13 and later.|
|`askForPasswordDelay`|Integer|Optional. Number of seconds to delay before the password will be required to unlock or stop the screen saver (the "grace period").   A value of 2147483647 (eg 0x7FFFFFFF) can be used to disable this requirement, and on 10.13, the payload is one of the only ways of disabling the feature.  Note that the `askForPassword` must still be set to `true` to use this option.</br>**Availability:** Available in macOS 10.13 and later. |
|`loginWindowModulePath`|String|Optional. A full path to the screen saver module to be used. </br>**Availability:** Available in macOS 10.11 and later.|
|`loginWindowIdleTime`|Integer|Optional. Number of seconds of inactivity before screensaver activates. (0=never activate).</br>**Availability:** Available in macOS 10.11 and later. |
  

The user level screensaver settings are specific to a user, instead of the device. The user level screensaver payloads are designated by specifying `com.apple.screensaver.user` as the `PayloadType`.  

The Screensaver User payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`modulePath`|String|Optional. A full path to the screen saver module to be used. </br>**Availability:** Available in macOS 10.11 and later.|
|`idleTime`|Integer|Optional. Number of seconds of inactivity before screensaver activates. (0=never activate).</br>**Availability:** Available in macOS 10.11 and later. |
  
