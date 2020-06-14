import argparse

from dispacher import Dispacher
from logic_handler import OptionsHandler
from models import User, get_cursor, create_connection

parser = argparse.ArgumentParser(description='Program options')
parser.add_argument('--username', '-u', help='Login - user email', action='store')
parser.add_argument('--password', '-p', help='User password', action='store')
parser.add_argument('--new-password', '-n', help='New password', action='store')
parser.add_argument('--edit', '-e', help='Edit', action='store_true')
parser.add_argument('--delete', '-d', help='Delete user', action='store_true')
parser.add_argument('--list', '-l', help='List of user or massages', action='store_true')
parser.add_argument('--send', '-s', help='Send', action='store')
parser.add_argument('--to', '-t', help='Address of message', action='store')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)

    connection = create_connection()
    cursor = get_cursor(connection)

    dispacher = Dispacher(cursor)

    option_handler = OptionsHandler(
        args.password, args.username, args.new_password, args.edit, args.delete, args.list, args.send, args.to
    )

    if option_handler.create_user:
        dispacher.create_user(args.username, args.password)
        print('User Created')
    elif option_handler.list_all_users:
        print('All users list')
        dispacher.all_users_list()
    elif option_handler.list_all_messages_for_user:
        print('All messages for user')
        user = dispacher.login_user(args.username, args.password)
        if user:
            dispacher.list_messages_to_user(user)
        else:
            raise Exception('Incorrect user')
    elif option_handler.change_password:
        user = dispacher.login_user(args.username, args.password)
        if user:
            dispacher.change_password(user=user, new_password=args.new_password)
            print('Password Changed!')
        else:
            raise Exception('Incorrect user')
    elif option_handler.send_message:
        user = dispacher.login_user(args.username, args.password)
        if user:
            user_to = User.load_by_id(cursor, args.to)
            dispacher.send_message(user_to, user, args.send)
        print('Message send from user to user with txt')
    elif option_handler.delete_user:
        dispacher.delete_user(dispacher.login_user(args.username, args.password))
        print('User deleted')
    else:
        print('Available options:')
        print('Create user: -u {user_name} -p {password}')
        print('List all users: -l')
        print('All messages for user: -u {user_name} -p {password} -l')
        print('Change password: -u {user_name} -p {password} -e -n {new_password}')
        print('Send message: -u {user_name} -p {password} -t {to} -s "{text_msg}"')
        print('Delete user: -u {user_name} -p {password} -d')

    cursor.close()
    connection.close()