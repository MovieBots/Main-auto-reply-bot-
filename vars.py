from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "N2 Auto Reply Bot")
API_ID = 29361730
API_HASH = "9d327b43fc075d760f16bab18b4cb90e"
USER_SESSION = environ.get("USER_SESSION", "BQGxCJ4Au2sMgAgl3rPxAOXPyPEusC3ikA4vIWINRSrNIuVleSt2mDKoe3fDZF63dViInWImNeRhCeF4TZ59m3q6DowrXsiay8oo9oi8dobkpnsaV48T17pB6EA55B9HhM8XbS2fySybUOYDu5lfWj_n_fiLAR12g8Uw6gifaYt8KCrW4SfDiZ_eZizwzfcuPsM9YnTuZPtAwFGGEJhffBugo7Av60rGfmaYgpSnk3aauk2dFZ52ZnAhIS0QF5PCCCTmf1ZkV6bU08ns77w5PC0BJXdZqrPrjTjdJlKZYshjJlTWwNGxwhElJYXM-jrTfuJEZvryUzp-gwozE7BSggU3L5YM8wAAAAGad7H_AA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003184409377"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002982298986').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6886502911').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
