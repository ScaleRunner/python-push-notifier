# Push Notifier
``push-notifier`` is a library for sending push notifications to supported clients.

Supported clients are:
* Prowl
* Pushover
* Pushsafer
* Custom Clients

**NOTE**: This repository is still in heavy development and is not production ready yet.

## Messages
Since different clients may require/use different fields, messages are generalized to the ``Message`` class. This class contains all possible fields and will be handled by the various clients.

The following fields are supported:
* ``receiver_key``: The API key of the receiver
* ``title``: Title of the notification
* ``description``: Description of the notification
* ``priority``: A priority value
* ``url``: URL that will be attached in the notification, this may contain URL schemes
* ``url_title``: A supplementary title for the URL
* ``application_name``: **Prowl Only** The name of your application
* ``providerkey``: **Prowl Only** Your provider API key. This key only has to be supplied if you have been whitelisted.
* ``images``: BASE64 encoded images to be attached to the notification
* ``device``: ID of the receivers device
* ``sound``: the name of one of the sounds supported by device clients to override the user's default sound choice
* ``timestamp``: a Unix timestamp of your message's date and time to display to the user, rather than the time your message is received by our API
* ``vibration``: Vibration of the notification
* ``icon``: Notification Icon
* ``icon_color``: Hexadecimal Colorcode for notifications
* ``time_to_live``: Number of minutes after which the message gets purged from the notification
* ``expire``: Time in seconds after which sending a failed notification should stop
* ``answer``: Whether you can answer the notification

The table below gives a summary of which clients support what:

Field | Prowl | Pushover | Pushsafer
:---- | :----:| :------: | :--------
``receiver_key`` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:
``title`` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:
``description`` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:
``priority`` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:
``url`` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:
``url_title`` | | :heavy_check_mark: | :heavy_check_mark:
``application_name`` | :heavy_check_mark: |  |
``providerkey`` | :heavy_check_mark: |  | 
``images`` | | :heavy_check_mark: (1) | :heavy_check_mark: (3)
``device`` | | :heavy_check_mark: | :heavy_check_mark:
``sound`` | | :heavy_check_mark: | :heavy_check_mark:
``timestamp`` | | | :heavy_check_mark:
``vibration`` | | | :heavy_check_mark:
``icon`` | | | :heavy_check_mark:
``icon_color`` | | | :heavy_check_mark:
``time_to_live`` | | | :heavy_check_mark:
``expire`` | | | :heavy_check_mark:
``answer`` | | | :heavy_check_mark:


## Prowl
[Prowl](https://www.prowlapp.com) is a push notification client for iOS devices.

#### Field Description
* ``receiver_key``: API keys of the receivers separated by commas. Each API key is a 40-byte hexadecimal string.
* ``application_name``: Name of your application
* ``title``: Subject of the notification.
* ``description``: A description of the event, generally terse.
* (``url``): The URL which should be attached to the notification. This will trigger a redirect when launched, and is viewable in the notification list.
* (``providerkey``): Application provider API key. Only necessary if you have been whitelisted.
* (``priority``): Priority value

## Pushover
[Pushover](https://pushover.net/) is a push notification client for iOS, Android and desktop.
