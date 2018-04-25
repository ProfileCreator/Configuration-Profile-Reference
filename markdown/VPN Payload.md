# VPN Payload  

 [Configuration Profile Reference - VPN Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27)  

The VPN payload is used for traditional systemwide VPNs based on L2TP, PPTP, and IPSec. This payload should not be confused with the Per-App VPN, described in [Per-App VPN Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW37).  

The VPN payload is designated by specifying `com.apple.vpn.managed` as the `PayloadType` value. In addition to the settings common to all payload types, the VPN payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`UserDefinedName`|String|Optional. Description of the VPN connection displayed on the device.|
|`OverridePrimary`|Boolean|Specifies whether to send all traffic through the VPN interface. If `true`, all network traffic is sent over VPN. Defaults to `false`.|
|`VPNType`|String|Determines the settings available in the payload for this type of VPN connection. It can have one of the following values:</br></br>* `L2TP`  </br></br>* `PPTP`  </br></br>* `IPSec` (Cisco)  </br></br>* `IKEv2` (see [IKEv2 Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW612))  </br></br>* `AlwaysOn` (see [AlwaysOn VPN Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW613))  </br></br>* `VPN` (solution uses a VPN plugin or `NetworkExtension`, so the `VPNSubType` key is required (see below)).  </br></br>* Cisco AnyConnect: `com.cisco.anyconnect.applevpn.plugin`  </br></br>* Juniper SSL: `net.juniper.sslvpn`  </br></br>* F5 SSL: `com.f5.F5-Edge-Client.vpnplugin`  </br></br>* SonicWALL Mobile Connect: `com.sonicwall.SonicWALL-SSLVPN.vpnplugin`  </br></br>* Aruba VIA: `com.arubanetworks.aruba-via.vpnplugin`  </br></br>|
|`VPNSubType`|String|Optional. If `VPNType` is `VPN`, this field is required. If the configuration is targeted at a VPN solution that uses a VPN plugin, then this field contains the bundle identifier of the plugin. Here are some examples:</br></br>* `L2TP`  </br></br>* `PPTP`  </br></br>* `IPSec` (Cisco)  </br></br>* `IKEv2` (see [IKEv2 Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW612))  </br></br>* `AlwaysOn` (see [AlwaysOn VPN Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW613))  </br></br>* `VPN` (solution uses a VPN plugin or `NetworkExtension`, so the `VPNSubType` key is required (see below)).  </br></br>* Cisco AnyConnect: `com.cisco.anyconnect.applevpn.plugin`  </br></br>* Juniper SSL: `net.juniper.sslvpn`  </br></br>* F5 SSL: `com.f5.F5-Edge-Client.vpnplugin`  </br></br>* SonicWALL Mobile Connect: `com.sonicwall.SonicWALL-SSLVPN.vpnplugin`  </br></br>* Aruba VIA: `com.arubanetworks.aruba-via.vpnplugin`  </br></br></br>If the configuration is targeted at a VPN solution that uses a `NetworkExtension` provider, then this field contains the bundle identifier of the app that contains the provider. Contact the VPN solution vendor for the value of the identifier.</br>If `VPNType` is `IKEv2`, then the `VPNSubType` field is optional and is reserved for future use. If it is specified, it must contain the empty string.|
|`ProviderBundleIdentifier`|String|Optional. If the `VPNSubType` field contains the bundle identifier of an app that contains multiple VPN providers of the same type (`app-proxy` or `packet-tunnel`), then this field is used to specify which provider to use for this configuration.|
|If `VPNType` is `VPN`, `IPSec`, or `IKEv2`, the following keys may be defined in the corresponding `VPN`, `IPSec`, or `IKEv2` dictionaries to configure VPN On Demand:|
|`OnDemandEnabled`|Integer|`1` if the VPN connection should be brought up on demand, else `0`.|
|`OnDemandMatchDomainsAlways`|Array of Strings|*Deprecated.* A list of domain names. In versions of iOS prior to iOS 7, if the hostname ends with one of these domain names, the VPN is started automatically.</br>In iOS 7 and later, if this key is present, the associated domain names are treated as though they were associated with the `OnDemandMatchDomainsOnRetry` key.</br>This behavior can be overridden by `OnDemandRules`.|
|`OnDemandMatchDomainsNever`|Array of Strings|*Deprecated.* A list of domain names. If the hostname ends with one of these domain names, the VPN is *not* started automatically. This might be used to exclude a subdomain within an included domain.</br>This behavior can be overridden by `OnDemandRules`.</br>In iOS 7 and later, this key is deprecated (but still supported) in favor of `EvaluateConnection` actions in the `OnDemandRules` dictionaries.|
|`OnDemandMatchDomainsOnRetry`|Array of Strings|*Deprecated.* A list of domain names. If the hostname ends with one of these domain names, if a DNS query for that domain name fails, the VPN is started automatically.</br>This behavior can be overridden by `OnDemandRules`.</br>In iOS 7 and later, this key is deprecated (but still supported) in favor of `EvaluateConnection` actions in the `OnDemandRules` dictionaries.|
|`OnDemandRules`|Array of Dictionaries|Determines when and how an on-demand VPN should be used. See [On Demand Rules Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW36) for details.|
|If `VPNType` is not `AlwaysOn`, the following key may be defined:|
|`VendorConfig`|Dictionary|A dictionary for configuration information specific to a given third-party VPN solution.|
  

