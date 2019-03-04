# Web Content Filter Payload  

 [Configuration Profile Reference - Web Content Filter Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW45)  

The Web Content Filter payload allows you to whitelist and blacklist specific web URLs. This payload is supported only on supervised devices.  

Web content filtering is designated by specifying `com.apple.webcontent-filter` as the `PayloadType` value and adding a `FilterType` string with one of these values:  


* `BuiltIn` (Default)  

* `Plugin`  
  

On macOS, `FilterType` must be `Plugin`.  

If `FilterType` is `BuiltIn`, this payload defines the following keys in addition to the settings common to all payloads:  

|Key|Type|Value|
|-|-|-|
|`AutoFilterEnabled`|Boolean|Optional. If `true`, automatic filtering is enabled. This function evaluates each web page as it is loaded and attempts to identify and block content not suitable for children. The search algorithm is complex and may vary from release to release, but it is basically looking for adult language, i.e. swearing and sexually explicit language. The default value is `false`.|
|`PermittedURLs`|Array of Strings|Optional. Used only when `AutoFilterEnabled` is `true`. Otherwise, this field is ignored.</br>Each entry contains a URL that is accessible whether the automatic filter allows access or not.|
|`WhitelistedBookmarks`|Array of Dictionaries|Optional. If present, these URLs are added to the browser’s bookmarks, and the user is not allowed to visit any sites other than these. The number of these URLs should be limited to about 500.|
|`BlacklistedURLs`|Array of Strings|Optional. Access to the specified URLs is blocked. The number of these URLs should be limited to about 500.|
  

Each entry in the `WhitelistedBookmarks` field contains a dictionary with the following keys:  

|Key|Type|Value|
|-|-|-|
|`URL`|String|URL of the whitelisted bookmark.|
|`BookmarkPath`|String|Optional. The folder into which the bookmark should be added in Safari—`/Interesting Topic Pages/Biology/`, for example.</br>If absent, the bookmark is added to the default bookmarks directory.|
|`Title`|String|The title of the bookmark.|
  

When multiple content filter payloads are present:  


* The blacklist is the union of all blacklists—that is, any URL that appears in any blacklist is inaccessible.  

* The permitted list is the intersection of all permitted lists—that is, only URLs that appear in *every* permitted list are accessible when they would otherwise be blocked by the automatic filter.  

* The whitelist list is the intersection of all whitelists—that is, only URLs that appear in *every* whitelist are accessible.  
  

URLs are matched by using string-based root matching. A URL matches a whitelist, blacklist, or permitted list pattern if the exact characters of the pattern appear as the root of the URL. For example, if `test.com/a` is blacklisted, then `test.com`, `test.com/b`, and `test.com/c/d/e` will all be blocked. Matching does not discard subdomain prefixes, so if `test.com/a` is blacklisted, `m.test.com` is not blocked. Also, no attempt is made to match aliases (IP address versus DNS names, for example) or to handle requests with explicit port numbers.  

If a profile does not contain an array for `PermittedURLs` or `WhitelistedBookmarks`, that profile is skipped when evaluating the missing array or arrays. As an exception, if a payload contains an `AutoFilterEnabled` key, but does not contain a `PermittedURLs` array, that profile is treated as containing an empty array—that is, all websites are blocked.  

All filtering options are active simultaneously. Only URLs and sites that pass **all** rules are permitted.  

If `FilterType` is `Plugin`, this payload defines the following keys in addition to the settings common to all payloads:  

|Key|Type|Value|
|-|-|-|
|`UserDefinedName`|String|A string which will be displayed for this filtering configuration.|
|`PluginBundleID`|String|The Bundle ID of the plugin that provides filtering service.|
|`ServerAddress`|String|Optional. Server address (may be IP address, hostname, or URL).|
|`UserName`|String|Optional. A username for the service.|
|`Password`|String|Optional. A password for the service.|
|`PayloadCertificateUUID`|String|Optional. UUID pointing to an identity certificate payload. This identity will be used to authenticate the user to the service.|
|`Organization`|String|Optional. An Organization string that will be passed to the 3rd-party plugin.|
|`VendorConfig`|Dictionary|Optional. Custom dictionary needed by the filtering service plugin.|
|`FilterBrowsers`|Integer|Optional. If set to 1, filter WebKit traffic. Defaults to 0.|
|`FilterSockets`|Integer|Optional. If set to 1, filter socket traffic. Defaults to 0.|
  

At least one of `FilterBrowsers` or `FilterSockets` must be `true` for the filter to have any effect.  
