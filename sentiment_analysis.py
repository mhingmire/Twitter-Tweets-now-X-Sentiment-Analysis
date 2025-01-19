"""
Name - Mrida Hingmire
Student Number - 251371008
UWO Username - mhingmir
Date - 17/11/2023

This file 'sentiment_analysis' contains a list of all necessary function required to make a
sentiment analysis report for a given set of tweets. The functions read the tweets, clean tweets,
calculate the sentiments, make the report and finally write/generate the sentiment analysis report.
"""

# The function 'read_keywords' takes one argument 'keyword_file_name' and reads the TSV keywords file.The function splits the TSV file and add it to another dictionary as key-value pairs.
def read_keywords(keyword_file_name):
    keywords = {}
    try:
        with open(keyword_file_name, 'r') as f:
            for line in f:
                keyword, value = line.strip().split('\t')
                keywords[keyword] = int(value)
        return keywords
    except IOError:
        print("Could not open file", keyword_file_name, "!")
        return {}

#This function takes the tweet_text and removes all special characters, cleans the tweet and keeps only the english characters with spaces
def clean_tweet_text(tweet_text):
    clean_chars = []
    for char in tweet_text.lower():
        if char.isalpha() or char == ' ':   # If the character is alphabetic or a space, append its lowercase version
            clean_chars.append(char)
    clean_tweet = ''.join(clean_chars)
    return clean_tweet

#This function calculates the sentiment for each individual tweet based on the text provided
def calc_sentiment(tweet_text, keyword_dict):
    sentiment_scores = []
    words = clean_tweet_text(tweet_text).split()
    for w in words:
        score = keyword_dict.get(w,0)  #This method is used to get the value associated with the key from keyword_dict. If the word not found, it returns 0 as the default value.
        sentiment_scores.append(score)
    sentiment_score = sum(sentiment_scores)
    return sentiment_score

#This function takes the sentiment score and classifies it as either positive, negative or neutral
def classify(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

#This function reads the contents of the file and segregates them based on date, user, retweet etc and stores the values in a list 'tweet_list'
def read_tweets(tweet_file_name):
    try:
        with open(tweet_file_name, "r") as f:
            tweet_list = []
            for line in f:
                value = line.strip().split(',')
                tweet_dict = {                   # We create a dictionary to store all the info from a single tweet
                    'date': value[0],
                    'text': clean_tweet_text(value[1]),
                    'user': value[2],
                    'retweet': int(value[3]),
                    'favorite': int(value[4]),
                    'lang': value[5],
                    'country': value[6],
                    'state': value[7] ,
                    'city': value[8] ,
                    'lat': float(value[9]) if value[9] != 'NULL' else 'NULL',
                    'lon': float(value[10]) if value[10] != 'NULL' else 'NULL'}
                tweet_list.append(tweet_dict)

            if not tweet_list:
                raise ValueError("Empty tweet file!")
        return tweet_list
    except IOError:
        print("Could not open file",tweet_file_name,"!")
        return []

#This function takes a list of tweets, from the above given functions and makes a detailed report after calculating the average sentiments, number of positive/negative tweets etc.
def make_report(tweet_list, keyword_dict):
    num_positive = num_negative = num_neutral = num_favorite = num_retweet = num_tweets = 0
    sum_sentiment = sum_favorite = sum_retweet = 0
    country_sentiment = {}

    num_tweets = len(tweet_list)
    if num_tweets == 0:
        raise Exception("Tweet list is empty!")

    for tweet_dict in tweet_list:
        sentiment = calc_sentiment(tweet_dict["text"],keyword_dict)
        tweet_dict["sentiment"] = sentiment

        if sentiment > 0:
            num_positive += 1
        elif sentiment < 0:
            num_negative += 1
        else:
            num_neutral += 1

        sum_sentiment += sentiment

        if tweet_dict["favorite"] > 0:
            num_favorite += 1
            sum_favorite += sentiment

        if tweet_dict["retweet"] > 0:
            num_retweet += 1
            sum_retweet += sentiment

        country = tweet_dict["country"]
        if country != "NULL":
            if country not in country_sentiment:
                country_sentiment[country] = {"count": 0, "sum_sentiment": 0}
            country_sentiment[country]["count"] += 1
            country_sentiment[country]["sum_sentiment"] += sentiment

    # We use the lambda function below to determine the total country_sentiment
    sorted_countries = sorted(country_sentiment, key=lambda x: country_sentiment[x]["sum_sentiment"] / country_sentiment[x]["count"], reverse=True)
    top_five = sorted_countries[:5]

    avg_favorite = round(sum_favorite / num_favorite, 2) if num_favorite > 0 else "NAN"
    avg_retweet = round(sum_retweet / num_retweet, 2) if num_retweet > 0 else "NAN"
    avg_sentiment = round(sum_sentiment / num_tweets, 2) if num_tweets > 0 else "NAN"

    report = {

        "avg_sentiment": avg_sentiment,
        "num_tweets": num_tweets,
        "num_positive": num_positive,
        "num_negative": num_negative,
        "num_neutral": num_neutral,
        "num_favorite": num_favorite,
        "avg_favorite": avg_favorite,
        "num_retweet": num_retweet,
        "avg_retweet": avg_retweet,
        "top_five": ",".join(top_five)
    }
    return report

#This function simply takes all the output from the make_report function and displays and writes it to a .txt file in a more structured way
def write_report(report, output_file):
    try:
        with open(output_file,"w") as f:
            f.write(f"Average sentiment of all tweets: {report['avg_sentiment']}\n")
            f.write(f"Total number of tweets: {report['num_tweets']}\n")
            f.write(f"Number of positive tweets: {report['num_positive']}\n")
            f.write(f"Number of negative tweets: {report['num_negative']}\n")
            f.write(f"Number of neutral tweets: {report['num_neutral']}\n")
            f.write(f"Number of favorited tweets: {report['num_favorite']}\n")
            f.write(f"Average sentiment of favorited tweets: {report['avg_favorite']}\n")
            f.write(f"Number of retweeted tweets: {report['num_retweet']}\n")
            f.write(f"Average sentiment of retweeted tweets: {report['avg_retweet']}\n")
            f.write(f"Top five countries by average sentiment: {report['top_five']}\n")
        print("Wrote report to", output_file)
    except IOError:
        print("Could not open file", output_file)