# Python数据库 (Python Database)

这是一个使用SQLite实现的简单Python数据库模块，提供基本的CRUD（创建、读取、更新、删除）操作。

This is a simple Python database module implemented using SQLite, providing basic CRUD (Create, Read, Update, Delete) operations.

## ⚠️ 安全警告 (Security Warning)

**本模块仅用于教学和演示目的。在生产环境中使用数据库时，请注意以下安全事项：**

**This module is for educational and demonstration purposes only. When using databases in production, please note:**

- ✋ 始终验证和清理用户输入 (Always validate and sanitize user inputs)
- ✋ 使用参数化查询防止SQL注入攻击 (Use parameterized queries to prevent SQL injection attacks)
- ✋ 实施适当的访问控制和权限管理 (Implement proper access control and permission management)
- ✋ 在生产环境中考虑使用ORM（如SQLAlchemy）(Consider using an ORM like SQLAlchemy in production)
- ✋ 加密敏感数据 (Encrypt sensitive data)

## 功能特性 (Features)

- ✅ 数据库连接管理 (Database connection management)
- ✅ 表创建 (Table creation)
- ✅ 数据插入 (Data insertion)
- ✅ 数据查询 (Data querying)
- ✅ 数据更新 (Data updating)
- ✅ 数据删除 (Data deletion)
- ✅ 自定义SQL查询 (Custom SQL queries)
- ✅ 上下文管理器支持 (Context manager support)

## 文件说明 (File Description)

- `database.py` - 数据库核心模块 (Database core module)
- `example.py` - 使用示例 (Usage example)
- `example.db` - SQLite数据库文件（运行后生成）(SQLite database file, generated after running)

## 使用方法 (Usage)

### 基本使用 (Basic Usage)

```python
from database import Database

# 创建数据库实例 (Create database instance)
db = Database("my_database.db")

# 连接数据库 (Connect to database)
db.connect()

# 创建表 (Create table)
db.create_table("users", "id INTEGER PRIMARY KEY, name TEXT, age INTEGER")

# 插入数据 (Insert data)
db.insert("users", ("name", "age"), ("张三", 25))

# 查询数据 (Query data)
results = db.select("users")
print(results)

# 关闭连接 (Close connection)
db.disconnect()
```

### 使用上下文管理器 (Using Context Manager)

```python
from database import Database

# 使用with语句自动管理连接 (Use with statement to automatically manage connection)
with Database("my_database.db") as db:
    db.create_table("users", "id INTEGER PRIMARY KEY, name TEXT")
    db.insert("users", ("name",), ("李四",))
    results = db.select("users")
    print(results)
# 连接会自动关闭 (Connection closes automatically)
```

### 运行示例程序 (Run Example Program)

```bash
python example.py
```

## API 文档 (API Documentation)

### Database 类 (Database Class)

#### `__init__(db_name: str = "example.db")`
初始化数据库对象 (Initialize database object)

#### `connect() -> None`
建立数据库连接 (Establish database connection)

#### `disconnect() -> None`
关闭数据库连接 (Close database connection)

#### `create_table(table_name: str, columns: str) -> None`
创建表 (Create table)

**参数 (Parameters):**
- `table_name`: 表名 (Table name)
- `columns`: 列定义，例如 "id INTEGER PRIMARY KEY, name TEXT" (Column definitions)

#### `insert(table_name: str, columns: Tuple[str, ...], values: Tuple[Any, ...]) -> None`
插入数据 (Insert data)

**参数 (Parameters):**
- `table_name`: 表名 (Table name)
- `columns`: 列名元组 (Column names tuple)
- `values`: 值元组 (Values tuple)

#### `select(table_name: str, columns: str = "*", condition: str = "") -> List[Tuple]`
查询数据 (Select data)

**参数 (Parameters):**
- `table_name`: 表名 (Table name)
- `columns`: 要查询的列，默认为所有列 (Columns to query, default is all columns)
- `condition`: WHERE条件 (WHERE condition)

**返回 (Returns):**
- 查询结果列表 (List of query results)

#### `update(table_name: str, set_clause: str, condition: str) -> None`
更新数据 (Update data)

**参数 (Parameters):**
- `table_name`: 表名 (Table name)
- `set_clause`: SET子句，例如 "age = 30" (SET clause)
- `condition`: WHERE条件 (WHERE condition)

#### `delete(table_name: str, condition: str) -> None`
删除数据 (Delete data)

**参数 (Parameters):**
- `table_name`: 表名 (Table name)
- `condition`: WHERE条件 (WHERE condition)

#### `execute_query(query: str, params: Optional[Tuple] = None) -> Optional[List[Tuple]]`
执行自定义SQL查询 (Execute custom SQL query)

**参数 (Parameters):**
- `query`: SQL查询语句 (SQL query statement)
- `params`: 查询参数（可选）(Query parameters, optional)

**返回 (Returns):**
- 如果是SELECT语句，返回查询结果；否则返回None (Query results if SELECT statement, otherwise None)

## 示例输出 (Example Output)

运行 `python example.py` 后的输出示例：

```
============================================================
Python数据库示例程序 (Python Database Example Program)
============================================================

成功连接到数据库: example.db (Successfully connected to database: example.db)

1. 创建用户表 (Creating users table)...
表 'users' 创建成功 (Table 'users' created successfully)

2. 插入用户数据 (Inserting user data)...
数据插入成功 (Data inserted successfully)
数据插入成功 (Data inserted successfully)
数据插入成功 (Data inserted successfully)

3. 查询所有用户 (Querying all users)...
找到 3 个用户: (Found 3 users:)
  ID: 1, 姓名: 张三, 年龄: 25, 邮箱: zhangsan@example.com
  ID: 2, 姓名: 李四, 年龄: 30, 邮箱: lisi@example.com
  ID: 3, 姓名: 王五, 年龄: 28, 邮箱: wangwu@example.com

...
```

## 依赖项 (Dependencies)

本项目仅使用Python标准库，无需安装额外依赖：
This project only uses Python standard library, no additional dependencies required:

- `sqlite3` (Python标准库 / Python standard library)
- `typing` (Python标准库 / Python standard library)

## 系统要求 (System Requirements)

- Python 3.6 或更高版本 (Python 3.6 or higher)

## 许可证 (License)

MIT License

## 贡献 (Contributing)

欢迎提交问题和拉取请求！
Issues and pull requests are welcome!
