# FDE Recovery Key Escrow Payload  

 [Configuration Profile Reference - FDE Recovery Key Escrow Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW42)  

FileVault Full Disk Encryption (FDE) recovery keys are, by default, sent to Apple if the user requests it. Starting with macOS 10.13, recovery key escrow payloads are designated by specifying `com.apple.security.FDERecoveryKeyEscrow` as the `PayloadType` value. Only one payload of this type is allowed per system.  

If FileVault is enabled after this payload is installed on the system, the FileVault PRK will be encrypted with the specified certificate, wrapped with a CMS envelope and stored at `/var/db/FileVaultPRK.dat`. The encrypted data will be made available to the MDM server as part of the `SecurityInfo` command. Alternatively, if a site uses its own administration software, it can extract the PRK from the foregoing location at any time. Because the PRK is encrypted using the certificate provided in the profile, only the author of the profile can extract the data.  

Note these cautions:  


* The payload must exist in a system-scoped profile.  

* Installing more than one payload of this type per machine will cause an error.  

* The previous payload (`com.apple.security.FDERecoveryRedirect`) is no longer supported. It can still be installed, but it will be ignored. This lets servers send out the same profile to old and new clients.  

* If only an old-style redirection payload is installed at the time FileVault is turned on (by means of the Security Preferences pane), an error will be displayed and FileVault will not be enabled.  

* No warning or error will be provided if FileVault is already enabled and an old-style payload is installed. In this case, it’s assumed that the recovery key has already been escrowed with the server.  
  

This payload contains these keys:  

|Key|Type|Value|
|-|-|-|
|`Location`|String|Required. A short description of the location where the recovery key will be escrowed. This text will be inserted into the message the user sees when enabling FileVault.|
|`EncryptCertPayloadUUID`|String|Required. The UUID of a payload within the same profile that contains the certificate that will be used to encrypt the recovery key. The referenced payload must be of type `com.apple.security.pkcs1`.|
|`DeviceKey`|String|Optional. An optional string that will be included in help text if the user appears to have forgotten the password. Can be used by a site admin to look up the escrowed key for the particular machine. Replaces the `RecordNumber` key used in previous escrow mechanism. If missing, the device serial number will be used instead.|
  
