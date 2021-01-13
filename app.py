import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)


st.title("Sentiment analysis of Yelp reviews")
st.sidebar.title("Sentiment analysis of reviews of Yelp")


st.markdown("This app is a streamlit dashboard to analyze the sentiment of reviews 🤖 ")


st.sidebar.markdown("This app is a streamlit dashboard to analyze the sentiment of reviews 🐧 ")


@st.cache(persist=True)
def load_data():
    df = pd.read_csv("yelp.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

st.write(df)

st.sidebar.subheader("Show  a random review")

random_review = st.sidebar.radio('stars', (1,2,3,4,5))

st.sidebar.markdown(df.query('stars == @random_review')[["text"]].sample(n=1).iat[0,0])

st.sidebar.markdown("### Number of reviews by sentiment")
select = st.sidebar.selectbox('Visualization type', ['Histogram', 'Pie chart'], key = '1')

sentiment_count = df['stars'].value_counts()
sentiment_count = pd.DataFrame({'Stars': sentiment_count.index, 'Reviews': sentiment_count.values})


if not st.sidebar.checkbox("Hide", True):
    st.markdown("### Number of reviews by star")
    if select == "Histogram":
        fig = px.bar(sentiment_count, x ='Stars', y='Reviews', color='Reviews', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count, values='Reviews', names='Stars')
        st.plotly_chart(fig)


st.sidebar.header("Word Cloud")
word_sentiment = st.sidebar.radio("Choose a star for word cloud", (1,2,3,4,5))

if not st.sidebar.checkbox("Close", True, key='3'):
    st.header("Word cloud for %i star" % (word_sentiment))
    df_new = df[df['stars']==word_sentiment]
    words = ' '.join(df_new['text'])
    processed_words = ' '.join([word for word in words.split()])
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', height=400, width=800).generate(processed_words)
    plt.imshow(wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()