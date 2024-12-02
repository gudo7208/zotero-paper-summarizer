import logging
from typing import Optional
import PyPDF2
from .base import BaseOCR

logger = logging.getLogger(__name__)

class PyPDFOCR(BaseOCR):
    """使用PyPDF2实现的OCR"""
    
    def extract_text(self, file_path: str) -> Optional[str]:
        """从PDF文件中提取文本"""
        try:
            text_content = []
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text_content.append(page.extract_text())
            
            return '\n'.join(text_content)
        except Exception as e:
            logger.error(f"提取PDF内容时出错: {str(e)}")
            return None 