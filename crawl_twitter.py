from twython import Twython, TwythonError
import requests
import file_utils
import json
import time
import gzip
import sys, getopt




def query_twitter(twython_api, id):
    try:
        result = twython_api.show_status(id=id, tweet_mode='extended')
        return 200, result
    except TwythonError as e:
        return e.error_code, None


def download_data(file_name, url):
    try:
        r = requests.get(url)
        f = open(file_name, 'wb')
        for chunk in r.iter_content(chunk_size=255):
            if chunk:
                f.write(chunk)
        f.close()
        return True
    except:
        return False


def is_valid_video(video_data):
    if video_data['type'] == 'video':
        if 'video_info' in video_data:
            # min 10 sec and max 2 mins videos
            if video_data['video_info']['duration_millis'] >= 10000 and video_data['video_info'][
                'duration_millis'] <= 120000:
                if 'variants' in video_data['video_info']:
                    return True
    return False


def get_video_url(video_data):
    max_bit_rate = 0
    video_url = ''

    for variant_index in range(0, len(video_data['video_info']['variants'])):
        variant = video_data['video_info']['variants'][variant_index]
        if 'bitrate' in variant:
            bit_rate = variant['bitrate']
            v_url = variant['url']

            if bit_rate > max_bit_rate:
                max_bit_rate = bit_rate
                video_url = v_url

    return video_url

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

def get_image_url(image_data):
    if 'media_url' in image_data:
        if image_data['media_url'].lower().endswith(('.png', '.jpg', '.jpeg')):
            return image_data['media_url']
    return ''


def process(gzip_file, keys_file, topic):
    # to query Twitter API with credentials
    twitter_keys = file_utils.read_json_file(keys_file)
    twython_api = Twython(twitter_keys['app_key'], twitter_keys['app_secret'])


    checkpoint = list()
    try:
        checkpoint = file_utils.read_file_to_list('checkpoint.txt')
    except:
        pass

    print('checkpoint size', len(checkpoint))

    if not file_utils.path_exists('data'):
        file_utils.create_folder('data')

    if not file_utils.path_exists('data/' + topic):
        file_utils.create_folder('data/' + topic)

    if not file_utils.path_exists('data/' + topic + '/videos'):
        file_utils.create_folder('data/' + topic + '/videos')

    if not file_utils.path_exists('data/' + topic + '/images'):
        file_utils.create_folder('data/' + topic + '/images')

    print('Running the crawling ...')
    with gzip.open(gzip_file) as f:
        while True:
            lines = f.readlines(10000)
            if not lines:
                break
            for line in lines:

                tweet_id = line.decode("utf-8").replace('\n', '')

                if tweet_id in checkpoint:
                    continue

                checkpoint.append(tweet_id)
                if len(checkpoint) %10 == 0:
                    print(len(checkpoint))

                # ----------------------------------------------------------------#
                # STEP 1: Query Twitter
                # STEP 2: Save the returned tweet
                # ----------------------------------------------------------------#

                # STEP 1: Query Twitter
                counter_request_for_tweet = 0
                while True:
                    status_code, result = query_twitter(twython_api, tweet_id)
                    counter_request_for_tweet += 1

                    if status_code in (200, 404, 403):
                        break

                    # max number of requests per tweet is reached
                    if counter_request_for_tweet == 10:
                        break

                    if status_code == 429:
                        print("Rate limit is reached, sleeping for 15 mins")
                        file_utils.save_list_to_file(checkpoint, 'checkpoint.txt')
                        time.sleep(15 * 60)

                if status_code != 200:
                    continue

                # STEP 2: Save the returned tweet
                if 'extended_entities' in result and result['lang'] == 'en':
                    is_video = False
                    for v_index in range(0, len(result['extended_entities']['media'])):
                        if is_valid_video(result['extended_entities']['media'][v_index]):
                            video_url = get_video_url(result['extended_entities']['media'][v_index])

                            if video_url != '':
                                is_downloaded = download_data('data/' + topic + '/videos/' + result['id_str'] + '.mp4', video_url)
                                if is_downloaded:
                                    json_output = json.dumps(result)
                                    file_utils.append_string_to_file(json_output, 'data/' + topic +'/video_tweets.jsonl')

                                    is_video = True
                                    break

                    if not is_video:
                        for v_index in range(0, len(result['extended_entities']['media'])):
                            image_url = get_image_url(result['extended_entities']['media'][v_index])
                            if image_url != '':
                                is_downloaded = download_data('data/' + topic + '/images/' + result['id_str'] + '.jpg', image_url)
                                if is_downloaded:
                                    json_output = json.dumps(result)
                                    file_utils.append_string_to_file(json_output, 'data/' + topic + '/image_tweets.jsonl')
                                    break

                if len(checkpoint) % 100 == 0:
                    file_utils.save_list_to_file(checkpoint, 'checkpoint.txt')

def main(argv):
   gzip_file = ''
   keys_file = ''
   topic = ''
   try:
       opts, args = getopt.getopt(argv,"hi:k:t:",["ifile=","kfile=", "topic="])
   except getopt.GetoptError:
       print('crawl_twitter.py -i <input_file> -k <keys_file>')
       sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print('crawl_twitter.py -i <input_file> -k <keys_file>')
           sys.exit()
       elif opt in ("-i", "--ifile"):
           gzip_file = arg
       elif opt in ("-k", "--kfile"):
           keys_file = arg
       elif opt in ("-t", "--topic"):
           topic = arg

   print('Input file: ', gzip_file)
   print('Keys file: ', keys_file)
   print('Topic: ', topic)

   process(gzip_file, keys_file, topic)


if __name__ == "__main__":
   main(sys.argv[1:])
