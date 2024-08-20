class ToDoList:
    def __init__(self):
        self.todo_list = []
        
    def add_to_do(self, task):
        self.todo_list.append(task)
        
    def remove_to_do(self, task):
        if task in self.todo_list:
            self.todo_list.remove(task)
            
    def view_to_do_list(self):
        for task in self.todo_list:
            print(task)

def main():
    todo_list = ToDoList()
    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. View task")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            task = input("Enter task to be added: ")
            todo_list.add_to_do(task)
        elif choice == 2:
            task = input("Enter task to be removed: ")
            todo_list.remove_to_do(task)
        elif choice == 3:
            todo_list.view_to_do_list()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()