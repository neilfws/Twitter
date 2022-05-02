#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:45:27 2021

@author: neilsaunders
"""

import spacy
import re
import markovify
import warnings
import json
import advertools as adv
import yaml
from twython import Twython
import pandas as pd
import os.path
import demoji
from pathlib import Path
import datetime

script_dir = Path(__file__).parent
data_dir = '../data/'
output_dir = '../output/'

warnings.filterwarnings('ignore')
nlp = spacy.load('en_core_web_sm')

# fix max length error
nlp.max_length = 2000000 # or higher


# simple text cleaner
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = re.sub('@[A-Za-z0-9_]+', '', text)
  text = re.sub(r'http\S+', '', text)
  text = re.sub('LISTEN HERE:', '', text)
  text = demoji.replace(text, '')
  text = ' '.join(text.split())
  return text

# class for text POS
class POSifiedText(markovify.Text):
  def word_split(self, sentence):
    return ['::'.join((word.orth_, word.pos_)) for word in nlp(sentence)]
    
  def word_join(self, words):
    sentence = ' '.join(word.split('::')[0] for word in words)
    return sentence


# get twitter credentials
print('Connecting to Twitter...\n')
credentials_file = 'credentials.yaml'
with open((script_dir / credentials_file).resolve(), 'r') as f:
    auth_params = yaml.safe_load(f)

# authenticate
twitter = Twython(**auth_params)
adv.twitter.set_auth_params(**auth_params)

# fetch as many latest tweets as possible
print('Fetching latest tweets...\n')
tweets = adv.twitter.get_user_timeline(screen_name='TomBrowne7', count=3200, tweet_mode='extended')
tweets = tweets[tweets.tweet_retweeted_status.isnull()]
tweets = tweets[tweets.tweet_is_quote_status == False]
tweets = tweets[['user_id', 'tweet_id', 'tweet_created_at', 'tweet_full_text']]

# read file of existing tweets if it exists
# only retain fetched tweets where id not in saved tweets
# append new tweets to saved tweets
# save tweets to CSV
print('Reading saved tweets...\n')
infile = 'tombrowne7.csv'

if os.path.isfile((script_dir / data_dir / infile).resolve()):
    saved_tweets = pd.read_csv((script_dir / data_dir / infile).resolve())
    tweets = tweets.loc[~tweets['tweet_id'].isin(saved_tweets['tweet_id'])]
    tweets = pd.concat([saved_tweets, tweets])
    tweets.to_csv((script_dir / data_dir / infile).resolve(), index=False)
else:
    tweets.to_csv((script_dir / data_dir / infile).resolve(), index=False)

# extract and process tweet text
print('Processing text...\n')
text = ' '.join(tweets['tweet_full_text'])
text = text_cleaner(text)
text_doc = nlp(text)
text_sentences = ' '.join([sent.text for sent in text_doc.sents if len(sent.text) > 1])

# build markov model and save
print('Building model...\n')
generator = POSifiedText(text_sentences, state_size=3)
model_json = generator.to_json()

model_file = 'tom_browne_model.json'
with open((script_dir / data_dir / model_file).resolve(), 'w') as f:
    json.dump(model_json, f)


# generate fake tweets and save
print('Generating fake tweet text...\n')
fake_tweets = []
for i in range(50):
    fake_tweets.append(generator.make_short_sentence(280))
fake_tweets = pd.DataFrame(fake_tweets, columns=['text'])
fake_tweets = fake_tweets.drop_duplicates()

now = datetime.datetime.now()
ts = str(now.strftime('%Y%m%d_%H%M%S'))
outfile = 'faketombrowne7_' + ts + '.csv'
fake_tweets.to_csv((script_dir / output_dir / outfile).resolve(), index=False, header=False)

print('All done.\n')
