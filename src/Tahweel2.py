## to convert to exe Use  Auto PY instruction in this link https://www.analyticsvidhya.com/blog/2024/01/ways-to-convert-python-scripts-to-exe-files/
##
import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
from Levenshtein import distance as levenshtein_distance
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tahweel.enums import TahweelType
from tahweel.managers import PdfFileManager
from tahweel.processors import GoogleDriveOcrProcessor
from tahweel.writers import DocxWriter
from tqdm import tqdm
import os
import os

# Add Poppler path (update the path as per where Poppler is installed)
poppler_path = r"poppler-24.08.0\Library\bin"
os.environ["PATH"] += os.pathsep + poppler_path
# Tkinter GUI for desktop application
class TahweelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF to DOCX OCR Application")
        self.geometry("600x400")
        self.configure(bg="#f0f8ff")  # Light blue background color

        # Introductory text
        self.label_intro = tk.Label(self, text="يحتاج البرنامج للإنترنت للتحويل", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#ff4500")
        self.label_intro.pack(pady=10)

        # PDF file selection
        self.label_pdf = tk.Label(self, text="Select PDF File:", font=("Arial", 10), bg="#f0f8ff")
        self.label_pdf.pack(pady=5)

        self.button_pdf = tk.Button(self, text="اختر ملف", command=self.browse_pdf, font=("Arial", 12), bg="#1e90ff", fg="white", width=20)
        self.button_pdf.pack(pady=5)

        # Ground truth DOCX selection
        #self.label_gt = tk.Label(self, text="اختار ملف نصي اساسي", font=("Arial", 10), bg="#f0f8ff")
       # self.label_gt.pack(pady=5)

       # self.button_gt = tk.Button(self, text="Browse Ground Truth DOCX", command=self.browse_ground_truth, font=("Arial", 10), bg="#1e90ff", fg="white", width=20)
       # self.button_gt.pack(pady=5)

        # Process button
        self.button_process = tk.Button(self, text="التحويل", command=self.process_files, font=("Arial", 12), bg="#228b22", fg="white", width=20)
        self.button_process.pack(pady=10)

        # Result display label
        self.result_label = tk.Label(self, text="", font=("Arial", 10, "bold"), bg="#f0f8ff", fg="#006400")
        self.result_label.pack(pady=5)

        # Footer text
        self.label_footer = tk.Label(self, text="created by Asmaa", font=("Arial", 12), bg="#f0f8ff", fg="#708090")
        self.label_footer.pack(side="bottom", pady=10)

        self.pdf_path = None
        self.gt_path = None

    def browse_pdf(self):
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.pdf_path:
            self.label_pdf.config(text=f"PDF Selected: {os.path.basename(self.pdf_path)}")

    def browse_ground_truth(self):
        self.gt_path = filedialog.askopenfilename(filetypes=[("DOCX files", "*.docx")])
        if self.gt_path:
            self.label_gt.config(text=f"Ground Truth DOCX Selected: {os.path.basename(self.gt_path)}")

    def process_files(self):
        #if not self.pdf_path or not self.gt_path:
            #messagebox.showerror("Error", "Please select both PDF and Ground Truth DOCX files.")
           # return

        try:
            # Process the PDF
            processor = GoogleDriveOcrProcessor('asmaa-expriments-b3e362cb9f21.json')
            pdf_file_manager = PdfFileManager(Path(self.pdf_path), 8)
            pdf_file_manager.to_images()

            with ThreadPoolExecutor(max_workers=8) as executor:
                content = list(tqdm(executor.map(processor.process, pdf_file_manager.images_paths), 
                                    total=pdf_file_manager.pages_count()))

            # Write the processed content to DOCX
            output_docx = pdf_file_manager.docx_file_path(TahweelType.FILE)
            DocxWriter(output_docx).write(content, False)

            # Calculate accuracy
            #accuracy_char, accuracy_word = self.calculate_measurement(self.gt_path, output_docx)

            # Display results
            self.result_label.config(text=f"تم التحويل")

        except Exception as e:
            messagebox.showerror("Processing Error", str(e))


if __name__ == '__main__':
    app = TahweelApp()
    app.mainloop()
