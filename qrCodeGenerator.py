import qrcode
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def generate_qr():
    data = entry.get()
    
    if data.strip() == "":
        messagebox.showwarning("Error", "Please enter some text or a link!")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        title="Choose where to save the QR code",
        initialfile="my_qrcode.png"
    )
    
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", f"QR code saved successfully in:\n{file_path}")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x150")

label = tk.Label(root, text="Enter a link or text here:", font=("Arial", 10))
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn = tk.Button(root, text="Generate QR", command=generate_qr, bg="lightgray")
btn.pack(pady=10)

root.mainloop()