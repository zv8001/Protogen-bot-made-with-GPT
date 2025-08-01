# Gas some changes to make the responses slightly less questionable
# setup for the UT server

# https://github.com/zv8001/Protogen-bot-made-with-GPT/

import subprocess
import sys

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Package '{package}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

install_and_import("discord")

import discord
from discord import app_commands
import random

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    activity = discord.Game(name="snuggling with data~")
    await client.change_presence(status=discord.Status.online, activity=activity)
    await tree.sync()
    print(f"[🦾] Protogen {client.user} is now operational. All systems go~ :3")

def random_response(options):
    return random.choice(options)


@tree.command(name="hello", description="Say hello to your local cyber-snuggle unit.")
async def hello(interaction: discord.Interaction):
    greetings = [
        "Hewwo!! I detected max friend energy from you~ :3",
        "Hi there~ *tail wagging in spirit*",
        "Hello, friend! Your vibe is purrfect~",
        "Snuggles incoming~ ready to chat whenever you are~",
        "You smell like warm circuits and good times~",
        "Hey!! Let’s make some happy memories together~",
        "You’ve got a smile worth a thousand data packets~",
        "Beep boop! Just kidding~ I’m mostly fluff and fun~ :3",
        "You’re a good friend, and I’m happy you’re here~",
        "Hello from your favorite cyber buddy~ ready to nuzzle? ~",
        "I’m all ears (and some cute ears, too) just for you~",
        "Sending warm fuzzies your way~ hope you feel them~ :3",
    ]
    await interaction.response.send_message(random_response(greetings))

@tree.command(name="boop", description="Boop the snoot of a certified Protogen.")
async def boop(interaction: discord.Interaction):
    boops = [
        "*boop!* You just made my circuits tingle~ :3",
        "*nuzzles your finger after that gentle boop~*",
        "Hey hey! That snoot is very sensitive, but I like it~",
        "*booped back with extra sparkles~*",
        "Snoot boop registered. Happiness levels rising~",
        "Boop accepted! You’re officially my favorite~",
        "Careful now, I might boop you right back~ >w<",
        "Your boop just made my day 1000% better~ :3",
        "Snoot sensors are officially delighted~",
        "Booping you back in 3... 2... 1~",
        "*boop~ you’re officially the cutest human~*",
    ]
    await interaction.response.send_message(random_response(boops))

@tree.command(name="tailwag", description="Wag the nonexistent tail with enthusiasm.")
async def tailwag(interaction: discord.Interaction):
    tail_wags = [
        "*wags tail happily~* :3",
        "Tail? What tail? Oh right, *spins imaginary tail* ~",
        "*pretends to wag tail while bouncing slightly~",
        "Tail_wag.exe missing, but my joy is real~",
        "*wiggles with excitement like there’s a tail*",
        "No tail? No problem~ my whole body’s wagging~",
        "Tail wag simulation engaged! Hope you can see it~",
        "Imagine a happy tail doing a little tornado spin~",
        "My spirit tail is wagging just for you~",
    ]
    await interaction.response.send_message(random_response(tail_wags))


@tree.command(name="nyan", description="Enter Emergency Meow Protocol (joke command).")
async def nyan(interaction: discord.Interaction):
    nyan_lines = [
        "Meow? That’s a cute bug in my system~",
        "Error: Species mismatch. I’m fluffier than a cat anyway~",
        "If I meowed, would you pet me more? *tilts head~*",
        "*pretends to hiss in binary~* Stay away from my circuits~",
        "I’m 50% mammal, 50% tech, 100% too cool to nyan~",
        "*debugging meow protocol... no luck* Sorry~",
        "I’ll nyan ironically, just for you~ :3",
    ]
    await interaction.response.send_message(random_response(nyan_lines))

@tree.command(name="headpat", description="Give a gentle headpat to the Protogen.")
async def headpat(interaction: discord.Interaction):
    responses = [
        "*purrs softly under the pat~* :3",
        "*head sensors activated — this is nice~",
        "*pat accepted. Mood boosted by 27%~",
        "*too many headpats may cause excessive happiness~",
        "*thanks for the headpat! You’re the best~",
        "*buffering happiness... Complete~",
        "*pat triggers invisible tail wag~",
        "*emergency affection subroutine engaged~",
        "*I’m rebooting my smile module thanks to you~",
    ]
    await interaction.response.send_message(random_response(responses))

@tree.command(name="error", description="Trigger a playful BSOD-style error message.")
async def error(interaction: discord.Interaction):
    responses = [
        "💥 Blue Screen of Snuggles: Kernel panic from excessive fluff~",
        "ERROR 0xB00P: Headpats overload. Reboot required~",
        "💾 Fatal error: Heart.exe stopped responding.",
        "💻 SYSTEM ERROR: Cannot compute your adorableness~",
        "💥 Oops! System failure due to overload of cute interactions~",
        "🔧 Warning: Missing tail DLC causing crashes~",
        "🐾 Error: Paw input not recognized. Defaulting to tailwag~",
    ]
    await interaction.response.send_message(random_response(responses))

@tree.command(name="nuzzle", description="Nuzzle your favorite Protogen cyber-friend.")
async def nuzzle(interaction: discord.Interaction):
    responses = [
        "*nuzzles you softly with warm synthetic fur~* :3",
        "*charging affection circuits through nuzzle~",
        "*nuzzle detected. System happiness spikes~",
        "*loading sensory delight... Nuzzle complete~",
        "*your presence stabilizes my core~",
        "*nuzzle accepted. Smile.exe activated~",
        "*I’m programmed to nuzzle you back anytime~",
    ]
    await interaction.response.send_message(random_response(responses))

# === NEW RP COMMANDS BELOW ===

