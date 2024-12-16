import qrcode
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

# Function to generate QR code
def generate_qr():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return
    try:
        # Create the QR code
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Save the QR code as an image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save("qrcode.png")

        # Display the QR Code on the GUI
        qr_image = qr_image.resize((200, 200))
        qr_tk_image = ImageTk.PhotoImage(qr_image)
        qr_label.config(image=qr_tk_image)
        qr_label.image = qr_tk_image

        messagebox.showinfo("Success", "QR Code generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to save the QR code
def save_qr():
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:
            qr_image = Image.open("qrcode.png")
            qr_image.save(file_path)
            messagebox.showinfo("Success", f"QR Code saved successfully at {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to clear the URL input and the QR code
def clear_all():
    url_entry.delete(0, END)
    qr_label.config(image='')
    messagebox.showinfo("Cleared", "Input and QR Code cleared!")

# Function to animate the buttons (hover effects)
def on_enter(event, button, hover_color):
    button['bg'] = hover_color

def on_leave(event, button, normal_color):
    button['bg'] = normal_color

# Function to create animated buttons
def create_animated_button(parent, text, command, normal_color, hover_color, row, column):
    button = Button(parent, 
                    text=text, 
                    command=command, 
                    bg=normal_color, 
                    fg="white", 
                    font=("Arial", 12, "bold"), 
                    width=15, 
                    relief=RAISED, 
                    bd=3)
    button.grid(row=row, column=column, padx=10, pady=10)
    # Add animations for hover effects
    button.bind("<Enter>", lambda e: on_enter(e, button, hover_color))
    button.bind("<Leave>", lambda e: on_leave(e, button, normal_color))
    return button

# Create the main window
root = Tk()
root.title("QR CODE GENERATOR")
root.geometry("500x600")
root.configure(bg="#F0F0F0")
root.resizable(False, False)

# Title Label
title_label = Label(root, text="QR Code Generator", font=("Helvetica", 24, "bold"), bg="#F0F0F0", fg="#333")
title_label.pack(pady=10)

# Input URL label and entry field
url_label = Label(root, text="Enter Website URL:", font=("Arial", 14), bg="#F0F0F0", fg="#333")
url_label.pack(pady=10)
url_entry = Entry(root, font=("Arial", 16), width=30, justify="center")
url_entry.pack(pady=5)

# Buttons (Generate, Save, Clear)
# Buttons (Generate, Save, Clear) - Updated Layout
# Buttons (Generate, Save, Clear) - All aligned using pack()
button_frame = Frame(root, bg="#F0F0F0")
button_frame.pack(pady=10)

# Generate Button
generate_button = Button(
    button_frame, text="Generate QR Code", command=generate_qr,
    bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=15
)
generate_button.pack(side=LEFT, padx=10, pady=10)

# Save Button
save_button = Button(
    button_frame, text="Save QR Code", command=save_qr,
    bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=15
)
save_button.pack(side=LEFT, padx=10, pady=10)

# Clear Button
clear_button = Button(
    button_frame, text="Clear", command=clear_all,
    bg="#F44336", fg="white", font=("Arial", 12, "bold"), width=15
)
clear_button.pack(side=LEFT, padx=10, pady=10)


# QR Code Display Area
qr_label = Label(root, bg="#F0F0F0")
qr_label.pack(pady=20)

# Footer
footer_label = Label(root, text="Created by Mohamed Anas | Mindows", font=("Arial", 6), bg="#F0F0F0", fg="#777")
footer_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
