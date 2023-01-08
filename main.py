import discord
import os
from discord.ext import commands
import inspect
from discord import gateway

token = os.getenv("token")

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

gatewayFile = inspect.getsourcefile(gateway)

with open(gatewayFile, "r") as file:
	lines = file.readlines()
	print(lines[445]) #to see the prior line

lines[445] = "'browser': 'Discord iOS',\n"

with open(gatewayFile, "w") as file:
	file.writelines(lines)

client.run(token)
