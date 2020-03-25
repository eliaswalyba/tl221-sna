import os

consumer = {
    "key": os.getenv("TL221SNA_CONSUMER_KEY"),
    "secret": os.getenv("TL221SNA_CONSUMER_SECRET")
}
access = {
    "token": os.getenv("TL221SNA_ACCESS_TOKEN"),
    "secret": os.getenv("TL221SNA_ACCESS_TOKEN_SECRET")
}