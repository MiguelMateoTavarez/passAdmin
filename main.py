from connection import *
from start import start

connection = connect()
createTables(connection)

start()