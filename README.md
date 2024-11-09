# PDF to DOCX OCR Application

This desktop application allows users to convert PDF files to DOCX format using OCR (Optical Character Recognition). The application leverages Google Drive's OCR capabilities to process the content and can display the results in an easy-to-read format. Built with Tkinter, this app provides a simple, user-friendly interface for file selection, conversion, and display of the results.\
![program](https://github.com/AsmaaMahmoudSaeed/Tahweel-OCR-App/blob/main/program.JPG)
## Features
* PDF to DOCX Conversion: Converts PDF files to DOCX format using OCR.
* Google Drive OCR Processor: Processes PDF images to extract text, leveraging Google OCR for high accuracy.
## Installation

* Poppler: PDF rendering library. Download and set the path in the code as per the instructions below.
1. Clone the Repository (or download the project files).

2. Install Dependencies:

```bash
pip install -r requirements.txt
```
3. Set Up Poppler:
 * Download Poppler from Poppler's website.
* Update the poppler_path variable in the code with the path to Poppler's bin directory.
4. Google OCR Configuration:

* Place your Google OCR JSON file (e.g., asmaa-expriments-cb9f21.json) in the project directory.
* Ensure that GoogleDriveOcrProcessor points to this file.
## Usage
1. Start the Application: Run the following command in your terminal:

bash
```python
python Tahweel2.py
```

2. Select PDF File:

*  Click اختر ملف to choose a PDF file for conversion.
3. Process the File:

* Click التحويل to start the OCR processing.
* The app will process each page and generate a DOCX file with the extracted text.
4. View Results:

* After processing, the app will display a message indicating the completion of the conversion.
* The generated DOCX file can be found in the same directory as the PDF.


## Configuration
* Poppler Path: Ensure the poppler_path variable points to the correct path for Poppler.
* Google OCR Credentials: Update the JSON file path for Google OCR in the GoogleDriveOcrProcessor instance.
Please make sure to update tests as appropriate.

## License

This project is open-source and free to use.