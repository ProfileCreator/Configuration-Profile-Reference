# Font Payload  

 [Configuration Profile Reference - Font Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW43)  

A Font payload lets you add an additional font to an iOS device. Font payloads are designated by specifying `com.apple.font` as the `PayloadType` value. You can include multiple Font payloads, as needed.  

A Font payload contains the following keys:  

|Key|Type|Value|
|-|-|-|
|`Name`|String|Optional. The user-visible name for the font. This field is replaced by the actual name of the font after installation.|
|`Font`|Data|The contents of the font file.|
  

Each payload must contain exactly one font file in TrueType (.ttf) or OpenType (.otf) format. Collection formats (.ttc or .otc) are not supported.  


> **Important:** Fonts are identified by their embedded PostScript names. Two fonts with the same PostScript name are considered to be the same font even if their contents differ. Installing two different fonts with the same PostScript name is not supported, and the resulting behavior is undefined.  
  
