# Multimodal-Claim-Detection


To start crawling provide the following parameters:
```
python crawl_twitter.py -i GZIPPED_FILE -k TWITTER_API_KEYS -t YOUR_TOPIC
```

Example script for coronavirus using the sample tweet ids
```
python crawl_twitter.py -i coronavirus_tweet_ids.txt.gz -k twitter_keys.json -t coronavirus
```


You need the create the JSON file called 'twitter_keys.json' as given below, add your APP Key and Secrets here:
```
{
  "app_key": "YOUR_APP_KEY",
  "app_secret": "YOUR_SECRET"
}
```


'coronavirus_tweet_ids.txt.gz' is Gzipped file where each line contains a single tweet ID
```
1212360731695427584
1212470713338286081
1212537749485449216
```
