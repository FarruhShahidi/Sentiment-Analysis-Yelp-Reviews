# Classification for Yelp reviews

In this project I use Natural Language Processing to classify review of the Yelp review dataset from Kaggle. 
The objective is  to classify the reviews into 1 to 5 star categories. 
Each observation in this dataset is is a review of a particular business by a particular user.

I start with using the NLTK library to clean and preprocess the data. For some missing data I was able to do a tailor filling which I believe
allowed me achieve a higher accuracy. I used the  [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) classifier for prediction.

In addition, I applied the  [LSTM]https://en.wikipedia.org/wiki/Long_short-term_memory model separately. The issue with applying an advanced model is that one needs a large dataset. With the dataset of size 10000 I was working it did not seem to work fine. While I achieved a higher accuracy of about 95\% the validation of 50\% was very low. Tuning hyperparameters, like  Dropout and SpacialDropout seemed to reduce the difference but the outcome was not good enough. I believe transfer learning, like applying [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html) should give a good accuracy.

Finally, I used the Streamlit framework to create an interactive dashboard of the reviews which depicts a random review according to given star, Histogram, Pie Chart. I also used the WordCloud library to visualize the most popular words. 

![](wc.png, "most popular words for 5 star")

Demo of the interactive dashboard. Also, feel free to work with the app.py file. [Streamlit](https://docs.streamlit.io/en/stable/troubleshooting/clean-install.html) installation is needed


