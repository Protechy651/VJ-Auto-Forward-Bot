from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "6057e930c3b495c98e979c1df311d6c3")
      API_ID = int(getenv("API_ID", "28037792"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6963108191:AAHR3WG0jcKxFzGWht6c9MF3nutwy4boeYs")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002022758511:-1002100847281").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
