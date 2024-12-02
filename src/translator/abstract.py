import logging
from typing import Optional, Dict
from ..models.openai import OpenAIModel
from config.prompts.translate import (
    get_abstract_translation_prompt,
    get_abstract_summary_prompt
)

logger = logging.getLogger(__name__)

class AbstractTranslator:
    """摘要翻译实现"""
    
    def __init__(self):
        self.model = OpenAIModel()
    
    def translate_and_summarize(self, abstract: str) -> Optional[Dict[str, str]]:
        """翻译摘要并生成一句话总结"""
        try:
            # 生成翻译prompt
            translation_prompt = get_abstract_translation_prompt(abstract)
            
            # 调用模型生成翻译
            translation = self.model.generate(translation_prompt)
            if not translation:
                logger.error("摘要翻译失败")
                return None
            
            # 提取翻译和总结
            try:
                translation_text = translation.split('翻译:\n')[-1].split('\n\n一句话总结:')[0].strip()
                summary = translation.split('一句话总结:\n')[-1].strip()
            except Exception as e:
                logger.error(f"解析翻译结果时出错: {str(e)}")
                return None
            
            return {
                'translation': translation_text,
                'summary': summary
            }
            
        except Exception as e:
            logger.error(f"翻译摘要时出错: {str(e)}")
            return None 