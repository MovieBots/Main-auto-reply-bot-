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
API_ID = 21299114
API_HASH = "8e846355fd1480c9416656238030200e"
USER_SESSION = environ.get("USER_SESSION", "BQFE_6oAD3eCGzznvlJOnDTnP9A2xiQALKpLecaEEVFaARH9wKHOazI3eK4kaD6RZZClTcCTPE9hzxRfHPqpOrRrvc7Cn7YeyRH576xDuTxYMXg9HVIB3YeEppxGUo3O5ttQ6gfqOzC-8QmKh0nwSdYhknMeaUeycEzUC1zURBuflfQ0LuPws4cXAwG0jg9hLLBEg9GRJqXpZhe88KohLzj58564Eto3BPa7xA-gCOO5ozGoyFoxQuxlH6F8Yv5RY1PKGRIF4nvbi66kcM1gGHNu6Du_tT9z-tMbWIBycJRY1DV1hdf-QBZ_jjmN8mbeR8wTSFNHs0TB0tbNBn5G7vjiaprQwwAAAAHndUqJAA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003184409377"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002220525479 -1002005238353 -1001232792540').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '8178190985').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
