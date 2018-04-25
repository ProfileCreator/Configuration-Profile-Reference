# SmartCard Settings Payload  

 [Configuration Profile Reference - SmartCard Settings Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW321)  

The SmartCard Settings payload is designated by specifying `com.apple.security.smartcard` as the `PayloadType`.  

This payload controls restrictions and settings for SmartCard pairing on macOS v10.12.4 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`UserPairing`|Boolean|Optional. If `false`, users will not get the pairing dialog, although existing pairings will still work. Default is `true`.|
|`allowSmartCard`|Boolean|Optional. If `false`, the SmartCard is disabled for logins, authorizations, and screensaver unlocking. It is still allowed for other functions, such as signing emails and web access. A restart is required for a change of setting to take effect. Default is `true`.|
|`checkCertificateTrust`|Boolean|Optional. If `true`, certificates on the card must be valid in these ways: its issuer is system-trusted, the certificate is not expired, its "valid-after" date is in the past, and it passes CRL and OCSP checking. User overrides are not allowed. Usually this key is set to `true` for SmartCard use in corporate environments. Default is `false`.|
|`oneCardPerUser`|Boolean|Optional. If `true`, a user can pair with only one SmartCard, although existing pairings will be allowed if already set up. Default is `false`.|
|`enforceSmartCard`|Boolean|Optional. If `true`, a user can only login or authenticate with a SmartCard. Default is `false`.|
  
