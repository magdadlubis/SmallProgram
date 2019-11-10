import argparse

from dispacher import Dispacher

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
    dispacher = Dispacher()

    if args.username and args.password:
        if not all([args.edit, args.delete, args.send, args.list, args.to, args.new_password]):
            print('Create User')
        elif all([args.edit, args.new_password]) and not all([args.delete, args.send, args.list, args.to]):
            print('Change Password')
    elif args.list and \
        not all([args.edit, args.delete, args.send, args.username, args.to, args.new_password, args.password]):
        print('All users')
    else:
        dispacher.not_available_option()