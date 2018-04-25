# Conference Room Display Payload  

 [Configuration Profile Reference - Conference Room Display Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW325)  

The Conference Room Display payload is designated by specifying `com.apple.conferenceroomdisplay` as the `PayloadType`.  

It configures an Apple TV to enter Conference Room Display mode and restricts exit from that mode. It is supported on supervised devices running tvOS 10.2 or later.  

In addition to the settings common to all payloads, this payload defines the following key:  

|Key|Type|Value|
|-|-|-|
|`Message`|String|Optional. A custom message displayed on the screen in Conference Room Display mode.|
  
