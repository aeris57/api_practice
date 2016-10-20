from twitter_utils import get_request_token, get_oauth_verifier, get_access_token
from user import User
from database import Database

Database.initialise()

user_screen_name = input("Enter your screen name: ")

user = User.load_from_db_sname(user_screen_name)

if not user:
    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    user = User(user_screen_name, access_token['oauth_token'],
                access_token['oauth_token_secret'], None)
    user.save_to_db()

tweets = (user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computer+filter:images'))

for tweet in tweets['statuses']:
    print(tweet['text'])
