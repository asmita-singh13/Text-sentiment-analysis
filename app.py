import streamlit as st
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def convert_to_df(sentiment):
    sentiment_dict = {'polarity': sentiment.polarity, 'subjectivity': sentiment.subjectivity}
    sentiment_df = pd.DataFrame(sentiment_dict.items(), columns=['metric', 'value'])
    return sentiment_df

def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    token_data = []
    for word in docx.split():
        res = analyzer.polarity_scores(word)['compound']
        sentiment_type = "Positive" if res > 0.1 else "Negative" if res <= -0.1 else "Neutral"
        token_data.append({'word': word, 'sentiment': sentiment_type, 'score': res})

    token_df = pd.DataFrame(token_data)
    return token_df

def main():
    st.title("Enhanced Sentiment Analysis NLP App")
    st.subheader("Analyze Text with NLP")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        with st.form(key='nlpForm'):
            raw_text = st.text_area("Enter Text Here")
            submit_button = st.form_submit_button(label='Analyze')

        if submit_button:
            if not raw_text:
                st.warning("Please enter some text to analyze.")
            else:
                st.info("Overall Sentiment Analysis")
                sentiment = TextBlob(raw_text).sentiment
                st.write(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")

                result_df = convert_to_df(sentiment)
                st.dataframe(result_df)

                st.info("Token-Level Sentiment Analysis")
                token_df = analyze_token_sentiment(raw_text)
                st.dataframe(token_df)

                st.info("Sentiment Visualization")
                chart = alt.Chart(token_df).mark_bar().encode(
                    x='word',
                    y='score',
                    color='sentiment',
                    tooltip=['word', 'sentiment', 'score']
                ).properties(width=700)

                st.altair_chart(chart, use_container_width=True)

    else:
        st.subheader("About")
        st.write("This is an enhanced NLP app for sentiment analysis using TextBlob and VADER.")

if __name__ == '__main__':
    main()
