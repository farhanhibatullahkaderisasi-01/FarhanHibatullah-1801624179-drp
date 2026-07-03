from manager.task_tracker import task_tracker
from manager.priority_task import priority_task
from manager.workload_monitor import workload_monitor
from manager.completion_progress import completion_progress
from manager.stress_reminder import stress_reminder
from export_import import export_json, import_json
from manager.task_statistics import task_statistics

from mapreduce_analysis import mapreduce_analysis

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
    print ("6. Task Statistics📋")
    print ("7. Export Data 📤")
    print ("8. Import Data 📥")
    print ("9. MapReduce Analysis")
    print ("10. Exit 🚪")

    print ("🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤")

def select_menu(menu):
    
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
        task_statistics()

    elif menu == "7":
        export_json()

    elif menu == "8":
        import_json()

    elif menu == "9":
        mapreduce_analysis()

    elif menu == "10":
        print ("\nExiting Program... ")
        return True

    else:
        print ("\n⚠️ Invalid Menu! Please choose 1-10")

    return False