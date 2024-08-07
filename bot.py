import discord
import secrets

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        post_channel = client.get_channel(secrets.post_channel)
        if post_channel != message.channel:
            embed, = message.embeds
            if embed.title in ['New Post', 'New Reblog posted']:
                embed.title = ''
                embed.remove_footer()
                await post_channel.send(embeds=[embed])
                await post_channel.send(f'[link]({embed.url})')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(secrets.token)
