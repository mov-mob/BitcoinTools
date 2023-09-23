#!/bin/python3
import sys
from bitcoin import *
a_valid_bitcoin_address = sys.argv[1]
print(history(a_valid_bitcoin_address))