There are two possible dictionaries present at the top level, under the keys "PPP" and "IPSec". The keys inside these two dictionaries are described below, along with the VPNType value under which the keys are used.  

### PPP Dictionary Keys  

 [Configuration Profile Reference - PPP Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27)  

The following elements are for VPN payloads of type PPP.  

|Key|Type|Value|
|-|-|-|
|`AuthName`|String|The VPN account user name. Used for L2TP and PPTP.|
|`AuthPassword`|String|Optional. Only visible if TokenCard is `false`. Used for L2TP and PPTP.|
|`TokenCard`|Boolean|Whether to use a token card such as an RSA SecurID card for connecting. Used for L2TP.|
|`CommRemoteAddress`|String|IP address or host name of VPN server. Used for L2TP and PPTP.|
|`AuthEAPPlugins`|Array|Only present if RSA SecurID is being used, in which case it has one entry, a string with value "EAP-RSA". Used for L2TP and PPTP.|
|`AuthProtocol`|Array|Only present if RSA SecurID is being used, in which case it has one entry, a string with value "EAP". Used for L2TP and PPTP.|
|`CCPMPPE40Enabled`|Boolean|See discussion under `CCPEnabled`. Used for PPTP.|
|`CCPMPPE128Enabled`|Boolean|See discussion under `CCPEnabled`. Used for PPTP.|
|`CCPEnabled`|Boolean|Enables encryption on the connection. If this key and `CCPMPPE40Enabled` are `true`, represents automatic encryption level; if this key and `CCPMPPE128Enabled` are `true`, represents maximum encryption level. If no encryption is used, then none of the CCP keys are `true`. Used for PPTP.|
  
  

### IPSec Dictionary Keys  

 [Configuration Profile Reference - IPSec Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27)  

The following elements are for VPN payloads of type IPSec.  

