from users import user_register,user_login,user_logout

while True:

    Menu = """
        ========== Menu ==========
        1.Registratsiya
        2.Login
        3.Logout
    """

    print(Menu)
    while True:
        choice = input('> ')
        if choice == '1':

            username = input('username: ')
            password = input('password: ')
            first_name = input('first_name: ')
            last_name = input('last_name: ')

            user_register(username,password,first_name,last_name)

        elif choice == '2':
            username = input('username: ')
            password = input('password: ')           
            user_login(username,password)
        elif choice == '3':
            username = input('username: ')
            password = input('password: ')   
            user_logout(username,password)
        else:
            print("Noto'g'ri tanlov qildingiz!")