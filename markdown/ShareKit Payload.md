# ShareKit Payload  

 [Configuration Profile Reference - ShareKit Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW642)  

MacOS 10.9 or later only. The ShareKit Payload is designated by specifying `com.apple.com.apple.ShareKitHelper` as the `PayloadType` value. It can contain only one payload. It is supported on the User Channel.  

The ShareKit Payload specifies which ShareKit plugin can be accessed on client.  Both allow and disallow lists can be specified.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`SHKAllowedShareServices`|Array of Strings|Optional. List of plugin IDs that will show up in the user’s Share menu. If this array exists then only these items will be permitted.|
|`SHKDeniedShareServices`|Array of Strings|Optional. List of plugin IDs that will not show up in the user’s Share menu. This key is used only if there is no `SHKAllowedShareServices` key.|
  

The following plugin IDs are supported by this payload:  


* "com.apple.share.AirDrop": AirDrop  

* "com.apple.share.Facebook": Facebook  

* "com.apple.share.Twitter": Twitter  

* "com.apple.share.Mail": Mail  

* "com.apple.share.Messages": Messages  

* "com.apple.share.Video": Video Services  

* "com.apple.share.addtoiphoto": Photos  

* "com.apple.share.addtoaperture": Aperture  

* "com.apple.share.readlater": Reading List  

* "com.apple.share.SinaWeibo": Sina Weibo  

* "com.apple.Notes.SharingExtension": Notes  

* "com.apple.reminders.RemindersShareExtension": Reminders  

* "com.apple.share.LinkedIn.post": LinkedIn  
  
