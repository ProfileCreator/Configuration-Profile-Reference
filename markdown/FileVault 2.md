# FileVault 2  

 [Configuration Profile Reference - FileVault 2](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW842)  

In macOS 10.9, you can use FileVault 2 to perform full XTS-AES 128 encryption on the contents of a volume. FileVault 2 payloads are designated by specifying `com.apple.MCX.FileVault2` as the `PayloadType` value. Removal of the FileVault payload does not disable FileVault.  

|Key|Type|Value|
|-|-|-|
|`Enable`|String|Set to 'On' to enable FileVault.  Set to 'Off' to disable FileVault. This value is required.|
|`Defer`|Boolean|Set to `true` to defer enabling FileVault until the designated user logs out. For details, see *fdesetup(8)*. The person enabling FileVault must be either a local user or a mobile account user.|
|`UserEntersMissingInfo`|Boolean|Set to `true` for manual profile installs to prompt for missing user name or password fields.|
|`UseRecoveryKey`|Boolean|Set to `true` to create a personal recovery key. Defaults to `true`.|
|`ShowRecoveryKey`|Boolean|Set to `false` to not display the personal recovery key to the user after FileVault is enabled. Defaults to `true`.|
|`OutputPath`|String|Path to the location where the recovery key and computer information plist will be stored.|
|`Certificate`|Data|DER-encoded certificate data if an institutional recovery key will be added.|
|`PayloadCertificateUUID`|String|UUID of the payload containing the asymmetric recovery key certificate payload.|
|`Username`|String|User name of the Open Directory user that will be added to FileVault.|
|`Password`|String|User password of the Open Directory user that will be added to FileVault. Use the `UserEntersMissingInfo` key if you want to prompt for this information.|
|`UseKeychain`|Boolean|If set to `true` and no certificate information is provided in this payload, the keychain already created at /Library/Keychains/FileVaultMaster.keychain will be used when the institutional recovery key is added.|
|`DeferForceAtUserLogin- MaxBypassAttempts`|Integer|When using the `Defer` option you can optionally set this key to the maximum number of times the user can bypass enabling FileVault before it will require that it be enabled before the user can log in. If set to 0, it will always prompt to enable FileVault until it is enabled, though it will allow you to bypass enabling it. Setting this key to –1 will disable this feature.</br>**Availability:** Available in macOS 10.10 and later.|
|`DeferDontAskAtUserLogout`|Boolean|When using the `Defer` option, set this key to `true` to not request enabling FileVault at user logout time.</br>**Availability:** Available in macOS 10.10 and later.|
  

A personal recovery user will normally be created unless the `UseRecoveryKey` key value is `false`. An institutional recovery key will be created only if either there is certificate data available in the `Certificate` key value, a specific certificate payload is referenced, or the `UseKeychain` key value is set to `true` and a valid `FileVaultMaster.keychain` file was created. In all cases, the certificate information must be set up properly for FileVault or it will be ignored and no institutional recovery key will be set up.  
