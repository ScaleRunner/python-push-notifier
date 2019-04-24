from abc import abstractmethod
from typing import Dict, Any

from push_notifier.message import Message


class Client:

    #: Required attributes in messages
    required_attributes = [
        "receiver_key", "title", "description"
    ]

    @property
    @abstractmethod
    def attribute_mapping(self) -> Dict[str, str]:
        """"
        This property holds the mapping from the Message fields to the
        supported fields in the client API
        """
        ...

    @abstractmethod
    def post(self, message: Message):
        """"
        This function would should perform the actual post request
        """
        ...

    def get_request_data(self, message: Message) -> Dict[str, Any]:
        request_dict = {}
        for message_field, api_field in self.attribute_mapping.items():
            attr = getattr(message, message_field)
            if message_field in self.required_attributes and \
                    attr is None:
                raise ValueError(f"Attribute {message_field} is not defined!")
            elif attr is not None:
                request_dict[api_field] = attr

        return request_dict
