# Content Caching Payload  

 [Configuration Profile Reference - Content Caching Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW64)  

The Content Caching payload is designated by specifying `com.apple.AssetCache.managed` as the `PayloadType`.  

It configures the Content Caching service.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`AllowPersonalCaching`|Boolean|Optional. If set to `true`, caches the user’s iCloud data. Clients may take some time (hours, days) to react to changes to this setting; it does not have an immediate effect. Default is `true`.</br>At least one of the `AllowPersonalCaching` or `AllowSharedCaching` keys must be `true`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`AllowSharedCaching`|Boolean|Optional. If set to `true`, caches non-iCloud content, such as apps and software updates. Clients may take some time (hours, days) to react to changes to this setting; it does not have an immediate effect. Default is `true`.</br>At least one of the `AllowPersonalCaching` or `AllowSharedCaching` keys must be `true`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`AutoActivation`|Boolean|Optional. If set to `true`, automatically activate the Content Cache when possible and prevent disabling of the Content Cache. Default is `false`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`CacheLimit`|Integer|Optional. Defines the maximum number of bytes of disk space that will be used for the Content Cache. A `CacheLimit` of 0 means unlimited disk space. Default is `0`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`DataPath`|String|Optional. The path to the directory used to store Cached Content.  Changing this setting manually does not automatically move cached content from the old to the new location. To move content automatically, use the Sharing preference's Content Caching pane.  </br>The value must be, or end with, `/Library/Application Support/Apple/AssetCache/Data`.  A directory (and its intermediates) will be created for the given `DataPath` if it does not already exist.  The directory will be owned by `_assetcache:_assetcache` and have mode 0750.  Its immediate parent directory (`.../Library/Application Support/Apple/AssetCache`) will be owned by `_assetcache:_assetcache` and have mode 0755. </br>Default is `/Library/Application Support/Apple/AssetCache/Data`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`DenyTetheredCaching`|Boolean|Optional. If set to `true`, tethered caching is disabled. Default is `false`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`ListenRanges`|Array of Dictionaries|Optional. Array of dictionaries describing a range of client IP addresses to serve.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`ListenRangesOnly`|Boolean|Optional. If set to `true`, the Content Cache provides content only to clients in the ranges specified by the `ListenRanges` key. To use the `ListenRangesOnly` key, the `ListenRanges` key must also be specified. Default is `false`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`ListenWithPeersAndParents`|Boolean|Optional. If set to `true`, the Content Cache provides content to the clients in the union of the ListenRanges, PeerListenRanges and Parents ranges. Default is `true`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`LocalSubnetsOnly`|Boolean|Optional. If set to `true`, the Content Cache offers content to clients only on the same immediate local network as the Content Cache. No content would be offered to clients on other networks reachable by the Content Cache. Default is `true`.</br>If `LocalSubnetsOnly` is set to true, `ListenRanges` will be ignored.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`LogClientIdentity`|Boolean|Optional. If set to `true`, the Content Cache will log the IP address and port number of the clients that request content. Default is `false`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`Parents`|Array of Strings|Optional. Array of the local IP addresses of other Content Caches that this cache should download from or upload to, instead of downloading from or uploading to Apple directly. Invalid addresses and addresses of computers that are not Content Caches are ignored. </br>Parent caches that become unavailable are skipped. If all parent Content Caches become unavailable, the Content Cache will download from or upload to Apple directly until a parent Content Cache becomes available again.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`ParentSelectionPolicy`|String|Optional. The policy to use when choosing among more than one configured parent Content Cache. With every policy, parent caches that are temporarily unavailable are skipped.
</br></br>* `first-available`: Always use the first parent in the Parents list that is available.  This is useful for designating permanent primary, secondary, and subsequent parents.  </br></br>* `url-path-hash`: Hash the path part of the requested URL so that the same parent is always used for the same URL.  This is useful for maximizing the size of the combined caches of the parents.  </br></br>* `random`: Choose a parent at random.  This is useful for load balancing.  </br></br>* `round-robin`: Rotate through the parents in order.  This is useful for load balancing.  </br></br>* `sticky-available`: Starting with the first parent in the Parents list, always use the first parent that is available. Use that parent until it becomes unavailable, then advance to the next one.  This is useful for designating floating primary, secondary, and subsequent parents.  </br></br></br>Default is `round-robin`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`PeerFilterRanges`|Array of Dictionaries|Optional. Array of dictionaries describing a range of peer IP addresses that the Content Cache will use to filter its list of peers to query for content.  The Content Cache only queries peers that are in the `PeerFilterRanges`.  When `PeerFilterRanges` is an empty array the Content Cache will not query any peers.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`PeerListenRanges`|Array of Dictionaries|Optional. Array of dictionaries describing a range of peer IP addresses the Content Cache will respond to peer cache queries from. When `PeerListenRanges` is an empty array, the Content Cache will respond with an error to all cache queries.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`PeerLocalSubnetsOnly`|Boolean|Optional. If set to `true`, the Content Cache will only peer with other Content Caches on the same immediate local network, rather than with Content Caches that use the same public IP address as the device. When `PeerLocalSubnetsOnly` is true, it overrides the configuration of `PeerFilterRanges` and `PeerListenRanges`. If the network changes, the local network peering restrictions update appropriately.</br>If set to `false`, the Content Cache defers to `PeerFilterRanges` and `PeerListenRanges` for configuring the peering restrictions.</br>Default is `true`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`Port`|Integer|Optional. The TCP port number on which the Content Cache accepts requests for uploads or downloads.  Port set to 0 picks a random, available port. Default is `0`.</br>**Availability:** Available in macOS 10.13.4 and later.|
|`PublicRanges`|Array of Dictionaries|Optional. Array of dictionaries describing a range of public IP addresses that the cloud servers should use for matching clients to Content Caches.</br>**Availability:** Available in macOS 10.13.4 and later.|
  

The dictionary used to define ranges used by the Content Cache uses the following keys:  

|Key|Type|Value|
|-|-|-|
|`type`|String|Optional. The IP address type (`IPv4` or `IPv6`). Default is `IPv4`.|
|`first`|String|Required. First IP address in the range.|
|`last`|String|Required. Last IP address in the range.|
  
