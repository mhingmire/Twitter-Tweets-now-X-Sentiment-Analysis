"""
Name - Mrida Hingmire
Student Number - 251371008
UWO Username - mhingmir
Date - 17/11/2023

This file 'main' imports the file 'sentiment_analysis' and calls all the functions. The final execution
of all functions and program is done by the 'main.py' file.
"""

# We import the sentiment_analysis module
from sentiment_analysis import *

# This is the main function that calls all the other functions from sentiment_analysis and executes them
def main():
    keyword_file = input("Input keyword filename (.tsv file):")
    if not keyword_file.endswith(".tsv"):
        raise Exception("Must have a .tsv file extension!")
    tweet_file = input("Input tweet filename (.csv file):")
    if not tweet_file.endswith(".csv"):
        raise Exception("Must have a .csv file extension!")
    report_file = input("Input filename to output report in (.txt file):")
    if not report_file.endswith(".txt"):
        raise Exception("Must have a .txt file extension!")

    keyword_dict = read_keywords(keyword_file)  # It reads the file using the function and then returns a dictionary
    if not keyword_dict:
        raise ValueError("Keyword file is empty!")

    tweet_text = read_tweets(tweet_file)  # It reads the tweet file using the function and then returns a list
    if not tweet_text:
        raise ValueError("Tweet file is empty!")

    for tweet_dict in tweet_text:
        tweet_dict["text"] = clean_tweet_text(tweet_dict["text"])
        tweet_dict["sentiment"] = classify(calc_sentiment(tweet_dict["text"], keyword_dict))

    write_report(make_report(tweet_text, keyword_dict),report_file)

main()