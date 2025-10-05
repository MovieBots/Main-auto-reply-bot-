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
USER_SESSION = environ.get("USER_SESSION", "BQGxCJ4AgzFvsDaIZ2pIG_3rGhcfuRBfWV23s_LNj8-DZsDoCR8I-6rKj_idGDXL8c0L3VK1IKTZnXaesVufu5w9_indAV8QGGGV2mwtf4JcScisWB9pe6ud6IHHPTbtkM1OqFElGNRmtHl2S3TQcBeecukm29cLSTONsB5PKnOQaOwPNhvYR1mVh2HM7_oYf43wmvscQoGB2HmIrIWvaxwiReyAfDMzGc86ow5vtHZSTHdUnHlvs23k3_UXeUqiAUyLd_-shFb8zU8cj0e8T-0G_bemHgY0G5nOQG_TXz8am8RgV9OpXS80hohkrABz47srhSdk6J4Ur-2AwhszDa_W9xb4TwAAAAHYPVj0AA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003184409377"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1001629066592').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6306052652').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
