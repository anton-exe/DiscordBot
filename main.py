import os
TOKEN = os.environ['TOKEN']

import asyncio

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='+')

letterEmojis = [
	"🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲",
	"🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿"
]

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	print('Prefix:' + bot.command_prefix)
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('with your mind'))

@bot.event
async def on_command_error(context, error):
	await context.reply(f'ERROR {error}\nReport this at https://github.com/anton-exe/DiscordBot/issues')

@bot.before_invoke
async def logCommand(context):
	print(f'\033[0;44m@{context.author}\033[0m ran \033[0;91m{context.prefix}{context.command}\033[0m in \033[0;44m#{context.channel.name}\033[0m on \033[1m{context.guild.name}\033[0m')

@bot.command(name='rps', brief="A game of rock paper scissors!", description='Definetely not rigged lol')
async def rockPaperScissors(context):
	msg = await context.reply('Rock, Paper, Scissors...')
	await msg.add_reaction('✊')
	await msg.add_reaction('✋')
	await msg.add_reaction('✌️')

	def check(reaction, user):
		return user == context.author and (str(reaction.emoji) == '✊' or str(reaction.emoji) == '✋' or str(reaction.emoji) == '✌️')
	
	play = ''

	try:
			reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
			play = str(reaction.emoji)
	except asyncio.TimeoutError:
		await msg.reply("Time's up lol")
	else:
		if play == '✊':
			await msg.reply('✋ I win lol')
		elif play == '✋':
			await msg.reply('✌️ Lamo loser')
		elif play == '✌️':
			await msg.reply('✊ ez')
		else:
			await msg.reply('CHEATER!!1!!!')

@bot.command(name='poll', usage="question, [options]...", brief="auto generate a message to do a poll")
async def weLiveInADemocracy(context):
	cmdArgs = context.message.content.split(" ", 1)[1].split(", ", 22)
	question = cmdArgs[0]
	choices = cmdArgs[1:21]
	desc = ""
	for i in range(len(choices)):
		desc = desc + f'{letterEmojis[i]}: {choices[i]}\n'
	embed = discord.Embed(title=question, description=desc)
	msg = await context.send(embed=embed)
	for i in range(len(choices)):
		await msg.add_reaction(letterEmojis[i])

class Tests(commands.Cog):
	"""Just some tests"""

	@commands.command(name='like', aliases=['react'], brief='Reaction Test', description = '"Likes" your command')
	async def like(self, context):
		await context.message.add_reaction('👍')

	@commands.command(name='server', aliases=["info"], description = 'Displays server info')
	async def fetchServerInfo(self, context):
		guild = context.guild

		await context.send(f'Server Name: {guild.name}')
		await context.send(f'Server Size: {len(guild.members)}')

class Anton_only(commands.Cog):
	"""Commands that can only be used by the creator of the bot, Anton"""

	@commands.command(name='shutdown')
	@commands.is_owner()
	async def shutdown(self, context):
		await context.bot.close()

	@commands.command(name='Troll')
	@commands.is_owner()
	async def atEveyone(self, context):
		for i in range(100):
			await context.send(f'@everyone #{i + 1}')

	@commands.command(name="throwerror", aliases=["error"])
	@commands.is_owner()
	async def throwError(self, context):
		1 / 0

bot.add_cog(Tests())
bot.add_cog(Anton_only())

bot.run(TOKEN) 
