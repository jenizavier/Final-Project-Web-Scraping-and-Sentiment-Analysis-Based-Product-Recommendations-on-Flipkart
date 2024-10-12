import streamlit as st
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained('/home/ubuntu/my_streamlit_app/sentiment_model2', num_labels=3)
tokenizer = AutoTokenizer.from_pretrained('/home/ubuntu/my_streamlit_app/sentiment_model2')

# Load the dataset with product scores
df = pd.read_csv('/home/ubuntu/my_streamlit_app/flipkart_reviews_with_score_based_recommendations.csv')

# Define sentiment labels
label_mapping = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}

# Streamlit UI
st.title("Phone Recommendation System Based on Your Question")

# User input: Question
user_question = st.text_area("Ask a question related to phones, and we'll recommend the best phone for you:")

# Optional: Allow user to specify their current phone for personalized recommendations
current_phone = st.selectbox("Select your current phone (optional):", options=["", "Samsung Galaxy S23", "Vivo T3", "Google Pixel 8", "Motorola Edge 50", "Realme 12 Pro"])

# Provide guidance to the user
st.sidebar.header("Need Help?")
st.sidebar.write("You can ask questions like:")
st.sidebar.write("- What phone should I buy?")
st.sidebar.write("- Recommend a phone for gaming.")

# Function to predict sentiment from user input (question)
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return label_mapping[predicted_class]

# Function to recommend products based on product score
def recommend_products_based_on_score(sentiment, current_phone=None):
    # Filter the dataset by removing the current phone if selected
    if current_phone:
        filtered_df = df[df['Phone Name'] != current_phone].copy()
    else:
        filtered_df = df.copy()

    # Sort by the product score in descending order
    filtered_df = filtered_df.sort_values(by='product_score', ascending=False)

    # Get the top phone based on product score
    top_phone = filtered_df['Phone Name'].iloc[0] if not filtered_df.empty else None

    if top_phone:
        return f"Based on your question, we recommend: {top_phone}."
    else:
        return "No recommendations available."

# Function to handle meaningless questions
def is_meaningful_question(question):
    keywords = ["phone", "recommend", "best", "suggest", "which", "what"]
    if len(question) < 3:
        return False
    if any(keyword in question.lower() for keyword in keywords):
        return True
    return False

# Function to provide a fallback recommendation
def fallback_recommendation():
    return "If you're not sure, we recommend the Samsung Galaxy S23 as a popular choice!"

# Function to handle the question and generate an answer
def answer_question(question, current_phone=None):
    if not is_meaningful_question(question):
        return fallback_recommendation()

    # Predict the sentiment of the question
    sentiment = predict_sentiment(question)

    # Display the predicted sentiment (optional, for user understanding)
    st.write(f"Predicted Sentiment: {sentiment}")

    # Generate recommendations based on product score and sentiment
    recommendation = recommend_products_based_on_score(sentiment, current_phone)

    return recommendation

# Button to trigger the recommendation based on the question
if st.button("Get Answer"):
    if user_question:
        # Generate an answer (phone recommendation) based on the user's question
        answer = answer_question(user_question, current_phone if current_phone else None)
        st.write(answer)
    else:
        st.write("Please enter a question to get recommendations.")
