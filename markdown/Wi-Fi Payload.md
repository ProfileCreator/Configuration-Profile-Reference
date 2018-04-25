# Wi-Fi Payload  

 [Configuration Profile Reference - Wi-Fi Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW30)  

The Wi-Fi payload is designated by specifying `com.apple.wifi.managed` as the `PayloadType` value.  

In addition to the settings common to all payload types, the payload defines the following keys.  

|Key|Type|Value|
|-|-|-|
|`SSID_STR`|String|SSID of the Wi-Fi network to be used.</br>In iOS 7.0 and later, this is optional if a `DomainName` value is provided|
|`HIDDEN_NETWORK`|Boolean|Besides SSID, the device uses information such as broadcast type and encryption type to differentiate a network. By default (`false`), it is assumed that all configured networks are open or broadcast. To specify a hidden network, must be `true`.|
|`AutoJoin`|Boolean|Optional. Default `true`. If `true`, the network is auto-joined. If `false`, the user has to tap the network name to join it.</br>**Availability:** Available in iOS 5.0 and later and in all versions of macOS.|
|`EncryptionType`|String|The possible values are `WEP`, `WPA`, `WPA2`, `Any`, and `None`. `WPA` specifies WPA only; WPA2 applies to both encryption types.</br>Make sure that these values exactly match the capabilities of the network access point. If you're unsure about the encryption type, or would prefer that it apply to all encryption types, use the value `Any`.</br>**Availability:** Key available in iOS 4.0 and later and in all versions of macOS. The `None` value is available in iOS 5.0 and later and the `WPA2` value is available in iOS 8.0 and later.|
|`IsHotspot`|Boolean|Optional. Default `false`. If `true`, the network is treated as a hotspot.</br>**Availability:** Available in iOS 7.0 and later and in macOS 10.9 and later.|
|`DomainName`|String|Optional. Domain Name used for Wi-Fi Hotspot 2.0 negotiation. This field can be provided instead of `SSID_STR`.</br>**Availability:** Available in iOS 7.0 and later and in macOS 10.9 and later..|
|`ServiceProviderRoamingEnabled`|Boolean|Optional. If `true`, allows connection to roaming service providers. Defaults to `false`.</br>**Availability:** Available in iOS 7.0 and later and in macOS 10.9 and later.|
|`RoamingConsortiumOIs`|Array of strings|Optional. Array of Roaming Consortium Organization Identifiers used for Wi-Fi Hotspot 2.0 negotiation.</br>**Availability:** Available in iOS 7.0 and later and in macOS 10.9 and later..|
|`NAIRealmNames`|Array of strings|Optional. Array of strings. List of Network Access Identifier Realm names used for Wi-Fi Hotspot 2.0 negotiation.</br>**Availability:** Available in iOS 7.0 and later and in macOS 10.9 and later..|
|`MCCAndMNCs`|Array of strings|Optional. Array of strings. List of Mobile Country Code (MCC)/Mobile Network Code (MNC) pairs used for Wi-Fi Hotspot 2.0 negotiation. Each string must contain exactly six digits.</br>**Availability:** Available in iOS 7.0 and later. This feature is not supported in macOS.|
|`DisplayedOperatorName`|String|</br>The operator name to display when connected to this network. Used only with Wi-Fi Hotspot 2.0 access points. **Availability:** Available in iOS 7.0 and later and in macOS 10.9 and later.|
|`ProxyType`|String|Optional. Valid values are `None`, `Manual`, and `Auto`.</br>**Availability:** Available in iOS 5.0 and later and on all versions of macOS.|
|`CaptiveBypass`|Boolean|Optional. If set to `true`, Captive Network detection will be bypassed when the device connects to the network. Defaults to `false`.</br>**Availability:** Available in iOS 10.0 and later.|
|`QoSMarkingPolicy`|Dictionary|Optional. When this dictionary is not present for a Wi-Fi network, all apps are whitelisted to use L2 and L3 marking when the Wi-Fi network supports Cisco QoS fast lane. When present in the Wi-Fi payload, the `QoSMarkingPolicy` dictionary should contain the list of apps that are allowed to benefit from L2 and L3 marking. For dictionary keys, see the table below.</br>**Availability:** Available in iOS 10.0 and later. Not supported in macOS.|
  

The `QoSMarkingPolicy` dictionary contains these keys:  

