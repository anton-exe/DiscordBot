import os
TOKEN = os.environ['TOKEN']

import asyncio
from time import sleep

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

@bot.command(name='fnaf')
async def fnafLore(context):
	async with context.typing():
		await context.send('\*inhales*')
		sleep(1)
		await context.send("""Fredbear's Family Diner
William Afton and Henry opened in 1967 the family friendly Fredbear's Family Diner, featuring a brown furry suit of a bear as a mascot. Henry would usually wear the suit, as they didn't have enough money to hire someone to do the job for a long time and they were studying at the time. William studied engineering and Henry business adminstration and communication.

William met an unnamed woman, with whom he married and three years later had a boy challed Michael. They met in the court; William was being charged for murdering a child that allegedly was crying outside the Diner for being scared of Fredbear, the bear, and she was working selling hot-dogs in from of the building. (Btw, he was released because they didn't have evidences pointing it).

It took them four years to actually achieve any success with the Diner, as they learnt from little Michael that Fredbear was boring. William them designed a new mascot: a yellow furry suit of a rabbit called Bonnie. The chemistry between both characters worked like black magic and the success rained on them like rain in a rainy day.

The amount of money they got was so much, William used it to test his engineering skills, designing the first two Spring Lock suits: which were obviously Bonnie and Fredbear. The success increased.""")
		sleep(0.5)
		await context.send("""Freddy Fazbear's Pizza
The Diner's success was so big, a company decided buy it and open a franchise around it. Hanry and William sold it, seeing a whole lot of profit coming from it, but there was a catch: the company used sneaky legal actions that allowed them to have the diner 100% under their possession, erasing Henry's and Michael's name from it. The company then opened Fazbear's Entertainment to take care of everything.

William was so pissed because of this he cut any relationship with anyone involved with the franchise. Henry, on the other hand, didn't know any other thing to do, so he asked for a job; he became Phone Guy.

FFP opened in 1973, and featured four furry suits of animals: Freddy Fazbear, a recolour of Bonnie, Chica and Foxy The Pirate. This made William even more pissed when he learnt they made four animatronics without him. He started planning his revenge.

Btw, the Diner was still opened - as a sister location for FFP.""")
		sleep(0.5)
		await context.send("""The Origin of Purple Guy
In 1976 William had twins: a little blonde girl and a little brunette boy. He started to teach Michael to take care of them, because "Daddy won't be around forever".

During his free time, William started designing and projecting new robots (he hated the name "animatronics") and plans for his own company: Afton Robotics. But he had another plan under his sleeve: ruin FFP from the inside.

He disguised himself as Dave Miller and started working applied for day time security guard at FFP. As he was always wearing purple - the uniform's colour - and usually hid in the shadows to stay out of sight of anyone who might recognize him, he was nicknamed by every child as "The Purple Guy".

During this time, in 1980, he did his evil plan: using the Spring Bonnie suit he built years earlier, he lured five children to a back room, murdered them and hid inside the body of the animatronics. In case you're wondering what he did with the fifth one, he obviously hid it inside a spare Freddy suit he then painted yellow, duh.

Fortunately for Billy, they actually caught Henry instead of him, as one of the cameras caught him walking around in one of the suits. He got out sometime later, as they managed to prove he had some mental disabilities and had a fixation with wearing the suits around, and had no violent behaviour.

But Dave? Well, he was fired when FFP closed.""")
		sleep(0.5)
		await context.send("""Circus Baby
With the help of the money he got from selling the children's organs in the black market, William opened Afton Robotics and had everything ready to open his own kid-friendly restaurant: Circus Baby's Pizza World. The problem is that he got a new hobby, and this where his hill went down.

He liked so much the idea of killing children and the profit he could get from selling their organs - healthy children organs are way more valuable than adults' -, he made special alterations in his robots, turning them into kid-kidnapping and killing machines.

The problem is that, in 1982, he accidently let his daughter get close to Baby when he wasn't looking; and Baby killed her. He knew he was the one to blame, but he actually blamed Michael for this, saying that he, as the older brother, should've protected her.

This incident lead to the pizzeria's cancellation and William's divorce. His wife took Michael and the other boy with her, leaving him alone. His new hobby and this incident in his life lead him to become a human monster.""")
		sleep(0.5)
		await context.send("""The Children
Going a little away from the entire "Afton story arch", let's talk about the children he murdered. The first one came to possess a Puppet from FFP. The other five, with the help of the first one, possessed the suits they were stuffed inside. They then started killing any adult they could at night, when there was no children around, because they thought every adult was the "Purple Guy" they heard of when they were still alive.""")
		sleep(0.5)
		await context.send("""The Bite of '83
William's ex-wife took the children and they started living close the Diner, that was still running great. For the good old times, before the problems, she would take them there.

William, on the other didn't like it in the slightest, and bought a warehouse close to their house, where he built an underground room he used to monitor cameras installed in the house, the Diner and in the street. He also started to prepare the warehouse to building Circus Baby Entertainment & Rental. He also returned to his Dave Miller persona, working at the Diner, taking a closer looka at his sons.

The Crying Child
After the Baby Incident, Michael became a rebel teenager who, rebelling against his father's will, bullied his younger brother. For the brother's unluckiness, he was also traumatized for actually having witnessed Baby killing his sister in the year before.

For his luckiness, though, he had a reliable friend: Psychic Friend Fredbear. Unbeknown for him, the plush was actually a camera his father used to check on him. More unbeknown for him, when the plush talked with him, it was actually the spirit of his sister, who was haunting William's warehouse, and with supernatural abilities managed to speak through the camera system.

The Bite per se
You all know how it happened. Birthday party, bad joke, head inside the bear's mouth and chomp, child's head's crushed. He went to the hospital, but died. His sister tried to help him, but in the end he became a ghost purple bear, crying in the corners of anywhere the suit that killed him was at.""")
		sleep(0.5)
		await context.send("""William's Revenge
After the Bite, Michael's mother committed suicide and he was taken under William's keeping. But Billy wasn't happy with his son, who caused the death of another one of his children.

William projected the new building to have a place for torturing children - specially made for Michael, actually. The room was designed to mimic Michael's room from the other house, so when he would fall asleep, William would take him to the "nightmare" room (Michael would be drugged) and unleash nightmarry robotic versions of the Fazbear animatronics to haunt him at night, giving him some reminders of what he did to his brother. This marked Michael for life, and turned him a better person, actually.""")
		sleep(0.5)
		await context.send("""1987
OMG, this is long, isn't it?

Well, in 1987 another FFP opened, with new animatronics. William became Dave again and killed more five children. The place temporarily shut down, reopened in November, but didn't last after Mangle bit someone. Henry was once again without a job.

The problem is that, in this attempt, they recognized Dave as William, so he had to hid himself for his own safety.""")
		sleep(0.5)
		await context.send("""Fixing past mistakes
During the time hiding, William started pondering about his decisions in life, and how it screwed everything for him. He caused the death of his family, lasting only him and his older son. That was it! The solution!

If he, William, ruined everything, Micheal could be the one to fix everything! He then sent a letter to Michael, explaining everything he should do.

William was aware of the spirits and possessions, and knew his daughter was haunting CBE&R, so he sent Michael there first. Then Sister Location happened and all that jazz. Or should I say, casual bongos? Kill me.

So, Baby first thought Michael was William, but then she recongnized his brother and saw an opportunity for her and the other sentient robots from the Rental to leave - using him as a "human disguise". To prevent his brother died from this, she did some black magic researchs and found a way to prevent him from dying.

Then Ennard came to be, Michael was fooled into the Scooping Room and became a suit. Ennard tried to live a life as a regular human being pretending to be Michael, but unfortunately the black magic didn't prevent flesh from rotting, so the disguise was ruined and Ennard left Michael' body, now living in the sewers, waiting for It to start shooting, hoping to get a role in it.

But, even though Michael became an undying walking corpse, his job wasn't done, he had one last thing to do: free the souls of his father's victims. So, he went to work at FFP, that reopened in the 90's, to check if the possession thing was really going on there. Oh, Henry died there before Michael begin to work.""")
		await context.send("""
Michael got a fake name - Mike Schmidt (he wasn't as good with names as his father was) -, and worked there. He was unfortunately fired for being a smelly corpse and "supposedly tampering the animatronics". So he waited for when the pizzeria closed for good.

With the help of Shadow Freddy, who was actually the spirit of his younger brother, he dismantled the animatronics, freeing the children's souls from their physical restraints. For Michael's unluckiness, in FNaF Universe rotten corpses are purple, which lead the spirits into believing he was the Purple Guy and consequently attacking him. Thankfully, Michael remember about the Spring Bonnie suit he could use to fool the spirits his father told him. Unfortunately, the suit failed on him, crushing his body. As the spirits thought their killer was dead for good, they left.

Michael stayed there, sitting in an abandoned room, a rotten body inside a broken rotten suit, with his brother.""")
		sleep(0.5)
		await context.send("""FNaF 3
No one likes FNaF 3. You all know what happens here.""")
		sleep(0.5)
		await context.send("""The Future
After Fazbear's Fright burnt down, in an attempt from Michael to remove the suit - he thought the fire would disintegrate the suit, but it only hurt more -, he concluded the last thing he had to do in his neverending life was to go after his father, one to caused all the shit that happened to everyone in this freaking franchise.

So, what's to come? Only FNaF 6 will answer us.""")

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
