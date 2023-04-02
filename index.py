import discord
import random
import time

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
            return False
        
    if message.content == '>help':
        await message.reply(f'<@{message.author.id}>, please check your DM for the list of commands.')
        await message.author.send(f'>play\n>help')
    
    if message.content == '>play':
        time.sleep(1)
        player = message.author.id
        randomNumber = random.randint(1,10)
        await message.channel.send(f'choose a number 1-10')
        if message.author.id == player: # check whos playing the game to prevent other guesses
                msg = await client.wait_for('message', timeout=60.0)
                print(f'{message.author} | {randomNumber}')
                if msg.content.lower() == str(randomNumber):
                    await message.channel.send('Correct!')
                else:
                    await message.channel.send(f'Incorrect... The number was {randomNumber}')
        else:
             return False

client.run('') # put your bots token here