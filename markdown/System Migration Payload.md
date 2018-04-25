# System Migration Payload  

 [Configuration Profile Reference - System Migration Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW221)  

The System Migration payload is designated by specifying `com.apple.systemmigration` as the `PayloadType`.  

System migration occurs when items are transferred to a macOS device from a Windows device by reading source and destination path pairs from plist files. This payload provides a way to customize those transfers.  

This payload must be single and exist only in a device profile. If the payload is present in a user profile, an error will be generated during installation and the profile will fail to install.  

This payload is supported only on macOS 10.12.4 and later.  

In addition to the settings common to all payloads, this payload defines the following key:  

|Key|Type|Value|
|-|-|-|
|`CustomBehavior`|Array of dictionaries|Optional. Specifies custom behavior for the context designated in each dictionary.|
  

Each dictionary in the `CustomBehavior` array contains these keys:  

|Key|Type|Value|
|-|-|-|
|`Context`|String|Required. The context to which custom paths apply.|
|`Paths`|Array of dictionaries|Required. The custom paths to be migrated from a source system to a target system.|
  

Each dictionary in the `Paths` array contains these keys:  

|Key|Type|Value|
|-|-|-|
|`SourcePath`|String|Required. The path to the migrating file or directory on the source system.|
|`SourcePathInUserHome`|Boolean|Required. If `true`, the source path is located within a user home directory.|
|`TargetPath`|String|Required. The path to the destination file or directory on the target system.|
|`TargetPathInUserHome`|Boolean|Required. If `true`, the target path is located within a user home directory.|
  
