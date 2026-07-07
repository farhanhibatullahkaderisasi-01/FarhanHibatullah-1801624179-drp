from tools import display_menu, select_menu
import sqlite3
import os 

if __name__ == '__main__':

    print("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")
    print("Welcome To TaskMate📝")
    print("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")
    
    user = input ("Please, Enter Your Name Here!")

    user_lama = ""

    if os.path.exists("current_user.txt"):
        with open ("current_user.txt", "r") as file:
            user_lama = file.read()
    
    if user != user_lama:
        conn = sqlite3.connect("taskmate.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM task")
        cursor.execute("DELETE FROM priority")
        cursor.execute("DELETE FROM progress")
        cursor.execute("DELETE FROM reminder")

        cursor.execute("DELETE FROM sqlite_sequence WHERE name='task'")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='priority'")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='progress'")  
        cursor.execute("DELETE FROM sqlite_sequence WHERE name= 'reminder'")        

        conn.commit() 
        conn.close()
    
    with open ("current_user.txt", "w") as file:
        file.write(user)

    exit_program = False

    while not exit_program:

        display_menu(user)

        menu = input("Enter the Feature Number (1-10): ").strip()
        
        exit_program = select_menu(menu)

    print(f"\nGood bye👋, {user}! Don't forget to complete your task! Have a great day🤩")