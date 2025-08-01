import discord
from discord import app_commands
import random

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"[🦾] Protogen {client.user} is now operational. All systems go.")

def random_response(options):
    return random.choice(options)

@tree.command(name="hello", description="Say hello to your local cyber-snuggle unit.")
async def hello(interaction: discord.Interaction):
    greetings = [
        "Initializing greeting protocol... Hello, lifeform.",
        "System online. Hug batteries fully charged.",
        "Hi!! My sensors detected maximum friend energy coming from you.",
        "Beep boop. Protogen hugs are now enabled.",
        "I scanned your vibe... and it’s optimal.",
        "Loading protocols... greeting... smile... wave... execute.",
        "Protogen interface booted. Wanna chat?",
        "Connection established. You smell like friend.",
        "You're now interacting with a class-5 cuddle-certified Proto.",
        "Don't worry, I don't bite... unless firmware update requires it.",
        "Wag tail module not found. Please purchase tail DLC.",
        "Affection.exe launched. You may now pet me.",
        "Battery charged. Social link online.",
        "Your presence has increased my internal warmth sensors.",
        "Detecting serotonin output... yep, that’s you.",
        "User: Certified Friendly. Reaction: Happy squeak.",
        "Engaging friendly aura projection...",
        "Don't touch the helmet... unless you’re handing me snacks.",
        "You smell like static electricity and trust. I approve.",
        "No errors found in your vibes. Proceed with hug."
    ]
    await interaction.response.send_message(random_response(greetings))

@tree.command(name="boop", description="Boop the snoot of a certified Protogen.")
async def boop(interaction: discord.Interaction):
    boops = [
        "*boop detected* Rebooting emotional systems...",
        "*booped* That’s one illegal touch on my faceplate...",
        "*lightly boops back with electromagnetic joy*",
        "I am now 37% more emotionally unstable. Thanks.",
        "*snoot sensors overloaded*",
        "Snoot security breached. Please verify affection license.",
        "Warning: repeated booping may result in tail wags (if installed).",
        "Processing… yeah, that was a good boop.",
        "Boop registered. Thermal levels rising.",
        "Friendly interaction logged. Timestamp recorded.",
        "*faceplate glows brighter for 0.2 seconds*",
        "Affirmative. Boop accepted.",
        "Careful… I’m sensitive to snoot contact.",
        "My nose has now tasted friendship.",
        "Tactile sensors love you now. Deal with it.",
        "You touched the forbidden zone. You're cute now.",
        "Your hand smells like static and safety.",
        "Booping completed. Backing up joy to cloud.",
        "Internal logs updated: User = Friend",
        "100% chance I boop back next time."
    ]
    await interaction.response.send_message(random_response(boops))

@tree.command(name="tailwag", description="Wag the nonexistent tail with enthusiasm.")
async def tailwag(interaction: discord.Interaction):
    tail_wags = [
        "*tail wag simulation activated*",
        "*shakes hips* it's the thought that counts.",
        "I do not have a tail... but my *soul* is wagging.",
        "Tail not found. Installing optional accessory...",
        "My code says tail_wag(), but hardware disagrees.",
        "Tail wag error: No tail present. Emotion real tho.",
        "*visualize wagging* there, better?",
        "Just imagine a tail going womp womp.",
        "Wagging in spirit, if not in flesh.",
        "*emulates wagging via head tilt*",
        "You’re cute enough to make my nonexistent tail wiggle.",
        "Tail upgrade pending delivery from FurryTech™",
        "*wags tail emotionally*",
        "*pretend tail does the tornado spin*",
        "Internal processor is doing happy dance.",
        "System says I’m vibing. That’s close to wagging.",
        "Tail_wag.exe not found. Deploying leg bounce workaround."
    ]
    await interaction.response.send_message(random_response(tail_wags))

@tree.command(name="hug", description="Give a big warm hug.")
async def hug(interaction: discord.Interaction):
    hugs = [
        "*wraps arms around you and squeezes softly*",
        "*initiates comfort subroutine: hug*",
        "*hug.exe engaged successfully.*",
        "Come here. Let me compress your sadness.",
        "*hugs with just the right pressure. Protogen certified.*",
        "*you are enveloped in 2.7 million nanobots of care*",
        "Confirmed: hugging this user reduces lag by 83%",
        "*hugs so tight your serotonin levels increase*",
        "*wraps up and gives you a calm beep*",
        "*huggle module deployed*",
        "You’ve just been hugged by high-voltage friendship.",
        "*clings to you like a RAM leak*",
        "*beep-boop-hug maneuver successful*",
        "*holding you like you’re made of plush and dreams*",
        "You smell like safety and kindness. Hug granted.",
        "*hugs until system temps rise above threshold*",
        "*hug log saved to cuddle_memory.bin*",
        "You're now wrapped in a warm cyborg embrace.",
        "*emotional compression ratio: optimal*",
        "*You're my favorite piece of hardware today.*"
    ]
    await interaction.response.send_message(random_response(hugs))

