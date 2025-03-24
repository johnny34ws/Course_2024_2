import tkinter as tk
from tkinter import messagebox
import random

# 全局变量
word_list = []  # 存储单词和中文解释


# 添加单词到列表
def add_word():
    word = entry_word.get().strip()
    meaning = entry_meaning.get().strip()

    if word and meaning:
        word_list.append((word, meaning))
        entry_word.delete(0, tk.END)
        entry_meaning.delete(0, tk.END)
        messagebox.showinfo("成功", "单词已添加！")
    else:
        messagebox.showwarning("错误", "单词和中文解释不能为空！")


# 切换到背单词模式
def switch_to_quiz_mode():
    if not word_list:
        messagebox.showwarning("错误", "请先添加单词！")
        return

    # 隐藏输入界面，显示背单词界面
    input_frame.pack_forget()
    quiz_frame.pack()
    next_question()


# 显示下一个单词
def next_question():
    global current_word
    if word_list:
        current_word = random.choice(word_list)
        label_quiz_word.config(text=f"单词: {current_word[0]}")
        entry_quiz_answer.delete(0, tk.END)
    else:
        messagebox.showinfo("提示", "没有更多单词了！")


# 检查用户答案
def check_answer():
    user_answer = entry_quiz_answer.get().strip()
    if user_answer == current_word[1]:
        messagebox.showinfo("正确", "恭喜你，答对了！")
    else:
        messagebox.showinfo("错误", f"正确答案是: {current_word[1]}")
    next_question()


# 返回输入模式
def switch_to_input_mode():
    quiz_frame.pack_forget()
    input_frame.pack()


# 创建主窗口
root = tk.Tk()
root.title("背单词小程序")
root.geometry("400x300")

# 输入模式界面
input_frame = tk.Frame(root)

label_word = tk.Label(input_frame, text="输入单词:")
label_word.pack(pady=5)
entry_word = tk.Entry(input_frame, width=30)
entry_word.pack(pady=5)

label_meaning = tk.Label(input_frame, text="输入中文解释:")
label_meaning.pack(pady=5)
entry_meaning = tk.Entry(input_frame, width=30)
entry_meaning.pack(pady=5)

button_add = tk.Button(input_frame, text="添加单词", command=add_word)
button_add.pack(pady=10)

button_switch_to_quiz = tk.Button(input_frame, text="切换到背单词模式", command=switch_to_quiz_mode)
button_switch_to_quiz.pack(pady=10)

input_frame.pack()

# 背单词模式界面
quiz_frame = tk.Frame(root)

label_quiz_word = tk.Label(quiz_frame, text="单词: ")
label_quiz_word.pack(pady=20)

entry_quiz_answer = tk.Entry(quiz_frame, width=30)
entry_quiz_answer.pack(pady=10)

button_check = tk.Button(quiz_frame, text="检查答案", command=check_answer)
button_check.pack(pady=10)

button_switch_to_input = tk.Button(quiz_frame, text="返回输入模式", command=switch_to_input_mode)
button_switch_to_input.pack(pady=10)

# 默认显示输入模式
quiz_frame.pack_forget()

# 运行主循环
root.mainloop()