# Active Directory Payload  

 [Configuration Profile Reference - Active Directory Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW62)  

In macOS 10.9 and later, a configuration profile can be used to configure macOS to join an Active Directory (AD) domain. Advanced AD options available via Directory Utility or the `dsconfigad` command line tool can also be set using a configuration profile, following this procedure:  


1 Start with a macOS Directory payload, created in Profile Manager.  

2 Save and download the profile so you can edit it manually.  
  

The following AD configuration keys can be added to the Directory payload, of type `com.apple.DirectoryService.managed. `Note that some settings will only be set if the associated flag key is set to `true. `For example, `ADPacketEncryptFlag` must be set to `true` to set the `ADPacketEncrypt` key to `enable.`  

|Key|Type|Description|
|-|-|-|
|`HostName`|String|The Active Directory domain to join.|
|`UserName`|String|User name of the account used to join the domain.|
|`Password`|String|Password of the account used to join the domain.|
|`ADOrganizationalUnit`|String|The organizational unit (OU) where the joining computer object is added.|
|`ADMountStyle`|String|Network home protocol to use: “afp” or “smb”.|
|`ADCreateMobileAccountAtLoginFlag`|Boolean|Enable or disable the ADCreateMobileAccountAtLogin key.|
|`ADCreateMobileAccountAtLogin`|Boolean|Create mobile account at login.|
|`ADWarnUserBeforeCreatingMAFlag`|Boolean|Enable or disable the ADWarnUserBeforeCreatingMA key.|
|`ADWarnUserBeforeCreatingMA`|Boolean|Warn user before creating a Mobile Account.|
|`ADForceHomeLocalFlag`|Boolean|Enable or disable the ADForceHomeLocal key.|
|`ADForceHomeLocal`|Boolean|Force local home directory.|
|`ADUseWindowsUNCPathFlag`|Boolean|Enable or disable the ADUseWindowsUNCPath key.|
|`ADUseWindowsUNCPath`|Boolean|Use UNC path from Active Directory to derive network home location.|
|`ADAllowMultiDomainAuthFlag`|Boolean|Enable or disable the ADAllowMultiDomainAuth key.|
|`ADAllowMultiDomainAuth`|Boolean|Allow authentication from any domain in the forest.|
|`ADDefaultUserShellFlag`|Boolean|Enable or disable the ADDefaultUserShell key.|
|`ADDefaultUserShell`|String|Default user shell; e.g. /bin/bash.|
|`ADMapUIDAttributeFlag`|Boolean|Enable or disable the ADMapUIDAttribute key.|
|`ADMapUIDAttribute`|String|Map UID to attribute.|
|`ADMapGIDAttributeFlag`|Boolean|Enable or disable the ADMapGIDAttribute key.|
|`ADMapGIDAttribute`|String|Map user GID to attribute.|
|`ADMapGGIDAttributeFlag`|Boolean|Enable or disable the ADMapGGIDAttributeFlag key.|
|`ADMapGGIDAttribute`|String|Map group GID to attribute.|
|`ADPreferredDCServerFlag`|Boolean|Enable or disable the ADPreferredDCServer key.|
|`ADPreferredDCServer`|String|Prefer this domain server.|
|`ADDomainAdminGroupListFlag`|Boolean|Enable or disable the ADDomainAdminGroupList key.|
|`ADDomainAdminGroupList`|Array of Strings|Allow administration by specified Active Directory groups.|
|`ADNamespaceFlag`|Boolean|Enable or disable the ADNamespace key.|
|`ADNamespace`|String|Set primary user account naming convention: “forest” or “domain”; “domain” is default.|
|`ADPacketSignFlag`|Boolean|Enable or disable the ADPacketSign key.|
|`ADPacketSign`|String|Packet signing: "allow", "disable" or "require"; “allow” is default.|
|`ADPacketEncryptFlag`|Boolean|Enable or disable the ADPacketEncrypt key.|
|`ADPacketEncrypt`|String|Packet encryption: "allow", "disable", "require" or "ssl"; “allow” is default.|
|`ADRestrictDDNSFlag`|Boolean|Enable or disable the ADRestrictDDNS key.|
|`ADRestrictDDNS`|Array of Strings|Restrict Dynamic DNS updates to the specified interfaces (e.g. en0, en1, etc).|
|`ADTrustChangePassIntervalDaysFlag`|Boolean|Enable or disable the ADTrustChangePassIntervalDays key.|
|`ADTrustChangePassIntervalDays`|Integer|How often to require change of the computer trust account password in days; “0” is disabled.|
  
