# Tweets Filtering


To start filtering provide the following parameters:
```
python TwitterFiltering.py -i GZIPPED_FILE -k TWITTER_API_KEYS -t YOUR_TOPIC
```

Example script for filtering covid realted tweets
```
python crawl_twitter.py -i coronavirus_tweet_ids.txt.gz -k twitter_keys.json -t coronavirus
```


You should have list of tweets in jsonl format. Here is an example of one tweet:
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
