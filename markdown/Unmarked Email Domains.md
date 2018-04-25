# Unmarked Email Domains  

 [Configuration Profile Reference - Unmarked Email Domains](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW262)  

Any email address that does not have a suffix that matches one of the unmarked email domains specified by the key `EmailDomains` will be considered out-of-domain and will be highlighted as such in the Mail app.  

|Key|Type|Value|
|-|-|-|
|`EmailDomains`|Array|Optional. An array of strings. An email address lacking a suffix that matches any of these strings will be considered out-of-domain.|
  
