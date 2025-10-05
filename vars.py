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
USER_SESSION = environ.get("USER_SESSION", "BQGV2YgAXLfe08g0ytXRDkDEiDriFIBK4IijBWTJlqMZrRiUBsB8kf6DRxE_EIA0LtqaOqFPJiXvwvpEDB8KyqDBgEaeEYEjzNvBvlrYaqOzuSxvQz8F6nFJBHIg4fTFllkxP617Mb1SLeeehDsNbSr7XMcBqNR_4XWM-2kM518RQzyjqKFccQ6eZZmHVFFKXg3uuJpucnpPbe1N9Y6QAonNP3jcFVhAAhXDghkvj1SIBOfANaJxE9akIG40JDsIcXCZ50DPlpvShICCpPOTQ1g5ja4Hi747kH9mgvthMw9iWrKrCrjI4GedSilMZMutrG1UZ9qZze8YlFeQXfUj98HOfceDiAAAAAHYPVj0AA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003184409377"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1001629066592').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6306052652').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
