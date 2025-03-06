# **📝 Text Summarization App**  

A **Streamlit-based** web application for text summarization using **Extractive (LexRank)** and **Abstractive (Transformer-based) NLP techniques**.  

---

## **🚀 Features**  
✅ Extractive summarization using **LexRank** (Sumy library)  
✅ Abstractive summarization using **BART** (Transformers library)  
✅ Simple **Streamlit UI** for easy use  
✅ REST API using **Flask**  
✅ Deployment-ready on **Render**  

---

## **📂 Project Structure**  
```
text-summarization-app/
│── extractive.py        # Extractive summarization (LexRank)
│── abstractive.py       # Abstractive summarization (BART Transformer)
│── app.py               # Flask API for summarization
│── streamlit_app.py     # Streamlit UI for web app
│── requirements.txt     # Project dependencies
│── runtime.txt          # Python version for Render
│── README.md            # Project documentation
```

---

## **🛠 Installation**  

### **🔹 Step 1: Clone the Repository**  
```bash
git clone https://github.com/your-username/text-summarization-app.git
cd text-summarization-app
```

### **🔹 Step 2: Create & Activate Virtual Environment (Optional)**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **🔹 Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## **🚀 Running the Application**  

### **🔹 Option 1: Run Streamlit UI**  
```bash
streamlit run streamlit_app.py
```
- Open **`http://localhost:8501`** in your browser.

### **🔹 Option 2: Run Flask API**  
```bash
python app.py
```
- Use **Postman** or **cURL** to test:
  ```bash
  curl -X POST http://127.0.0.1:5000/summarize -H "Content-Type: application/json" -d '{"text": "Your input text here..."}'
  ```

---

## **📜 License**
This project is open-source and available under the **MIT License**.