|Key|Type|Value|
|-|-|-|
|`QoSMarkingWhitelistedAppIdentifiers`|Array of strings|Optional. Array of app bundle identifiers that will be whitelisted for L2 and L3 marking for traffic sent to the Wi-Fi network. If the array is not present but the `QoSMarkingPolicy` key is present (even empty) no app gets whitelisted.|
|`QoSMarkingAppleAudioVideoCalls`|Boolean|Optional. Specifies if audio and video traffic of built-in audio/video services such as FaceTime and Wi-Fi Calling will be whitelisted for L2 and L3 marking for traffic sent to the Wi-Fi network. Defaults to `true`.|
|`QoSMarkingEnabled`|Boolean|Optional. May be used to disable L3 marking and only use L2 marking for traffic sent to the Wi-Fi network. When this key is `false` the system behaves as if Wi-Fi was not associated with a Cisco QoS fast lane network. Defaults to `true`.|
  

If the `EncryptionType` field is set to `WEP`, `WPA`, or `ANY`, the following fields may also be provided:  

|Key|Type|Value|
|-|-|-|
|`Password`|String|Optional.|
|`EAPClientConfiguration`|Dictionary|Described in [EAPClientConfiguration Dictionary](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW31).|
|`PayloadCertificateUUID`|String|Described in [Certificates](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW33).|
  


> **Note:** The absence of a password does not prevent a network from being added to the list of known networks. The user is eventually prompted to provide the password when connecting to that network.  
  

If the `ProxyType` field is set to `Manual`, the following fields must also be provided:  

|Key|Type|Value|
|-|-|-|
|`ProxyServer`|String|The proxy server's network address.|
|`ProxyServerPort`|Integer|The proxy server's port.|
|`ProxyUsername`|String|Optional. The username used to authenticate to the proxy server.|
|`ProxyPassword`|String|Optional. The password used to authenticate to the proxy server.|
|`ProxyPACURL`|String|Optional. The URL of the PAC file that defines the proxy configuration.|
|`ProxyPACFallbackAllowed`|Boolean|Optional. If `false`, prevents the device from connecting directly to the destination if the PAC file is unreachable. Default is `false`.</br>**Availability:** Available in iOS 7 and later.|
  

If the `ProxyType` field is set to `Auto` and no `ProxyPACURL` value is specified, the device uses the web proxy autodiscovery protocol (WPAD) to discover proxies.  

For 802.1X enterprise networks, the EAP Client Configuration Dictionary must be provided.  

### EAPClientConfiguration Dictionary  

 [Configuration Profile Reference - EAPClientConfiguration Dictionary](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW30)  

In addition to the standard encryption types, it is possible to specify an enterprise profile for a given network via the `EAPClientConfiguration` key. If present, its value is a dictionary with the following keys.  

