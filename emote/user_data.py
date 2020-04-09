import os
from pathlib import Path
import shelve


DATA_DIR = os.path.join(Path.home(), '.local/share/Emote')
SHELVE_PATH = os.path.join(DATA_DIR, 'user_data')
DEFAULT_RECENT_EMOJIS = ['🙂', '😄', '❤️', '👍', '🤞', '🔥', '🤣', '😍', '😭']
RECENT_EMOJIS = 'recent_emojis'
MAX_RECENT_EMOJIS = 54


# Ensure the data dir exists
os.makedirs(DATA_DIR, exist_ok=True)


def load_recent_emojis():
    with shelve.open(SHELVE_PATH) as db:
        return db.get(RECENT_EMOJIS, DEFAULT_RECENT_EMOJIS)


def update_recent_emojis(emoji):
    recent_emojis = load_recent_emojis()

    if emoji in recent_emojis:
        recent_emojis.remove(emoji)
        new_recent_emojis = [emoji] + recent_emojis[:MAX_RECENT_EMOJIS - 2]
    else:
        new_recent_emojis = [emoji] + recent_emojis[:MAX_RECENT_EMOJIS - 1]

    with shelve.open(SHELVE_PATH) as db:
        db[RECENT_EMOJIS] = new_recent_emojis
