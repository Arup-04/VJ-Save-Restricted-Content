import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24828869"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3b0dce801ac887dca64ca774a0f2e421")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1801203400"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://arupmondalofficial007:WLmgnUK3qUShlQBj@cluster0.pr055.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
