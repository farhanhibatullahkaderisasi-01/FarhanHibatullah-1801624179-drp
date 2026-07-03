from tools import display_menu, select_menu

if __name__ == '__main__':

    print("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")
    print("Welcome To TaskMate📝")
    print("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")
    
    user = input ("Please, Enter Your Name Here!")

    exit_program = False

    while not exit_program:

        display_menu(user)

        menu = input("Enter the Feature Number (1-10): ").strip()
        
        exit_program = select_menu(menu)

    print(f"\nGood bye👋, {user}! Don't forget to complete your task! Have a great day🤩")