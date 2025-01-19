# sentiment_analysis.py

def read_keywords(keyword_file_name):
    keyword_dict = {}
    try:
        with open(keyword_file_name, 'r') as file:
            for line in file:
                keyword, score = line.strip().split('\t')
                keyword_dict[keyword] = int(score)
    except IOError:
        print(f"Could not open file {keyword_file_name}!")
    return keyword_dict

def clean_tweet_text(tweet_text):
    cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else '' for char in tweet_text)
    return cleaned_text

def calc_sentiment(tweet_text, keyword_dict):
    words = tweet_text.split()
    sentiment_score = sum(keyword_dict.get(word, 0) for word in words)
    return sentiment_score

def classify(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

def read_tweets(tweet_file_name):
    tweet_list = []
    try:
        with open(tweet_file_name, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                tweet_dict = {
                    'date': fields[0],
                    'text': clean_tweet_text(fields[1]),
                    'user': fields[2],
                    'retweet': int(fields[3]),
                    'favorite': int(fields[4]),
                    'lang': fields[5],
                    'country': fields[6],
                    'state': fields[7],
                    'city': fields[8],
                    'lat': float(fields[9]) if fields[9] != 'NULL' else 'NULL',
                    'lon': float(fields[10]) if fields[10] != 'NULL' else 'NULL',
                }
                tweet_list.append(tweet_dict)
    except IOError:
        print(f"Could not open file {tweet_file_name}!")
    return tweet_list

def make_report(tweet_list, keyword_dict):
    # Add your code here for generating the report
    pass

def write_report(report, output_file):
    # Add your code here for writing the report to the output file
    pass
