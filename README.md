# Zotero论文总结助手

一个用于自动处理Zotero中论文的工具，可以：
1. 自动提取PDF内容并生成专业的论文总结
2. 自动翻译英文摘要并生成一句话总结
3. 支持处理指定文件夹或所有论文

## 功能特点

- 模块化设计，便于扩展
- 支持自定义模型和OCR方案
- 完善的错误处理和日志记录
- 配置灵活，支持多种参数调整

## 项目结构

```
zotero-paper-summarizer/
├── config/                # 配置管理
│   ├── settings.py       # 配置项
│   └── prompts/          # prompt模板
├── src/                  # 源代码
│   ├── models/          # 模型请求
│   ├── ocr/             # OCR处理
│   ├── summarizer/      # 论文总结
│   ├── translator/      # 摘要翻译
│   └── zotero/          # Zotero操作
├── tests/               # 单元测试
├── .env                # 环境变量
└── main.py             # 入口文件
```

## 安装使用

1. 克隆项目
```bash
git clone [项目地址]
cd zotero-paper-summarizer
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
复制`.env.example`为`.env`并填写以下配置：
```
# Zotero配置
ZOTERO_LIBRARY_ID=你的library_id
ZOTERO_API_KEY=你的api_key

# OpenAI配置
OPENAI_API_KEY=你的api_key
OPENAI_API_BASE=https://api.gptgod.online

# 可选配置
MAX_TOKENS=5000  # 摘要生成的最大token数
LANGUAGE=zh      # 摘要语言：en为英文，zh为中文 
TARGET_COLLECTION=目标文件夹路径  # 不填则处理所有笔记
```

4. 运行
```bash
python main.py
```

## 配置说明

- `ZOTERO_LIBRARY_ID`: Zotero的图书馆ID
- `ZOTERO_API_KEY`: Zotero的API密钥
- `OPENAI_API_KEY`: OpenAI的API密钥
- `OPENAI_API_BASE`: OpenAI的API地址
- `MAX_TOKENS`: 生成摘要的最大token数
- `LANGUAGE`: 生成摘要的语言(zh/en)
- `TARGET_COLLECTION`: 要处理的文件夹路径，不填则处理所有笔记

## 开发说明

1. 添加新的模型实现
继承`BaseModel`类并实现相关方法：
```python
from src.models.base import BaseModel

class NewModel(BaseModel):
    def generate(self, prompt: str, **kwargs) -> Optional[str]:
        # 实现文本生成
        pass
        
    def chat(self, messages: list[Dict[str, str]], **kwargs) -> Optional[str]:
        # 实现对话生成
        pass
```

2. 添加新的OCR实现
继承`BaseOCR`类并实现相关方法：
```python
from src.ocr.base import BaseOCR

class NewOCR(BaseOCR):
    def extract_text(self, file_path: str) -> Optional[str]:
        # 实现文本提取
        pass
```

## 注意事项

1. API密钥安全
- 不要将包含API密钥的`.env`文件提交到版本控制
- 建议使用环境变量或配置文件管理敏感信息

2. 错误处理
- 程序会自动跳过处理失败的条目
- 详细错误信息会记录在日志中

3. 资源占用
- 处理大量PDF可能需要较长时间
- 建议分批处理或在非高峰时段运行

## 许可证

MIT License