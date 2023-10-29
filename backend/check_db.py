import socket
import time
import os
from dotenv import load_dotenv

def main():
   load_dotenv()
   print("db connecting...")
   while True:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex((
         os.environ.get("POSTGRES_HOST"),
         int(os.environ.get("POSTGRES_PORT"))
      ))
      if result == 0:
         print("db is connected!")
         break
      else:
         print("db is not connected yet...")
         time.sleep(3)

if __name__ == "__main__":
   main()