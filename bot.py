import discord
from discord.ext import commands
import json
import os

data_file = "furti.json"

# Caricamento dati
if os.path.exists(data_file):
    try:
        with open(data_file, "r") as f:
            loaded_data = json.load(f)
            furti = {int(k): v for k, v in loaded_data.items()}
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Errore nel caricamento dei dati: {e}. Creazione nuovo file.")
        furti = {}
else:
    furti = {}


def salva_dati():
    with open(data_file, "w") as f:
        json.dump(furti, f, indent=4)


# Intents
intents = discord.Intents.default()
intents.message_content = False

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot connesso come {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands sincronizzati: {len(synced)}")
    except Exception as e:
        print(e)


from discord import app_commands


@bot.tree.command(
    name="furto",
    description="Registra un furto e i soldi sporchi guadagnati.")
@app_commands.describe(soldi="Inserisci i soldi sporchi guadagnati")
async def furto(interaction: discord.Interaction, soldi: int):
    user_id = interaction.user.id

    if user_id not in furti:
        furti[user_id] = {"conteggio": 0, "soldi": 0}

    furti[user_id]["conteggio"] += 1
    furti[user_id]["soldi"] += soldi

    salva_dati()

    await interaction.response.send_message(
        f"💰 **Furto registrato!**\nHai guadagnato **{soldi} soldi sporchi**.")


@bot.tree.command(name="classifica",
                  description="Mostra la classifica dei ladri")
async def classifica(interaction: discord.Interaction):

    if not furti:
        await interaction.response.send_message(
            "Nessun dato presente nella classifica!")
        return

    ordinati = sorted(furti.items(), key=lambda x: x[1]["soldi"], reverse=True)

    testo = "🏆 **CLASSIFICA LADRI**\n\n"
    posizione = 1

    for user_id, dati in ordinati:
        testo += (
            f"**{posizione}.** <@{user_id}> — "
            f"💰 {dati['soldi']} soldi sporchi | "
            f"🕵️ {dati['conteggio']} furti\n"
        )
        posizione += 1

    await interaction.response.send_message(testo)


@bot.tree.command(name="resetfurti",
                  description="Resetta tutta la memoria dei furti (solo admin)")
async def resetfurti(interaction: discord.Interaction):

    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "❌ Solo un amministratore può usare questo comando.",
            ephemeral=True
        )
        return

    furti.clear()
    salva_dati()

    await interaction.response.send_message(
        "🧹 Memoria dei furti completamente resettata!")


@bot.tree.command(name="totalefurti",
                  description="Mostra il totale dei furti e soldi guadagnati.")
async def totalefurti(interaction: discord.Interaction):

    user_id = interaction.user.id

    if user_id not in furti:
        await interaction.response.send_message(
            "Non hai ancora effettuato nessun furto!")
        return

    totale = furti[user_id]

    await interaction.response.send_message(
        f"🕵️ **STATISTICHE FURTI**\n"
        f"Furti totali: **{totale['conteggio']}**\n"
        f"Soldi sporchi totali: **{totale['soldi']}**"
    )


# ===== TOKEN =====
token = os.getenv("DISCORD_TOKEN")
if not token:
    print("ERRORE: Variabile d'ambiente DISCORD_TOKEN non trovata!")
    exit(1)

bot.run(token)