from abc import ABC, abstractmethod
from typing import Optional

class BaseOCR(ABC):
    """OCR基础接口类"""
    
    @abstractmethod
    def extract_text(self, file_path: str) -> Optional[str]:
        """从文件中提取文本"""
        pass 