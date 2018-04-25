# SCEP Payload  

 [Configuration Profile Reference - SCEP Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW18)  

The SCEP (Simple Certificate Enrollment Protocol) payload is designated by specifying `com.apple.security.scep` as the `PayloadType` value.  

An SCEP payload automates the request of a client certificate from an SCEP server, as described in *[Over-the-Air Profile Delivery and Configuration](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009505)*.  

In addition to the settings common to all payloads, this payload defines the following keys:  

|Key|Type|Value|
|-|-|-|
|`URL`|String|The SCEP URL. See *[Over-the-Air Profile Delivery and Configuration](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009505)* for more information about SCEP.|
|`Name`|String|Optional. Any string that is understood by the SCEP server. For example, it could be a domain name like `example.org`. If a certificate authority has multiple CA certificates this field can be used to distinguish which is required.|
|`Subject`|Array|Optional. The representation of a X.500 name represented as an array of OID and value. For example, `/C=US/O=Apple Inc./CN=foo/1.2.5.3=bar`, which would translate to:</br>`[ [ ["C", "US"] ], [ ["O", "Apple Inc."] ], ..., [ [ "1.2.5.3", "bar" ] ] ]`</br>OIDs can be represented as dotted numbers, with shortcuts for country (`C`), locality (`L`), state (`ST`), organization (`O`), organizational unit (`OU`), and common name (`CN`).|
|`Challenge`|String|Optional. A pre-shared secret.|
|`Keysize`|Number|Optional. The key size in bits, either 1024 or 2048.|
|`KeyType`|String|Optional. Currently always "RSA".|
|`KeyUsage`|Number|Optional. A bitmask indicating the use of the key. 1 is signing, 4 is encryption, 5 is both signing and encryption. Some certificate authorities, such as Windows CA, support only encryption or signing, but not both at the same time.</br>**Availability:** Available only in iOS 4 and later.|
|`Retries`|Integer|Optional. The number of times the device should retry if the server sends a PENDING response. Defaults to 3.|
|`RetryDelay`|Integer|Optional. The number of seconds to wait between subsequent retries. The first retry is attempted without this delay. Defaults to 10.|
  

### SubjectAltName Dictionary Keys  

 [Configuration Profile Reference - SubjectAltName Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW18)  

The SCEP payload can specify an optional `SubjectAltName` dictionary that provides values required by the CA for issuing a certificate. You can specify a single string or an array of strings for each key.  

The values you specify depend on the CA you're using, but might include DNS name, URL, or email values. For an example, see [Sample Configuration Profile](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW3) or read *[Over-the-Air Profile Delivery and Configuration](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009505)*.  
  

### GetCACaps Dictionary Keys  

 [Configuration Profile Reference - GetCACaps Dictionary Keys](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW18)  

If you add a dictionary with the key `GetCACaps`, the device uses the strings you provide as the authoritative source of information about the capabilities of your CA. Otherwise, the device queries the CA for `GetCACaps` and uses the answer it gets in response.If the CA doesn't respond, the device defaults to `GET 3DES` and `SHA-1` requests. For more information, read *[Over-the-Air Profile Delivery and Configuration](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009505)*. This feature is not supported in macOS.  
  
