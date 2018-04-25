# Email Payload  

 [Configuration Profile Reference - Email Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW11)  

The email payload is designated by specifying `com.apple.mail.managed` as the `PayloadType` value.  

An email payload creates an email account on the device.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`EmailAccountDescription`|String|Optional. A user-visible description of the email account, shown in the Mail and Settings applications.|
|`EmailAccountName`|String|Optional. The full user name for the account. This is the user name in sent messages, etc.|
|`EmailAccountType`|String|Allowed values are `EmailTypePOP` and `EmailTypeIMAP`. Defines the protocol to be used for that account.|
|`EmailAddress`|String|Designates the full email address for the account. If not present in the payload, the device prompts for this string during profile installation.|
|`IncomingMailServerAuthentication`|String|Designates the authentication scheme for incoming mail. Allowed values are `EmailAuthPassword`, `EmailAuthCRAMMD5`, `EmailAuthNTLM`, `EmailAuthHTTPMD5`, and `EmailAuthNone`.|
|`IncomingMailServerHostName`|String|Designates the incoming mail server host name (or IP address).|
|`IncomingMailServerPortNumber`|Number|Optional. Designates the incoming mail server port number. If no port number is specified, the default port for a given protocol is used.|
|`IncomingMailServerUseSSL`|Boolean|Optional. Default `false`. Designates whether the incoming mail server uses SSL for authentication.|
|`IncomingMailServerUsername`|String|Designates the user name for the email account, usually the same as the email address up to the @ character. If not present in the payload, and the account is set up to require authentication for incoming email, the device will prompt for this string during profile installation.|
|`IncomingPassword`|String|Optional. Password for the Incoming Mail Server. Use only with encrypted profiles.|
|`OutgoingPassword`|String|Optional. Password for the Outgoing Mail Server. Use only with encrypted profiles.|
|`OutgoingPasswordSameAsIncomingPassword`|Boolean|Optional. If set, the user will be prompted for the password only once and it will be used for both outgoing and incoming mail.|
|`OutgoingMailServerAuthentication`|String|Designates the authentication scheme for outgoing mail. Allowed values are `EmailAuthPassword`, `EmailAuthCRAMMD5`, `EmailAuthNTLM`, `EmailAuthHTTPMD5`, and `EmailAuthNone`.|
|`OutgoingMailServerHostName`|String|Designates the outgoing mail server host name (or IP address).|
|`OutgoingMailServerPortNumber`|Number|Optional. Designates the outgoing mail server port number. If no port number is specified, ports 25, 587 and 465 are used, in this order.|
|`OutgoingMailServerUseSSL`|Boolean|Optional. Default `false`. Designates whether the outgoing mail server uses SSL for authentication.|
|`OutgoingMailServerUsername`|String|Designates the user name for the email account, usually the same as the email address up to the @ character. If not present in the payload, and the account is set up to require authentication for outgoing email, the device prompts for this string during profile installation.|
|`PreventMove`|Boolean|Optional. Default `false`.</br>If `true`, messages may not be moved out of this email account into another account. Also prevents forwarding or replying from a different account than the message was originated from.</br>**Availability:** Available only in iOS 5.0 and later.|
|`PreventAppSheet`|Boolean|Optional. Default `false`.</br>If `true`, this account is not available for sending mail in any app other than the Apple Mail app.</br>**Availability:** Available only in iOS 5.0 and later.|
|`SMIMEEnabled`|Boolean|Optional. Default `false`. If `true`, this account supports S/MIME. </br>As of iOS 10.0, this key is ignored.</br>**Availability:** Available only in iOS 5.0 through iOS 9.3.3.|
|`SMIMESigningEnabled`|Boolean|Optional. Default `true`. If set to `true`, S/MIME signing is enabled for this account. </br>**Availability:** Available only in iOS 10.3 and later.|
|`SMIMESigningCertificateUUID`|String|Optional. The `PayloadUUID` of the identity certificate used to sign messages sent from this account.  </br>**Availability:** Available only in iOS 5.0 and later.|
|`SMIMEEncryptionEnabled`|Boolean|Optional. Default `false`. If set to `true`, S/MIME encryption is on by default for this account.  </br>**Availability:** Available only in iOS 10.3 and later.|
|`SMIMEEncryptionCertificateUUID`|String|Optional. The `PayloadUUID` of the identity certificate used to decrypt messages sent to this account. The public certificate is attached to outgoing mail to allow encrypted mail to be sent to this user. When the user sends encrypted mail, the public certificate is used to encrypt the copy of the mail in their Sent mailbox. </br>**Availability:** Available only in iOS 5.0 and later.|
|`SMIMEEnablePerMessageSwitch`|Boolean|Optional. Default `false`. If set to `true`, displays the per-message encryption switch in the Mail Compose UI. </br>**Availability:** Available only in iOS 8.0 and later.|
|`disableMailRecentsSyncing`|Boolean|If `true`, this account is excluded from address Recents syncing. This defaults to `false`.</br>**Availability:** Available only in iOS 6.0 and later.|
|`allowMailDrop`|Boolean|Optional. If `true`, this account is allowed to use Mail Drop. The default is `false`.</br>**Availability:** Available in iOS 9.2 and later.|
  
