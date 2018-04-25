# AirPrint Payload  

 [Configuration Profile Reference - AirPrint Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW39)  

The AirPrint payload adds AirPrint printers to the user’s AirPrint printer list. This makes it easier to support environments where the printers and the devices are on different subnets. An AirPrint payload is designated by specifying `com.apple.airprint` as the `PayloadType` value.  

This payload is supported on iOS 7.0 and later and on macOS 10.10 and later.  

|Key|Type|Value|
|-|-|-|
|`AirPrint`|Array of dictionaries|An array of AirPrint printers that should always be shown.|
  

Each dictionary in the `AirPrint` array must contain the following keys and values:  

|Key|Type|Value|
|-|-|-|
|`IPAddress`|String|The IP Address of the AirPrint destination.|
|`ResourcePath`|String|The Resource Path associated with the printer. This corresponds to the `rp` parameter of the `_ipps.tcp` Bonjour record. For example:</br></br>* `printers/Canon_MG5300_series`  </br></br>* `printers/Xerox_Phaser_7600`  </br></br>* `ipp/print`  </br></br>* `Epson_IPP_Printer`  </br></br>|
|`Port`|Number|Listening port of the AirPrint destination. If this key is not specified AirPrint will use the default port.</br>**Availability:** Available only in iOS 11.0 and later.|
|`ForceTLS`|Boolean|If `true` AirPrint connections are secured by Transport Layer Security (TLS). Default is `false`.</br>**Availability:** Available only in iOS 11.0 and later.|
  