|Key|Type|Value|
|-|-|-|
|`RemoteAddress`|String|IP address or host name of the VPN server. Used for Cisco IPSec.|
|`AuthenticationMethod`|String|Either `SharedSecret` or `Certificate`. Used for L2TP and Cisco IPSec.|
|`XAuthEnabled`|Integer|`1` if Xauth is on, `0` if it is off. Used for Cisco IPSec.|
|`XAuthName`|String|User name for VPN account. Used for Cisco IPSec.|
|`XAuthPassword`|String|Required for VPN account user authentication. Used for Cisco IPSec.|
|`LocalIdentifier`|String|Present only if `AuthenticationMethod` is `SharedSecret`. The name of the group to use. If Hybrid Authentication is used, the string must end with `[hybrid]`. Used for Cisco IPSec.|
|`LocalIdentifierType`|String|Present only if `AuthenticationMethod` is `SharedSecret`. The value is `KeyID`. Used for L2TP and Cisco IPSec.|
|`SharedSecret`|Data|The shared secret for this VPN account. Only present if `AuthenticationMethod` is `SharedSecret`. Used for L2TP and Cisco IPSec.|
|`PayloadCertificateUUID`|String|The UUID of the certificate to use for the account credentials. Only present if `AuthenticationMethod` is `Certificate`. Used for Cisco IPSec.|
|`PromptForVPNPIN`|Boolean|Tells whether to prompt for a PIN when connecting. Used for Cisco IPSec.|
  
  

### On Demand Rules Dictionary Keys  

 [Configuration Profile Reference - On Demand Rules Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27)  

The `OnDemandRules` key in a VPN payload is associated with an array of dictionaries that define the network match criteria that identify a particular network location.  

In typical use, VPN On Demand matches the dictionaries in the `OnDemandRules` array against properties of your current network connection to determine whether domain-based rules should be used in determining whether to connect, then handles the connection as follows:  


* If domain-based matching is enabled for a matching `OnDemandRules` dictionary, then for each dictionary in that dictionary’s `EvaluateConnection` array, VPN On Demand compares the requested domain against the domains listed in the `Domains` array.  

* If domain-based matching is not enabled, the specified behavior (usually `Connect`, `Disconnect`, or `Ignore`) is used if the dictionary otherwise matches.  
  


> **Note:** For backwards compatibility, VPN On Demand also allows you to specify the `Allow` action, in which case the domains to match are determined by arrays in the VPN payload itself (`OnDemandMatchDomainsAlways`, `OnDemandMatchDomainsOnRetry`, and `OnDemandMatchDomainsNever`). However, this is deprecated in iOS 7.  
  

Whenever a network change is detected, the VPN On Demand service compares the newly connected network against the match network criteria specified in each dictionary (in order) to determine whether VPN On Demand should be allowed or not on the newly joined network. The matching criteria can include any of the following:  


* DNS domain or DNS server settings (with wildcard matching)  

* SSID  

* Interface type  

* reachable server detection  
  

Dictionaries are checked sequentially, beginning with the first dictionary in the array. A dictionary matches the current network only if *all* of the specified policies in that dictionary match. You should always set a default behavior for unknown networks by specifying an action with no matching criteria as the last dictionary in the array.  

If a dictionary matches the current network, a server probe is sent if a URL is specified in the profile. VPN then acts according to the policy defined in the dictionary (for example, allow VPNOnDemand, ignore VPNOnDemand, connect, or disconnect).  


> **Important:** Be sure to set a catch-all value. If you do not, the current default behavior is to allow the connection to occur, but this behavior is not guaranteed.  

>   
  

The `OnDemandRules` dictionaries can contain one or more of the following keys:  

