from AngelMusic.core.bot import Anony
from AngelMusic.core.dir import dirr
from AngelMusic.core.git import git
from AngelMusic.core.userbot import Userbot
from AngelMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
