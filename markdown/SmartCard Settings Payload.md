# SmartCard Settings Payload  

 [Configuration Profile Reference - SmartCard Settings Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW321)  

The SmartCard Settings payload is designated by specifying `com.apple.security.smartcard` as the `PayloadType`.  

This payload controls restrictions and settings for SmartCard pairing on macOS v10.12.4 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`UserPairing`|Boolean|Optional. If `false`, users will not get the pairing dialog, although existing pairings will still work. Default is `true`.|
|`allowSmartCard`|Boolean|Optional. If `false`, the SmartCard is disabled for logins, authorizations, and screensaver unlocking. It is still allowed for other functions, such as signing emails and web access. A restart is required for a change of setting to take effect. Default is `true`.|
|`checkCertificateTrust`|Integer|Optional. Valid values are 0-3:</br></br>* 0: certificate trust check is turned off  </br></br>* 1: certificate trust check is turned on. Standard validity check is being performed but this does not include additional revocation checks.  </br></br>* 2: certificate trust check is turned on, plus a soft revocation check is performed. Until the certificate is explicitly rejected by CRL/OCSP, it is considered as valid. This implies that unavailable/unreachable CRL/OCSP allows this check to succeed.  </br></br>* 3: certificate trust check is turned on, plus a hard revocation check is performed. Unless CRL/OCSP explicitly says “this certificate is OK”, the certificate is considered as invalid. The is the most secure option.  </br></br></br> Default is `0`.|
|`oneCardPerUser`|Boolean|Optional. If `true`, a user can pair with only one SmartCard, although existing pairings will be allowed if already set up. Default is `false`.|
|`enforceSmartCard`|Boolean|Optional. If `true`, a user can only login or authenticate with a SmartCard. Default is `false`.|
  
