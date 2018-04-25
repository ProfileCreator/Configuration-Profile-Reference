# Managed Safari Web Domains  

 [Configuration Profile Reference - Managed Safari Web Domains](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW272)  

Opening a document originating from a managed Safari web domain causes iOS to treat the document as managed for the purpose of Managed Open In.  

|Key|Type|Value|
|-|-|-|
|`WebDomains`|Array|Optional. An array of URL strings. URLs matching the patterns listed here will be considered managed. Not supported in macOS|
|`SafariPasswordAutoFillDomains`|Array|Optional. An array of URL strings. Supported in iOS 9.3 and later; not supported in macOS.</br>Users can save passwords in Safari only from URLs matching the patterns listed here.</br>Regardless of the iCloud account that the user is using, if the device is not supervised, there can be no whitelist. If the device is supervised, there may be a whitelist, but if there is still no whitelist, note these two cases:</br></br>* If the device is configured as ephemeral multi-user, no password can be saved.  </br></br>* If the device is not configured as ephemeral multi-user, all passwords can be saved.  </br></br>|
  

The `WebDomains` and `SafariPasswordAutoFillDomains` arrays may contain strings using any of the following matching patterns:  

|Format|Description|
|-|-|
|`apple.com`|Any path under `apple.com` matches, but not `site.apple.com/`.|
|`foo.apple.com`|Any path under `foo.apple.com` matches, but not `apple.com/` or `bar.apple.com/`.|
|`*.apple.com`|Any path under `foo.apple.com` or `bar.apple.com` matches, but not `apple.com`.|
|`apple.com/sub`|`apple.com/sub` and any path under it matches, but not `apple.com/`.|
|`foo.apple.com/sub`|Any path under `foo.apple.com/sub` matches, but not `apple.com`, `apple.com/sub`, `foo.apple.com/`, or `bar.apple.com/sub`.|
|`*.apple.com/sub`|Any path under `foo.apple.com/sub` or `bar.apple.com/sub` matches, but not `apple.com` or `foo.apple.com/`.|
|`*.co`|Any path under `apple.co` or `beats.co` matches, but not `apple.co.uk` or `apple.com`.|
  

A URL that begins with the prefix `www.` is treated as though it did not contain that prefix during matching. For example, `http://www.apple.com/store` will be matched as `http://apple.com/store`.  

Trailing slashes will be ignored.  

If a `ManagedWebDomain` string entry contains a port number, only addresses that specify that port number will be considered managed. Otherwise, the domain will be matched without regard to the port number specified. For example, the pattern `*.apple.com:8080` will match `http://site.apple.com:8080/page.html` but not `http://site.apple.com/page.html`, while the pattern `*.apple.com` will match both URLs.  

Managed Safari Web Domain definitions are cumulative. Patterns defined by all Managed Web Domains payloads will be used to match a URL request.  

`SafariPasswordAutoFillDomains` definitions are cumulative. Patterns defined by all `SafariPasswordAutoFillDomains` payloads will be used to determine if passwords can be stored for a given URL.  
