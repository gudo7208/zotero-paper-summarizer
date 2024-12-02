import logging
import requests
from typing import Optional, Dict, Any
from .base import BaseModel
from config.settings import (
    OPENAI_API_KEY,
    OPENAI_API_BASE,
    OPENAI_MODEL,
    MAX_TOKENS,
    API_TIMEOUT
)

logger = logging.getLogger(__name__)

class OpenAIModel(BaseModel):
    """OpenAI模型实现"""
    
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.api_base = OPENAI_API_BASE
        self.model = OPENAI_MODEL
        self.max_tokens = MAX_TOKENS
        self.timeout = API_TIMEOUT
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _make_request(self, payload: Dict[str, Any]) -> Optional[str]:
        """发送API请求"""
        try:
            response = requests.post(
                f"{self.api_base}/v1/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            logger.error(f"API请求失败: {str(e)}")
            return None
    
    def generate(self, prompt: str, **kwargs) -> Optional[str]:
        """生成文本"""
        messages = [
            {"role": "system", "content": "你是一个专业的学术论文分析助手。"},
            {"role": "user", "content": prompt}
        ]
        return self.chat(messages, **kwargs)
    
    def chat(self, messages: list[Dict[str, str]], **kwargs) -> Optional[str]:
        """对话形式生成"""
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": kwargs.get('max_tokens', self.max_tokens),
            "temperature": kwargs.get('temperature', 0.7)
        }
        return self._make_request(payload) 