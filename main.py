import logging
from config.settings import LOG_LEVEL, LOG_FORMAT, TARGET_COLLECTION, validate_config
from src.zotero.client import ZoteroClient
from src.summarizer.paper import PaperSummarizer
from src.translator.abstract import AbstractTranslator

# 配置日志
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

def main():
    """主函数"""
    try:
        # 验证配置
        validate_config()
        
        # 初始化客户端
        zotero = ZoteroClient()
        summarizer = PaperSummarizer()
        translator = AbstractTranslator()
        
        # 获取目标集合key
        collection_key = zotero.get_collection_key(TARGET_COLLECTION)
        
        # 获取需要处理的条目
        items = zotero.get_collection_items(collection_key)
        
        # 处理每个条目
        for item in items:
            try:
                if item['data'].get('contentType') == 'application/pdf':
                    logger.info(f"处理PDF: {item['data'].get('filename')}")
                    
                    # 获取父条目信息
                    parent_key = item['data']['parentItem']
                    parent_data = zotero.item(parent_key)
                    
                    # 处理摘要
                    abstract = parent_data['data'].get('abstractNote')
                    if abstract:
                        logger.info("开始处理摘要...")
                        abstract_info = translator.translate_and_summarize(abstract)
                        if abstract_info:
                            zotero.update_abstract(
                                parent_key,
                                abstract_info['translation'],
                                abstract_info['summary']
                            )
                    
                    # 处理笔记
                    if not zotero.has_notes(parent_key):
                        logger.info("开始生成论文总结...")
                        summary = summarizer.summarize(item['data']['filename'])
                        if summary:
                            zotero.create_note(parent_key, summary)
                    
            except Exception as e:
                logger.error(f"处理条目时出错: {str(e)}")
                continue
                
    except Exception as e:
        logger.error(f"程序执行出错: {str(e)}")

if __name__ == "__main__":
    main() 