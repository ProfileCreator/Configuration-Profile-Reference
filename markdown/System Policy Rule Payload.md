# System Policy Rule Payload  

 [Configuration Profile Reference - System Policy Rule Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW22)  

The System Policy Rule payload is designated by specifying `com.apple.systempolicy.rule` as the `PayloadType`. This is one of three payloads that allows control of various GateKeeper settings.  

This payload allows control over Gatekeeper’s system policy rules. The keys and functionality are tightly related to the `spctl` command line tool. You should be read the manual page for `spctl`.  

This payload must only exist in a device profile. If the payload is present in a user profile, an error will be generated during installation and the profile will fail to install.  

This payload is supported only on macOS v10.8 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`Requirement`|String|The policy requirement. This key must follow the syntax described in [Code Signing Requirement Language](https://developer.apple.com/library/content/documentation/Security/Conceptual/CodeSigningGuide/RequirementLang/RequirementLang.html#//apple_ref/doc/uid/TP40005929-CH5).|
|`Comment`|String|Optional. This string will appear in the System Policy UI. If it is missing, “PayloadDisplayName” or “PayloadDescription” will be put into this field before the rule is added to the System Policy database.|
|`Expiration`|Date|Optional. An expiration date for rule(s) being processed.|
|`OperationType`|String|Optional. One of `operation:execute`, `operation:install`, or `operation:lsopen`. This will default to `operation:execute`.|
  

The client has no way to display information about what certificate is being accepted by the signing requirement if the requirement keys is specified as:  

```
certificate leaf = H"7696f2cbf7f7d43fceb879f52f3cdc8fadfccbd4"
```  

You can embed the certificate within the payload itself, allowing the Profiles preference pane and System Profile report to display information about the certificate(s) being used. To do so, specify the `Requirement` key using a payload variable of the form $HASHCERT_xx$ where “xx” is the name of an additional key within the same payload that contains the certificate data in DER format.  

For example, if you specify:  

```
<key>Requirement</key>
<string>certificate leaf = $HASHCERT_Cert1Data$</string>
```  

and then provide:  

```
<key>Cert1Data</key>
<data>
MIIFTDCCBDSgAwIBAgIHBHXzxGzq8DANBgkqhkiG9w0BAQUFADCByjELMAkGA1UEBhMC
...
z1I6yBET5qaGhpWexEp3baLbXLcrtgufmDSUtUnImavGyw==
</data>
```  

The client will get the value of `Cert1Data` key, perform a SHA1 hash on it and use the resulting requirement string of:   

```
certificate leaf = H"7696f2cbf7f7d43fceb879f52f3cdc8fadfccbd4"
```  

If you want, you may reference multiple $HASHCERT_xx$ within the requirement string.  
