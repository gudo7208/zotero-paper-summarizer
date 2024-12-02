def get_abstract_translation_prompt(abstract: str) -> str:
    """生成摘要翻译的prompt模板"""
    return f"""请将以下英文摘要翻译成中文,并用一句话总结其核心内容:

摘要:
{abstract}

请按以下格式输出:
翻译:
[中文翻译]

一句话总结:
[核心内容总结]"""

def get_abstract_summary_prompt(translation: str) -> str:
    """生成摘要一句话总结的prompt模板"""
    return f"""请用一句话总结以下中文摘要的核心内容:

摘要:
{translation}

请按以下格式输出:
一句话总结:
[核心内容总结]""" 