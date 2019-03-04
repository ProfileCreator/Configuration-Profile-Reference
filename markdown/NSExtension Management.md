# NSExtension Management  

 [Configuration Profile Reference - NSExtension Management](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW70)  

The NSExtension payload is designated by specifying `com.apple.NSExtension` as the `PayloadType`.  

This payload specifies which NSExtensions are allowed or disallowed on a system. Extensions can be managed by bundleID in whitelists and blacklists or by a blacklist of extension points.  

It is supported on macOS 10.13 and later.  

In addition to the settings common to all payloads, this payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`AllowedExtensions`|Array|Optional. Array of extension identifiers for extensions that are allowed to run on the system.|
|`DeniedExtensions`|Array|Optional. Array of extension identifiers for extensions that are not allowed to run on the system.|
|`DeniedExtensionPoints`|Array|Optional. Array of NSExtension extension points for extensions that are not allowed to run on the system.|
  
