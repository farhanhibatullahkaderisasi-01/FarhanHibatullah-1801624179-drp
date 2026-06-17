from tools import display_menu, select_menu

if __name__ == '__main__':

    print("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")
    print("Welcome To TaskMate📝")
    print("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")
    user = input ("Please, Enter Your Name Here!")

print ()

while True: 

    display_menu(user)

    menu = input("Enter the Feature Number You Want To Use (1-6): ")

    is_done = select_menu(menu=menu)

    if is_done:
        print(f"\nGood bye👋, {user}! Don't forget to complete your task! Have a great day🤩")
        break 
