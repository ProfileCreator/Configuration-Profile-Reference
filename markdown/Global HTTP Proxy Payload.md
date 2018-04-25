# Global HTTP Proxy Payload  

 [Configuration Profile Reference - Global HTTP Proxy Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW34)  

The Global HTTP Proxy payload is designated by specifying `com.apple.proxy.http.global` as the `PayloadType`.  

This payload allows you to specify global HTTP proxy settings.  

There can only be one of this payload at any time. This payload can only be installed on a supervised device.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`ProxyType`|String|If you choose manual proxy type, you need the proxy server address including its port and optionally a username and password into the proxy server. If you choose auto proxy type, you can enter a proxy autoconfiguration (PAC) URL.|
|`ProxyServer`|String|The proxy server’s network address.|
|`ProxyServerPort`|Integer|The proxy server’s port|
|`ProxyUsername`|String|Optional. The username used to authenticate to the proxy server.|
|`ProxyPassword`|String|Optional. The password used to authenticate to the proxy server.|
|`ProxyPACURL`|String|Optional. The URL of the PAC file that defines the proxy configuration.|
|`ProxyPACFallbackAllowed`|Boolean|Optional. If `false`, prevents the device from connecting directly to the destination if the PAC file is unreachable. Default is `false`.</br>**Availability:** Available in iOS 7 and later.|
|`ProxyCaptiveLoginAllowed`|Boolean|Optional. If `true`, allows the device to bypass the proxy server to display the login page for captive networks. Default is `false`.</br>**Availability:** Available in iOS 7 and later.|
  

If the `ProxyType` field is set to `Auto` and no `ProxyPACURL` value is specified, the device uses the web proxy autodiscovery protocol (WPAD) to discover proxies.  
