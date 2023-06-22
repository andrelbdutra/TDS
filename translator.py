import discord
import asyncio
from google.cloud import translate

# Configuração do cliente do Google Cloud Translate
client = translate.TranslationServiceClient.from_service_account_json('#') # substitua o # pela sua respectiva chave do google cloud.

# Configuração do bot do Discord
bot_token = '#' #substitua o # pelo token do seu respectivo bot

# Criação do cliente do Discord

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True

client_discord = discord.Client(intents=intents)

@client_discord.event
async def on_ready():
    print(f'Bot conectado como {client_discord.user.name}')

@client_discord.event
async def on_raw_reaction_add(payload):
    if payload.event_type == 'REACTION_ADD':
        await asyncio.sleep(1)  # Aguarda 1 segundo
        channel = client_discord.get_channel(payload.channel_id)
        message =  await channel.fetch_message(payload.message_id)
        author = message.author
        content = message.content
        # content = message.embeds
        # content = content[0]
        # content = content.description
        # content = content.split(")")[1]
        

        if payload.emoji.name == '🇧🇷':  # Exemplo com a bandeira do Brasil
            translated_text = translate_text(content, 'pt')
            reply = f'{author}: {translated_text}'
            await channel.send(reply)
        
        else:
            if payload.emoji.name == '🇺🇸':  # Exemplo com a bandeira do Brasil
                translated_text = translate_text(content, 'en')
                reply = f'{author}: {translated_text}'
                await channel.send(reply)
        
            else:
                if payload.emoji.name == '🇷🇺':  # Exemplo com a bandeira do Brasil
                    translated_text = translate_text(content, 'ru')
                    reply = f'{author}: {translated_text}'
                    await channel.send(reply)
                else:
                    if payload.emoji.name == '🇪🇸':
                        translated_text = translate_text(content, 'es')
                        reply = f'{author}: {translated_text}'
                        await channel.send(reply)
                    else:
                        if payload.emoji.name == '🇨🇳':
                            translated_text = translate_text(content, 'zh-CN')
                            reply = f'{author}: {translated_text}'
                            await channel.send(reply)


def translate_text(text, target_language):
    project_id = '#'  # ID do projeto do Google Cloud Translate
    location = 'global'

    response = client.translate_text(
        request={
            "parent": f"projects/{project_id}/locations/{location}",
            "contents": [text],
            "target_language_code": target_language,
        }
    )

    return response.translations[0].translated_text



print(translate_text("Test",'pt'))



client_discord.run(bot_token)
