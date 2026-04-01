import yaml
from langchain_openai.chat_models import ChatOpenAI
from langchain_anthropic.chat_models import ChatAnthropic

with open("models_config/confg.yaml") as f:
    config = yaml.safe_load(f)

def get_openai_model(tier="low"):
    key = config["routing"]["default"][tier]
    model=  config["models"][key]['model']
    return ChatOpenAI(model=model, temperature=0)

def get_anthropic_model(tier="low"):
    model = config["models"][f"claude_{tier}"]['model']
    return ChatAnthropic(model_name=model, temperature=0)
