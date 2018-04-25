# Per-App VPN Payload  

 [Configuration Profile Reference - Per-App VPN Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW37)  

The Per-App VPN payload is used for configuring add-on VPN software, and it works only on VPN services of type 'VPN'. It should not be confused with the standard VPN payload, described in [VPN Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27).  

This payload is supported only in iOS 7.0 and later and macOS v10.9 and later.  

The VPN payload is designated by specifying `com.apple.vpn.managed.applayer` as the `PayloadType` value. The Per-App VPN payload supports all of the keys described in [VPN Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27) plus the following additional keys:  

|Key|Type|Value|
|-|-|-|
|`VPNUUID`|String|A globally-unique identifier for this VPN configuration. This identifier is used to configure apps so that they use the Per-App VPN service for all of their network communication. See [App-to-Per-App VPN Mapping](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW40).|
|`SafariDomains`|Array|This optional key is a special case of App-to-Per App VPN Mapping. It sets up the app mapping for Safari (Webkit) with a specific identifier and a designated requirement.</br>The array contains strings, each of which is a domain that should trigger this VPN connection in Safari. The rule matching behavior is as follows:</br></br>* Before being matched against a host, all leading and trailing dots are stripped from the domain string. For example, if the domain string is `".com"` the domain string used to match is `"com"`.  </br></br>* Each label in the domain string must match an entire label in the host string. For example, a domain of `"example.com"` matches `"www.example.com"`, but not `"foo.badexample.com"`.  </br></br>* Domain strings with only one label must match the entire host string. For example, a domain of `"com"` matches `"com"`, not `"www.example.com"`.  </br></br>|
|`OnDemandMatchAppEnabled`|Boolean|This key is placed in the VPN payload sub-dictionary.</br>If `true`, the Per-App VPN connection starts automatically when apps linked to this Per-App VPN service initiate network communication.</br>If `false`, the Per-App VPN connection must be started manually by the user before apps linked to this Per-App VPN service can initiate network communication.</br>If this key is not present, the value of the `OnDemandEnabled` key is used to determine the status of Per-App VPN On Demand.|
  

### VPN Dictionary Keys  

 [Configuration Profile Reference - VPN Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW37)  

In addition to the VPN Dictionary keys defined in the com.apple.vpn.managed payload, the VPN Dictionary within the com.apple.vpn.managed.applayer payload can also contain the following keys:  

|Key|Type|Value|
|-|-|-|
|`ProviderType`|String|Optional. Either `packet-tunnel` or `app-proxy`. The default is `app-proxy`. If the value of this key is `app-proxy`, then the VPN service will tunnel traffic at the application layer. If the value of this key is `packet-tunnel`, then the VPN service will tunnel traffic at the IP layer.|
  
  
