from manager.task_tracker import task_tracker
from manager.priority_task import priority_task
from manager.workload_monitor import workload_monitor
from manager.completion_progress import completion_progress
from manager.stress_reminder import stress_reminder
from export_import import export_json, import_json

def display_menu(user):

    print ()
    print ("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")
    print (f"Hello, {user}! Choose a feature you want to use!✨")
    print ("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")

    print ("1. Task Tracker 🧮")
    print ("2. Priority Task ⚡")
    print ("3. Workload Monitor📊")
    print ("4. Completion Progress 📈")
    print ("5. Stress Reminder 🧠")
    print ("6. Export Data 📤")
    print ("7. Import Data 📥")
    print ("8. Exit 🚪")

    print ("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")

def select_menu (menu):
    
    if menu == "1":
        task_tracker()

    elif menu == "2":
        priority_task()

    elif menu == "3":
        workload_monitor()

    elif menu == "4":
        completion_progress()

    elif menu == "5":
        stress_reminder()

    elif menu == "6":
        export_json()

    elif menu == "7":
        import_json()

    elif menu == "8":
        print ("\nExiting Program... ")
        return True
    
    else:
        print ("\n⚠️ Invalid Menu!")

    return False