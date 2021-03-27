import discord
import datetime
import json
import random
import csv
from time import sleep
from time import *
from discord.ext import commands
import os


client = commands.Bot(command_prefix=".", help_command=None)

f = ["name", "rank"]

@client.event
async def on_ready():
  print("!.!")

@client.command()
async def add_mod(ctx, mod=None, rank=None):

  if mod == None or rank == None or mod and rank == None:
    await ctx.send("mising argument!! exception: async def add_mod(ctx, mod=None, rank=None);")

  file2 = open("mods.csv", "r")
  with open("mods.csv", "a+", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=f)
    reader = csv.DictReader(file2)

    for line in file2:
      if line == mod:
        await ctx.send("Mod Is Alredy In Database!")
        file.close()
      else:
        pass
    writer.writerow({"name": mod, "rank": rank})
    await ctx.send(f"Mod Added! Rank: {rank} mod: {mod}")

@client.command()
async def show_mods(ctx):
  
  with open("mods.csv", "r") as file3:
    data = csv.DictReader(file3)

    for line in data:
      await ctx.send(line)

@client.command()
async def help(ctx):
  await ctx.send("type '.add_mod <mod name> <rank> to add a mod'\n'type .show_mods' to show all the mods\nCreated by CAPE_GUY[PY]#8526")

client.run(os.getenv("TOKEN"))
