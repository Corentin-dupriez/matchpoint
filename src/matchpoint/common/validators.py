from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import re


@deconstructible
class ValidHoursValidator:
    def __init__(self, message=None) -> None:
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not value:
            value = "Incorrect time"
        self.__message = value

    def __call__(self, value: str) -> None:
        if not re.match(r"^([0-1][0-9]|2[0-4]):[0-5][0-9]$", value):
            raise ValidationError(message=self.message)
        hours, min = value.split(":")
        print(hours, min)
        if int(hours) < 0 or int(hours) > 24 or int(min) < 0 or int(min) > 59:
            raise ValidationError(message=self.message)
