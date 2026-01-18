#Aatiqa Attaullah
#First Task
#To-Do List Manager
import json
import os

class TodoManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("⚠ Corrupted file. Starting with empty list.")
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        title = input("Enter task title: ")
        due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
        tags = input("Enter tags (comma separated): ")

        task = {
            "title": title,
            "done": False,
            "due_date": due_date if due_date else None,
            "tags": [tag.strip() for tag in tags.split(",")] if tags else []
        }

        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.")
            return

        for i, task in enumerate(self.tasks, start=1):
            status = "✔ Done" if task["done"] else "❌ Pending"
            print(f"\n{i}. {task['title']}")
            print(f"   Status: {status}")
            print(f"   Due Date: {task['due_date']}")
            print(f"   Tags: {', '.join(task['tags'])}")

    def mark_done(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to mark done: ")) - 1
            self.tasks[index]["done"] = True
            self.save_tasks()
            print("✔ Task marked as done.")
        except (ValueError, IndexError):
            print("❌ Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"🗑 Task '{removed['title']}' deleted.")
        except (ValueError, IndexError):
            print("❌ Invalid task number.")

    def menu(self):
        while True:
            print("\n📋 TO-DO LIST MANAGER")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Done")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_done()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    app = TodoManager()
    app.menu()
