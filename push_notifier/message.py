from typing import NamedTuple, Optional, List


class Message(NamedTuple):
    """"
    Encapsulation of a message. Mind that not every attribute has to be
    initialized.

    Supported Fields

    * ``receiver_key``: The API key of the receiver
    * ``title``: Title of the notification
    * ``description``: Description of the notification
    * ``priority``: A priority value
    * | ``url``: URL that will be attached in the notification,
      | this may contain URL schemes
    * ``url_title``: A supplementary title for the URL
    * | ``providerkey``: **Prowl Only** Your provider API key. This key only
      | has to be supplied if you have been whitelisted.
    * application_name: Name of the application to be displayed by **Prowl**
    * | ``images``: List of BASE64 encoded images to be attached to the
      | notification
    * ``device``: ID of the receivers device
    * | ``sound``: the name of one of the sounds supported by device clients
      | to override the user's default sound choice
    * | ``timestamp``: a Unix timestamp of your message's date and time to
      | display to the user, rather than the time your message is received
      | by our API
    * ``vibration``: Vibration of the notification
    * ``icon``: Notification Icon
    * ``icon_color``: Hexadecimal Colorcode for notifications
    * | ``time_to_live``: Number of minutes after which the message gets
      | purged from the notification
    * | ``expire``: Time in seconds after which sending a failed
      | notification should stop
    * ``answer``: Whether you can answer the notification
    """
    receiver_key: str
    title: str
    description: str
    priority: Optional[int] = None
    url: Optional[str] = None
    url_title: Optional[str] = None
    provider_key: Optional[str] = None
    application_name: Optional[str] = None
    images: List[str] = []
    device: Optional[str] = None
    sound: Optional[int] = None
    timestamp: Optional[int] = None
    vibration: Optional[int] = None
    icon: Optional[int] = None
    icon_color: Optional[str] = None
    time_to_live: Optional[str] = None
    expire: Optional[int] = None
    answer: Optional[bool] = None
