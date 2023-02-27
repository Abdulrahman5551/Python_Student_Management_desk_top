from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import random


def about_us():
    messagebox.showinfo('نحن', 'هذا المشروع تم تطويره لإدارة الطلاب في المدارس بواسطة Abdulrahman5551')


class Student:

    def __init__(self, window):
        # ------------ Create Window
        self.window = window
        self.window.geometry('1369x719+0+1')
        # Title For Window
        self.window.title("Management Schools")
        # Background For Window
        self.window.config(background="silver")
        self.window.iconbitmap(
            "C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Student_project_2\\icons\\write_student.ico")

        # ------------ Create Title
        title_1 = Label(self.window, text='[نظام تسجيل الطلاب]',
                        bg='#8E44AD',
                        font=('monospace', 14),
                        fg='white')
        title_1.pack(fill=X)

        # --------------- Variable Student
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.qualifications_var = StringVar()
        self.class_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.delete_student_var = StringVar()

        # --------------- Variable Search
        self.search_by_var_1 = StringVar()
        self.search_var_2 = StringVar()

        # --------------- Tools Control
        frame_1 = Frame(self.window, bg='#34495E')
        frame_1.place(x=1159, y=30, width=210, height=370)

        label_name = Label(frame_1, text='اسم الطالب', bg='#34495E', font=('monospace', 11), fg='white')
        label_name.pack()

        entry_name = Entry(frame_1, textvariable=self.name_var, justify='center', bg='white', bd='3')
        entry_name.pack()
        # --------------

        label_phone = Label(frame_1, text='رقم الهاتف', bg='#34495E', font=('monospace', 11), fg='white')
        label_phone.pack()

        entry_phone = Entry(frame_1, textvariable=self.phone_var, justify='center', bg='white', bd='3')
        entry_phone.pack()
        # --------------

        label_email = Label(frame_1, text='إيميل الطالب', bg='#34495E', font=('monospace', 11), fg='white')
        label_email.pack()

        entry_email = Entry(frame_1, textvariable=self.email_var, justify='center', bg='white', bd='3')
        entry_email.pack()
        # --------------

        label_qualifications = Label(frame_1, text='مؤهلات الطالب', bg='#34495E', font=('monospace', 11), fg='white')
        label_qualifications.pack()

        entry_qualifications = Entry(frame_1, textvariable=self.qualifications_var, justify='center', bg='white',
                                     bd='3')
        entry_qualifications.pack()
        # --------------

        label_gander = Label(frame_1, text='الصف', bg='#34495E', font=('monospace', 11), fg='white')
        label_gander.pack()

        combobox_class = ttk.Combobox(frame_1, textvariable=self.class_var)
        combobox_class['value'] = ('أول إبتدائي', 'ثاني إبتدائي', 'ثالث إبتدائي', 'رابع إبتدائي', 'خامس إبتدائي',
                                   'سادس إبتدائي', 'أولى متوسط', 'ثاني متوسط', 'ثالث متوسط',
                                   'اولى ثانوي', 'ثاني ثانوي', 'ثالث ثانوي')
        combobox_class['state'] = 'readonly'
        combobox_class.pack()
        # --------------

        label_gander = Label(frame_1, text='جنس الطالب', bg='#34495E', font=('monospace', 11), fg='white')
        label_gander.pack()

        combobox_gander = ttk.Combobox(frame_1, textvariable=self.gender_var)
        combobox_gander['value'] = ('ذكر', 'أنثى')
        combobox_gander['state'] = 'readonly'
        combobox_gander.pack()

        label_address = Label(frame_1, text='عنوان الطالب', bg='#34495E', font=('monospace', 11), fg='white')
        label_address.pack()

        entry_address = Entry(frame_1, textvariable=self.address_var, justify='center', bg='white',
                              bd='3')
        entry_address.pack()
        # --------------

        label_delete_student = Label(frame_1, text='حذف طالب بالرقم التسلسلي', bg='#34495E', font=('monospace', 11),
                                     fg='#E74C3C')
        label_delete_student.pack()

        entry_address = Entry(frame_1, textvariable=self.delete_student_var, justify='center', bg='white',
                              bd='3')
        entry_address.pack()
        # --------------
        # ----------------- Buttons
        frame_2 = Frame(self.window, bg='#34495E')
        frame_2.place(x=1159, y=412, width='210', height=284)

        title_2 = Label(frame_2, text='لوحة التحكم', font=('Deco', 14), fg='white', bg='#8E44AD')
        title_2.pack(fill=X)

        Button_add = Button(frame_2, text='إضافة طالب', bg='#8E44AD', fg='white',
                            font=('monospace', 11), command=self.add_student)
        Button_add.place(x=34, y=40, width=150, height=30)

        Button_delete = Button(frame_2, text='حذف طالب', bg='#8E44AD', fg='white',
                               font=('monospace', 11), command=self.delete_student)
        Button_delete.place(x=34, y=80, width=150, height=30)

        Button_update = Button(frame_2, text='تعديل بيانات طالب', bg='#8E44AD', fg='white',
                               font=('monospace', 11), command=self.update_student)
        Button_update.place(x=34, y=120, width=150, height=30)

        Button_clear = Button(frame_2, text='إفراغ', bg='#8E44AD', fg='white',
                              font=('monospace', 11), command=self.clear_all)
        Button_clear.place(x=34, y=160, width=150, height=30)

        Button_about_us = Button(frame_2, text='من نحن', bg='#8E44AD', fg='white',
                                 font=('monospace', 11), command=about_us)
        Button_about_us.place(x=34, y=200, width=150, height=30)

        Button_exit = Button(frame_2, text='خروج', bg='#8E44AD', fg='white',
                             font=('monospace', 11), command=self.window.quit)
        Button_exit.place(x=34, y=240, width=150, height=30)

        # --------------- Search Area
        frame_3 = Frame(self.window, bg='#34495E')
        frame_3.place(x=1, y=30, width=1150, height=55)

        label_search = Label(frame_3, text='البحث عن طالب', bg='#34495E', fg='white', font=('monospace', 11))
        label_search.place(x=1040, y=14)

        combobox_search = ttk.Combobox(frame_3, textvariable=self.search_by_var_1)
        combobox_search['value'] = ('ID', 'Name', 'Email', 'Phone')
        combobox_search['state'] = 'readonly'
        combobox_search.place(x=892, y=14)

        entry_search = Entry(frame_3, bd='3', justify='right', textvariable=self.search_var_2)
        entry_search.place(x=751, y=13)

        button_search = Button(frame_3, text='بحث', bg='#8E44AD', fg='white', font=('monospace', 11),
                               command=self.Search_for_student)
        button_search.place(x=631, y=13, width=100, height=26)

        # ------------- View Data and Result

        frame_4 = Frame(self.window, bg='#34495E')
        frame_4.place(x=2, y=88, width=1148, height=606)

        # ------- Scroll
        scroll_x = Scrollbar(frame_4, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame_4, orient=VERTICAL)

        # ------- Treeview
        self.student_table = ttk.Treeview(frame_4,
                                          columns=('address', 'gender', 'class', 'qualifications',
                                                   'email', 'phone', 'name', 'id'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        self.student_table.place(x=15, y=1, width=1130, height=588)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        self.student_table['show'] = 'headings'
        self.student_table.heading('address', text='عنوان الطالب')
        self.student_table.heading('gender', text='جنس الطالب')
        self.student_table.heading('class', text='الصف')
        self.student_table.heading('qualifications', text='المؤهلات')
        self.student_table.heading('email', text='ايميل الطالب')
        self.student_table.heading('phone', text='رقم الهاتف')
        self.student_table.heading('name', text='أسم الطالب')
        self.student_table.heading('id', text='الرقم التسلسلي')

        self.student_table.column('address', width=115, anchor='center')
        self.student_table.column('gender', width=30, anchor='center')
        self.student_table.column('class', width=80, anchor='center')
        self.student_table.column('qualifications', width=65, anchor='center')
        self.student_table.column('email', width=80, anchor='center')
        self.student_table.column('phone', width=65, anchor='center')
        self.student_table.column('name', width=100, anchor='center')
        self.student_table.column('id', width=12)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_all()

    # ------- Connect With Database

    def add_student(self):

        random_1 = random.randint(1000, 9999)
        random_2 = random.randint(1000, 9999)

        result_random = "23" + str(random_1) + str(random_2)
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        qualifications = self.qualifications_var.get()
        class_c = self.class_var.get()
        gender = self.gender_var.get()
        address = self.address_var.get()

        if len(name) > 2:
            if len(phone) == 10:
                if len(email) > 5:
                    if len(qualifications) > 2:
                        if len(class_c) != 0:
                            if len(gender) != 0:
                                if len(address) > 5:

                                    db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project"
                                                         "\\Student_project_2\\Database\\School_stud.db")
                                    cursor = db.cursor()
                                    sql = f"INSERT INTO student" \
                                          f"(id, name, phone, email, qualifications, class, gender, address)" \
                                          f"VALUES('{result_random}', '{name}', '{phone}', '{email}', " \
                                          f"'{qualifications}', '{class_c}'," \
                                          f"'{gender}', '{address}')"
                                    cursor.execute(sql)
                                    messagebox.showinfo('تم', '...تم إضافة طالب بنجاح')

                                    db.commit()
                                    self.clear_all()
                                    self.delete_children()
                                    self.fetch_all()
                                    db.close()
                                else:
                                    messagebox.showerror('عفوا', '!!يجب أن يكون العنوان كاملا')
                            else:
                                messagebox.showerror('عفوا', 'يجب تحديد الجنس')
                        else:
                            messagebox.showerror('عفوا', 'يجب تحديد الصف')
                    else:
                        messagebox.showerror('عفوا', '!!يجب كتابة الصف')
                else:
                    messagebox.showerror('عفوا', '!!يجب كتابة الايميل')
            else:
                messagebox.showerror('عفوا', '!!يجب ألايكون رقم الهاتف فارغ')
        else:
            messagebox.showerror('عفوا', 'يجب كتابة الاسم الاول والثاني')

    def delete_student(self):
        id_student_delete = self.delete_student_var.get()

        if len(id_student_delete) != 10:
            messagebox.showerror('عفوا', 'يجب أن يتكون الرقم التسلسلي من 10 أرقام')

        else:
            db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Student_project_2\\Database"
                                 "\\School_stud.db")
            cursor = db.cursor()

            cursor.execute(f"DELETE FROM student WHERE id = '{id_student_delete}'")
            db.commit()
            self.delete_children()
            self.fetch_all()
            messagebox.showinfo('تم', '...تم حذف الطالب')
            db.close()

    def update_student(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        qualifications = self.qualifications_var.get()
        class_c = self.class_var.get()
        gender = self.gender_var.get()
        address = self.address_var.get()

        if len(name) > 0 or len(phone) > 0 or len(email) > 0 or len(qualifications) > 0 or len(class_c) > 0 \
                or len(gender) > 0 or len(address) > 0:

            qu1 = messagebox.askquestion('Change', 'هل تريد حفظ التغيرات التي اجريات؟')
            if qu1 == 'yes' or qu1 == 'Yes':
                db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Student_project_2"
                                     "\\Database\\School_stud.db")
                cursor = db.cursor()
                cursor_row = self.student_table.focus()
                contents = self.student_table.item(cursor_row)
                row = contents['values']

                sql = f"UPDATE student SET address = '{address}', gender = '{gender}', class = '{class_c}'," \
                      f"qualifications = '{qualifications}', email = '{email}', phone = '{phone}'," \
                      f"name = '{name}' WHERE id = '{row[7]}'"
                cursor.execute(sql)
                db.commit()
                db.close()
                self.delete_children()
                self.fetch_all()
                messagebox.showinfo('Done', 'تم..')

            else:
                pass
        else:
            pass

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        if len(row) > 0:

            self.address_var.set(row[0])
            self.gender_var.set(row[1])
            self.class_var.set(row[2])
            self.qualifications_var.set(row[3])
            self.email_var.set(row[4])
            self.phone_var.set(row[5])
            self.name_var.set(row[6])
        else:
            pass

    def fetch_all(self):
        db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Student_project_2\\Database"
                             "\\School_stud.db")
        cursor = db.cursor()
        cursor.execute("SELECT address, gender, class, qualifications, email, phone, name, id FROM student ORDER BY id")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.children)

            for row in rows:
                self.student_table.insert("", END, values=row)
            db.commit()
        db.close()

    def delete_children(self):  # This method by my
        for items in self.student_table.get_children():
            self.student_table.delete(items)

    def Search_for_student(self):
        db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Student_project_2\\Database"
                             "\\School_stud.db")
        cursor = db.cursor()
        sql = f"SELECT address, gender, class, qualifications, email, phone, name, id FROM student WHERE " + str(
            self.search_by_var_1.get()) + " LIKE '%" + str(self.search_var_2.get()) + "%'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        self.delete_children()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.children)

            for row in rows:
                self.student_table.insert("", END, values=row)
            db.commit()
        cursor.close()

    def clear_all(self):
        self.name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.qualifications_var.set('')
        self.class_var.set('')
        self.gender_var.set('')
        self.address_var.set('')
        self.delete_children()
        self.fetch_all()

        self.search_by_var_1.set('')
        self.search_var_2.set('')


root = Tk()
Student(root)
root.mainloop()
