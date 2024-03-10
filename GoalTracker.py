import tkinter as tk
from tkinter import messagebox

class GoalTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Goal Tracker")

        self.goals = {
            "Weight Training": {"target": 120, "current": 30},

            # Add more goals here
        }

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New Goal", command=self.new_goal)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def create_widgets(self):
        for goal, progress in self.goals.items():
            frame = tk.Frame(self.master)
            frame.pack(fill=tk.X, padx=10, pady=5)

            label = tk.Label(frame, text=goal, width=15)
            label.pack(side=tk.LEFT)

            progress_bar = tk.Canvas(frame, width=200, height=20, bg='white')
            progress_bar.pack(side=tk.LEFT, padx=10)

            progress_bar.create_rectangle(0, 0, progress["current"] / progress["target"] * 200, 20, fill="green")

    def new_goal(self):
        def add_goal():
            goal_name = name_entry.get()
            if goal_name:
                self.goals[goal_name] = {"target": 0, "current": 0}
                messagebox.showinfo("Success", f"New goal '{goal_name}' added successfully!")
                self.master.destroy()
                self.__init__(tk.Tk())  # Refresh the GUI with the new goal
            else:
                messagebox.showerror("Error", "Goal name cannot be empty!")

        new_goal_window = tk.Toplevel(self.master)
        new_goal_window.title("Add New Goal")

        name_label = tk.Label(new_goal_window, text="Goal Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5)

        name_entry = tk.Entry(new_goal_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        add_button = tk.Button(new_goal_window, text="Add", command=add_goal)
        add_button.grid(row=1, column=0, columnspan=2, pady=10)

def main():
    root = tk.Tk()
    app = GoalTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
