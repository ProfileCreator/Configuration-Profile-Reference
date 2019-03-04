# LDAP Payload  

 [Configuration Profile Reference - LDAP Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW14)  

The LDAP payload is designated by specifying `com.apple.ldap.account` as the `PayloadType` value.  

An LDAP payload provides information about an LDAP server to use, including account information if required, and a set of LDAP search policies to use when querying that LDAP server.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`LDAPAccountDescription`|String|Optional. Description of the account.|
|`LDAPAccountHostName`|String|The host.|
|`LDAPAccountUseSSL`|Boolean|Whether or not to use SSL.|
|`LDAPAccountUserName`|String|Optional. The username.|
|`LDAPAccountPassword`|String|Optional. Use only with encrypted profiles.|
|`LDAPSearchSettings`|Dictionary|Top level container object. Can have many of these for one account. Should have at least one for the account to be useful.</br>Each `LDAPSearchSettings` object represents a node in the LDAP tree to start searching from, and tells what scope to search in (the node, the node plus one level of children, or the node plus all levels of children).|
|`LDAPSearchSettingDescription`|String|Optional. Description of this search setting.|
|`LDAPSearchSettingSearchBase`|String|Conceptually, the path to the node where a search should start. For example:</br>`ou=people,o=example corp`|
|`LDAPSearchSettingScope`|String|Defines what recursion to use in the search.</br>Can be one of the following 3 values:</br>LDAPSearchSettingScopeBase: Just the immediate node pointed to by SearchBase</br>LDAPSearchSettingScopeOneLevel: The node plus its immediate children.</br>LDAPSearchSettingScopeSubtree: The node plus all children, regardless of depth.|
  
