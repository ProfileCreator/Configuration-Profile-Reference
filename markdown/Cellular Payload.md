# Cellular Payload  

 [Configuration Profile Reference - Cellular Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW48)  

A cellular payload configures cellular network settings on the device. It is not supported on macOS. On iOS 7 and later, a cellular payload is designated by specifying `com.apple.cellular` as the `PayloadType` value. Cellular payloads have two important installation requirements:  


* No more than one cellular payload can be installed at any time.  

* A cellular payload cannot be installed if an APN payload is already installed.  
  

This payload replaces the `com.apple.managedCarrier` payload, which is supported, but deprecated.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`AttachAPN`|Dictionary|Optional. An `AttachAPN` configuration dictionary, described below.|
|`APNs`|Array|Optional. An array of APN dictionaries, described below. Only the first entry is currently used.|
  

The `AttachAPN` dictionary contains the following keys:  

|Key|Type|Value|
|-|-|-|
|`Name`|String|Required. The Access Point Name.|
|`AuthenticationType`|String|Optional. Must contain either `CHAP` or `PAP`. Defaults to `PAP`.
|
|`Username`|String|Optional. A user name used for authentication.|
|`Password`|String|Optional. A password used for authentication.|
  

Each `APN` dictionary contains the following keys:  

|Key|Type|Value|
|-|-|-|
|`Name`|String|Required. The Access Point Name.|
|`AuthenticationType`|String|Optional. Must contain either `CHAP` or `PAP`. Defaults to `PAP`.
|
|`Username`|String|Optional. A user name used for authentication.|
|`Password`|String|Optional. A password used for authentication.|
|`ProxyServer`|String|Optional. The proxy server's network address.|
|`ProxyServerPort`|Number|Optional. The proxy server's port.|
  
