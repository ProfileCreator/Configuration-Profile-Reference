# Notifications Payload  

 [Configuration Profile Reference - Notifications Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW604)  

The Notifications Payload is designated by specifying `com.apple.notificationsettings` as the `PayloadType` value. It can contain only one payload, which must be installed on supervised devices. It is supported on the User Channel.  

This payload specifies the restriction enforced notification settings for apps, using their bundle identifiers. It is supported on iOS 9.3 and later.  

In addition to the settings common to all payloads, this payload defines the following key:  

|Key|Type|Value|
|-|-|-|
|`NotificationSettings`|Array|Required. An array of dictionaries, each of which specifies notification settings for one bundle identifier.|
  

Each entry in the NotificationSettings field contains the following dictionary:  

|Key|Type|Value|
|-|-|-|
|`BundleIdentifier`|String|Required. Bundle identifier of app to which to apply these notification settings.|
|`NotificationsEnabled`|Boolean|Optional. Whether notifications are allowed for this app. Default is `true`.|
|`ShowInNotificationCenter`|Boolean|Optional. Whether notifications can be shown in notification center. Default is `true`.|
|`ShowInLockScreen`|Boolean|Optional. Whether notifications can be shown in the lock screen. Default is `true`.|
|`AlertType`|Integer|Optional. The type of alert for notifications for this app:</br></br>* 0: None  </br></br>* 1: Banner  </br></br>* 2: Modal Alert  </br></br></br>Default is 1.|
|`BadgesEnabled`|Boolean|Optional. Whether badges are allowed for this app. Default is `true`.|
|`SoundsEnabled`|Boolean|Optional. Whether sounds are allowed for this app. Default is `true`.|
  
