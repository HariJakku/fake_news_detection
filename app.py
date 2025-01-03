import streamlit as st
import joblib

# 🎯 Title and Description
st.title('📰 Fake News Detection App')
st.write('Enter news text to predict whether it is Fake or Real.')

# 🚀 Load the Trained Model and Vectorizer
@st.cache_resource  # Cache the model and vectorizer to avoid reloading every interaction
def load_model_and_vectorizer():
    try:
        # Load your model and vectorizer from files
        model = joblib.load('fake_news_model.pkl')  # Ensure this is the correct path
        vectorizer = joblib.load('vectorizer.pkl')  # Ensure this is the correct path
        return model, vectorizer
    except Exception as e:
        st.error(f"❌ Error loading model or vectorizer: {e}")
        return None, None

model, vectorizer = load_model_and_vectorizer()

# 📥 User Input Section
st.header('📝 Enter News Text')

# User input for text
news_text = st.text_area("Paste the news article here:")

# 🧠 Make Predictions
if st.button('🔍 Predict'):
    if model and vectorizer:
        try:
            # Vectorize the user input text
            news_vectorized = vectorizer.transform([news_text])

            # Make prediction
            prediction = model.predict(news_vectorized)  # Ensure model has predict method
            
            result = '🛑 Fake News' if prediction == 0 else '✅ Real News'
            st.success(f'Prediction: {result}')
        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")
    else:
        st.warning('⚠️ Model or vectorizer is not loaded. Please check your setup.')

# 📊 Additional Information
st.sidebar.header('ℹ️ About')
st.sidebar.info(
    'This app uses a trained machine learning model to classify news articles as Fake or Real. '
    'Simply paste the news text and click "Predict" to get the result.'
)

# 👣 Footer
st.markdown('---')
st.caption('Developed with ❤️ by Jakku Kumarswami')
