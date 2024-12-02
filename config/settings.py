import os
from pathlib import Path
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

# Zotero配置
ZOTERO_LIBRARY_ID = os.getenv('ZOTERO_LIBRARY_ID')
ZOTERO_API_KEY = os.getenv('ZOTERO_API_KEY')

# OpenAI配置
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_BASE = os.getenv('OPENAI_API_BASE', 'https://api.gptgod.online')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
MAX_TOKENS = int(os.getenv('MAX_TOKENS', '5000'))

# 语言配置
LANGUAGE = os.getenv('LANGUAGE', 'zh')  # zh或en

# 目标集合配置
TARGET_COLLECTION = os.getenv('TARGET_COLLECTION', None)  # 不指定则处理所有笔记

# 日志配置
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# API配置
API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))  # API请求超时时间(秒)

def validate_config():
    """验证必要的配置项"""
    required_vars = {
        'ZOTERO_LIBRARY_ID': ZOTERO_LIBRARY_ID,
        'ZOTERO_API_KEY': ZOTERO_API_KEY,
        'OPENAI_API_KEY': OPENAI_API_KEY,
    }
    
    missing = [k for k, v in required_vars.items() if not v]
    if missing:
        raise ValueError(f"缺少必要的环境变量: {', '.join(missing)}") 