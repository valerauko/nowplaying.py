# nowplaying.py

Minimal Ubuntu script that posts whatever you're listening to in Clementine or Spotify to Twitter and Mastodon.

# Requirements

* [Tweepy](https://github.com/tweepy/tweepy)
* [Mastodon.py](https://github.com/halcy/Mastodon.py)
* It also uses Notify from Python gi

# Setup

You'll have to generate and enter your own tokens to mastodon_app.txt, mastodon_user.txt (Mastodon.py will generate these for you), twitter_app.txt (Twitter app OAuth tokens), twitter_user.txt (Twitter access tokens).
The default Mastodon instance is Pawoo -- if you use something else, don't forget to change it on [line 49](https://github.com/valerauko/nowplaying.py/blob/master/nowplaying.py#L49).

# License

WTFPL. Refer to [LICENSE.md](https://github.com/valerauko/nowplaying.py/blob/master/LICENSE.md).