|Key|Type|Value|
|-|-|-|
|`Action`|String|The action to take if this dictionary matches the current network. Possible values are:</br></br>* `Allow`—*Deprecated.* Allow VPN On Demand to connect if triggered.  </br></br>* `Connect`—Unconditionally initiate a VPN connection on the next network attempt.  </br></br>* `Disconnect`—Tear down the VPN connection and do not reconnect on demand as long as this dictionary matches.  </br></br>* `EvaluateConnection`—Evaluate the `ActionParameters` array for each connection attempt.  </br></br>* `Ignore`—Leave any existing VPN connection up, but do not reconnect on demand as long as this dictionary matches.  </br></br>|
|`ActionParameters`|Array of dictionaries|A dictionary that provides rules similar to the `OnDemandRules` dictionary, but evaluated on each connection instead of when the network changes. These dictionaries are evaluated in order, and the behavior is determined by the first dictionary that matches.</br>The keys allowed in each dictionary are described in [Table 1-1](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW41).</br>**Note:** This array is used only for dictionaries in which `EvaluateConnection` is the `Action` value.|
|`DNSDomainMatch`|Array of strings|An array of domain names.
This rule matches if any of the domain names in the specified list matches any domain in the device’s search domains list.</br>A wildcard '*' prefix is supported. For example, `*.example.com` matches against either `mydomain.example.com` or `yourdomain.example.com`.|
|`DNSServerAddressMatch`|Array of strings|An array of IP addresses. This rule matches if any of the network’s specified DNS servers match any entry in the array.</br>Matching with a single wildcard is supported. For example, `17.*` matches any DNS server in the class A 17 subnet.|
|`InterfaceTypeMatch`|String|An interface type. If specified, this rule matches only if the primary network interface hardware matches the specified type.</br>Supported values are `Ethernet`, `WiFi`, and `Cellular`.|
|`SSIDMatch`|Array of strings|An array of SSIDs to match against the current network. If the network is not a Wi-Fi network or if the SSID does not appear in this array, the match fails.</br>Omit this key and the corresponding array to match against any SSID.|
|`URLStringProbe`|String|A URL to probe. If this URL is successfully fetched (returning a `200` HTTP status code) without redirection, this rule matches.|
  

The keys allowed in each `ActionParameters` dictionary are described in .  
### [Table 1-1Keys in the ActionParameters dictionary](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW41)  

|Key|Type|Value|
|-|-|-|
|`Domains`|Array of strings|*Required.* The domains for which this evaluation applies.|
|`DomainAction`|String|*Required.* Defines the VPN behavior for the specified domains. Allowed values are:</br></br>* ConnectIfNeeded—The specified domains should trigger a VPN connection attempt if domain name resolution fails, such as when the DNS server indicates that it cannot resolve the domain, responds with a redirection to a different server, or fails to respond (timeout).  </br></br>* NeverConnect—The specified domains will not trigger a VPN connection nor be accessible through an existing VPN connection.  </br></br>|
|`RequiredDNSServers`|Array of strings|*Optional.* An array of IP addresses of DNS servers to be used for resolving the specified domains. These servers need not be part of the device’s current network configuration. If these DNS servers are not reachable, a VPN connection is established in response. These DNS servers should be either internal DNS servers or trusted external DNS servers.</br>**Note:** This key is valid only if the value of `DomainAction` is `ConnectIfNeeded`.|
|`RequiredURLStringProbe`|String|*Optional.* An `HTTP` or `HTTPS` (preferred) URL to probe, using a `GET` request. If no HTTP response code is received from the server, a VPN connection is established in response.</br>**Note:** This key is valid only if the value of `DomainAction` is `ConnectIfNeeded`.|
  
  

### IKEv2 Dictionary Keys  

 [Configuration Profile Reference - IKEv2 Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27)  

If `VPNType` is `IKEv2`, the following keys may be provided in a dictionary:  

