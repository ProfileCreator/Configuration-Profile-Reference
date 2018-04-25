# Payload Dictionary Keys Common to All Payloads  

 [Configuration Profile Reference - Payload Dictionary Keys Common to All Payloads](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW1)  

If a `PayloadContent` value is provided in a payload, each entry in the array is a dictionary representing a configuration payload. The following keys are common to all payloads:  

|Key|Type|Content|
|-|-|-|
|`PayloadType`|String|The payload type. The payload types are described in [Payload-Specific Property Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW2).|
|`PayloadVersion`|Number|The version number of the individual payload.</br>A profile can consist of payloads with different version numbers. For example, changes to the VPN software in iOS might introduce a new payload version to support additional features, but Mail payload versions would not necessarily change in the same release.|
|`PayloadIdentifier`|String|A reverse-DNS-style identifier for the specific payload. It is usually the same identifier as the root-level `PayloadIdentifier` value with an additional component appended.|
|`PayloadUUID`|String|A globally unique identifier for the payload. The actual content is unimportant, but it must be globally unique. In macOS, you can use `uuidgen` to generate reasonable UUIDs.|
|`PayloadDisplayName`|String|A human-readable name for the profile payload. This name is displayed on the Detail screen. It does not have to be unique.|
|`PayloadDescription`|String|Optional. A human-readable description of this payload. This description is shown on the Detail screen.|
|`PayloadOrganization`|String|Optional. A human-readable string containing the name of the organization that provided the profile.</br>The payload organization for a payload need not match the payload organization in the enclosing profile.|
  
