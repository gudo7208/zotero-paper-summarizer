import logging
from typing import Optional
from ..models.openai import OpenAIModel
from ..ocr.pypdf import PyPDFOCR
from config.prompts.summary import get_paper_summary_prompt

logger = logging.getLogger(__name__)

class PaperSummarizer:
    """论文总结实现"""
    
    def __init__(self):
        self.model = OpenAIModel()
        self.ocr = PyPDFOCR()
    
    def summarize(self, pdf_path: str) -> Optional[str]:
        """生成论文总结"""
        try:
            # 提取PDF文本
            content = self.ocr.extract_text(pdf_path)
            if not content:
                logger.error("PDF文本提取失败")
                return None
            
            # 生成prompt
            prompt = get_paper_summary_prompt(content)
            
            # 调用模型生成总结
            summary = self.model.generate(prompt)
            if not summary:
                logger.error("总结生成失败")
                return None
            
            return summary
            
        except Exception as e:
            logger.error(f"生成论文总结时出错: {str(e)}")
            return None 