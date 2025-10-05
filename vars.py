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
API_ID = 28379294
API_HASH = "f586b601ced6eeed819b280d6a9bc8eb"
USER_SESSION = environ.get("USER_SESSION", "BQGxCJ4ABRoW1QEcpWaCqqyY9c6HSRyt56cCITXVnnJ4D0XgB_MV0OYqh9pH0YHHjf6D3LFLfZAoxLo1aqjfBZheo1lilXKwcdusjVWdk_SW62QQaRCiDQxr02L38hxhN2DnmzyTHG0_uummHJJCH5QYIlmn-AwQAsQYPIsZRTsAIzJOnq1xZ19cb5DXlOgsHIiWHqXV3GedN6vw45Hl8R_eAVJ-8AxxME-H9mGn_lSqOzPj-YaE-ncCe2lPlr7IZzSAltwzkyu0GMYisq0ZtRfsG-jnkVVgLzUPrQTuyxjechrxwEMA5Rbz-ZnQk3x-Ow0XhEAVJOOjhRiOFpLkMFSmcKOI5wAAAAF33rosAA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003184409377"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002005238353 -1001232792540 -1001629066592 -1001763793679 -1001080367092').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6306052652').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
