"""
Jinil Desai
251393750
jdesai43
8/11/23
This file contains all the functions that are used to analyze the sentiment
score of a tweet. They take a list of tweets as input, analyze them, and create a report.
"""


# Function to read keywords and their associated sentiment scores from a file
def read_keywords(keyword_file_name):
    keywords = {}

    try:
        with open(keyword_file_name, "r") as keyword_file:
            for line in keyword_file:
                fields = line.strip().split("\t")
                if len(fields) == 2:
                    keyword, value = fields[0], int(fields[1])
                    keywords[keyword] = value

        return keywords

    except IOError:
        print("Could not open file, ", keyword_file_name, "!")


# Function to clean and preprocess tweet text
def clean_tweet_text(tweet_text):
    cleaned_text = ""
    for char in tweet_text:
        if char.isalpha() or char.isspace():
            cleaned_text += char.lower()
    return cleaned_text


# Function to calculate the sentiment score of a tweet based on keywords
def calc_sentiment(tweet_text, keyword_dict):
    words = tweet_text.split()
    sentiment_score = 0

    for word in words:
        if word in keyword_dict:
            sentiment_score += keyword_dict[word]

    return sentiment_score


# Function to classify the sentiment as positive, negative, or neutral
def classify(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"


# Function to read and parse tweets from a file into a list of dictionaries
def read_tweets(tweet_file_name):
    try:
        tweets = []
        with open(tweet_file_name, "r") as tweet_file:
            for line in tweet_file:
                fields = line.strip().split(',')
                if len(fields) == 12:
                    tweet_dict = {
                        'date': fields[0],
                        'text': clean_tweet_text(fields[1]),
                        'user': fields[2],
                        'favorite': int(fields[3]),
                        'retweet': int(fields[4]),
                        'lang': fields[5],
                        'country': fields[6] if fields[6] != 'NULL' else 'NULL',
                        'state': fields[7] if fields[7] != 'NULL' else 'NULL',
                        'city': fields[8] if fields[8] != 'NULL' else 'NULL',
                        'lat': float(fields[9]) if fields[9] != 'NULL' else 'NULL',
                        'lon': float(fields[10]) if fields[10] != 'NULL' else 'NULL',
                    }
                    tweets.append(tweet_dict)
        return tweets
    except IOError:
        print(f"Could not open file {tweet_file_name}")
        return []


# Function to generate a report based on the list of tweets and keyword dictionary
def make_report(tweet_list, keyword_dict):
    # Initialize variables to calculate statistics
    num_favorite = 0
    num_retweet = 0
    num_tweets = len(tweet_list)
    sentiment_total = 0
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    country_sentiments = {}

    # Iterate through the tweets
    for tweet in tweet_list:
        sentiment = calc_sentiment(tweet['text'], keyword_dict)
        sentiment_total += sentiment

        # Update sentiment counts
        if sentiment > 0:
            num_positive += 1
        elif sentiment < 0:
            num_negative += 1
        else:
            num_neutral += 1

        # Update favorite and retweet counts
        if tweet['favorite'] > 0:
            num_favorite += 1
        if tweet['retweet'] > 0:
            num_retweet += 1

        # Update country sentiment information
        country = tweet['country']
        if country != 'NULL':
            if country in country_sentiments:
                country_sentiments[country].append(sentiment)
            else:
                country_sentiments[country] = [sentiment]

    # Calculate average sentiment for each country
    avg_country_sentiments = {}
    for country, sentiments in country_sentiments.items():
        avg_sentiment = round(sum(sentiments) / len(sentiments), 2)
        avg_country_sentiments[country] = avg_sentiment

    # Sort countries by average sentiment in descending order
    sorted_countries = sorted(avg_country_sentiments.items(), reverse=True)

    # Extract the top five countries
    top_five_countries = []
    for i in range(min(5, len(sorted_countries))):
        top_five_countries.append(sorted_countries[i][0])

    # Calculate average sentiment values (with "NAN" handling)
    avg_favorite = round(sentiment_total / num_favorite, 2) if num_favorite > 0 else "NAN"
    avg_retweet = round(sentiment_total / num_retweet, 2) if num_retweet > 0 else "NAN"
    avg_sentiment = round(sentiment_total / num_tweets, 2) if num_tweets > 0 else "NAN"

    # Create and return the report dictionary
    report = {
        'avg_favorite': avg_favorite,
        'avg_retweet': avg_retweet,
        'avg_sentiment': avg_sentiment,
        'num_favorite': num_favorite,
        'num_negative': num_negative,
        'num_neutral': num_neutral,
        'num_positive': num_positive,
        'num_retweet': num_retweet,
        'num_tweets': num_tweets,
        'top_five': ', '.join(top_five_countries),
    }
    return report


# Function to write the report to an output file
def write_report(report, output_file):
    try:
        with open(output_file, "w") as file:
            file.write(f"Average sentiment of all tweets: {report['avg_sentiment']}\n")
            file.write(f"Total number of tweets: {report['num_tweets']}\n")
            file.write(f"Number of positive tweets: {report['num_positive']}\n")
            file.write(f"Number of negative tweets: {report['num_negative']}\n")
            file.write(f"Number of neutral tweets: {report['num_neutral']}\n")
            file.write(f"Number of favorited tweets: {report['num_favorite']}\n")
            file.write(f"Average sentiment of favorited tweets: {report['avg_favorite']}\n")
            file.write(f"Number of retweeted tweets: {report['num_retweet']}\n")
            file.write(f"Average sentiment of retweeted tweets: {report['avg_retweet']}\n")
            file.write(f"Top five countries by average sentiment: {report['top_five']}\n")

        print(f"Wrote report to {output_file}")
    except IOError:
        print(f"Could not open file {output_file}")
