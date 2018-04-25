# Active Directory Payload  

 [Configuration Profile Reference - Active Directory Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW62)  

In macOS 10.9 and later, a configuration profile can be used to configure macOS to join an Active Directory (AD) domain. Advanced AD options available via Directory Utility or the `dsconfigad` command line tool can also be set using a configuration profile, following this procedure:  


1 Start with an macOS Directory payload, created in Profile Manager.  

2 Save and download the profile so you can edit it manually.  
  

The following AD configuration keys can be added to the Directory payload, of type `com.apple.DirectoryService.managed. `Note that some settings will only be set if the associated flag key is set to `true. `For example, `ADPacketEncryptFlag` must be set to `true` to set the `ADPacketEncrypt` key to `enable.`  

|Key|Type|Description|
|-|-|-|
|`HostName`|string|The Active Directory domain to join.|
|`UserName`|string|User name of the account used to join the domain.|
|`Password`|string|Password of the account used to join the domain.|
|`ADOrganizationalUnit`|string|The organizational unit (OU) where the joining computer object is added.|
|`ADMountStyle`|string|Network home protocol to use: “afp” or “smb”.|
|`ADCreateMobileAccountAtLoginFlag`|boolean|Enable or disable the ADCreateMobileAccountAtLogin key.|
|`ADCreateMobileAccountAtLogin`|boolean|Create mobile account at login.|
|`ADWarnUserBeforeCreatingMAFlag`|boolean|Enable or disable the ADWarnUserBeforeCreatingMA key.|
|`ADWarnUserBeforeCreatingMA`|boolean|Warn user before creating a Mobile Account.|
|`ADForceHomeLocalFlag`|boolean|Enable or disable the ADForceHomeLocal key.|
|`ADForceHomeLocal`|boolean|Force local home directory.|
|`ADUseWindowsUNCPathFlag`|boolean|Enable or disable the ADUseWindowsUNCPath key.|
|`ADUseWindowsUNCPath`|boolean|Use UNC path from Active Directory to derive network home location.|
|`ADAllowMultiDomainAuthFlag`|boolean|Enable or disable the ADAllowMultiDomainAuth key.|
|`ADAllowMultiDomainAuth`|boolean|Allow authentication from any domain in the forest.|
|`ADDefaultUserShellFlag`|boolean|Enable or disable the ADDefaultUserShell key.|
|`ADDefaultUserShell`|string|Default user shell; e.g. /bin/bash.|
|`ADMapUIDAttributeFlag`|boolean|Enable or disable the ADMapUIDAttribute key.|
|`ADMapUIDAttribute`|string|Map UID to attribute.|
|`ADMapGIDAttributeFlag`|boolean|Enable or disable the ADMapGIDAttribute key.|
|`ADMapGIDAttribute`|string|Map user GID to attribute.|
|`ADMapGGIDAttributeFlag`|boolean|Enable or disable the ADMapGGIDAttributeFlag key.|
|`ADMapGGIDAttribute`|string|Map group GID to attribute.|
|`ADPreferredDCServerFlag`|boolean|Enable or disable the ADPreferredDCServer key.|
|`ADPreferredDCServer`|string|Prefer this domain server.|
|`ADDomainAdminGroupListFlag`|boolean|Enable or disable the ADDomainAdminGroupList key.|
|`ADDomainAdminGroupList`|array of strings|Allow administration by specified Active Directory groups.|
|`ADNamespaceFlag`|boolean|Enable or disable the ADNamespace key.|
|`ADNamespace`|string|Set primary user account naming convention: “forest” or “domain”; “domain” is default.|
|`ADPacketSignFlag`|boolean|Enable or disable the ADPacketSign key.|
|`ADPacketSign`|string|Packet signing: "allow", "disable" or "require"; “allow” is default.|
|`ADPacketEncryptFlag`|boolean|Enable or disable the ADPacketEncrypt key.|
|`ADPacketEncrypt`|string|Packet encryption: "allow", "disable", "require" or "ssl"; “allow” is default.|
|`ADRestrictDDNSFlag`|boolean|Enable or disable the ADRestrictDDNS key.|
|`ADRestrictDDNS`|array of strings|Restrict Dynamic DNS updates to the specified interfaces (e.g. en0, en1, etc).|
|`ADTrustChangePassIntervalDaysFlag`|boolean|Enable or disable the ADTrustChangePassIntervalDays key.|
|`ADTrustChangePassIntervalDays`|number|How often to require change of the computer trust account password in days; “0” is disabled.|
  
