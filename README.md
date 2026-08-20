# Python与Agent开发学习记录

## 当前进度

### Python与AI应用课程

- [x] 1—8：环境安装与入门程序
- [x] 9—35：Python基础语法
- [x] 36—56：数据容器
- [x] 57—76：函数、模块、类型注解
- [x] 77—87：面向对象和异常
- [x] 88—99：大模型API
- [x] 100—119：Streamlit聊天项目
- [ ] 120—158：网络爬虫与数据分析（选择性学习实用部分）
- [ ] 159—174：高级面向对象和FastAPI
- [ ] 175—184：AI Web项目

### Agent岗位补充路线

- [ ] FastAPI工程化补充
  - REST API、Pydantic请求与响应模型
  - `async`/`await`、`httpx`、异常处理和CORS
  - `pytest`与FastAPI `TestClient`

#### LangChain 1.2课程

课程：[BV1rv7A6oEeP](https://www.bilibili.com/video/BV1rv7A6oEeP/)

- [ ] 1—10：LangChain概述、主要模块与Agent应用场景
- [ ] 11—22：模型创建与调用、Ollama、流式、批量和异步调用
- [ ] 23—24：LangSmith基础、链路追踪与调试
- [ ] 25—32：Message、对话历史和提示词模板
- [ ] 33—40：Tools定义、参数Schema、多工具调用和工具选择
- [ ] 41—50：Pydantic、TypedDict、JSON Schema与结构化输出
- [ ] 51—63：Agent创建、工具绑定、错误处理和流式输出
- [ ] 64—85：中间件、重试、调用限制、fallback、隐私保护和人工审批
- [ ] 86—101：上下文、短期记忆、长期记忆和PostgreSQL持久化
- [ ] 102—120：文档加载与切分、Embedding、Milvus和RAG知识库项目

- [ ] 独立完成一个Agent项目
  - 使用FastAPI提供后端接口，Streamlit作为演示页面
  - 至少包含工具调用、结构化输出、会话记忆和异常处理
  - 项目运行结果、测试方法和架构说明能够写入README

#### LangGraph课程

课程：[BV1z3NY66EY1](https://www.bilibili.com/video/BV1z3NY66EY1/)

- [ ] 1—7：环境配置、依赖安装、API Key和Jupyter环境验证
- [ ] 8—27：State、Node、Edge、Reducer和基础Graph流程
- [ ] 28—55：顺序、并行、分支、循环、重试、超时、错误处理和缓存
- [ ] 56—83：检查点、PostgreSQL持久化、失败恢复和长期记忆
- [ ] 84—106：Human-in-the-loop、中断机制、工具节点和Agent部署
- [ ] 107—132：流式执行、子图、动态路由和工作流设计模式

- [ ] MCP工具接入与业务系统集成
- [ ] Agent测试评测、日志、可观测性和安全控制
- [ ] 数据库、Docker、Docker Compose和项目部署
- [ ] 整理1—2个可展示的求职作品

## 网络爬虫与数据分析学习范围

### 需要掌握

- HTTP请求、参数、请求头、状态码、超时和重试
- 公开API与JSON数据解析
- BeautifulSoup基础HTML解析
- pandas读取CSV/JSON、筛选、排序、去重和缺失值处理
- `groupby()`分组统计与基础图表
- 将采集和分析能力封装为可被Agent调用的工具

### 暂不深入

- 验证码识别、代理池和绕过反爬系统
- 大规模分布式爬虫
- 复杂统计建模和机器学习算法
- 与当前Agent项目无关的数据可视化美化

## 学习规则

1. 所有代码必须亲自输入。
2. 每个案例至少独立重写一次。
3. 每个知识点按照“跟写一次 → 关闭视频重写 → 修改需求 → 用自己的话解释”完成。
4. 每个知识模块完成后进行Git提交。
5. API密钥不得进入Git仓库。
6. LangChain项目完成前不开始LangGraph，基础Agent工作流完成前不学习复杂多智能体。
