import os
from pathlib import Path
import shelve


DATA_DIR = os.path.join(Path.home(), ".local/share/Emote")
SHELVE_PATH = os.path.join(DATA_DIR, "user_data")

RECENT_EMOJIS = "recent_emojis"
DEFAULT_RECENT_EMOJIS = ["🙂", "😄", "❤️", "👍", "🤞", "🔥", "🤣", "😍", "😭"]
MAX_RECENT_EMOJIS = 54

ACCELERATOR_STRING = "accelerator_string"
DEFAULT_ACCELERATOR_STRING = "<Primary><Alt>e"

ACCELERATOR_LABEL = "accelerator_label"
DEFAULT_ACCELERATOR_LABEL = "Ctrl+Alt+E"

SHOWN_WELCOME = "shown_welcome"
DEFAULT_SHOWN_WELCOME = False


# Ensure the data dir exists
os.makedirs(DATA_DIR, exist_ok=True)


def load_recent_emojis():
    with shelve.open(SHELVE_PATH) as db:
        return db.get(RECENT_EMOJIS, DEFAULT_RECENT_EMOJIS)


def update_recent_emojis(emoji):
    recent_emojis = load_recent_emojis()

    if emoji in recent_emojis:
        recent_emojis.remove(emoji)
        new_recent_emojis = [emoji] + recent_emojis[: MAX_RECENT_EMOJIS - 2]
    else:
        new_recent_emojis = [emoji] + recent_emojis[: MAX_RECENT_EMOJIS - 1]

    with shelve.open(SHELVE_PATH) as db:
        db[RECENT_EMOJIS] = new_recent_emojis


def load_accelerator():
    with shelve.open(SHELVE_PATH) as db:
        return (
            db.get(ACCELERATOR_STRING, DEFAULT_ACCELERATOR_STRING),
            db.get(ACCELERATOR_LABEL, DEFAULT_ACCELERATOR_LABEL),
        )


def update_accelerator(accel_string, accel_label):
    with shelve.open(SHELVE_PATH) as db:
        db[ACCELERATOR_STRING] = accel_string
        db[ACCELERATOR_LABEL] = accel_label


def load_shown_welcome():
    with shelve.open(SHELVE_PATH) as db:
        return db.get(SHOWN_WELCOME, DEFAULT_SHOWN_WELCOME)


def update_shown_welcome():
    with shelve.open(SHELVE_PATH) as db:
        db[SHOWN_WELCOME] = True