|Key|Type|Value|
|-|-|-|
|`RemoteAddress`|String|Required. IP address or hostname of the VPN server.|
|`LocalIdentifier`|String|Required. Identifier of the IKEv2 client in one of the following formats:</br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `SharedSecret`  </br></br>* `Certificate`  </br></br>* `None`  </br></br>* `RSA` (Default)  </br></br>* `ECDSA256`  </br></br>* `ECDSA384`  </br></br>* `ECDSA521`  </br></br>* `None` (Disable)  </br></br>* `Low` (`keepalive` sent every 30 minutes)  </br></br>* `Medium` (`keepalive` sent every 10 minutes)  </br></br>* `High` (`keepalive` sent every 1 minute)  </br></br>|
|`RemoteIdentifier`|String|Required. Remote identifier in one of the following formats:</br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `SharedSecret`  </br></br>* `Certificate`  </br></br>* `None`  </br></br>* `RSA` (Default)  </br></br>* `ECDSA256`  </br></br>* `ECDSA384`  </br></br>* `ECDSA521`  </br></br>* `None` (Disable)  </br></br>* `Low` (`keepalive` sent every 30 minutes)  </br></br>* `Medium` (`keepalive` sent every 10 minutes)  </br></br>* `High` (`keepalive` sent every 1 minute)  </br></br>|
|`AuthenticationMethod`|String|Required. One of the following:</br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `SharedSecret`  </br></br>* `Certificate`  </br></br>* `None`  </br></br>* `RSA` (Default)  </br></br>* `ECDSA256`  </br></br>* `ECDSA384`  </br></br>* `ECDSA521`  </br></br>* `None` (Disable)  </br></br>* `Low` (`keepalive` sent every 30 minutes)  </br></br>* `Medium` (`keepalive` sent every 10 minutes)  </br></br>* `High` (`keepalive` sent every 1 minute)  </br></br></br>To enable EAP-only authentication, the authentication method should be set to `None` and the `ExtendedAuthEnabled` key should be set to 1. If this key is set to `None` and the `ExtendedAuthEnabled` key is not set, the authentication configuration defaults to `SharedSecret`.|
|`PayloadCertificateUUID`|String|Optional. The UUID of the identity certificate used as the account credential. If the value of `AuthenticationMethod` is `Certificate`, this certificate is sent out for IKEv2 machine authentication. If extended authentication (EAP) is used, it is sent out for EAP-TLS authentication.|
|`CertificateType`|String|Optional. This key specifies the type of `PayloadCertificateUUID` used for IKEv2 machine authentication. Its value is one of the following:</br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `SharedSecret`  </br></br>* `Certificate`  </br></br>* `None`  </br></br>* `RSA` (Default)  </br></br>* `ECDSA256`  </br></br>* `ECDSA384`  </br></br>* `ECDSA521`  </br></br>* `None` (Disable)  </br></br>* `Low` (`keepalive` sent every 30 minutes)  </br></br>* `Medium` (`keepalive` sent every 10 minutes)  </br></br>* `High` (`keepalive` sent every 1 minute)  </br></br></br>If this key is included, the `ServerCertificateIssuerCommonName` key is required.|
|`SharedSecret`|String|Optional. If `AuthenticationMethod` is `SharedSecret`, this value is used for IKE authentication.|
|`ExtendedAuthEnabled`|Integer|Optional. Set to 1 to enable EAP-only authentication (see `AuthenticationMethod`, above). Defaults to 0.|
|`AuthName`|String|Optional. Username used for authentication.|
|`AuthPassword`|String|Optional. Password used for authentication.|
|`DeadPeerDetectionRate`|String|Optional. One of the following:</br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `FQDN`  </br></br>* `UserFQDN`  </br></br>* `Address`  </br></br>* `ASN1DN`  </br></br>* `SharedSecret`  </br></br>* `Certificate`  </br></br>* `None`  </br></br>* `RSA` (Default)  </br></br>* `ECDSA256`  </br></br>* `ECDSA384`  </br></br>* `ECDSA521`  </br></br>* `None` (Disable)  </br></br>* `Low` (`keepalive` sent every 30 minutes)  </br></br>* `Medium` (`keepalive` sent every 10 minutes)  </br></br>* `High` (`keepalive` sent every 1 minute)  </br></br></br>Defaults to Medium.|
|`ServerCertificateIssuerCommonName`|String|Optional. Common Name of the server certificate issuer. If set, this field will cause IKE to send a certificate request based on this certificate issuer to the server.</br>This key is required if both the `CertificateType` key is included and the `ExtendedAuthEnabled` key is set to 1.|
|`ServerCertificateCommonName`|String|Optional. Common Name of the server certificate. This name is used to validate the certificate sent by the IKE server. If not set, the Remote Identifier will be used to validate the certificate.|
|`TLSMinimumVersion`|String|Optional. The minimum TLS version to be used with EAP-TLS authentication. Value may be 1.0, 1.1, or 1.2. If no value is specified, the default minimum is 1.0. **Availability:** Available in iOS 11.0 and macOS 10.13 and later.|
|`TLSMaximumVersion`|String|Optional. The maximum TLS version to be used with EAP-TLS authentication. Value may be 1.0, 1.1, or 1.2. If no value is specified, the default maximum is 1.2. **Availability:** Available in iOS 11.0 and macOS 10.13 and later.|
|`NATKeepAliveOffloadEnable`|Integer|Optional. Set to 1 to enable or 0 to disable NAT Keepalive offload for Always On VPN IKEv2 connections. Keepalive packets are sent by the device to maintain NAT mappings for IKEv2 connections that have a NAT on the path. Keepalive packets are sent at regular interval when the device is awake. If `NATKeepAliveOffloadEnable` is set to 1, Keepalive packets will be offloaded to hardware while the device is asleep. NAT Keepalive offload has an impact on the battery life since extra workload is added during sleep. The default interval for the Keepalive offload packets is 20 seconds over WiFi and 110 seconds over Cellular interface. The default NAT Keepalive works well on networks with small NAT mapping timeouts but imposes a potential battery impact. If a network is known to have larger NAT mapping timeouts, larger Keepalive intervals may be safely used to minimize battery impact. The Keepalive interval can be modified by setting the `NATKeepAliveInterval` key. Default value for `NATKeepAliveOffloadEnable` is 1.|
|`NATKeepAliveInterval`|Integer|Optional. NAT Keepalive interval for Always On VPN IKEv2 connections. This value controls the interval over which Keepalive offload packets are sent by the device. The minimum value is 20 seconds. If no key is specified, the default is 20 seconds over WiFi and 110 seconds over a Cellular interface.|
|`EnablePFS`|Integer|Optional. Set to 1 to enable Perfect Forward Secrecy (PFS) for IKEv2 Connections. Default is 0. |
|`EnableCertificate- RevocationCheck`|Integer|Optional. Set to 1 to enable a certificate revocation check for IKEv2 connections.  This is a best-effort revocation check; server response timeouts will not cause it to fail.</br>**Availability:** Available in iOS 9.0 and later.|
|`IKESecurityAssociation- Parameters`|Dictionary|Optional. See table below. Applies to child Security Association unless `ChildSecurityAssociationParameters` is specified.|
|`ChildSecurityAssociation- Parameters`|Dictionary|Optional. See table below.|
  

