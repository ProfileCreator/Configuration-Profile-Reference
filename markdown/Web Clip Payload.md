# Web Clip Payload  

 [Configuration Profile Reference - Web Clip Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW12)  

The Web Clip payload is designated by specifying `com.apple.webClip.managed` as the `PayloadType` value.  

A Web Clip payload provides a web clipping on the user’s home screen as though the user had saved a bookmark to the home screen.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`URL`|String|The URL that the Web Clip should open when clicked. The URL must begin with HTTP or HTTPS or it won't work.|
|`Label`|String|The name of the Web Clip as displayed on the Home screen.|
|`Icon`|Data|Optional. A PNG icon to be shown on the Home screen. Should be 59 x 60 pixels in size. If not specified, a white square will be shown.|
|`IsRemovable`|Boolean|Optional. If `false`, the web clip is unremovable. Defaults to `true`. Not available in macOS.|
  
