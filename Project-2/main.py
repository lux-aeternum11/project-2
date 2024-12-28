import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from PIL import Image
import customtkinter as cu
import PassGen



class App(cu.CTk):
    def __init__(self):
        super().__init__()
        # базовые параметры
        self.geometry("700x400")
        self.title("PassGen")
        self.resizable(False, False)
        # логотип
        self.logo = cu.CTkImage(dark_image=Image.open("img.png"), size=(460, 150))
        self.logo_label = cu.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)
        #графа для вывода пароля
        self.password_frame = cu.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.entry_password = cu.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=1, padx=(0, 20))
        # кнопка для графы с паролем
        self.btn_generate = cu.CTkButton(master=self.password_frame, text="Создать", width=100,
                                          command=self.set_password)
        self.btn_generate.grid(row=0, column=2)
        # пояснение для строки
        self.label_login = cu.CTkLabel(master=self.password_frame, text="Пароль:")
        self.label_login.grid(row=0, column=0, padx=(0, 10), pady=(10, 0))

        # кнопка для копирования пароля
        self.btn_copy = cu.CTkButton(master=self.password_frame, text="Копировать", width=100,
                                       command=self.copy_password)
        self.btn_copy.grid(row=0, column=3)

        # поле для длины пароля
        self.password_length_entry = cu.CTkEntry(master=self.password_frame, width=50)
        self.password_length_entry.grid(row=1, column=1, padx=(0, 20), pady=(10, 0))
        # кнопка
        self.label_login = cu.CTkLabel(master=self.password_frame, text="Длина:")
        self.label_login.grid(row=1, column=0, padx=(0, 20), pady=(10, 0))

        # reset длины
        self.password_length_entry.insert(0, "12")

        # поле для ввода конкретных символов
        self.entry_word = cu.CTkEntry(master=self.password_frame, width=100)
        self.entry_word.grid(row=2, column=1, padx=(0, 20), pady=(10, 0))
        # кнопка
        self.label_login = cu.CTkLabel(master=self.password_frame, text="Добавить символы:")
        self.label_login.grid(row=2, column=0, padx=(0, 10), pady=(15, 10))

        # пояснение для логина
        self.label_login = cu.CTkLabel(master=self.password_frame, text="Логин:")
        self.label_login.grid(row=3, column=0, padx=(0, 10), pady=(10, 0))
        # поле ввода для логина
        self.entry_login = cu.CTkEntry(master=self.password_frame, width=100)
        self.entry_login.grid(row=3, column=1, padx=(0, 20), pady=(10, 0))

        # сайт
        self.label_site = cu.CTkLabel(master=self.password_frame, text="Сайт:")
        self.label_site.grid(row=4, column=0, padx=(0, 10), pady=(10, 0))
        # Поле для сайта
        self.entry_site = cu.CTkEntry(master=self.password_frame, width=100)
        self.entry_site.grid(row=4, column=1, padx=(0, 20), pady=(10, 0))

        # Кнопка для сохранения данных
        self.btn_save = cu.CTkButton(master=self.password_frame, text="Save", width=100,
                                       command=self.save_data)
        self.btn_save.grid(row=4, column=2, padx=(10, 0))

    def get_characters(self):
        return digits + ascii_lowercase + ascii_uppercase + punctuation

    def set_password(self):
        self.entry_password.delete(0, 'end')
        word = self.entry_word.get()
        password_length = int(self.password_length_entry.get())
        characters = self.get_characters()

        # генерация пароля
        random_password = PassGen.create_new(length=password_length - len(word), characters=characters)

        # добавить символы в пароль
        if word:
            insert_position = secrets.randbelow(len(random_password) + 1)
            final_password = random_password[:insert_position] + word + random_password[insert_position:]
        else:
            final_password = random_password

        self.entry_password.insert(0, final_password)
    # копирование пароля для кнопки копировать
    def copy_password(self):
        password = self.entry_password.get()
        self.clipboard_clear()
        self.clipboard_append(password)
        self.update()

    def save_data(self):
        login = self.entry_login.get()
        site = self.entry_site.get()
        password = self.entry_password.get()

        # Сохранение данных в .тхт
        with open("passwords.txt", "a") as file:
            file.write(f"Site: {site}\nLogin: {login}\nPass: {password}\n\n")

        #очищает поле
        self.entry_login.delete(0, 'end')
        self.entry_site.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.entry_word.delete(0, 'end')
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, "12")

if __name__ == "__main__":
    app = App()
    app.mainloop()