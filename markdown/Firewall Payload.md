# Firewall Payload  

 [Configuration Profile Reference - Firewall Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW443)  

Available in macOS 10.12 and later. A Firewall payload manages the Application Firewall settings accessible in the Security Preferences pane. Note these restrictions:  


* The payload must exist in a system-scoped profile.  

* If more than one profile contains this payload, the most restrictive union of settings will be used.  

* The "Automatically allow signed downloaded software" and "Automatically allow built-in software" options are not supported, but both will be forced ON when this payload is present.  
  

This payload is designated by specifying `com.apple.security.firewall` as the `PayloadType` value.  

The Firewall payload contains the following keys:  

|Key|Type|Value|
|-|-|-|
|`EnableFirewall`|Boolean|Required. Whether the firewall should be enabled or not.|
|`BlockAllIncoming`|Boolean|Optional. Corresponds to the “Block all incoming connections” option.|
|`EnableStealthMode`|Boolean|Optional. Corresponds to “Enable stealth mode.”|
|`Applications`|Array of dictionaries|Optional. The list of applications. Each dictionary contains these keys:</br></br>* `BundleID` (string) : identifies the application  </br></br>* `Allowed` (Boolean) : specifies whether or not incoming connections are allowed  </br></br>|
  
