import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
TELEGRAM_TOKEN = config_yaml["telegram_token"]
OPENAI_API_KEY = config_yaml["openai_api_key"]
OPENAI_API_BASE = config_yaml.get("openai_api_base", None)
OPENROUTER_API_KEY = config_yaml.get("openrouter_api_key", None)
OPENROUTER_API_BASE = config_yaml.get(
    "openrouter_api_base", "https://openrouter.ai/api/v1")
ALLOWED_TELEGRAM_USERNAMES = config_yaml["allowed_telegram_usernames"]
ENABLE_MESSAGE_STREAMING = config_yaml.get("enable_message_streaming", True)
RETURN_N_GENERATED_IMAGES = config_yaml.get("return_n_generated_images", 1)
IMAGE_SIZE = config_yaml.get("image_size", "1024x1024")
N_CHAT_MODES_PER_PAGE = config_yaml.get("n_chat_modes_per_page", 5)
MONGODB_URI = f"mongodb://mongo:{config_env['MONGODB_PORT']}"
HELP_MESSAGE = config_yaml["help_message"]
HELP_GROUP_CHAT_MESSAGE = config_yaml["help_group_chat_message"]
OPENAI_COMPLETION_OPTIONS = config_yaml["openai_completion_settings"]

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
HELP_GROUP_CHAT_VIDEO_PATH = Path(
    __file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
