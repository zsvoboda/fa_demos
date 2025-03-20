from dotenv import load_dotenv
import os

def load_env():
    load_dotenv(dotenv_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.load_env")))

if __name__ == "__main__":
    load_env()
    