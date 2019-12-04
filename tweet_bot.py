import tweepy
import time

auth = tweepy.OAuthHandler('RyoagsmaSaiDuwX7AerUYbAiy', 'kLUF6bGs4UgH61S1yjr0Pz2qnLv1G8Gu7YHaqApAVNYwSno2Ej')
auth.set_access_token('48384533-hBn1IH63zLXrXCyCuEVLyNk66WEafATCGhB4Q7FT0', 'evRCTWy62d97D4g6qaU5Cy4Y3Cvthozm8yiSUZQoImibF')

api = tweepy.API(auth)
user = api.get_user('twitter')


def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)


# Narcissistic Bot
search_string = '@hey_patterson'
numbersOfTweets = 20

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numbersOfTweets)):
	try:
		tweet.favorite()
		print("I like that tweet.")
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

# Generous Bot (Follows everyone who follow me)
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	follower.follow()
		

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)