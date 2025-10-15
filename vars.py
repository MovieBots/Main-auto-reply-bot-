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
USER_SESSION = environ.get("USER_SESSION", "BQGcAJsALR1kVjaDHPOdtpl7ueK01wbehgiK07TxSXu5T1bQEqrE4IQe118uRM_TRaWMyAfC-9RTSGw4dqOyhgZZnD5vkOp526oyRCuB5zHhbpH3mysE6JqKCwOXH8DlX-08b_6FrKmreOBX7P3unnEKIjInODSdoqfa9nppbCqjIURPZx9xdC1QMCpkT9tBE6DZkz6hIx5lhYMgMf46_tf8___9t4FmTw9GK0gXI9osfhK1ZQ7IFHjRCDxjORNc4Jm7WY8k4Bukc1pq3aER0KlkMvxZPoQKJIr8jxjMFZujwS56xAsJJw29L3EE8X4wLLPjYV8OEUs_SaFpK3GIYLPvT8hQnQAAAAF33rosAA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003184409377"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1001629066592').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6306052652').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
