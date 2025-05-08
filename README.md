# Sentiment Analysis Web Application

This project is a simple sentiment analysis web application built using Streamlit. It leverages two powerful Natural Language Processing (NLP) techniques — TextBlob for basic sentiment analysis and VADER Sentiment for token-level sentiment analysis.

## Features
- **TextBlob Sentiment Analysis**: Provides an overall sentiment analysis with two key metrics:
  - **Polarity**: Indicates the positivity (positive value) or negativity (negative value) of the text.
  - **Subjectivity**: Measures how subjective the text is (closer to 1 is more subjective).
- **VADER Token-Level Analysis**: Analyzes individual words (tokens) in the text, classifying them as positive, negative, or neutral based on their sentiment score.
- **Interactive Visualization**: Displays a bar chart showing the sentiment score for each word, providing a clear view of the text's sentiment distribution.

## Technologies Used
- **Streamlit**: For creating an interactive web application.
- **TextBlob**: For overall sentiment analysis (polarity and subjectivity).
- **VADER Sentiment Analyzer**: For token-level sentiment analysis.
- **Pandas**: For data handling and manipulation.
- **Altair**: For creating dynamic data visualizations.

## Installation
1. Clone this repository to your local machine.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app using the command:
   ```bash
   streamlit run app.py
   ```
4. The app will be accessible at `http://localhost:8501`.

## How to Use
- Navigate to the "Home" page.
- Enter text in the provided text area.
- Click "Analyze".
- The app will display:
  - Overall sentiment (Polarity and Subjectivity) using TextBlob.
  - Token-wise sentiment analysis with VADER.
  - A bar chart showing sentiment scores for each word.

## About Sentiment Analysis
Sentiment Analysis is a branch of NLP focused on determining the sentiment expressed in text data. It helps classify text as positive, negative, or neutral. This can be useful for analyzing customer reviews, social media posts, feedback, and much more.

### How It Works
1. **Text Preprocessing**:
   - The text is split into individual words (tokens).
   - Each word is analyzed for sentiment using VADER.

2. **Sentiment Calculation**:
   - TextBlob provides an overall sentiment score (polarity and subjectivity).
   - VADER provides a score for each word, categorized as positive, negative, or neutral.

3. **Visualization**:
   - The results are displayed as a DataFrame and visualized using a bar chart for clear understanding.

## Why Use This Application?
- Easy to use, with a clean UI built using Streamlit.
- Combines two powerful NLP techniques for comprehensive sentiment analysis.
- Suitable for quick sentiment analysis of text data without complex setup.
