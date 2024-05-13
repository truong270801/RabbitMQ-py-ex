import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "Hello, this is a message box!")

def main():
    # Tạo cửa sổ giao diện
    root = tk.Tk()
    root.title("Simple GUI Example")

    # Thêm một nhãn (label)
    label = tk.Label(root, text="Welcome to my GUI!")
    label.pack()

    # Thêm một nút (button) để hiển thị hộp thoại tin nhắn
    button = tk.Button(root, text="Click me!", command=show_message)
    button.pack()

    # Bắt đầu vòng lặp chính của giao diện
    root.mainloop()

if __name__ == "__main__":
    main()
