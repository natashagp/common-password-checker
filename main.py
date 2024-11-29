def check_password(password: str):
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
        
    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: ❌ (#{i})')
            return
        elif password == '':
            print('Invalid password, try again')
            password: str = input('Please, enter a valid password: ')
        
    print(f'{password}: ✅ (Unique)')


def main():
    user_password: str = input('Enter a password: ')
    check_password(user_password)


if __name__ == '__main__':
    main()