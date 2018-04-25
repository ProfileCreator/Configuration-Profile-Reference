# App-to-Per-App VPN Mapping  

 [Configuration Profile Reference - App-to-Per-App VPN Mapping](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW40)  

The App-to-Per-App mapping payload is designated by specifying `com.apple.vpn.managed.appmapping` as the `PayloadType` value.  

This payload is supported only in macOS 10.9 and later. It is not supported in iOS.  

|Key|Type|Value|
|-|-|-|
|`AppLayerVPNMapping`|Array of Dictionaries|An array of mapping dictionaries.|
  

Each dictionary in the array can contain the following keys:  

|Key|Type|Value|
|-|-|-|
|`Identifier`|String|The app’s bundle ID.|
|`VPNUUID`|String|The VPNUUID of the Per-App VPN defined in a Per-App VPN payload.|
|`DesignatedRequirement`|String|The code signature designated requirement of the app that will use the per-app VPN. |
|`SigningIdentifier`|String|The code signature signing identifier of the app that will use the per-app VPN. |
  
