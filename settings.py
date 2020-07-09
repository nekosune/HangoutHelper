from dotenv import load_dotenv

import os


def load_configs():
    load_dotenv(verbose=True)


def get_prefix():
    return os.getenv("BOT_PREFIX")


def get_key():
    return os.getenv("BOT_KEY")

def get_channel():
    return os.getenv("ANNOUNCE_CHANNEL")