# Loginwindow Payload  

 [Configuration Profile Reference - Loginwindow Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW101)  

The Loginwindow payload is designated by specifying `com.apple.loginwindow` as the `PayloadType` value.  

This payload creates managed preferences on all versions of macOS for system and device profiles. Multiple Loginwindow payloads may be installed together.  

In addition to the settings common to all payloads, this payload defines these keys:  

|Key|Type|Value|
|-|-|-|
|`SHOWFULLNAME`|Boolean|Optional. Set to `true` to show the name and password dialog. Set to `false` to display a list of users.|
|`HideLocalUsers`|Boolean|Optional. When showing a user list, set to `true` to  show only network and system users.|
|`IncludeNetworkUser`|Boolean|Optional. When showing a user list, set to `true` to show network users.|
|`HideAdminUsers`|Boolean|Optional. When showing a user list, set to `false` to hide the administrator users.|
|`SHOWOTHERUSERS_MANAGED`|Boolean|Optional. When showing a list of users, set to `true` to display Other... users.|
|`AdminHostInfo`|String|Optional. If this key is included in the payload, its value will be displayed as additional computer information on the login window. Before macOS 10.10, this string could contain only particular information (`HostName`, `SystemVersion`, or `IPAddress`). After macOS 10.10, setting this key to any value will allow the user to click the “time” area of the menu bar to toggle through various computer information values.|
|`AllowList`|Array of Strings|Optional. User or group GUIDs of users that are allowed to log in. An asterisk '*' string specifies all users or groups.|
|`DenyList`|Array of Strings|Optional. User or group GUIDs of users that cannot log in. This list takes priority over the list in the `AllowList` key.|
|`HideMobileAccounts`|Boolean|Optional. If set to `true`, mobile account users will not be visible in a user list. In some cases mobile users will show up as network users.|
|`ShutDownDisabled`|Boolean|Optional. If set to `true`, the Shut Down button item will be hidden.|
|`RestartDisabled`|Boolean|Optional. If set to `true`, the Restart item will be hidden.|
|`SleepDisabled`|Boolean|Optional. If set to `true`, the Sleep button item will be hidden.|
|`DisableConsoleAccess`|Boolean|Optional. If set to `true`, the Other user will disregard use of the '>console' special user name.|
|`LoginwindowText`|String|Optional. Text to display in the login window.|
|`ShutDownDisabledWhileLoggedIn`|Boolean|Optional. If set to `true`, the Shut Down menu item will be disabled when the user is logged in.|
|`RestartDisabledWhileLoggedIn`|Boolean|Optional. If set to `true`, the Restart menu item will be disabled when the user is logged in.|
|`PowerOffDisabledWhileLoggedIn`|Boolean|Optional. If set to `true`, the Power Off menu item will be disabled when the user is logged in.|
|`DisableLoginItemsSuppression`|Boolean|Optional. If set to `true`, the user is prevented from disabling login item launching using the Shift key.|
  
