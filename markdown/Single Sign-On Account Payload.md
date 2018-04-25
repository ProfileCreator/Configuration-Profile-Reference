# Single Sign-On Account Payload  

 [Configuration Profile Reference - Single Sign-On Account Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW44)  

The Single Sign-On Account payload is designated by specifying `com.apple.sso` as the `PayloadType`.  

This payload is supported only in iOS 7.0 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`Name`|String|Human-readable name for the account.|
|`Kerberos`|Dictionary|Kerberos-related information, described below.|
  

The Kerberos `dictionary` can contain the following keys:  

|Key|Type|Value|
|-|-|-|
|`PrincipalName`|String|Optional. The Kerberos principal name. If not provided, the user is prompted for one during profile installation.</br>This field must be provided for MDM installation.|
|`PayloadCertificateUUID`|String|Optional. The PayloadUUID of an identity certificate payload that can be used to renew the Kerberos credential without user interaction. The certificate payload must have either the `com.apple.security.pkcs12` or `com.apple.security.scep` payload type. Both the Single Sign On payload and the identity certificate payload must be included in the same configuration profile|
|`Realm`|String|The Kerberos realm name. This value should be properly capitalized.|
|`URLPrefixMatches`|Array of Strings|List of URLs prefixes that must be matched to use this account for Kerberos authentication over HTTP. **Note** that the URL postfixes must match as well.|
|`AppIdentifierMatches`|Array of Strings|Optional. List of app identifiers that are allowed to use this login. If this field missing, this login matches all app identifiers.</br>This array, if present, may not be empty.|
  

Each entry in the `URLPrefixMatches` array must contain a URL prefix. Only URLs that begin with one of the strings in this account are allowed to access the Kerberos ticket. URL matching patterns must include the scheme—for example, `http://www.example.com/`. If a matching pattern does not end in `/`, a `/` is appended to it.  

The URL matching patterns must begin with either `http://` or `https://`. A simple string match is performed, so the URL prefix `http://www.example.com/` does not match `http://www.example.com:80/`. With iOS 9.0 or later, however, a single wildcard * may be used to specify all matching values. For example, http://*.example.com/ will match both `http://store.example.com/` and `http://www.example.com`.  

The patterns `http://.com` and `https://.com` match all HTTP and HTTPS URLs, respectively.  

The `AppIdentifierMatches` array must contain strings that match app bundle IDs. These strings may be exact matches (`com.mycompany.myapp`, for example) or may specify a prefix match on the bundle ID by using the `*` wildcard character. The wildcard character must appear after a period character (`.`), and may appear only once, at the end of the string (`com.mycompany.*`, for example). When a wildcard is included, any app whose bundle ID begins with the prefix is granted access to the account.  
