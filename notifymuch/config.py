import os
import configparser
from gi.repository import GLib


__all__ = ['load', 'get']


CONFIG_DIR = os.path.join(GLib.get_user_config_dir(), 'notifymuch')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'notifymuch.cfg')

DEFAULT_CONFIG = {
    'query': 'is:unread and is:inbox',
    'mail_client': 'gnome-terminal -x mutt -y',
    'recency_interval_hours': '48',
    'hidden_tags': 'inbox unread attachment replied sent encrypted signed',
}

CONFIG = configparser.ConfigParser()


def load():
    global CONFIG
    CONFIG['notifymuch'] = DEFAULT_CONFIG
    if not CONFIG.read(CONFIG_FILE):
        try:
            os.makedirs(CONFIG_DIR)
        except OSError as e:
            if e.errno == 17:
                print('The directory CONFIG_DIR exists')
        with open(CONFIG_FILE, "w") as f:
            CONFIG.write(f)


def get(option):
    return CONFIG['notifymuch'][option]