|Key|Type|Value|
|-|-|-|
|`UserName`|String|Optional. Unless you know the exact user name, this property won't appear in an imported configuration. Users can enter this information when they authenticate.|
|`AcceptEAPTypes`|Array of integers. |The following EAP types are accepted:</br>13 = TLS</br>17 = LEAP</br>18 = EAP-SIM</br>21 = TTLS</br>23 = EAP-AKA</br>25 = PEAP</br>43 = EAP-FAST|
|`UserPassword`|String|Optional. User password. If not provided, the user may be prompted during login.|
|`OneTimePassword`|Boolean|Optional. If `true`, the user will be prompted for a password each time they connect to the network. Defaults to `false`.|
|`PayloadCertificateAnchorUUID`|Array of strings|Optional. Identifies the certificates to be trusted for this authentication. Each entry must contain the UUID of a certificate payload. Use this key to prevent the device from asking the user if the listed certificates are trusted.</br>Dynamic trust (the certificate dialogue) is disabled if this property is specified, unless TLSAllowTrustExceptions is also specified with the value `true`.|
|`TLSTrustedServerNames`|Array of strings|Optional. This is the list of server certificate common names that will be accepted. You can use wildcards to specify the name, such as wpa.*.example.com. If a server presents a certificate that isn't in this list, it won't be trusted.</br>Used alone or in combination with TLSTrustedCertificates, the property allows someone to carefully craft which certificates to trust for the given network, and avoid dynamically trusted certificates.</br>Dynamic trust (the certificate dialogue) is disabled if this property is specified, unless TLSAllowTrustExceptions is also specified with the value `true`.|
|`TLSAllowTrustExceptions`|Boolean|Optional. Allows/disallows a dynamic trust decision by the user. The dynamic trust is the certificate dialogue that appears when a certificate isn't trusted. If this is `false`, the authentication fails if the certificate isn't already trusted. See PayloadCertificateAnchorUUID and TLSTrustedNames above.</br>The default value of this property is `true` unless either PayloadCertificateAnchorUUID or TLSTrustedServerNames is supplied, in which case the default value is `false`.|
|`TLSCertificateIsRequired`|Boolean|Optional. If `true`, allows for two-factor authentication for EAP-TTLS, PEAP, or EAP-FAST. If `false`, allows for zero-factor authentication for EAP-TLS. The default is `true` for EAP-TLS, and `false` for other EAP types.</br>**Availability:** Available in iOS 7.0 and later.|
|`TLSMinimumVersion`|String|Optional. The minimum TLS version to be used with EAP authentication. Value may be 1.0, 1.1, or 1.2. If no value is specified, the default minimum is 1.0. </br>**Availability:** Available in iOS 11.0 and macOS 10.13 and later.|
|`TLSMaximumVersion`|String|Optional. The maximum TLS version to be used with EAP authentication. Value may be 1.0, 1.1, or 1.2. If no value is specified, the default maximum is 1.2. </br>**Availability:** Available in iOS 11.0 and macOS 10.13 and later.
|
|`OuterIdentity`|String|Optional. This key is only relevant to TTLS, PEAP, and EAP-FAST.</br>This allows the user to hide his or her identity. The user's actual name appears only inside the encrypted tunnel. For example, it could be set to "anonymous" or "anon", or "anon@mycompany.net".</br>It can increase security because an attacker can't see the authenticating user's name in the clear.|
|`TTLSInnerAuthentication`|String|Optional. Specifies the inner authentication used by the TTLS module. Possible values are PAP, CHAP, MSCHAP, MSCHAPv2, and EA. Defaults to MSCHAPv2.|
  


> **Note:** 
For information about EAP-SIM, see [tools.ietf.org/html/rfc4186](http://tools.ietf.org/html/rfc4186).  
  
  

### EAP-Fast Support  

 [Configuration Profile Reference - EAP-Fast Support](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW30)  

The EAP-FAST module uses the following properties in the EAPClientConfiguration dictionary.  

|Key|Type|Value|
|-|-|-|
|`EAPFASTUsePAC`|Boolean|Optional.If `true`, the device will use an existing PAC if it's present. Otherwise, the server must present its identity using a certificate. Defaults to `false`.|
|`EAPFASTProvisionPAC`|Boolean|Optional. Used only if `EAPFASTUsePAC` is `true`. If set to `true`, allows PAC provisioning. Defaults to `false`. This value must be set to `true` for EAP-FAST PAC usage to succeed, because there is no other way to provision a PAC.|
|`EAPFASTProvisionPACAnonymously`|Boolean|Optional. If `true`, provisions the device anonymously. Note that there are known man-in-the-middle attacks for anonymous provisioning. Defaults to `false`.|
|`EAPSIMNumberOfRANDs`|Integer|Optional. Number of expected RANDs for EAPSIM. Valid values are 2 and 3. Defaults to 3.|
  

These keys are hierarchical in nature: if EAPFASTUsePAC is `false`, the other two properties aren't consulted. Similarly, if EAPFASTProvisionPAC is `false`, EAPFASTProvisionPACAnonymously isn't consulted.  

If EAPFASTUsePAC is `false`, authentication proceeds much like PEAP or TTLS: the server proves its identity using a certificate each time.  

If EAPFASTUsePAC is `true`, then an existing PAC is used if present. The only way to get a PAC on the device currently is to allow PAC provisioning. So, you need to enable EAPFASTProvisionPAC, and if desired, EAPFASTProvisionPACAnonymously. EAPFASTProvisionPACAnonymously has a security weakness: it doesn't authenticate the server so connections are vulnerable to a man-in-the-middle attack.  
  

### Certificates  

 [Configuration Profile Reference - Certificates](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW30)  

As with VPN configurations, it is possible to associate a certificate identity configuration with a Wi-Fi configuration. This is useful when defining credentials for a secure enterprise network. To associate an identity, specify its payload UUID via the "PayloadCertificateUUID" key.  

|Key|Type|Value|
|-|-|-|
|`PayloadCertificateUUID`|String|UUID of the certificate payload to use for the identity credential.|
  
  
