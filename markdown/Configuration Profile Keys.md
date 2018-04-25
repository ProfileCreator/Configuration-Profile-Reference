# Configuration Profile Keys  

 [Configuration Profile Reference - Configuration Profile Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW7)  

At the top level, a profile property list contains the following keys:  

|Key|Type|Content|
|-|-|-|
|`PayloadContent`|Array|Optional. Array of payload dictionaries. Not present if IsEncrypted is `true`.|
|`PayloadDescription`|String|Optional. A description of the profile, shown on the Detail screen for the profile. This should be descriptive enough to help the user decide whether to install the profile.|
|`PayloadDisplayName`|String|Optional. A human-readable name for the profile. This value is displayed on the Detail screen. It does not have to be unique.|
|`PayloadExpirationDate`|Date|Optional. A date on which a profile is considered to have expired and can be  updated over the air. This key is only used if the profile is delivered via over-the-air profile delivery.|
|`PayloadIdentifier`|String|A reverse-DNS style identifier (com.example.myprofile, for example) that identifies the profile. This string is used to determine whether a new profile should replace an existing one or should be added.|
|`PayloadOrganization`|String|Optional. A human-readable string containing the name of the organization that provided the profile.|
|`PayloadUUID`|String|A globally unique identifier for the profile. The actual content is unimportant, but it must be globally unique. In macOS, you can use `uuidgen` to generate reasonable UUIDs.|
|`PayloadRemovalDisallowed`|Boolean|Optional. Supervised only. If present and set to `true`, the user cannot delete the profile (unless the profile has a removal password and the user provides it).|
|`PayloadType`|String|The only supported value is `Configuration`.|
|`PayloadVersion`|Integer|The version number of the profile format. This describes the version of the configuration profile as a whole, not of the individual profiles within it.</br>Currently, this value should be `1`.|
|`PayloadScope`|String|Optional. Determines if the profile should be installed for the system or the user. In many cases, it determines the location of the certificate items, such as keychains. Though it is not possible to declare different payload scopes, payloads, like VPN, may automatically install their items in both scopes if needed.</br>Legal values are `System` and `User`, with `User` as the default value.</br>**Availability:** Available in macOS 10.7 and later.|
|`RemovalDate`|Date|Optional. The date on which the profile will be automatically removed.|
|`DurationUntilRemoval`|Float|Optional. Number of seconds until the profile is automatically removed. If the `RemovalDate` keys is present, whichever field yields the earliest date will be used.|
|`ConsentText`|Dictionary|Optional. A dictionary containing these keys and values:</br></br>* For each language in which a consent or license agreement is available, a key consisting of the IETF BCP 47 identifier for that language (for example, `en` or `jp`) and a value consisting of the agreement localized to that language. The agreement is displayed in a dialog to which the user must agree before installing the profile.  </br></br>* The optional key `default` with its value consisting of the unlocalized agreement (usually in `en`).  </br></br></br>The system chooses a localized version in the order of preference specified by the user (macOS) or based on the user’s current language setting (iOS). If no exact match is found, the default localization is used. If there is no default localization, the `en` localization is used. If there is no `en` localization, then the first available localization is used.</br>You should provide a default value if possible. No warning will be displayed if the user’s locale does not match any localization in the `ConsentText` dictionary.|
  


> **Note:** 
Profile payload dictionary keys that are prefixed with “Payload” are reserved key names and must never be treated as managed preferences. Any other key in the payload
dictionary may be considered a managed preference for that preference domain.  
  

Keys in the payload dictionary are described in detail in the next section.  
