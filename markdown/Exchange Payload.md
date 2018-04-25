# Exchange Payload  

 [Configuration Profile Reference - Exchange Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW25)  

In iOS, the Exchange payload is designated by specifying `com.apple.eas.account` as the `PayloadType` value. This payload configures an Exchange Active Sync account on the device.  

In macOS, the Exchange payload is designated by specifying `com.apple.ews.account` as the `PayloadType` value. This payload will configure an Exchange Web Services account for Contacts, Mail, Notes, Reminders, and Calendar.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|Available in both iOS and macOS|
|`EmailAddress`|String| Specifies the full email address for the account. If not present in the payload, the device prompts for this string during profile installation.</br>In macOS, this key is required.|
|`Host`|String|Specifies the Exchange server host name (or IP address).</br>In macOS 10.11 and later, this key is optional.|
|`SSL`|Boolean|Optional. Default YES. Specifies whether the Exchange server uses SSL for authentication.|
|`UserName`|String|This string specifies the user name for this Exchange account. If missing, the devices prompts for it during profile installation.</br>In macOS, this key is required.|
|`Password`|String|Optional. The password of the account. Use only with encrypted profiles.|
|Available in iOS only|
|`Certificate`|NSData blob|Optional. For accounts that allow authentication via certificate, a .p12 identity certificate in NSData blob format.|
|`CertificateName`|String|Optional. Specifies the name or description of the certificate.|
|`CertificatePassword`|data|Optional. The password necessary for the p12 identity certificate. Used with mandatory encryption of profiles.|
|`PreventMove`|Boolean|Optional. Default `false`.</br>If set to `true`, messages may not be moved out of this email account into another account. Also prevents forwarding or replying from a different account than the message was originated from.</br>**Availability:** Available in iOS 5.0 and later.|
|`PreventAppSheet`|Boolean|Optional. Default `false`. If set to `true`, this account will not be available for sending mail in any app other than the Apple Mail app.</br>**Availability:** Available in iOS 5.0 and later.|
|`PayloadCertificateUUID`|String|UUID of the certificate payload to use for the identity credential. If this field is present, the `Certificate` field is not used.</br>**Availability:** Available in iOS 5.0 and later.|
|`SMIMEEnabled`|Boolean|Optional. Default `false`. If set to `true`, this account supports S/MIME.</br>**Availability:** Available in iOS 5.0 and later.|
|`SMIMESigningCertificateUUID`|String|Optional. The `PayloadUUID` of the identity certificate used to sign messages sent from this account.</br>**Availability:** Available in iOS 5.0 and later.|
|`SMIMEEncryptionCertificateUUID`|String|Optional. The `PayloadUUID` of the identity certificate used to decrypt messages sent to this account.</br>**Availability:** Available in iOS 5.0 and later.|
|`SMIMEEnablePerMessageSwitch`|Boolean|Optional. If set to `true`, enable the per-message signing and encryption switch. Defaults to `true`.|
|`disableMailRecentsSyncing`|Boolean|If `true`, this account is excluded from address Recents syncing. This defaults to `false`.</br>**Availability:** Available only in iOS 6.0 and later.|
|`MailNumberOfPastDaysToSync`|Integer|The number of days since synchronization.|
|`CommunicationServiceRules`|Dictionary|Optional. The communication service handler rules for this account. The `CommunicationServiceRules` dictionary currently contains only a `DefaultServiceHandlers` key; its value is a dictionary which contains an `AudioCall` key whose value is a string containing the bundle identifier for the default application that handles audio calls made to contacts from this account.|
|Available in macOS Only|
|`Path`|String|Optional.|
|`Port`|Number|Optional.|
|`ExternalHost`|String|Optional.|
|`ExternalSSL`|Boolean|Optional.|
|`ExternalPath`|String|Optional.|
|`ExternalPort`|Number|Optional.|
  


> **Note:** Note: As with VPN and Wi-Fi configurations, it is possible to associate an SCEP credential with an Exchange configuration via the `PayloadCertificateUUID` key.  
  
