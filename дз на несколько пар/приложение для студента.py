import tkinter as tk
from tkinter import messagebox
import json
import os



class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Дневник с расписанием")
        self.root.geometry("600x520")
        self.root.configure(bg="white")

        self.schedule = {
            "Понедельник": [
                {"time": "10:05-11:30", "name": "Математика", "room": "В 329", "teacher": "Вольнова Д.В.",
                 "type": "Лек"},
                {"time": "11:40-13:05", "name": "Основы предпринимательской деятельности", "room": "В 380",
                 "teacher": "Плешакова Е.А.", "type": "Лек"}
            ],
            "Вторник": [
                {"time": "13:45-15:10", "name": "Основы коммуникационного дизайна", "room": "С 407",
                 "teacher": "Талант В.В.", "type": "Пр"},
                {"time": "15:20-16:45", "name": "Мультимедиа-технологии", "room": "С 407",
                 "teacher": "Ярославцева Е.К.", "type": "Пр"},
                {"time": "16:55-18:20", "name": "Алгоритмизация и программирование", "room": "С 407",
                 "teacher": "Баев Н.А.", "type": "Пр"}
            ],
            "Среда": [
                {"time": "11:40-13:05", "name": "Алгоритмизация и программирование", "room": "В 452",
                 "teacher": "Якуничева Е.Н.", "type": "Лек"},
                {"time": "13:45-15:10", "name": "Философия", "room": "В 405", "teacher": "-", "type": "Пр"}
            ],
            "Четверг": [
                {"time": "15:20-16:45", "name": "Философия", "room": "В 406", "teacher": "-", "type": "Лек"},
                {"time": "16:55-18:20", "name": "Математика", "room": "В 324", "teacher": "Евсеев Е.А.", "type": "Пр"}
            ],
            "Пятница": [
                {"time": "11:40-13:05", "name": "Физика", "room": "334", "teacher": "-", "type": "Лаб"},
                {"time": "13:45-15:10", "name": "Практикум по физ. культуре", "room": "Спортзал", "teacher": "-",
                 "type": "Пр"},
                {"time": "15:20-16:45", "name": "Иностранный язык", "room": "411", "teacher": "-", "type": "Пр"},
                {"time": "16:55-18:20", "name": "Физика", "room": "333", "teacher": "Гребенкин А.Н.", "type": "Лек"}
            ]
        }


        lb = tk.Label(root, text="Выбери день:", bg="white", font=("Arial", 12, "bold"))
        lb.pack(pady=(10, 0))

        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        self.day_var = tk.StringVar(value="Понедельник")
        self.day_menu = tk.OptionMenu(root, self.day_var, *days, command=self.show_schedule)
        self.day_menu.pack(pady=5)


        lbl2 = tk.Label(root, text="--- Расписание ---", bg="white", font=("Arial", 12, "bold"))
        lbl2.pack(pady=(10, 0))

        self.schedule_text = tk.Text(root, height=8, width=65, font=("Arial", 10), state="disabled")
        self.schedule_text.pack(pady=5)


        lbl3 = tk.Label(root, text="Домашка:", bg="white", font=("Arial", 12, "bold"))
        lbl3.pack()

        self.homework_entry = tk.Text(root, height=4, width=65, font=("Arial", 10))
        self.homework_entry.pack(pady=5)


        btn_frame = tk.Frame(root, bg="white")
        btn_frame.pack(pady=10)

        b1 = tk.Button(btn_frame, text="Сохранить", command=self.save_homework, bg="lightblue", width=12)
        b1.pack(side="left", padx=5)

        b2 = tk.Button(btn_frame, text="Показать", command=self.show_homework, bg="lightgreen", width=12)
        b2.pack(side="left", padx=5)

        b3 = tk.Button(btn_frame, text="Удалить", command=self.delete_homework, bg="lightcoral", width=12)
        b3.pack(side="left", padx=5)


        lbl4 = tk.Label(root, text="--- Всё дз ---", bg="white", font=("Arial", 12, "bold"))
        lbl4.pack(pady=(10, 0))

        self.all_tasks = tk.Text(root, height=6, width=65, font=("Arial", 10), state="disabled")
        self.all_tasks.pack(pady=5)


        self.show_schedule()
        self.load_all_tasks()

    def show_schedule(self, event=None):
        day = self.day_var.get()

        self.schedule_text.config(state="normal")
        self.schedule_text.delete("1.0", "end")

        if day in self.schedule:
            for les in self.schedule[day]:
                self.schedule_text.insert("end", f"{les['time']}  {les['name']}\n")
                self.schedule_text.insert("end", f"  Ауд: {les['room']}  {les['teacher']}  {les['type']}\n")
                self.schedule_text.insert("end", "-" * 50 + "\n")
        else:
            self.schedule_text.insert("end", "Нет пар")

        self.schedule_text.config(state="disabled")

    def save_homework(self):
        day = self.day_var.get()
        hw = self.homework_entry.get("1.0", "end-1c").strip()

        if hw == "":  # вместо not hw
            messagebox.showwarning("Ошибка", "Напиши задание!")
            return

        tasks = self.load_tasks()
        tasks[day] = hw

        with open("../homework.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)

        messagebox.showinfo("Ура!", f"Задание на {day} сохранено")
        self.homework_entry.delete("1.0", "end")
        self.load_all_tasks()

    def show_homework(self):
        day = self.day_var.get()
        tasks = self.load_tasks()

        if day in tasks:
            messagebox.showinfo(f"Дз на {day}", tasks[day])
        else:
            messagebox.showinfo(f"Дз на {day}", "Нет заданий")

    def delete_homework(self):
        day = self.day_var.get()
        tasks = self.load_tasks()

        if day in tasks:
            del tasks[day]
            with open("../homework.json", "w", encoding="utf-8") as f:
                json.dump(tasks, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Готово", f"Задание на {day} удалено")
            self.load_all_tasks()
        else:
            messagebox.showwarning("Ошибка", "Задания нет")

    def load_tasks(self):
        if os.path.exists("../homework.json"):
            with open("../homework.json", "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def load_all_tasks(self):
        tasks = self.load_tasks()

        self.all_tasks.config(state="normal")
        self.all_tasks.delete("1.0", "end")

        if tasks:
            for d, t in tasks.items():
                self.all_tasks.insert("end", f"{d}:\n{t}\n{'-' * 40}\n")
        else:
            self.all_tasks.insert("end", "Нет дз")

        self.all_tasks.config(state="disabled")



if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()