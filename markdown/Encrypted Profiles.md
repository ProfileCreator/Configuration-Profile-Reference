# Encrypted Profiles  

 [Configuration Profile Reference - Encrypted Profiles](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW52)  

A profile can be encrypted so that it can only be decrypted using a private key previously installed on a device.  

To encrypt a profile do the following:  


1 Remove the `PayloadContent` array and serialize it as a proper plist. Note that the top-level object in this plist is an array, not a dictionary.  

2 CMS-encrypt the serialized plist as enveloped data.  

3 Serialize the encrypted data in DER format.  

4 Set the serialized data as the value of as a Data plist item in the profile, using the key `EncryptedPayloadContent`.  
  
