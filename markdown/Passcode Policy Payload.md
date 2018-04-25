# Passcode Policy Payload  

 [Configuration Profile Reference - Passcode Policy Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW9)  

The Passcode Policy payload is designated by specifying `com.apple.mobiledevice.passwordpolicy` as the `PayloadType` value.  

The presence of this payload type prompts an iOS or macOS device to present the user with an alphanumeric passcode entry mechanism, which allows the entry of arbitrarily long and complex passcodes.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`allowSimple`|Boolean|Optional. Default `true`. Determines whether a simple passcode is allowed. A simple passcode is defined as containing repeated characters, or increasing/decreasing characters (such as 123 or CBA). Setting this value to `false` is synonymous to setting minComplexChars to "1".|
|`forcePIN`|Boolean|Optional. Default NO. Determines whether the user is forced to set a PIN. Simply setting this value (and not others) forces the user to enter a passcode, without imposing a length or quality.|
|`maxFailedAttempts`|Number|Optional. Default 10 (iOS only). Allowed range [1...10]. Specifies the number of allowed failed attempts to enter the passcode at the device's lock screen. Once this number is exceeded, the device is locked and must be connected to its designated iTunes in order to be unlocked.|
|`maxInactivity`|Number|Optional. Default Infinity. Specifies the number of minutes for which the device can be idle (without being unlocked by the user) before it gets locked by the system. Once this limit is reached, the device is locked and the passcode must be entered.</br>In macOS, this will be translated to screensaver settings.|
|`maxPINAgeInDays`|Number|Optional. Default Infinity. Specifies the number of days for which the passcode can remain unchanged. After this number of days, the user is forced to change the passcode before the device is unlocked.|
|`minComplexChars`|Number|Optional. Default 0. Specifies the minimum number of complex characters that a passcode must contain. A "complex" character is a character other than a number or a letter, such as &%$#.|
|`minLength`|Number|Optional. Default 0. Specifies the minimum overall length of the passcode. This parameter is independent of the also optional minComplexChars argument.|
|`requireAlphanumeric`|Boolean|Optional. Default NO. Specifies whether the user must enter alphabetic characters ("abcd"), or if numbers are sufficient.|
|`pinHistory`|Number|Optional. When the user changes the passcode, it has to be unique within the last N entries in the history. Minimum value is 1, maximum value is 50.|
|`maxGracePeriod`|Number|Optional. The maximum grace period, in minutes, to unlock the phone without entering a passcode. Default is 0, that is no grace period, which requires a passcode immediately.</br>In macOS, this will be translated to screensaver settings.|
|`allowFingerprintModification`|Boolean|Optional. Supervised only. Not supported on macOS. Allows the user to modify Touch ID. Default NO.|
|`changeAtNextAuth`|Boolean|Optional. On macOS, setting this to `true` will cause a password reset to occur the next time the user tries to authenticate.  If this key is set in a device profile, the setting takes effect for all users, and admin authentications may fail until the admin user password is also reset.</br>**Availability:** Available in macOS 10.13 and later.|
  
