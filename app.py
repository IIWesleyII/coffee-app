import db

MENU_PROMPT = '''
-- COFFEE BEAN APP --

Please choose an option:

1. Add a new bean
2. See all beans
3. Find a bean by name
4. See which preparation method is best for a bean
5. Exit

Your selection:
'''

def menu():
    conn = db.connect()
    db.create_table(conn)

    while (user_input := input(MENU_PROMPT)) != '5':
        if user_input == '1':
            name = input('Enter coffee bean name: ')
            method = input('Enter method in preparing coffee bean: ')
            rating = int(input('Enter bean rating: '))
            db.add_bean(conn,name,method,rating)

        elif user_input == '2':
            beans = db.get_all_beans(conn)
            for bean in beans:
                print(bean)

        elif user_input == '3':
            name = input('Enter coffee bean name: ')
            beans = db.get_beans_by_name(conn,name)
            for bean in beans:
                print(bean)
            
        elif user_input == '4':
            name = input("Enter bean name to find: ")
            best_method = db.get_best_preparation_by_bean(conn,name)
            print(f'The best preparation method for {name} is {best_method[2]}.')

        else:
            print('\n\n! INVALID INPUT !\n\n')

menu()