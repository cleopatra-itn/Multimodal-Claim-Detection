#!/usr/bin/env python
# coding: utf-8

from tweet_parser.tweet import Tweet
from tweet_parser.tweet_parser_errors import NotATweetError
import fileinput
import json
import cv2 as cv
from PIL import Image 
from shutil import copyfile 
import os, os.path 
import sys, getopt

import spacy
from spacy_langdetect import LanguageDetector
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)

from PIL import Image
import requests
from io import BytesIO
import numpy as np
import pandas as pd


covidPath = ""
covidImgPath = ""

techPath = ""
techImgPath = ""

climatePath = ""
climateImgPath = ""


def process(tweets_path, images_path, output_file):
    df=pd.read_json(tweets_path, lines=True)
    df = df.loc[1:1000, ['id','text','entities','extended_entities','retweet_count']]

    
    #Replace the extended_entities column with only image_url
    inds = []
    Type_new = pd.Series([])
    c = 0
    for index, row in df.iterrows():
        rows = df['extended_entities'][index]
        b = rows['media']
        if b[0]['media_url'] != "":
            df['extended_entities'][index] = b[0]['media_url']
        else:
            df['extended_entities'][index] = ""
        c = c+1
    
    
    #Remove tweets which don't have text in english
    inds = []
    c = 0
    for row in df['text']:
        doc = nlp(row)
    
        if doc._.language['language'] != "en":
            inds.append(c)
        c = c+1
    
    
    #Sort tweets by retweet count
    df.sort_values(by=['retweet_count'], inplace=True, ascending=False)
    
    
    #Deduplicate the tweets based on text and keep the first one
    df = df.drop_duplicates('text', keep='first')

    
    #Remove tweets which have image-size less than our threshold 
    inds = []
    c = 0
    for index, row in df.iterrows():
        b = row['id']
        path = os.path.join(images_path,str(b)+".jpg")
        image = Image.open(path)
        width, height = image.size 
        if (width < 200 or height < 200):
            inds.append(c)
        c = c+1
    
    inds = []
    Type_new = pd.Series([])
    c = 0
    
    #Parse the hashtags
    for row in df['entities']:
        b = row['hashtags']
        tags = ""
        for t in b:    
            if t['text'] != "":
                tags = tags+"_"+t['text']
        Type_new[c] = tags
        c = c+1
        
        
    #Insert new column of hashtags
    df.insert(4, "hashtags", Type_new)
    df = df.dropna(subset=['text'])
    
    #Export CSV file
    df.to_csv(output_file)
    
    
def main(argv):
    
    tweets_path = ''
    images_path = ''
    output_file = ''
    
    try:
       opts, args = getopt.getopt(argv,"ht:i:o:",["ifile=","ifile=","ofile="])
    except getopt.GetoptError:
       print('tweet_filtering.py -t <tweets_file> -i <images_folder> -o <output_file>')
       sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('tweet_filtering.py -t <tweets_file> -i <images_folder> -o <output_file>')
            sys.exit(2)
            
        elif opt in ("-t", "--ifile"):
            tweets_path = arg
            
        elif opt in ("-i", "--ifile"):
            images_path = arg
            
        elif opt in ("-o", "--ofile"):
            output_file = arg
        
    print('Tweets file: ', tweets_path)
    print('Images file: ', images_path)
    print('Output file: ', output_file)
        
    process(tweets_path, images_path, output_file)
    

if __name__ == "__main__":
    main(sys.argv[1:])