The `IKESecurityAssociationParameters` and `ChildSecurityAssociationParameters` dictionaries may contain the following keys:  

|Key|Type|Value|
|-|-|-|
|`EncryptionAlgorithm`|String|Optional. One of:</br></br>* `DES`  </br></br>* `3DES`  </br></br>* `AES-128`  </br></br>* `AES-256` (Default)  </br></br>* `AES-128-GCM (16-octet ICV)`  </br></br>* `AES-256-GCM (16-octet ICV)`  </br></br>* `SHA1-96`  </br></br>* `SHA1-160`  </br></br>* `SHA2-256` (Default)  </br></br>* `SHA2-384`  </br></br>* `SHA2-512`  </br></br>|
|`IntegrityAlgorithm`|String|Optional. One of:</br></br>* `DES`  </br></br>* `3DES`  </br></br>* `AES-128`  </br></br>* `AES-256` (Default)  </br></br>* `AES-128-GCM (16-octet ICV)`  </br></br>* `AES-256-GCM (16-octet ICV)`  </br></br>* `SHA1-96`  </br></br>* `SHA1-160`  </br></br>* `SHA2-256` (Default)  </br></br>* `SHA2-384`  </br></br>* `SHA2-512`  </br></br>|
|`DiffieHellmanGroup`|Integer|Optional. One of: 1, 2 (Default), 5, 14, 15, 16, 17, 18, 19, 20, or 21.|
|`LifeTimeInMinutes`|Integer|Optional SA lifetime (rekey interval) in minutes. Valid values are 10 through 1440. Defaults to 1440 minutes.|
|`UseConfigurationAttributeInternalIPSubnet`|Integer|Optional. If set to 1, negotiations should use IKEv2 Configuration Attribute INTERNAL_IP4_SUBNET and INTERNAL_IP6_SUBNET. Defaults to 0.</br>**Availability:** Available in iOS 9.0 and later.|
|`DisableMOBIKE`|Integer|Optional. If set to 1, disables MOBIKE. Defaults to 0.</br>**Availability:** Available in iOS 9.0 and later.|
|`DisableRedirect`|Integer|Optional. If set to 1, disables IKEv2 redirect. If not set, the IKEv2 connection would be redirected if a redirect request is received from the server. Defaults to 0.</br>**Availability:** Available in iOS 9.0 and later.|
|`NATKeepAliveOffloadEnable`|Integer|Optional. Set to 1 to enable and 0 to disable NAT Keepalive offload for Always On VPN IKEv2 connections. Keepalive packets are used to maintain NAT mappings for IKEv2 connections. These packets are sent at regular interval when the device is awake. If `NATKeepAliveOffloadEnable` is set to 1, Keepalive packets would be sent by the chip even while the device is asleep. The default interval for the Keepalive packets for Always On VPN is 20 seconds over WiFi and 110 seconds over Cellular interface. The interval could be changed by setting the desired value in `NATKeepAliveInterval`. Defaults to 1.</br>**Availability:** Available in iOS 9.0 and later.|
|`NATKeepAliveInterval`|Integer|Optional. Controls the interval over which Keepalive packets are sent by the device. The minimum value is 20 seconds. If no key is specified, the default is 20 seconds.</br>**Availability:** Available in iOS 9.0 and later.|
  
  

