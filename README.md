
[![pydotplus v2.0.2](https://img.shields.io/badge/pydotplus-2.0.2-blue?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/pydotplus/2.0.2/)
[![pytesseract v0.3.13](https://img.shields.io/badge/pytesseract-0.3.13-green?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/pytesseract/0.3.13/)
[![gTTS v2.5.3](https://img.shields.io/badge/gTTS-2.5.3-orange?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/gTTS/2.5.3/)
[![pdf2image v1.17.0](https://img.shields.io/badge/pdf2image-1.17.0-red?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/pdf2image/1.17.0/)
[![Pillow v10.3.0](https://img.shields.io/badge/Pillow-10.3.0-purple?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/Pillow/10.3.0/)
[![python-docx v1.1.2](https://img.shields.io/badge/python--docx-1.1.2-yellow?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/python-docx/1.1.2/)
[![Levenshtein v0.26.0](https://img.shields.io/badge/Levenshtein-0.26.0-teal?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/python-Levenshtein/0.26.0/)
[![opencv v4.10.0](https://img.shields.io/badge/opencv-4.10.0-lightgrey?style=plastic&logo=opencv&logoColor=white)](https://pypi.org/project/opencv/4.10.0/)
[![tqdm v4.66.5](https://img.shields.io/badge/tqdm-4.66.5-brightgreen?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/tqdm/4.66.5/)
[![opencv-python v4.10.0.84](https://img.shields.io/badge/opencv--python-4.10.0.84-cyan?style=plastic&logo=opencv&logoColor=white)](https://pypi.org/project/opencv-python/4.10.0.84/)
[![jupyter v6.5.7](https://img.shields.io/badge/jupyter-6.5.7-magenta?style=plastic&logo=jupyter&logoColor=white)](https://pypi.org/project/jupyter/6.5.7/)
[![tahweel v0.1.0](https://img.shields.io/badge/tahweel-0.1.0-ff69b4?style=plastic&logo=python&logoColor=white)](https://pypi.org/project/tahweel/0.1.0/)
# PDF to DOCX OCR Application

This desktop application allows users to convert PDF files to DOCX format using OCR (Optical Character Recognition). This application is based on the Tahweel library [https://github.com/ieasybooks/tahweel ](https://github.com/ieasybooks/tahweel)
.The application leverages Google Drive's OCR capabilities to process the content and can display the results in an easy-to-read format. Built with Tkinter, this app provides a simple, user-friendly interface for file selection, conversion, and display of the results.\
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
* Google  Credentials: Update the JSON file path for Google OCR in the GoogleDriveOcrProcessor instance.
## create a Google Credentials JSON file
to create a Google Credentials JSON file, follow these steps:

1. Go to Google Cloud Console: Open Google Cloud Console.

2. Create a New Project:

* In the Console, click on the Select a Project dropdown in the top navigation bar.
* Select New Project.
* Name your project and click Create.
3. Enable APIs and Services:

* With your project selected, go to APIs & Services > Library in the left-hand menu.
* Search for the specific API your project needs (e.g., Google Drive API, Google Vision API, etc.).
* Click on the API and then click Enable.
4. Create Service Account:

* Go to APIs & Services > Credentials.
* Click on + CREATE CREDENTIALS and select Service account.
* Fill in a name, ID, and description for the service account, then click Create and Continue.
5. Grant Service Account Access (Optional):

* If you want to set specific permissions, select roles as needed. For many applications, Editor or Viewer roles work, but check documentation for the required permissions for your API.
* Click Continue and then Done.
6. Create Key for Service Account:

* In the Service Accounts section, click on the service account you just created.
* Go to the Keys tab and click Add Key > Create new key.
* Choose JSON as the key type and click Create. This will download the JSON file containing your credentials.
7. Secure the JSON File:

*  Keep this JSON file safe and secure, as it contains sensitive information that provides access to your Google Cloud services.
* Place the JSON file in a secure location in your project and set the environment variable or path to access it.
Use the JSON Key in Your Code:

In your code, point to this JSON file to authenticate your API requests. For example, you might set it with an environment variable:

## Converting to .exe file 
#### To convert your Python Tkinter desktop application into an executable file (.exe), you can use a tool called Auto PY to EXE. 


###  Steps to Convert Python Script to .exe Auto PY to EXE

bash
```
pip install auto-py-to-exe
```
2. Run Auto PY to EXE
Once installed, you can run Auto PY to EXE by executing the following command in the terminal or command prompt:

bash
```
Run Auto PY to EXE
```
\
![auto py to exe](https://github.com/AsmaaMahmoudSaeed/Tahweel-OCR-App/blob/main/auto.JPG)
3. Configure the settings
The Auto PY to EXE GUI will open. In the GUI, you’ll see various options and settings.
Click on the “Browse” button and select your Python script file.
* In Additional files 
add Poppler
Add Google OCR JSON file


## License

This project is open-source and free to use.
