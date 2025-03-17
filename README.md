# ATS Resume Match Scoring System

This script evaluates a **resume's ATS (Applicant Tracking System) match score** against a list of predefined **embedded engineering keywords**.

## **How It Works**
1. Extracts text from the resume (**CV**) provided in a text format.
2. Compares it against a **predefined set of keywords** used by ATS in the embedded industry.
3. Assigns weightage to each keyword based on relevance.
4. Computes an **ATS match percentage** based on keyword occurrences.

## **Installation & Usage**
### **1. Install Python**
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```
If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### **2. Clone or Download the Script**
```sh
git clone https://github.com/your-repo/ats-resume-scoring.git
cd ats-resume-scoring
```

### **3. Prepare Your Resume**
- Save your resume as a **plain text file** (e.g., `resume.txt`).
- Ensure it's formatted properly for accurate keyword extraction.

### **4. Run the Script**
```sh
python ats_scoring.py
```

## **Customizing the Keyword List**
This script uses a **hardcoded list of keywords**, but you can dynamically extract **relevant skills from the job description** using AI.

### **Extract Keywords Using AI**
To enhance accuracy, extract the most relevant **keywords from the job description** before running the ATS match.

#### **Steps:**
1. **Copy and paste the job description** into an AI tool (e.g., ChatGPT, OpenAI API, or spaCy).
2. **Ask AI to extract technical skills** as a Python list.
3. **Replace the `keywords` dictionary** in the script with the extracted terms.

**Example prompt to ChatGPT:**
```plaintext
Extract key technical skills and relevant terms from this job description. Return them as a Python list.
---
<PASTE JOB DESCRIPTION HERE>
---
```

### **Modify the Keyword List in the Script**
Once extracted, update the `keywords` dictionary inside `ats_scoring.py`.

```python
keywords = {
    "Embedded C": 10, "RTOS": 8, "Embedded Linux": 10, "Bootloader": 7,
    "Device Tree": 7, "Kernel Modules": 7, "ARM Cortex-M": 10, "Microcontrollers": 8,
    "MPUs": 6, "Protocols": 6, "UART": 6, "SPI": 6, "I2C": 6,
    "Ethernet": 6, "Debugging": 7, "Oscilloscope": 7, "Logic Analyzers": 7,
    "Git": 7, "Jira": 5, "Confluence": 5, "GCC": 7, "VS Code": 5,
    "ISO 26262": 8, "Functional Safety": 8, "Compiler": 7, "Firmware": 10,
    "Board bring-up": 9, "System Validation": 8, "Automotive": 7,
    "Defense": 6, "Avionics": 6
}
```

## **Improving Accuracy**
To further refine the ATS score calculation:
- **Use AI-powered keyword extraction** from job descriptions.
- **Incorporate NLP** (`spaCy`, `NLTK`, or `Transformers`) to match synonyms.
- **Enhance scoring** with keyword frequency analysis.

## **License**
MIT License - Feel free to use and modify this script!
