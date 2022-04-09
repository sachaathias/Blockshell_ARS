# -*- coding: utf-8 -*-
# ===================================================
# ==================== META DATA ===================
# ==================================================
__author__ = "Daxeel Soni"
__url__ = "https://daxeel.github.io"
__email__ = "daxeelsoni44@gmail.com"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daxeel Soni"

# ==================================================
# ================= IMPORT MODULES =================
# ==================================================
import click
import urllib
import json
from blockchain.chain import Block, Blockchain

# ==================================================
# ===== SUPPORTED COMMANDS LIST IN BLOCKSHELL ======
# ==================================================
SUPPORTED_COMMANDS = [
    'new',
    'allblocks',
    'getblock',
    'help'
]

# Init blockchain
coin = Blockchain()

# Create group of commands
@click.group()
def cli():
    """
        Create a group of commands for CLI
    """
    pass

# ==================================================
# ============= BLOCKSHELL CLI COMMAND =============
# ==================================================
@cli.command()
@click.option("--difficulty", default=3, help="Define difficulty level of blockchain.")
def init(difficulty):
    """Initialize local blockchain"""
    print """
  ____    _                  _       _____   _              _   _
 |  _ \  | |                | |     / ____| | |            | | | |
 | |_) | | |   ___     ___  | | __ | (___   | |__     ___  | | | |
 |  _ <  | |  / _ \   / __| | |/ /  \___ \  | '_ \   / _ \ | | | |
 | |_) | | | | (_) | | (__  |   <   ____) | | | | | |  __/ | | | |
 |____/  |_|  \___/   \___| |_|\_\ |_____/  |_| |_|  \___| |_| |_|

 > A command line utility for learning Blockchain concepts.
 > Type 'help' to see supported commands.
 > Project by Daxeel Soni - https://daxeel.github.io

    """

    # Set difficulty of blockchain
    coin.difficulty = difficulty

    # Start blockshell shell
    while True:
        cmd = raw_input("[BlockShell] $ ")
        processInput(cmd)

# Process input from Blockshell shell
def processInput(cmd):
    """
        Method to process user input from Blockshell CLI.
    """
    userCmd = cmd.split(" ")[0]
    if len(cmd) > 0:
        if userCmd in SUPPORTED_COMMANDS:
            globals()[userCmd](cmd)
        else:
            # error
            msg = "Command not found. Try help command for documentation"
            throwError(msg)


# ==================================================
# =========== BLOCKSHELL COMMAND METHODS ===========
# ==================================================
def new(cmd):
    """
        Do Transaction - Method to perform new transaction on blockchain.
    """
    block_data = cmd.split(" ")
    if (len(block_data) != 6):
        print "Error Transaction incorrect data, pls try again"
    else:
        print "Doing transaction..."
        coin.addBlock(Block(uid_epita=block_data[1],
                        email_epita=block_data[2],
                        name=block_data[3],
                        surname=block_data[4],
                        major=block_data[5]))

def allblocks(cmd):
    """
        Method to list all mined blocks.
    """
    print ""
    for eachBlock in coin.chain:
        print eachBlock.hash
    print ""

def getblock(cmd):
    """
        Method to fetch the details of block for given hash.
    """
    blockHash = cmd.split(" ")[-1]
    for eachBlock in coin.chain:
        if eachBlock.hash == blockHash:
            print ""
            print eachBlock.__dict__
            print ""

def help(cmd):
    """
        Method to display supported commands in Blockshell
    """
    print "Commands:"
    print "   new <uid,email,name,surname,major>    Create new transaction"
    print "   allblocks                             Fetch all mined blocks in blockchain"
    print "   getblock <block hash>                 Fetch information about particular block"

def throwError(msg):
    """
        Method to throw an error from Blockshell.
    """
    print "Error : " + msg
