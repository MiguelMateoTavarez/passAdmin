import os
from getpass import getpass
from tabulate import tabulate
from connection import *

connection = connect()
createTables(connection)