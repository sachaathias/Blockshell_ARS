# -*- coding: utf-8 -*-
# ===================================================
# ==================== META DATA ===================
# ==================================================
__author__ = "Sacha ATHIAS / Baptiste VINCENT / Hugo GENDARME"
__url__ = "https://sacha.athias.fr"
__email__ = "sacha.athias@EPITA.fr"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Sacha ATHIAS"

# ==================================================
# ================= IMPORT MODULES =================
# ==================================================
import hashlib
import datetime
import json
from colorama import Fore, Back, Style
import time
import sys
import base64

# ==================================================
# =================== BLOCK CLASS ==================
# ==================================================
class Block:
    """
        Create a new block in chain with metadata
    """
    def __init__(self, uid_epita, email_epita, name, surname, major, index=0):
        self.index = index
        self.previousHash = ""
        self.uid_epita = uid_epita
        self.email_epita = email_epita
        self.name = name
        self.surname = surname
        self.picture = base64.b64encode(self.uid_epita)
        self.major = major
        self.timestamp = str(datetime.datetime.now())
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        """
            Method to calculate hash from metadata
        """
        hashData = str(self.index) + str(self.uid_epita) + str(self.email_epita) + str(self.name) + str(self.surname) + str(self.picture) + str(self.major) + self.timestamp + self.previousHash + str(self.nonce)
        return hashlib.sha256(hashData).hexdigest()

    def mineBlock(self, difficulty):
        """
            Method for Proof of Work
        """
        print Back.RED + "\n[Status] Mining block (" + str(self.index) + ") with PoW ..."
        startTime = time.time()

        while self.hash[:difficulty] != "0"*difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()

        endTime = time.time()
        print Back.BLUE + "[ Info ] Time Elapsed : " + str(endTime - startTime) + " seconds."
        print Back.BLUE + "[ Info ] Mined Hash : " + self.hash
        print Style.RESET_ALL

# ==================================================
# ================ BLOCKCHAIN CLASS ================
# ==================================================
class Blockchain:
    """
        Initialize blockchain
    """
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 3

    def createGenesisBlock(self):
        """
            Method create genesis block
        """
        uid_ = "0000"
        email_ = "login@epita.fr"
        name_ = "name"
        surname_ = "surname"
        major_ = "SRS"
        return Block(uid_epita=uid_, email_epita=email_, name=name_, surname=surname_, major=major_)

    def addBlock(self, newBlock):
        """
            Method to add new block from Block class
        """
        newBlock.index = len(self.chain)
        newBlock.previousHash = self.chain[-1].hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
        self.writeBlocks()

    def writeBlocks(self):
        """
            Method to write new mined block to blockchain
        """
        dataFile = file("chain.txt", "w")
        chainData = []
        for eachBlock in self.chain:
            chainData.append(eachBlock.__dict__)
        dataFile.write(json.dumps(chainData, indent=4))
        dataFile.close()
