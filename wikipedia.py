import tkinter as tk
from tkinter import ttk, messagebox
from bs4 import BeautifulSoup
import requests
from reportlab.lib.pagesizes import legal, landscape
from reportlab.pdfgen import canvas
from tkinter import filedialog
import textwrap
import time
from PIL import Image, ImageTk

# Function to fetch data from Wikipedia
def get_country_info():
    country = entry.get().strip()
    if not country:
        messagebox.showwarning("Input Error", "Please enter a country name.")
        return

    country = country.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{country}"

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}


    try:
        response = requests.get(url, headers=headers)
        time.sleep(1)
        if response.status_code != 200:
            messagebox.showerror("Error", f"Page not found (HTTP {response.status_code})")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("span", class_="mw-page-title-main")
        if title:
            title_label.config(text=f"📘 {title.text.strip()}")
        else:
            title_label.config(text="No title found")

        # --- Summary (first paragraph) ---
        paragraph = soup.find_all("p")
        summary_text.delete(1.0, tk.END)
        if paragraph:
            for par in paragraph[:3]:
                summary_text.insert(tk.END, par.text.strip()+ "\n\n")
        else:
            summary_text.insert(tk.END, "No summary found")

        # --- Infobox Data ---
        info_box = soup.find("table", class_="infobox")
        imge = info_box.find_all("img")
        imag_data = None
        URL =None
        for im in imge:
            alt = im.get("alt", "").lower()
            src = im.get("src") or im.get("data-src")
            if "flag" in alt or "flag" in src or ".svg" in src:
                URL = "https:" + src
                break    

        if URL:
            imag_data = requests.get(URL,headers=headers).content
            time.sleep(1)
            with open("image.jpg", "wb") as f:
                f.write(imag_data)
        else:
            print("error in url",URL)
    

        info_text.delete(1.0, tk.END)
        if info_box:
            for row in info_box.find_all("tr"):
                header = row.find("th")
                data = row.find("td")
                if header and data:
                    info_text.insert(tk.END, f"{header.text.strip()}: {data.text.strip()}\n")
        else:
            info_text.insert(tk.END, "No infobox found.")
        set_background()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


def set_background():
    try:
        
        img = Image.open("image.jpg")
        img = img.resize((700, 600))
        # Convert for Tkinter
        bg_image = ImageTk.PhotoImage(img)

        # Create a label to hold the background
        background_label.config(image=bg_image)
        background_label.image = bg_image  # prevent garbage collection
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        background_label.lower()
    except Exception as e:
        print("Error:", e)

def save_to_pdf(title, summary, infobox):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        initialfile=f"{title}.pdf",
        filetypes=[("PDF files", "*.pdf")],
    )

    if not file_path:
        return  # user cancelled

    pdf = canvas.Canvas(file_path, pagesize=landscape(legal))
    width, height = landscape(legal)

    pdf.setFont("Helvetica-Bold", 16) 
    pdf.drawString(250, height - 50, f"Wikipedia Information: {title}")

    # --- Summary Section ---
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 80, "Summary:")
    pdf.setFont("Helvetica", 12)

    text_object = pdf.beginText(50, height - 100)
    text_object.setLeading(16)

    # Wrap text to fit within page width (~120 chars for landscape legal)
    wrapped_summary = []
    for line in summary.splitlines():
        wrapped_summary.extend(textwrap.wrap(line, width=180))

    for line in wrapped_summary:
        text_object.textLine(line)
        if text_object.getY() <= 50:
            pdf.drawText(text_object)
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            text_object = pdf.beginText(50, height - 50)
            text_object.setLeading(16)

    pdf.drawText(text_object)

    # --- Infobox Section ---
    pdf.showPage()
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 50, "Infobox Details:")
    pdf.setFont("Helvetica", 12)

    text_object = pdf.beginText(50, height - 80)
    text_object.setLeading(16)

    wrapped_infobox = []
    for line in infobox.splitlines():
        wrapped_infobox.extend(textwrap.wrap(line, width=120))

    for line in wrapped_infobox:
        text_object.textLine(line)
        if text_object.getY() <= 50:
            pdf.drawText(text_object)
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            text_object = pdf.beginText(50, height - 50)
            text_object.setLeading(16)

    pdf.drawText(text_object)
    pdf.save()

    messagebox.showinfo("Success", f"PDF saved successfully as:\n{file_path}")

# --- GUI Setup ---
root = tk.Tk()
root.title("🌍 Wikipedia Country Info")
root.geometry("700x600")

# --- Input ---
frame = ttk.Frame(root, padding=10)
frame.pack(pady=10)

label = ttk.Label(frame, text="Enter Country Name:")
label.pack(side=tk.LEFT)

entry = ttk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

search_button = ttk.Button(frame, text="Search", command=get_country_info)
search_button.pack(side=tk.LEFT)

# --- Title ---
title_label = ttk.Label(root, text="", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# --- Summary ---
summary_label = ttk.Label(root, text="Summary:")
summary_label.pack()
summary_text = tk.Text(root, height=8, width=80, wrap="word")
summary_text.pack(pady=5)

# --- Infobox ---
info_label = ttk.Label(root, text="Infobox Details:")
info_label.pack()
info_text = tk.Text(root, height=15, width=80, wrap="word")
info_text.pack(pady=5)

def call_save_pdf():
    save_to_pdf (title_label.cget("text").strip(),summary_text.get(1.0, tk.END).strip(),info_text.get(1.0,tk.END).strip())
                 
pdf_button = ttk.Button(root,text = "Pdf",command=call_save_pdf)
pdf_button.pack(side=tk.BOTTOM)

background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()
root.mainloop()