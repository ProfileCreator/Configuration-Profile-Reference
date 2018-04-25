# Kernel Extension Policy  

 [Configuration Profile Reference - Kernel Extension Policy](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-DontLinkElementID_1)  

The Kernel Extension Policy payload is designated by specifying `com.apple.syspolicy.kernel-extension-policy` as the `PayloadType` value. It is supported on macOS 10.13.2 and later.  

This profile must be delivered via a user approved MDM server.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`AllowUserOverrides`|Boolean|If set to `true`, users can approve additional kernel extensions not explicitly allowed by configuration profiles.|
|`AllowedTeamIdentifiers`|Array of Strings|An array of team identifiers that define which validly signed kernel extensions will be allowed to load.|
|`AllowedKernelExtensions`|Dictionary|A dictionary representing a set of kernel extensions that will always be allowed to load on the machine. The dictionary maps team identifiers (keys) to arrays of bundle identifiers.|
  