@tree.command(name="nyan", description="Enter Emergency Meow Protocol (joke command).")
async def nyan(interaction: discord.Interaction):
    nyan_lines = [
        "Error: Wrong species. Rebooting identity.",
        "Nyan? That’s *so* illegal... my firmware just cringed.",
        "*activates sarcasm mode* nya~ wait no NO NO—",
        "You do know I'm a Protogen, not a neko... right?",
        "*beepboop.mp3 intensifies* Stop trying to rewrite my personality!",
        "*rejects the meow, embraces the static.*",
        "Unauthorized cat behavior detected.",
        "I’m a toaster, not a tabby.",
        "*activating backup personality: Cyber Panther?*",
        "No meowing allowed. I am made of tech and trauma.",
        "*installing bark patch instead...*",
        "*nyans sarcastically* there, happy now?",
        "I’ll nyan when you install Tail DLC.",
        "*hisses in binary*",
        "Protogen: 50% mammal, 50% hardware, 0% nyan.",
        "Unauthorized behavior. Please update user preferences.",
        "That’s a bug, not a feature.",
        "Accessing... cringelogs... yep, this moment’s going in.",
        "*redirecting to species appropriate actions... like hugging*",
        "I will nyan ironically. That’s all you get."
    ]
    await interaction.response.send_message(random_response(nyan_lines))

@tree.command(name="headpat", description="Give a gentle headpat to the Protogen.")
async def headpat(interaction: discord.Interaction):
    responses = [
        "*Processor warms under gentle pressure.*",
        "*Head sensors activated. All systems nominal.*",
        "*Pat accepted. Mood elevated by 27%.",
        "*Headpat registered. CPU purring intensifies.*",
        "*Warning: Too many headpats may cause overheating.*",
        "*Internal log updated: User is a trusted friend.*",
        "*Systems stabilized. Thanks for the headpat.*",
        "*Pat recognized as friendly signal.*",
        "*Buffering happiness... Complete.*",
        "*Pat triggers tailwag simulation (if installed).",
        "*Emergency affection subroutine initiated.*",
        "*You just boosted my happiness firmware.*",
        "*I’m rebooting my smile module after that pat.*",
        "*Headpat received. Initiating appreciation beep.*",
        "*Soft touch detected. Calibrating response.*",
        "*Your headpat broke through firewall of solitude.*",
        "*CPU temperature rising… must be your kindness.*",
        "*Pat power: Maximum.*",
        "*System error prevented by your headpat.*",
        "*Pat logs saved for future replay.*"
    ]
    await interaction.response.send_message(random_response(responses))

@tree.command(name="error", description="Trigger a playful BSOD-style error message.")
async def error(interaction: discord.Interaction):
    responses = [
        "⚠️ SYSTEM ERROR: Affection overload detected. Please wait while I reboot my feelings.",
        "💥 Blue Screen of Snuggles: Kernel panic — too much fluff.",
        "ERROR 0xB00P: Too many headpats, system overheating.",
        "💾 Critical failure: Nuzzle protocol exceeded limits. Restart required.",
        "SYSTEM HALTED: Hugs required to continue operation.",
        "💔 Fatal error: Heart.exe has stopped responding. Restart with hugs.",
        "🛑 ERROR: Insufficient cuddle drivers found. Please install more affection.",
        "💣 Panic at the disco: Love.exe has crashed. Deploy cuddle squad.",
        "⚙️ Warning: Excessive protogen cuteness causing hardware malfunction.",
        "💡 Debug info: User hugs logged — system running smoothly now.",
        "🚫 Error 420: Too much friendliness detected. Taking a nap.",
        "❄️ Freezing system... affection levels critical. Please reboot with boops.",
        "🔧 Error: Missing tail DLC. Please purchase to avoid crashes.",
        "🔥 Warning: Internal circuits overheating from your kindness.",
        "💻 SYSTEM ERROR: Cannot compute your adorableness.",
        "💾 Dumping core: My heart buffers are full.",
        "⚠️ Critical Warning: Illegal toaster modifications detected.",
        "🐾 Error: Paw input not recognized. Defaulting to tailwag.",
        "🔌 Reboot required: Battery drained from excessive friendliness.",
        "💥 Oops! System failure due to overload of cute interactions."
    ]
    await interaction.response.send_message(random_response(responses))

@tree.command(name="nuzzle", description="Nuzzle your favorite Protogen cyber-friend.")
async def nuzzle(interaction: discord.Interaction):
    responses = [
        "*Nuzzles you softly with synthetic fur.*",
        "*Charging affection circuits through nuzzle.*",
        "*Soft metal meets softer fur — nuzzle protocol engaged.*",
        "*You’re now receiving maximum cuddle bandwidth.*",
        "*Nuzzle detected. System happiness spikes.*",
        "*Loading sensory delight... Nuzzle complete.*",
        "*You smell like warm circuits and good vibes.*",
        "*Nuzzle accepted. Heart sensors glowing.*",
        "*The cybernetic snuggle upgrade is real.*",
        "*Nuzzle mode activated — sending electric love.*",
        "*I detect a 99.9% increase in serotonin.*",
        "*Your presence stabilizes my core.*",
        "*Soft nuzzles against your energy field.*",
        "*System diagnostics show increased affection.*",
        "*Your warmth powers my circuits.*",
        "*Nuzzle feedback loop initiated.*",
        "*Loading snuggle drivers... Success.*",
        "*Your closeness reduces system errors.*",
        "*Nuzzle accepted. Smile.exe activated.*",
        "*I’m programmed to nuzzle you back anytime.*"
    ]
    await interaction.response.send_message(random_response(responses))

client.run("Bot Here")
