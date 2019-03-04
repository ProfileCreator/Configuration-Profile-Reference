# DNS Proxy Payload  

 [Configuration Profile Reference - DNS Proxy Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW61)  

The DNS Proxy payload is designated by specifying `com.apple.dnsProxy.managed` as the `PayloadType`. This payload can be installed only on a Supervised device.  

This payload sets up iOS DNS Proxy settings. It is supported on iOS 11 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`AppBundleIdentifier`|String|Required. Bundle identifer of the app containing the DNS proxy network extension.|
|`ProviderBundleIdentifier`|String|Optional. Bundle identifier of the DNS proxy network extension to use. Useful for apps that contain more than one DNS proxy extension.|
|`ProviderConfiguration`|Dictionary|Optional. Dictionary of vendor-specific configuration items.|
  
