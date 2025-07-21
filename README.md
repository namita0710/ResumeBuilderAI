# ResumeBuilderAI

Step 1: Install Python (if not already installed)
Make sure you have Python installed on your machine. You can check this by running:
python --version
If Python isn’t installed, download it from the official website.
Step 2: Create a Virtual Environment
A virtual environment helps isolate your project and keeps your dependencies organized.
1.	Open your terminal (or Command Prompt for Windows).
2.	Navigate to the folder where you want to store your project and run:
python -m venv ai_resume_venv
3. Activate the virtual environment:
•	On Windows:
ai_resume_venv\Scripts\activate
•	On macOS/Linux:
source ai_resume_venv/bin/activate
Step 3: Install Required Libraries
Once the virtual environment is activated, install the following Python packages:
pip install streamlit markdown2 pdfkit openai==0.28
•	Streamlit: To create an interactive web app for our resume generator.
•	markdown2: For converting markdown text into HTML.
•	pdfkit: To convert HTML content into PDF format.
•	openai: To interact with the OpenAI GPT-4 API.
You’ll also need wkhtmltopdf for pdfkit to work correctly. Follow the installation guide for your OS from here:https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf.



