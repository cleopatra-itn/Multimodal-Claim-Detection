# Tweets Filtering


To start filtering provide the following parameters:
```
python tweet_filtering.py -t <tweets_file.json> -i <images_folder_path> -o <output_file.json>
```

Example script for filtering covid realted tweets
```
python tweet_filtering.py -i coronavirus_tweet.json -k "../corona_images/" -t filtered_Corona_Tweets.json
```

You should have list of tweets in jsonl format. Here is the example format of jsonl file:
```
{
	"created_at": "Thu Aug 23 13:01:06 +0000 2018",
	"id": 1032613703617859584,
	"id_str": "1032613703617859584",
	"full_text": "Floods that have been described as \u201cthe worst in 100 years\u201d by #Kerala state\u2019s chief minister shows how floods are changing. \n\nComment: https://t.co/R6ox3eoPP3 #climatechange https://t.co/r4xeb7vY1n",
	"truncated": false,
	"display_text_range": [0, 174],
	"entities": {
		"hashtags": [{
			"text": "Kerala",
			"indices": [63, 70]
		}, {
			"text": "climatechange",
			"indices": [160, 174]
		}],
		"symbols": [],
		"user_mentions": [],
		"urls": [{
			"url": "https://t.co/R6ox3eoPP3",
			"expanded_url": "https://buff.ly/2wedQGb",
			"display_url": "buff.ly/2wedQGb",
			"indices": [136, 159]
		}],
		"media": [{
			"id": 1032613701927325696,
			"id_str": "1032613701927325696",
			"indices": [175, 198],
			"media_url": "http://pbs.twimg.com/media/DlSUsN2UUAA026V.jpg",
			"media_url_https": "https://pbs.twimg.com/media/DlSUsN2UUAA026V.jpg",
			"url": "https://t.co/r4xeb7vY1n",
			"display_url": "pic.twitter.com/r4xeb7vY1n",
			"expanded_url": "https://twitter.com/ClimateHome/status/1032613703617859584/photo/1",
			"type": "photo",
			"sizes": {
				"thumb": {
					"w": 150,
					"h": 150,
					"resize": "crop"
				},
				"large": {
					"w": 800,
					"h": 450,
					"resize": "fit"
				},
				"medium": {
					"w": 800,
					"h": 450,
					"resize": "fit"
				},
				"small": {
					"w": 680,
					"h": 383,
					"resize": "fit"
				}
			}
		}]
	},
	"extended_entities": {
		"media": [{
			"id": 1032613701927325696,
			"id_str": "1032613701927325696",
			"indices": [175, 198],
			"media_url": "http://pbs.twimg.com/media/DlSUsN2UUAA026V.jpg",
			"media_url_https": "https://pbs.twimg.com/media/DlSUsN2UUAA026V.jpg",
			"url": "https://t.co/r4xeb7vY1n",
			"display_url": "pic.twitter.com/r4xeb7vY1n",
			"expanded_url": "https://twitter.com/ClimateHome/status/1032613703617859584/photo/1",
			"type": "photo",
			"sizes": {
				"thumb": {
					"w": 150,
					"h": 150,
					"resize": "crop"
				},
				"large": {
					"w": 800,
					"h": 450,
					"resize": "fit"
				},
				"medium": {
					"w": 800,
					"h": 450,
					"resize": "fit"
				},
				"small": {
					"w": 680,
					"h": 383,
					"resize": "fit"
				}
			}
		}]
	},
	"source": "<a href=\"https://buffer.com\" rel=\"nofollow\">Buffer</a>",
	"in_reply_to_status_id": null,
	"in_reply_to_status_id_str": null,
	"in_reply_to_user_id": null,
	"in_reply_to_user_id_str": null,
	"in_reply_to_screen_name": null,
	"user": {
		"id": 43092107,
		"id_str": "43092107",
		"name": "Climate Home News",
		"screen_name": "ClimateHome",
		"location": "London",
		"description": "Climate Home News is an award-winning independent news site dedicated to reporting news you can trust on the international politics of the climate crisis.",
		"url": "https://t.co/ChwqaH5eYC",
		"entities": {
			"url": {
				"urls": [{
					"url": "https://t.co/ChwqaH5eYC",
					"expanded_url": "http://www.climatechangenews.com",
					"display_url": "climatechangenews.com",
					"indices": [0, 23]
				}]
			},
			"description": {
				"urls": []
			}
		},
		"protected": false,
		"followers_count": 49169,
		"friends_count": 3088,
		"listed_count": 1572,
		"created_at": "Thu May 28 11:34:51 +0000 2009",
		"favourites_count": 1684,
		"utc_offset": null,
		"time_zone": null,
		"geo_enabled": true,
		"verified": false,
		"statuses_count": 51873,
		"lang": null,
		"contributors_enabled": false,
		"is_translator": false,
		"is_translation_enabled": false,
		"profile_background_color": "C0DEED",
		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
		"profile_background_tile": false,
		"profile_image_url": "http://pbs.twimg.com/profile_images/646596449145192448/AD5HVZuE_normal.png",
		"profile_image_url_https": "https://pbs.twimg.com/profile_images/646596449145192448/AD5HVZuE_normal.png",
		"profile_banner_url": "https://pbs.twimg.com/profile_banners/43092107/1523876802",
		"profile_link_color": "1DA1F2",
		"profile_sidebar_border_color": "C0DEED",
		"profile_sidebar_fill_color": "DDEEF6",
		"profile_text_color": "333333",
		"profile_use_background_image": true,
		"has_extended_profile": false,
		"default_profile": true,
		"default_profile_image": false,
		"following": null,
		"follow_request_sent": null,
		"notifications": null,
		"translator_type": "none"
	},
	"geo": null,
	"coordinates": null,
	"place": null,
	"contributors": null,
	"is_quote_status": false,
	"retweet_count": 2,
	"favorite_count": 1,
	"favorited": false,
	"retweeted": false,
	"possibly_sensitive": false,
	"possibly_sensitive_appealable": false,
	"lang": "en"
}
```
