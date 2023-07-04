# nowplaying.py

Minimal Ubuntu script that posts whatever you're listening to to social media.

## Usage

```
usage: python3 nowplaying.py [-h] [-c FILE] [--dry-run]

Script to post what you're listening to to social media

options:
  -h, --help            show this help message and exit
  -c, --config FILE     location of the config file. Default ./config.yaml
  --dry-run             if specified, the script won't actually post to social media
```

![image](https://github.com/valerauko/nowplaying.py/assets/6322484/695cf594-1445-4ed7-a996-1f26353e7316)

## Configuration

The script needs a config file in the same location. Refer to the [config.yaml.sample](config.yaml.sample) for an example.

### Misskey token

Misskey's API token can be generated according to [the library's readme](https://github.com/YuzuRyo61/Misskey.py#create-token).

## Dev

1. `python3 -m venv .`
2. `bin/pip3 install -r requirements.txt`

Enjoy.

## License

WTFPL. Refer to [LICENSE.md](https://github.com/valerauko/nowplaying.py/blob/master/LICENSE.md).

### Cover photo

[Photo](https://unsplash.com/photos/n4BDkIEls78) by [Denisse Leon](https://unsplash.com/@denisseleon?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).
