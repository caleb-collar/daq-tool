from database import ini_database
from dashboard import run_dash

def main():
  ini_database()
  run_dash()

if __name__ == '__main__':
  main()