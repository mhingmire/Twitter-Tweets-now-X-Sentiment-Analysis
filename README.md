# Sentiment Analysis on Twitter Data

This project analyzes Twitter data to calculate sentiment scores for tweets and provides statistical insights such as the number of positive, negative, and neutral tweets, and the top 5 countries with the highest positive sentiment.

---

## **Features**
- Cleans and processes raw Twitter data.
- Calculates sentiment scores for individual tweets using a keyword-based scoring system.
- Outputs detailed statistics, including:
  - Average sentiment score of the dataset.
  - Positive/negative/neutral tweet counts.
  - Top 5 countries by average sentiment score.
- Supports user-defined keyword files for custom analysis.

---

## **Dataset Structure**
### `keywords.tsv`
- A tab-separated file containing keywords and their sentiment scores.
- Format: keyword<TAB>score
- Example: happy 3 sad -2


### `tweets.csv`
- A CSV file containing tweets and metadata.
- Columns:
- `Created At`, `Tweet Text`, `Username`, `Retweet Count`, `Favorite Count`, `Language`, `Country`, `State/Province`, `City`, `Latitude`, `Longitude`

---

## **How It Works**
1. Cleans the tweets to remove punctuation and convert text to lowercase.
2. Calculates the sentiment score for each tweet based on provided keywords.
3. Computes statistics such as average sentiment, favorite/retweet-based sentiment, and top 5 countries by sentiment.

---

