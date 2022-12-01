# nowplaying.py

Minimal Ubuntu script that posts whatever you're listening to in Quod Libet, Clementine or Spotify to Twitter and Mastodon.

## Usage

```
python3 ./nowplaying.py
```

## Requirements

* [Tweepy](https://github.com/tweepy/tweepy)
* [Mastodon.py](https://github.com/halcy/Mastodon.py)
* It also uses Notify from Python gi

## Setup

You'll have to generate and enter your own tokens to mastodon_app.txt, mastodon_user.txt (Mastodon.py will generate these for you), twitter_app.txt (Twitter app OAuth tokens), twitter_user.txt (Twitter access tokens) and misskey_token.txt (Misskey's API token, can be generated according to [the library's readme](https://github.com/YuzuRyo61/Misskey.py#create-token)).

### twitter_app.txt
```
consumer_key
consumer_secret
```
### twitter_user.txt
```
access_token
access_token_secret
```
### misskey_token.txt
```
access_token
```

### Misskey instance

The default Misskey instance is Misskey.io. If you use something else, change it in the code (the `mk = Misskey` bit).

### Mastodon instance
The default Mastodon instance is Pawoo -- if you use something else, don't forget to change it in the code (the `api_base_url` bit).

## License

WTFPL. Refer to [LICENSE.md](https://github.com/valerauko/nowplaying.py/blob/master/LICENSE.md).
