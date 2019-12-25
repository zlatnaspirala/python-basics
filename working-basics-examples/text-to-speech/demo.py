
# pip install gTTS

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = """ Project: Visual ts game engine

  Version: Sunshine - 2019

  2d canvas game engine based on Matter.js 2D physics engine for the web.

  Writen in typescript current version 3.5.1.
  Text editor used and recommended: Visual Studio Code. Luanch debugger configuration comes with this project.
  Physics engine based on Matter.js.
  Multiplatform video chat(for all browsers) implemented. SocketIO used for session staff. MultiRTC2 used for data transfer also for video chat. MultiRTC3 alias 'broadcaster' used for video chat. ! """


# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
