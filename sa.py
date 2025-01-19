
def read_keywords(keyword_file_name):
    keywords = {}
    try:
        with open(keyword_file_name, 'r') as file:
            for line in file:
                keyword, score = line.strip().split('\t')
                keywords[keyword] = int(score)
    except IOError:
        print("Could not open file",keyword_file_name,"!")
    return keywords


def clean_tweet_text(tweet_text):
    tweet = ""
    tweet_text = tweet_text.lower()
    for c in tweet_text:
        if c.isalpha() or c == " ":
            tweet += c
    return tweet

def clean_tweet_text(tweet_text):
    cleaned_text = ""
    for char in tweet_text:
        if char.isalpha() or char.isspace():
            cleaned_text += char.lower()
    return cleaned_text


def clean_tweet_text(tweet_text):
    cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else '' for char in tweet_text)
    return cleaned_text

def clean_tweet_text(tweet_text):
    clean_tweet = ""
    for char in tweet_text:
        if char.isalpha() or char.isspace():    # If the character is alphabetic or a space, append its lowercase version
            clean_tweet.append(char.lower())
        else:                                  # If the character is not alphabetic or a space, append an empty string
            clean_tweet.append("")
    return clean_tweet



def calc_sentiment(tweet_text, keyword_dict):
    words = tweet_text.split()
    sentiment_score = 0

    for word in words:
        if word in keyword_dict:
            sentiment_score += keyword_dict[word]

    return sentiment_score