### DNS Dictionary Keys  

 [Configuration Profile Reference - DNS Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27)  

If `VPNType` is `IKEv2`, the following DNS keys may be provided:  

|Key|Type|Value|
|-|-|-|
|`ServerAddresses`|Array of Strings|Required. An array of DNS server IP address strings. These IP addresses can be a mixture of IPv4 and IPv6 addresses.</br>**Availability:** Available in iOS 10.0 and later and macOS 10.12 and later.|
|`SearchDomains`|Array of Strings|Optional. A list of domain strings used to fully qualify single-label host names.</br>**Availability:** Available in iOS 10.0 and later and macOS 10.12 and later.|
|`DomainName`|String|Optional. The primary domain of the tunnel.</br>**Availability:** Available in iOS 10.0 and later and macOS 10.12 and later.|
|`SupplementalMatchDomains`|Array of Strings|Optional. A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in `ServerAddresses`. This key is used to create a split DNS configuration where only hosts in certain domains are resolved using the tunnel’s DNS resolver. Hosts not in one of the domains in this list are resolved using the system’s default resolver.</br>If `SupplementalMatchDomains` contains the empty string it becomes the default domain. This is how a split-tunnel configuration can direct all DNS queries first to the VPN DNS servers before the primary DNS servers. If the VPN tunnel becomes the network’s default route, the servers listed in `ServerAddresses` become the default resolver and the `SupplementalMatchDomains` list is ignored.</br>**Availability:** Available in iOS 10.0 and later and macOS 10.12 and later.|
|`SupplementalMatch- DomainsNoSearch`|Integer|Optional. Whether (0) or not (1) the domains in the `SupplementalMatchDomains` list should be appended to the resolver’s list of search domains. Default is 0.</br>**Availability:** Available in iOS 10.0 and later and macOS 10.12 and later.|
  
  

### Proxies Dictionary Keys  

 [Configuration Profile Reference - Proxies Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27)  

The `Proxies` dictionary may contain the following keys:  

