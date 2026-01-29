# Smart Resume Parser using Transformer-Based Named Entity Recognition

## Overview  
Resumes are unstructured documents that contain important information such as personal details, education history, work experience, and technical skills. Manually extracting this information is time-consuming and inefficient. This project presents a **Smart Resume Parser** that automatically extracts structured information from resumes using **transformer-based Natural Language Processing (NLP) models** from Hugging Face.

The system converts resume PDFs into text, applies a pretrained **BERT-based Named Entity Recognition (NER)** model to identify entities such as names and organizations, and post-processes the results to generate structured JSON output. A **Streamlit web interface** is provided for real-time resume upload and parsing.

---

## Features  

- Upload resume in PDF format  
- Named Entity Recognition using Transformer models  
- Extract key fields:  
  - Name  
  - Organizations / Companies  
  - Skills (rule-based extraction)  
- Structured JSON output for downstream processing  
- Interactive Streamlit web interface  
- Google Colab notebook for experimentation and evaluation  

---

##  Technologies Used  

- **Python 3**  
- **Hugging Face Transformers**  
- **BERT (dslim/bert-base-NER)** for Named Entity Recognition  
- **PyPDF2** for PDF text extraction  
- **Streamlit** for web-based UI  
- **Google Colab / Jupyter Notebook** for experimentation  


---

## Methodology  

1. **PDF Preprocessing:**  
   Resume PDFs are converted into plain text using PyPDF2.  

2. **Named Entity Recognition:**  
   A pretrained BERT-based NER model (`dslim/bert-base-NER`) is used to identify entities such as Person (PER) and Organization (ORG).  

3. **Post-processing:**  
   Extracted entities are filtered and organized into structured fields such as Name, Organizations, and Skills.  

4. **User Interface:**  
   A Streamlit-based web application allows users to upload resumes and view extracted information in real time.  

5. **Notebook Evaluation:**  
   A Google Colab notebook is included to demonstrate model loading, entity extraction, and JSON output for academic evaluation.

---

## Example Output  

```json
{
    "Name": "John Doe",
    "Organizations": ["Google", "Microsoft"],
    "Skills": ["Python", "Machine Learning", "AWS"]
}

