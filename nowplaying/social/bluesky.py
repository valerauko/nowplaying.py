#coding=utf-8

from chitose import BskyAgent
from chitose.app.bsky.feed.post import Post
from datetime import datetime, timezone
from .isocial import ISocial

class Bluesky(ISocial):
    def __init__(self, config):
        self.agent = BskyAgent(service = config['service'])
        self.agent.login(
            identifier = config['user'], password = config['password'])

    def post(self, text):
        date = datetime.now(timezone.utc).isoformat()
        self.agent.post(
            record = Post(text = text, created_at = date))
