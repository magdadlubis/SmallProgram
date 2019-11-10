from typing import Union, List

from models import User, Message


class WrongParameterError(Exception):
    """Error when wrong params set is given"""
    pass


class Dispacher:
    def create_user(self, username: str, password: str) -> User:
        """Check if user exist in database and return True if password is correct."""
        raise NotImplementedError

    def login_user(self, username: str, password: str) -> Union[User, None]:
        """Check if user exist in database and return True if password is correct."""
        raise NotImplementedError

    def print_all_users(self) -> List[Union[User, None]]:
        """"""
        raise NotImplementedError

    def change_password(self, user: User, new_password: str) -> None:
        """"""
        raise NotImplementedError

    def delete_user(self, user: User) -> None:
        """"""
        raise NotImplementedError

    def list_messages(self, user: User) -> List[Union[Message, None]]:
        """"""
        raise NotImplementedError

    def send_message(self, adress: User, sender: User, message: str) -> Message:
        """"""
        raise NotImplementedError

    def not_available_option(self):
        """"""
        raise WrongParameterError("Wrong parameters set up!")