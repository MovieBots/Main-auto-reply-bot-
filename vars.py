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
USER_SESSION = environ.get("USER_SESSION", "BQHABkIAbu_0JAtgStlyEbQ5rSDjsywsbQ8pVV37JG9ZrNj-DCUdv9hYng6qCh4g1gcx7IyJD6nxaD1GMQMz5xHoIquNenRmqrM_clv_CJ9elntC3tEdCQEYiLBlP2YZaq-OETXYXtOuE39KPuMGl8elg-NMDt_Nl5hHBSCqvebpFC1ovR6TZPal1716chdNV_gGA8zmm7wMtPk6y5O7k0X2qt4BTozO6MzfbDFLtucP3b_u5i_zUeJkMyDuX5tdfFkyIsN5i_UF4jIembInnOdAqHJeCwJa71YamWN6ZWj8jy_w5ZepA50l1XooBrDsf86Ir_ZsKRZ0d9e0Scq4zECUyv7BxgAAAAGad7H_AA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003184409377"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002982298986 -1002834069268').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6886502911').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
