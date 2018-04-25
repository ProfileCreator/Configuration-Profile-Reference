# FileVault 2  

 [Configuration Profile Reference - FileVault 2](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW842)  

In macOS 10.9, you can use FileVault 2 to perform full XTS-AES 128 encryption on the contents of a volume. FileVault 2 payloads are designated by specifying `com.apple.MCX.FileVault2` as the `PayloadType` value. Removal of the FileVault payload does not disable FileVault.  

|Key|Type|Value|
|-|-|-|
|`Enable`|String|Set to 'On' to enable FileVault.  Set to 'Off' to disable FileVault. This value is required.|
|`Defer`|Boolean|Set to true to defer enabling FileVault until the designated user logs out. For details, see *fdesetup(8)*. The person enabling FileVault must be either a local user or a mobile account user.|
|`UserEntersMissingInfo`|Boolean|Set to true for manual profile installs to prompt for missing user name or password fields.|
|`UseRecoveryKey`|Boolean|Set to true to create a personal recovery key. Defaults to true.|
|`ShowRecoveryKey`|Boolean|Set to false to not display the personal recovery key to the user after FileVault is enabled. Defaults to true.|
|`OutputPath`|String|Path to the location where the recovery key and computer information plist will be stored.|
|`Certificate`|Data|DER-encoded certificate data if an institutional recovery key will be added.|
|`PayloadCertificateUUID`|String|UUID of the payload containing the asymmetric recovery key certificate payload.|
|`Username`|String|User name of the Open Directory user that will be added to FileVault.|
|`Password`|String|User password of the Open Directory user that will be added to FileVault. Use the `UserEntersMissingInfo` key if you want to prompt for this information.|
|`UseKeychain`|Boolean|If set to true and no certificate information is provided in this payload, the keychain already created at /Library/Keychains/FileVaultMaster.keychain will be used when the institutional recovery key is added.|
|`DeferForceAtUserLogin- MaxBypassAttempts`|Integer|When using the `Defer` option you can optionally set this key to the maximum number of times the user can bypass enabling FileVault before it will require that it be enabled before the user can log in. If set to 0, it will always prompt to enable FileVault until it is enabled, though it will allow you to bypass enabling it. Setting this key to –1 will disable this feature.</br>**Availability:** Available in macOS 10.10 and later.|
|`DeferDontAskAtUserLogout`|Boolean|When using the `Defer` option, set this key to true to not request enabling FileVault at user logout time.</br>**Availability:** Available in macOS 10.10 and later.|
  

A personal recovery user will normally be created unless the `UseRecoveryKey` key value is false. An institutional recovery key will be created only if either there is certificate data available in the `Certificate` key value, a specific certificate payload is referenced, or the `UseKeychain` key value is set to true and a valid `FileVaultMaster.keychain` file was created. In all cases, the certificate information must be set up properly for FileVault or it will be ignored and no institutional recovery key will be set up.  

### FileVault Recovery Key Redirection Payload  

 [Configuration Profile Reference - FileVault Recovery Key Redirection Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW842)  

FileVault full-volume encryption (FDE) recovery keys are, by default, sent to Apple if the user requests it. With this key, you can redirect those recovery keys to a corporate server. FileVault Recovery Key Redirection payloads are designated by specifying `com.apple.security.FDERecoveryRedirect` as the `PayloadType` value. Only one payload of this type is allowed per system.  

A site providing support for archiving the recovery key must implement its own HTTPS server. The client issues a POST request to the server with XML data in the request body containing the recovery key and serial number of the client computer. The server must respond with XML data echoing the device's serial number and provide a RecordNumber, which can be any data that locates the recovery key.  

The SSL certificate chain of the server is evaluated by the client, which must trust it. If needed, the configuration profile can include an additional certificate to set up a chain of trust.  

|Key|Type|Value|
|-|-|-|
|`RedirectURL`|String|The URL to which FDE recovery keys should be sent instead of Apple. Must begin with `https://`.|
|`EncryptCertPayloadUUID`|String|The UUID of a payload within the same profile that contains a certificate whose public key is used to encrypt the recovery key when it is sent to the redirected URL. The referenced payload must be of type `com.apple.security.pkcs1`.|
  

Once installed, this payload causes any FileVault recovery keys to be redirected to the specified URL instead of being sent to Apple. This will require sites to implement their own HTTPS server that will receive the recovery keys via a POST request.  

This payload is valid only in system-scoped profiles (where `PayloadScope` is `System`). Installing more than one payload of this type per machine causes an error. The SSL certificate chain of the server is evaluated by the client, which must trust it. If
needed, the configuration profile may contain another payload with the server’s root certificate to be marked as trusted when the profile is installed.  

If the client cannot communicate with the server it will continually retry the connection. The retry interval starts at 5 seconds and doubles until retries are hourly. The client then retries once an hour until it successfully contacts the server.  
  

### FileVault Client Request  

 [Configuration Profile Reference - FileVault Client Request](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW842)  

The client issues a HTTPS POST request to the server with XML data containing the following:  

|Key|Type|Value|
|-|-|-|
|`VersionNumber`|String|Currently set to '1.0'.|
|`SerialNumber`|String|The serial number of the client computer. The server must include this value in its response back to the client (see below).|
|`RecoveryKeyCMS64`|String|The recovery key encrypted using the encryption certificate provided in the configuration profile (referenced by the `EncryptCertPayloadUUID` key). The encrypted payload contains only the recovery key string without any XML wrapper. The encrypted data is wrapped in a CMS envelope and is then Base-64 encoded.|
  

These tags are enclosed within a parent `FDECaptureRequest` tag. An example of an XML message body is:  

```
<FDECaptureRequest>
<VersionNumber>1.0</VersionNumber>
<SerialNumber>A02FE08UCC8X</SerialNumber>
<RecoveryKeyCMS64>MIAGCSqGSIb3DQEHA ... AAAAAAAAA==</RecoveryKeyCMS64>
</FDECaptureRequest>
```  
  

### FileVault Server Response  

 [Configuration Profile Reference - FileVault Server Response](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW842)  

Upon receiving the client’s request, the server must respond to the client with XML data containing:  

|Key|Type|Value|
|-|-|-|
|`SerialNumber`|String|The serial number of the client computer. This value must be the same as the one sent in the request.|
|`RecordNumber`|Short string|This value must be nonempty but otherwise is up to the site to define it. This value will be displayed to the user along with the serial number on the EFI login screen when the user is asked to enter the recovery key. As an example, this could be a value to assist the site administrator in locating or verifying the user's recovery key in a database.|
  
  
