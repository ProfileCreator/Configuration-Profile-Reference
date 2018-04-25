# Active Directory Certificate Profile Payload  

 [Configuration Profile Reference - Active Directory Certificate Profile Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW238)  

The Active Directory Certificate Profile payload is designated by specifying `com.apple.ADCertificate.managed` as the `PayloadType` value.  

You can request a certificate from a Microsoft Certificate Authority (CA) using DCE/RPC and the Active Directory Certificate profile payload instructions detailed at [support.apple.com/kb/HT5357](http://support.apple.com/kb/HT5357).  

This payload includes the following unique keys:  

|Key|Type|Value|
|-|-|-|
|`AllowAllAppsAccess`|Boolean|If `true`, apps have access to the private key.|
|`CertServer`|String|Fully qualified host name of the Active Directory issuing CA.|
|`CertTemplate`|String|Template Name as it appears in the General tab of the template’s object in the Certificate Templates’ Microsoft Management Console snap-in component.|
|`CertificateAcquisitionMechanism`|String|Most commonly `RPC`. If using ‘Web enrollment,’ `HTTP`.
|
|`CertificateAuthority`|String|Name of the CA. This value is determined from the Common Name (CN) of the Active Directory entry: CN=<your CA name>, CN='Certification Authorities', CN='Public Key Services', CN='Services', or CN='Configuration', <your base Domain Name>.|
|`CertificateRenewalTimeInterval`|Integer|Number of days in advance of certificate expiration that the notification center will notify the user.|
|`Description`|String|User-friendly description of the certification identity.|
|`KeyIsExtractable`|Boolean|If `true`, the private key can be exported.|
|`PromptForCredentials`|Boolean|This key applies only to user certificates where Manual Download is the chosen method of profile delivery. If `true`, the user will be prompted for credentials when the profile is installed. Omit this key for computer certificates.|
|`Keysize`|Integer|Optional; defaults to 2048. The RSA key size for the Certificate Signing Request (CSR).</br>**Availability:** Available in macOS 10.11 and later.|
|`EnableAutoRenewal`|Boolean|Optional. If set to `true`, the certificate obtained with this payload will attempt auto-renewal. Only applies to device Active Directory certificate payloads.</br>**Availability:** Available in macOS 10.13.4 and later.|
  
