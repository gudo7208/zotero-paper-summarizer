import logging
from typing import Optional, List, Dict, Any
from pyzotero import zotero
from config.settings import ZOTERO_LIBRARY_ID, ZOTERO_API_KEY

logger = logging.getLogger(__name__)

class ZoteroClient:
    """Zotero客户端"""
    
    def __init__(self):
        self.library_id = ZOTERO_LIBRARY_ID
        self.api_key = ZOTERO_API_KEY
        self.zot = zotero.Zotero(self.library_id, 'user', self.api_key)
    
    def get_collection_key(self, collection_path: Optional[str]) -> Optional[str]:
        """获取指定路径的文件夹key"""
        if not collection_path:
            return None
            
        try:
            collections = self.zot.collections()
            path_parts = collection_path.split('/')
            
            current_collections = collections
            for part in path_parts:
                found = False
                for collection in current_collections:
                    if collection['data']['name'] == part:
                        if part == path_parts[-1]:
                            return collection['key']
                        current_collections = self.zot.collections_sub(collection['key'])
                        found = True
                        break
                if not found:
                    logger.error(f"未找到文件夹: {part}")
                    return None
                    
            return None
        except Exception as e:
            logger.error(f"获取文件夹key时出错: {str(e)}")
            return None
    
    def get_collection_items(self, collection_key: Optional[str] = None) -> List[Dict[str, Any]]:
        """获取集合中的所有条目"""
        try:
            if collection_key:
                return self.zot.collection_items(collection_key)
            else:
                return self.zot.items()  # 获取所有条目
        except Exception as e:
            logger.error(f"获取条目列表时出错: {str(e)}")
            return []
    
    def has_notes(self, item_key: str) -> bool:
        """检查条目是否已有笔记"""
        try:
            children = self.zot.children(item_key)
            return any(child['data']['itemType'] == 'note' for child in children)
        except Exception as e:
            logger.error(f"检查笔记时出错: {str(e)}")
            return False
    
    def create_note(self, parent_key: str, content: str) -> bool:
        """创建笔记"""
        try:
            note = {
                'itemType': 'note',
                'parentItem': parent_key,
                'note': f'<h1>AI生成的论文摘要</h1><p>{content}</p>'
            }
            self.zot.create_items([note])
            return True
        except Exception as e:
            logger.error(f"创建笔记时出错: {str(e)}")
            return False
    
    def update_abstract(self, item_key: str, translation: str, summary: str) -> bool:
        """更新条目的摘要"""
        try:
            item = self.zot.item(item_key)
            original_abstract = item['data'].get('abstractNote', '')
            
            new_abstract = f"# 核心内容\n{summary}\n\n# 中文翻译\n{translation}\n\n# 原文摘要\n{original_abstract}"
            
            item['data']['abstractNote'] = new_abstract
            self.zot.update_item(item)
            return True
        except Exception as e:
            logger.error(f"更新摘要时出错: {str(e)}")
            return False 