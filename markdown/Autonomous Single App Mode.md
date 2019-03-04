# Autonomous Single App Mode  

 [Configuration Profile Reference - Autonomous Single App Mode](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW65)  

The payload is designated by specifying `com.apple.asam` as the `PayloadType`.  

This payload grants Autonomous Single App Mode capabilities for specific applications. Available in macOS 10.13.4 and later.  

It must be installed as a device profile. Only one payload of this type can be installed on a system. This payload can only be installed via a “user approved” MDM server.  


> **Note:** Applications listed in this payload will have low-level access to the system, including, but not limited to, key logging and user interface manipulation outside of the application's context.  
  

In addition to the settings common to all payloads, this payload defines the following key:  

|Key|Type|Value|
|-|-|-|
|`AllowedApplications`|Array|Array of dictionaries that specify applications that are to be granted access to Assessment APIs.|
  

Each dictionary in the `AllowedApplications` array consists of:  

|Key|Type|Value|
|-|-|-|
|`BundleIdentifier`|String|The application’s bundle identifier. `BundleIdentifier` must be unique. If two dictionaries contain the same `BundleIdentifier` but different `TeamIdentifiers`, this will be considered a hard error and the payload will not be installed.|
|`TeamIdentifier`|String|The developer’s team identifier used to sign the application.|
  

To be granted access, applications must be signed with the specified bundle identifier and team identifier using an Apple-issued production developer certificate. Applications must specify the `com.apple.developer.assessment` entitlement with a value of `true`.  
