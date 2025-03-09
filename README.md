# 📰 Fake News Detection Using Machine Learning 🤖  

🚀 **A machine learning-based web application that detects fake news with an accuracy of 99.43%!**  

## 📌 Overview  
In today's digital world, misinformation spreads rapidly, influencing public opinion and decision-making.  
This project provides a **machine learning model** trained to classify **news articles as real or fake**,  
using **TF-IDF vectorization and the Passive Aggressive Classifier (PAC)**.  
The model is deployed as a **Streamlit web application** for real-time predictions.  

---

## 🔥 Key Features  
✅ **Real-time fake news classification** 📊  
✅ **Uses Passive Aggressive Classifier (PAC) for high-speed learning** ⚡  
✅ **TF-IDF Vectorization for effective text analysis** 🔍  
✅ **User-friendly Streamlit web app for predictions** 🌍  
✅ **Achieves 99.43% accuracy on a dataset of 44,000 news articles** 📈  

---

## 🛠 Technologies Used  
🔹 **Programming Language:** Python 🐍  
🔹 **Machine Learning Library:** Scikit-learn 📚  
🔹 **Data Handling:** Pandas, NumPy 📊  
🔹 **Deployment:** Streamlit 🚀  
🔹 **Development Tools:** Google Colab, VS Code 🖥️  

---

## 📊 Model Performance  
| Metric      | Score  |  
|------------|--------|  
| **Accuracy**  | 99.43%  |  
| **Precision** | 99.43%  |  
| **Recall**    | 99.36%  |  
| **F1-Score**  | 99.40%  |  

---

## 📂 Project Structure  
📂 fake_news_detection  
│── 📂 streamlit_env/        # Virtual environmen(Do not push this to GitHub)  
│── 📂 models/               # Store trained ML models  
│   │── fake_news_model.pkl  # Trained model  
│   │── vectorizer.pkl       # TF-IDF vectorizer  
│── 📂 src/                  # Source code for training and prediction  
│   │── train_model.py       # Model training script 
│   │── predict.py           # Prediction script (loads model & vectorizer)  
│── app.py                   # Streamlit web app script  
│── requirements.txt         # Required dependencies  
│── README.md                # Project documentation  


---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/HariJakku/fake_news_detection.git
cd fake_news_detection

2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv streamlit_env
3️⃣ Activate the Virtual Environment
For Windows:

bash
Copy
Edit
streamlit_env\Scripts\activate
For Mac/Linux:

bash
Copy
Edit
source streamlit_env/bin/activate
4️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
6️⃣ Deactivate Virtual Environment (When Done)
bash
Copy
Edit
deactivate
🚀 How It Works?
1️⃣ Preprocessing: The text data is cleaned, tokenized, and vectorized using TF-IDF.
2️⃣ Model Training: The Passive Aggressive Classifier (PAC) is trained on 44,000 news articles.
3️⃣ Prediction: Users enter news text, and the model classifies it as Fake or Real.
4️⃣ Deployment: The model runs on Streamlit, allowing real-time predictions.

📌 Future Enhancements
🔹 Integrate Deep Learning (LSTM, BERT) for improved accuracy 🤖
🔹 Expand dataset for multilingual fake news detection 🌍
🔹 Enhance UI with a better interactive interface 🎨

💡 Contributing
Contributions are welcome! Feel free to fork this repository, raise an issue, or submit a pull request. 🚀

🔗 Connect with Me
📧 Email: harijakku2005@gmail.com
🔗 LinkedIn: Hari Jakku
🔗 GitHub Repository: Fake News Detection

🛠 Developed by: JAKKU KUMARSWAMI 🚀
🌟 If you found this project useful, don't forget to star ⭐ the repository!

yaml
Copy
Edit

---

## **✅ Next Steps**
📌 **Replace `[Your LinkedIn Profile]`** with your actual LinkedIn profile link.  
📌 **Commit & Push the Updated `README.md` to GitHub**:  
```bash
git add README.md
git commit -m "Added complete README with installation and setup details"
git push origin main

