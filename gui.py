import customtkinter as ctk
from tkinter import END

from chatbot import get_response

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("🤖 BuddyAI")
app.geometry("900x700")
app.resizable(False, False)

# ---------------- HEADER ---------------- #

header = ctk.CTkFrame(
    app,
    height=70,
    corner_radius=0
)

header.pack(fill="x")

title = ctk.CTkLabel(
    header,
    text="🤖 BuddyAI",
    font=("Segoe UI",26,"bold")
)

title.pack(side="left",padx=20,pady=18)

status = ctk.CTkLabel(
    header,
    text="🟢 Online",
    font=("Segoe UI",14)
)

status.pack(side="right",padx=20)

# ---------------- CHAT AREA ---------------- #

chat = ctk.CTkTextbox(
    app,
    font=("Segoe UI",15),
    wrap="word"
)

chat.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

chat.insert(
    END,
    "🤖 BuddyAI\n"
)

chat.insert(
    END,
    "Hello! Welcome to BuddyAI.\n\n"
)

chat.insert(
    END,
    "I can answer questions about:\n\n"
)

chat.insert(
    END,
    "• Artificial Intelligence\n"
)

chat.insert(
    END,
    "• Machine Learning\n"
)

chat.insert(
    END,
    "• NLP\n"
)

chat.insert(
    END,
    "• Python\n"
)

chat.insert(
    END,
    "• Date & Time\n"
)

chat.insert(
    END,
    "• Jokes\n"
)

chat.insert(
    END,
    "• Interesting Facts\n\n"
)

chat.insert(
    END,
    "-------------------------------------------------\n\n"
)

chat.configure(state="disabled")
# ---------------- BOTTOM AREA ---------------- #

bottom = ctk.CTkFrame(
    app,
    height=80
)

bottom.pack(fill="x", padx=20, pady=(0,20))

entry = ctk.CTkEntry(
    bottom,
    placeholder_text="Ask BuddyAI anything...",
    font=("Segoe UI",15),
    height=45
)

entry.pack(side="left", fill="x", expand=True, padx=(15,10), pady=15)


def send():

    message = entry.get().strip()

    if message == "":
        return

    chat.configure(state="normal")

    chat.insert(
        END,
        "👤 You\n"
    )

    chat.insert(
        END,
        message + "\n\n"
    )

    reply = get_response(message)

    chat.insert(
        END,
        "🤖 BuddyAI\n"
    )

    chat.insert(
        END,
        reply + "\n\n"
    )

    chat.insert(
        END,
        "-------------------------------------------------\n\n"
    )

    chat.configure(state="disabled")

    chat.see(END)

    entry.delete(0, END)


send_btn = ctk.CTkButton(
    bottom,
    text="➤ Send",
    width=120,
    height=45,
    font=("Segoe UI",14,"bold"),
    command=send
)

send_btn.pack(side="right", padx=(0,15), pady=15)


def clear_chat():

    chat.configure(state="normal")

    chat.delete("1.0", END)

    chat.insert(
        END,
        "🤖 BuddyAI\n\n"
    )

    chat.insert(
        END,
        "Hello! Welcome back.\n\n"
    )

    chat.insert(
        END,
        "Ask me anything about AI, Python, NLP, Machine Learning, Time, Date, Jokes and Facts.\n\n"
    )

    chat.insert(
        END,
        "-------------------------------------------------\n\n"
    )

    chat.configure(state="disabled")


clear_btn = ctk.CTkButton(
    app,
    text="🗑 Clear Chat",
    command=clear_chat,
    fg_color="#D32F2F",
    hover_color="#B71C1C",
    width=180,
    height=40,
    font=("Segoe UI",13,"bold")
)

clear_btn.pack(pady=(0,15))

entry.bind("<Return>", lambda event: send())

entry.focus()

app.mainloop()