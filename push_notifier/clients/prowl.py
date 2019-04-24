import requests
from xml.etree import ElementTree

from push_notifier.clients.client import Client

#: The default Prowl API endpoint format string
from push_notifier.message import Message

PROWL_API_URL = "https://api.prowlapp.com/publicapi/{method}"


class Prowl(Client):
    """"
    Constructs a Prowl object. This object is used to interact with the
    Prowl API.
    """

    attribute_mapping = {
        "receiver_key": "apikey",
        "title": "event",
        "description": "description",
        "application_name": "application",
        "provider_key": "providerkey",
        "priority": "priority",
        "url": "url",
        "url_title": "url_title"
    }

    def __init__(self):
        super().__init__()
        self.required_attributes.append("application_name")

    @staticmethod
    def _delegate_error(request):
        def parse_error(content: bytes) -> str:
            content = content.decode("utf-8")
            tree = ElementTree.fromstring(content)
            error = tree.find("error")
            return error.text

        if request.status_code == 400:
            error_message = parse_error(request.content)
        elif request.status_code == 401:
            error_message = f"The provided receiver_key " \
                f"'{message.receiver_key}' is invalid and " \
                f"does not correspond to a user."
        elif request.status_code == 406:
            error_message = "Your IP address has exceeded the API limit"
        elif request.status_code == 409:
            error_message = "The user has yet to approve your retrieve request"
        else:
            error_message = "Something failed to execute properly " \
                            "on the Prowl side"

        raise ConnectionError(f"Error {request.status_code} ({request.reason}: "
                              f"{error_message}")

    def post(self, message: Message):
        """" Send a POST request to the Prowl API.
        """
        post_attributes = self.get_request_data(message)

        request = requests.post(
            PROWL_API_URL.format(method="add"),
            data=post_attributes
        )

        if not request.ok:
            self._delegate_error(request)


if __name__ == "__main__":
    prowl = Prowl()

    message = Message(
        "a8e8f0591a713d58b65e44a9cb0bae89d412286f",
        "Title", "Description", -2, "http://fake_url.com",
        application_name="Test", url_title="LUL"
    )

    prowl.post(message)