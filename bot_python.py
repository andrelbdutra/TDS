from googletrans import Translator
import discord

translator = Translator()
#translation = translator.translate("O nome do meu cachorro é Woody", dest="en")

#print(translation.origin, ' -> ', translation.text)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def capturar_mensagens(ctx):
        token = 'seu_token_de_acesso'
        repo_owner = 'nome_do_proprietario'
        repo_name = 'nome_do_repositorio'

        g = Github(token)
        repo = g.get_repo(f'{repo_owner}/{repo_name}')
        messages = repo.get_issues(state='all')

        for message in messages:
            translation = translator.translate(message.title, dest="en")
            await ctx.send(f'Nova mensagem no repositório do GitHub: {translation.text}')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        print('Message from{0.author}:{0.content}'.format(message))
        translation = translator.translate(message.content, dest="en")
        await message.channel.send("[EN]: " + translation.text)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTEyMDExMDQwNDI4NzM0MDYyNg.GEpDLB.izfL33n5QykjKd-bJkd8pHa63mo-WGrmAXYX2g')