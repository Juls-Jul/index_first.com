import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

# ---------- WINDOW ----------
root = tk.Tk()
root.title("My Website")
root.geometry("700x500")
root.resizable(False, False)

# ---------- LOGIN CREDENTIALS ----------
USERNAME = "chichay"
PASSWORD = "121725"

# ---------- FUNCTIONS ----------
def login():
    if username_entry.get() == USERNAME and password_entry.get() == PASSWORD:
        login_frame.pack_forget()
        home_frame.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password 💔")

def show_monthsary_page():
    home_frame.pack_forget()
    monthsary_frame.pack(fill="both", expand=True)

def go_home():
    monthsary_frame.pack_forget()
    gallery_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)

def show_gallery_page():
    monthsary_frame.pack_forget()
    gallery_frame.pack(fill="both", expand=True)

def on_enter(e):
    special_btn.config(bg="#ff85c1")

def on_leave(e):
    special_btn.config(bg="#ff4d94")

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk

# ---------- LOGIN PAGE ----------
login_frame = tk.Frame(root, bg="#fff0f5")

login_title = tk.Label(
    login_frame,
    text="Login ૮ ˶ᵔ ᵕ ᵔ˶ ა",
    font=("Helvetica", 26, "bold"),
    bg="#fff0f5",
    fg="#cc0066"
)
login_title.pack(pady=30)

login_box = tk.Frame(login_frame, bg="white", padx=30, pady=30)
login_box.pack()

tk.Label(login_box, text="Username", font=("Helvetica", 12), bg="white").pack(anchor="w")
username_entry = tk.Entry(login_box, font=("Helvetica", 12))
username_entry.pack(fill="x", pady=5)

tk.Label(login_box, text="Password", font=("Helvetica", 12), bg="white").pack(anchor="w")
password_entry = tk.Entry(login_box, show="*", font=("Helvetica", 12))
password_entry.pack(fill="x", pady=5)

login_btn = tk.Button(
    login_box,
    text="Login",
    font=("Helvetica", 14, "bold"),
    bg="#ff4d94",
    fg="white",
    bd=0,
    pady=8,
    cursor="hand2",
    command=login
)
login_btn.pack(fill="x", pady=15)

# ---------- HOME PAGE ----------
home_frame = tk.Frame(root, bg="#fdeff4")

header = tk.Frame(home_frame, bg="#ff4d94", height=70)
header.pack(fill="x")

header_title = tk.Label(header, text=" Welcome ", font=("Helvetica", 22, "bold"), bg="#ff4d94", fg="white")
header_title.pack(pady=15)

content = tk.Frame(home_frame, bg="#fdeff4")
content.pack(expand=True)

title = tk.Label(content, text="A Little Surprise Awaits You", font=("Helvetica", 24, "bold"), bg="#fdeff4", fg="#b30059")
title.pack(pady=30)

subtitle = tk.Label(content, text="Click the button below ꉂ(˵˃ ᗜ ˂˵)", font=("Helvetica", 14), bg="#fdeff4", fg="#4d0026")
subtitle.pack(pady=10)

special_btn = tk.Button(content, text="OPEN ME!", font=("Helvetica", 16, "bold"), bg="#ff4d94", fg="white",
                        padx=30, pady=12, bd=0, activebackground="#ff85c1", cursor="hand2", command=show_monthsary_page)
special_btn.pack(pady=40)

special_btn.bind("<Enter>", on_enter)
special_btn.bind("<Leave>", on_leave)

# ---------- MONTHSARY PAGE ----------
monthsary_frame = tk.Frame(root, bg="#fff0f5")

# Background flower (simple repeated pattern using label)
flower_bg = tk.Label(monthsary_frame, text="🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸", font=("Arial", 16), bg="#fff0f5", fg="#ff99cc")
flower_bg.pack(pady=10)

header2 = tk.Frame(monthsary_frame, bg="#cc0066", height=70)
header2.pack(fill="x")

header2_title = tk.Label(header2, text="( ˶˘ ³˘(ˊᗜˋ*)!♡", font=("Helvetica", 22, "bold"), bg="#cc0066", fg="white")
header2_title.pack(pady=15)

card = tk.Frame(monthsary_frame, bg="white", highlightthickness=1, highlightbackground="#ffb3d9")
card.pack(pady=30, padx=100)

message = tk.Label(card, text="Happy Monthsary, Love ❤️",
                   font=("Helvetica", 22), bg="white", fg="#cc0066", justify="center")
message.pack(padx=40, pady=40)

btn_frame = tk.Frame(monthsary_frame, bg="#fff0f5")
btn_frame.pack(pady=10)

back_btn = tk.Button(btn_frame, text="← Back to Home", font=("Helvetica", 12, "bold"), bg="#ff4d94",
                     fg="white", bd=0, padx=20, pady=8, cursor="hand2", command=go_home)
back_btn.pack(side="left", padx=10)

next_btn = tk.Button(btn_frame, text="Next", font=("Helvetica", 12, "bold"), bg="#ff4d94",
                     fg="white", bd=0, padx=20, pady=8, cursor="hand2", command=show_gallery_page)
next_btn.pack(side="left", padx=10)

# ---------- GALLERY PAGE ----------
gallery_frame = tk.Frame(root, bg="#fdeff4")

header3 = tk.Frame(gallery_frame, bg="#ff4d94", height=70)
header3.pack(fill="x")

header3_title = tk.Label(header3, text="🖼️ Gallery 🖼️", font=("Helvetica", 22, "bold"), bg="#ff4d94", fg="white")
header3_title.pack(pady=15)

upload_btn = tk.Button(gallery_frame, text="Upload an image (⸝⸝> ᴗ•⸝⸝)", font=("Helvetica", 14, "bold"), bg="#ff4d94",
                       fg="white", bd=0, padx=20, pady=10, cursor="hand2", command=upload_image)
upload_btn.pack(pady=20)

img_label = tk.Label(gallery_frame, bg="#fdeff4")
img_label.pack(pady=10)

back_gallery_btn = tk.Button(gallery_frame, text="← Back to Monthsary", font=("Helvetica", 12, "bold"),
                             bg="#ff4d94", fg="white", bd=0, padx=20, pady=8, cursor="hand2",
                             command=lambda: [gallery_frame.pack_forget(), monthsary_frame.pack(fill="both", expand=True)])
back_gallery_btn.pack(pady=10)

# ---------- START APP ----------
login_frame.pack(fill="both", expand=True)
root.mainloop()