|Key|Type|Value|
|-|-|-|
|`ProxyAutoConfigEnable`|Integer|Optional. Set to 1 to enable automatic proxy configuration. Defaults to 0.|
|`ProxyAutoConfigURLString`|String|Optional. URL to the location of the proxy auto-configuration file. Used only when `ProxyAutoConfigEnable` is 1.|
|`SupplementalMatchDomains`|Array of strings|Optional. If set, then only connections to hosts within one or more of the specified domains will use the proxy settings|
  

If `ProxyAutoConfigEnable` is 0, the dictionary may also contain the following keys:  

|Key|Type|Value|
|-|-|-|
|`HTTPEnable`|Integer|Optional. Set to 1 to enable proxy for HTTP traffic. Defaults to 0.|
|`HTTPProxy`|String|Optional. The host name of the HTTP proxy.|
|`HTTPPort`|Integer|Optional. The port number of the HTTP proxy. This field is required if HTTPProxy is specified.|
|`HTTPProxyUsername`|String|Optional. The username used for authentication.|
|`HTTPProxyPassword`|String|Optional. The password used for authentication.|
|`HTTPSEnable`|Integer|Optional. Set to 1 to enable proxy for HTTPS traffic. Defaults to 0.|
|`HTTPSProxy`|String|Optional. The host name of the HTTPS proxy.|
|`HTTPSPort`|Integer|Optional. The port number of the HTTPS proxy. This field is required if `HTTPSProxy` is specified.|
  
  

### AlwaysOn Dictionary Keys  

 [Configuration Profile Reference - AlwaysOn Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW27)  

If `VPNType` is `AlwaysOn`, the following keys may be provided in a dictionary:  

|Key|Type|Value|
|-|-|-|
|`UIToggleEnabled`|Integer|Optional. If set to 1, allows the user to disable this VPN configuration. Defaults to 0.|
|`TunnelConfigurations`|Array of dictionaries|Required. See below.|
|`ServiceExceptions`|Array of dictionaries|Optional. See below.|
|`AllowCaptiveWebSheet`|Integer|Optional. Set to 1 to allow traffic from Captive Web Sheet outside the VPN tunnel. Defaults to 0.|
|`AllowAllCaptiveNetworkPlugins`|Integer|Optional. Set to 1 to allow traffic from all Captive Networking apps outside the VPN tunnel to perform Captive network handling. Defaults to 0.|
|`AllowedCaptiveNetworkPlugins`|Array of dictionaries|Optional. Array of Captive Networking apps whose traffic will be allowed outside the VPN tunnel to perform Captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is 0.</br>Each dictionary in the `AllowedCaptiveNetworkPlugins` array must contain a `BundleIdentifier` key of type string, the value of which is the app’s bundle identifier.</br>Captive Networking apps may require additional entitlements to operate in a captive environment.|
  

Each dictionary in a `TunnelConfigurations` array may contain the following keys:  

|Key|Type|Value|
|-|-|-|
|`ProtocolType`|String|Must be IKEv2.|
|`Interfaces`|Array of strings|Optional. Specify the interfaces to which this configuration applies. Valid values are `Cellular` and `WiFi`. Defaults to `Cellular, WiFi`.|
  

In addition, all keys defined for the IKEv2 dictionary, such as `RemoteAddress` and `LocalIdentifier` may be present in a `TunnelConfigurations` dictionary.  

Each dictionary in a ServiceExceptions array may contain the following keys:  

|Key|Type|Value|
|-|-|-|
|`ServiceName`|String|Required. The name of a system service which is exempt from Always On VPN. Must be one of:</br></br>* `VoiceMail`  </br></br>* `AirPrint`  </br></br>* `Allow`  </br></br>* `Drop`  </br></br>|
|`Action`|String|Required. One of the following:</br></br>* `VoiceMail`  </br></br>* `AirPrint`  </br></br>* `Allow`  </br></br>* `Drop`  </br></br>|
  
  
