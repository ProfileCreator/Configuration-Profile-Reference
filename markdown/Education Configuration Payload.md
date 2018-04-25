# Education Configuration Payload  

 [Configuration Profile Reference - Education Configuration Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW601)  

The Education Configuration Payload is designated by specifying `com.apple.education` as the `PayloadType` value. It can contain only one payload, which must be supervised. It is not supported on the User Channel.  

The Education Configuration Payload defines the users, groups, and departments within an educational organization. It is supported on iOS 9.3 and later.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`OrganizationUUID`|String|Required. The organization’s UUID identifier. This can be any valid UUID. All teacher and student devices that need to communicate with one another must have the same `OrganizationUUID`, particularly if they originated from different Device Enrollment Programs.|
|`OrganizationName`|String|Required. The organization’s display name. This name will be shown in the iOS login screen.|
|`PayloadCertificateUUID`|String|Required. The UUID of an identity certificate payload that will be used to perform client authentication with other devices.|
|`LeaderPayloadCertificateAnchorUUID`|Array|Optional. An array of UUIDs referring to certificate payloads that will be used to authorize leader peer certificate identities. This array must contain all certificates needed to validate the entire chain of trust. Leader certificates must have the common name prefix `leader` (case insensitive).|
|`MemberPayloadCertificateAnchorUUID`|Array|Optional. An array of UUIDs referring to certificate payloads that will be used to authorize group member peer certificate identities. This array must contain all certificates needed to validate the entire chain of trust. Member certificates must have the common name prefix `member` (case insensitive).|
|`UserIdentifier`|String|Optional. A unique string that identifies the user of this device within the organization.|
|`Departments`|Array|Optional. Shared: An array of dictionaries that define departments that are shown in the iOS login window.</br>Leader: An array of dictionaries that define departments that are shown in the Classroom app.|
|`Groups`|Array|Required. Shared: An array of dictionaries that define groups that the user can select in the login window.</br>Leader: An array of dictionaries that define the groups that the user can control.</br>Member: An array of dictionaries that define the groups of which the user is a member.|
|`Users`|Array|Required. Shared: An array of dictionaries that define the users that are shown in the iOS login window.</br>Leader: An array of dictionaries that define users that are members of the leader’s groups.</br>Member: An array of a dictionaries that must contain the definition of the user specified in the `UserIdentifier` key.</br>With one-to-one member devices, this key should include only the device user and the leader but not other class members.|
|`DeviceGroups`|Array|Optional. Leader: An array of dictionaries that define the device groups to which the leader can assign devices. This key is not included in member payloads.|
|`ScreenObservation- PermissionModification- Allowed`|Boolean|Optional. If set to `true`, students enrolled in managed classes can modify their teacher’s permissions for screen observation on this device. Defaults to `false`.|
  

The `Departments` key must contain an array of dictionaries with the following key-value pairs:  

|Key|Type|Content|
|-|-|-|
|`Name`|String|Required: the display name of the department.|
|`GroupBeaconIDs`|Array|Required: group beacon identifiers that are members of this department.|
  

The `Groups` key must contain an array of dictionaries with the following key-value pairs:  

|Key|Type|Content|
|-|-|-|
|`BeaconID`|Number|Required: unsigned 16 bit integer specifying this group’s unique beacon ID.|
|`Name`|String|Required: the display name of the group.|
|`Description`|String|Optional: description of the group.|
|`ImageURL`|String|**Deprecated in iOS 9.3.1 and later.** URL of an image for the group.|
|`ConfigurationSource`|String|Optional: the  source that provided this group; e.g. iTunesU, SIS, or MDM.|
|`LeaderIdentifiers`|Array|Optional: user identifiers that are leaders of this group.|
|`MemberIdentifiers`|Array|Required: strings that refer to entries in the `Users` array that are members of the group.|
|`DeviceGroupIdentifiers`|Array|Required: identifier strings that refer to entries in the `DeviceGroups` array that are device groups to which the instructor can assign users from this class.|
  

The `Users` key must contain an array of dictionaries with the following key-value pairs:  

|Key|Type|Content|
|-|-|-|
|`Identifier`|String|Required: uniquely identifies a user in the organization.|
|`Name`|String|Required: will be displayed as the name of the user.|
|`GivenName`|String|Optional: will be displayed as the given name of the user. |
|`FamilyName`|String|Optional: will be displayed as the family name of the user. |
|`ImageURL`|String|Optional: A string containing a URL pointing to an image of the user. This image will be displayed in the iOS login screen and in the Classroom app. The recommended resolution is 256 x 256 pixels (512 x 512 pixels on a 2x device). The recommended formats are JPEG, PNG, and TIFF. The `ResourcePayloadCertificateUUID` identity certificate or the MDM client identity will be used to perform authentication when fetching the image.|
|`FullScreenImageURL`|String|**Deprecated in iOS 9.3.1 and later.** URL pointing to an image of the user. The `ResourcePayloadCertificateUUID` identity certificate or the MDM client identity will be used to perform authentication when fetching the specified resource.|
|`AppleID`|String|Optional: the Managed Apple ID for this user.|
|`PasscodeType`|String|Optional: the passcode UI to show when the user is at the login window; possible values are `complex`, `four`, or `six`.|
  

The `DeviceGroups` key must contain an array of dictionaries with the following key-value pairs:  

|Key|Type|Content|
|-|-|-|
|`Identifier`|String|Required: uniquely identifies the device group in the organization.|
|`Name`|String|Required: will be displayed as the name of the device group, which must be unique in the organization.|
|`SerialNumbers`|Array|Required: strings containing the serial numbers of the devices in the group.|
  

**Notes:**  


* All identities must be configured as both SSL clients and servers.  

* Leader certificates must have the common name prefix `leader` (case insensitive).  

* Member certificates must have the common name prefix `member` (case insensitive).  
  
