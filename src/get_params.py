from dotenv import load_dotenv
import os
import yaml
def get_api_key():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

def load_yaml():
    with open("gpt_params.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)