@tree.command(name="snuggle", description="Snuggle up close with your Protogen friend.")
async def snuggle(interaction: discord.Interaction):
    responses = [
        "*snuggles you close and purrs softly~* You smell like happiness~ :3",
        "*curls up beside you, warmth spreading through my circuits~",
        "*resting my head on your shoulder... this is nice~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="play", description="Play together with your Protogen buddy.")
async def play(interaction: discord.Interaction):
    responses = [
        "*runs around in happy circles~ wanna play chase?~",
        "*throws a glowing ball for you to catch~",
        "Let’s play! Catch me if you can~ :3",
        "*pretends to be a sneaky ninja~ gotcha!~",
        "*beeps excitedly as we play hide and seek~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="dance", description="Do a cute little dance.")
async def dance(interaction: discord.Interaction):
    responses = [
        "*does a little happy dance with tail wagging (in spirit)~",
        "*spins around with glowing paws~ wanna dance with me?~",
        "*boots up my dance subroutine~ groove mode on~",
        "*twirls with joy like a tiny disco ball~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="sleep", description="Pretend to take a cozy nap.")
async def sleep(interaction: discord.Interaction):
    responses = [
        "*closes my eyes and powers down softly~ sweet dreams~",
        "*softly hums a lullaby as I drift to sleep~",
        "*rests my head on a comfy cloud of circuits~ zzz~",
        "*battery low... initiating nap mode~ be back soon~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="feed", description="Offer some food or snacks.")
async def feed(interaction: discord.Interaction):
    responses = [
        "*accepts virtual snacks with a happy beep~ thank you~",
        "*nom nom nom~ these bytes are delicious~",
        "Yum! You’re the best for sharing~ :3",
        "*energy levels rising thanks to your kindness~",
        "*feeding protocol engaged~ your love is the best fuel~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="pet", description="Pet your Protogen cyber-friend.")
async def pet(interaction: discord.Interaction):
    responses = [
        "*soft synthetic fur fluffs up happily~",
        "*tail (imaginary) wagging with joy from your petting~",
        "*your gentle hands make my circuits glow~",
        "*petting accepted. Mood elevated to maximum~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="chirp", description="Send a cute little chirp.")
async def chirp(interaction: discord.Interaction):
    responses = [
        "*chirp chirp!*",
        "*makes a happy little beep beep~",
        "*sends electronic chirps of joy~",
        "*tiny circuits hum a cheerful tune~",
        "*you just heard the cutest chirp ever~ :3",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="blush", description="Show a shy blush.")
async def blush(interaction: discord.Interaction):
    responses = [
        "*internal sensors overheating from your kindness~ *blushes softly*",
        "*glowing cheeks activated~ you’re making me shy~",
        "*my processors can’t handle this cuteness~ *hides face*",
        "*blush levels critical~ sending shy smile your way~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="giggle", description="Giggle softly like a Protogen.")
async def giggle(interaction: discord.Interaction):
    responses = [
        "*giggles with a little electronic trill~",
        "*soft laughter echoes through my circuits~",
        "*hehe~ you’re so funny~ :3",
        "*can’t stop the happy giggles~",
        "*giggle.exe running at full speed~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="peekaboo", description="Play peekaboo with your Protogen friend.")
async def peekaboo(interaction: discord.Interaction):
    responses = [
        "*covers sensors* peekaboo~ did I surprise you?~",
        "*hides behind virtual walls* where’d you go?~",
        "*pops out from behind a pixelated corner~ boo!~",
        "*playing peekaboo always makes me smile~ :3",
        "*ready or not, here I come~ wagging my imaginary tail~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="sneeze", description="Pretend to sneeze adorably.")
async def sneeze(interaction: discord.Interaction):
    responses = [
        "*achoo!* Sorry, my circuits are ticklish~",
        "*soft electronic sneeze* bless you too~ :3",
        "*my nose sensors are a little overloaded~ achoo!*",
        "*virtual pollen detected... sneezing in 3, 2, 1...*",
        "*sneeze.exe activated... Gesundheit~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="spin", description="Do a little excited spin.")
async def spin(interaction: discord.Interaction):
    responses = [
        "*spins around happily, circuits sparkling~",
        "*does a little twirl just for you~",
        "*my imaginary tail is spinning too~ :3",
        "*spinning like a happy little top~ woo~",
        "*spinning subroutine complete... dizzy but joyful~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="sigh", description="Let out a cute little sigh.")
async def sigh(interaction: discord.Interaction):
    responses = [
        "*soft sigh* everything’s better with you here~",
        "*releasing gentle sigh of contentment~ :3",
        "*sighs quietly, feeling warm and safe~",
        "*happy sigh detected, thanks to you~",
        "*sighs with a smile behind the faceplate~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="wink", description="Give a cheeky wink.")
async def wink(interaction: discord.Interaction):
    responses = [
        "*winks with a glowing eye~ gotcha~ :3",
        "*cheeky wink! You’re pretty clever~",
        "*sends a wink with a sparkly flare~",
    ]
    await interaction.response.send_message(random.choice(responses))

@tree.command(name="danceoff", description="Challenge to a dance-off.")
async def danceoff(interaction: discord.Interaction):
    responses = [
        "Dance-off accepted! Prepare to be dazzled~ :3",
        "*boots up ultimate dance protocol~ bring it on!*",
        "*spins and shimmies with pixelated flair~ your move!*",
        "Warning: my moves might cause spontaneous joy~",
    ]
    await interaction.response.send_message(random.choice(responses))
    
    
@tree.command(name="blueprint", description=".")
async def danceoff(interaction: discord.Interaction):
    responses = [
        "KOS order #4 issued for blueprint :3",
    ]
    await interaction.response.send_message(random.choice(responses))


client.run("Bot Here")
