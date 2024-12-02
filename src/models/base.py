from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class BaseModel(ABC):
    """模型请求的基础接口类"""
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> Optional[str]:
        """生成文本"""
        pass
    
    @abstractmethod
    def chat(self, messages: list[Dict[str, str]], **kwargs) -> Optional[str]:
        """对话形式生成"""
        pass 