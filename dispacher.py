from typing import Union, List

from clcrypto import generate_salt
from models import User, Message, get_cursor, create_connection

class WrongParameterError(Exception):
    """Error when wrong params set is given"""
    pass


class Dispacher:
    """HINT: USERNAME == EMAIL """

    def __init__(self, cursor):
        self.cursor = cursor

    #connection = create_connection()
    #cursor = get_cursor(connection)

    def login_user(self, email: str, password: str) -> Union[User, None]:
        """Check if user exist in database and return True if password is correct."""
        user = User.load_by_email(self.cursor, email=email)
        if user:
            if user.check_password(password):
                return user
            else:
                raise Exception("Incorrect password")
        #raise NotImplementedError

    def create_user(self, email: str, password: str) -> User:
        """Create user to User table"""
        if not self.login_user(email=email, password=password):
            user = User()
            user.email = email
            salt = generate_salt()
            user.set_password(password, salt)
            user.save(self.cursor)
            return user
        else:
            raise Exception("User already exist")
        #raise NotImplementedError

    def all_users_list(self) -> List[Union[User, None]]:
        """Print all users which are in database"""
        users = User.load_all(self.cursor)
        for user in users:
            print("User ID: {user_id}\nUsername: {username}\nE-mail: {email}\n".format(user_id=user.id, username=user.username, email=user.email))
        #raise NotImplementedError

    def list_messages_to_user(self, user: User) -> List[Union[Message, None]]:
        """Return list of all messages in database for specific user"""
        messages = Message.load_all_messages_for_user(cursor=self.cursor, to_id=user.id)
        lp = 1
        if messages:
            for message in messages:
                print('{}. Data: {} Od: {} Do: {} Message: {}'.format(lp, message.creation_date, message.from_id, message.to_id, message.text))
                lp += 1
        else:
            print("You don't have any messages")
        #raise NotImplementedError

    def change_password(self, user: User, new_password: str) -> None:
        """Change password of given user to new one"""
        salt = generate_salt()
        user.set_password(new_password, salt)
        user.save(self.cursor)
        #raise NotImplementedError

    def send_message(self, adress: User, sender: User, message: str) -> Message:
        """Create message to adress (User) to sender (User) into database."""
        text = message.strip()
        if text:
            message = Message()
            message.from_id = sender.id
            message.to_id = adress.id
            message.text = text
            message.save(self.cursor)
            return message
        else:
            raise Exception('Your message is empty')
        #raise NotImplementedError

    def delete_user(self, user: User) -> None:
        """Delete given user"""
        user.delete(self.cursor)
        #raise NotImplementedError

    def not_available_option(self):
        """No other available option"""
        raise WrongParameterError("Wrong parameters set up!")




#d = Dispacher()
#Dispacher.login_user(d, email="user1@domain.com", password="pass")
