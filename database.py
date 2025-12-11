"""
Python数据库模块 (Python Database Module)
使用SQLite实现基本的数据库操作 (Basic database operations using SQLite)

警告 (WARNING):
本模块为教学示例，用于演示基本的数据库操作。
在生产环境中使用时，请注意以下安全事项：
1. 对用户输入进行严格验证
2. 使用参数化查询防止SQL注入
3. 实施适当的访问控制和权限管理

This module is an educational example for demonstrating basic database operations.
When using in production, please note the following security considerations:
1. Strictly validate user inputs
2. Use parameterized queries to prevent SQL injection
3. Implement proper access control and permission management
"""

import sqlite3
import os
import re
from typing import List, Tuple, Optional, Any


class Database:
    """数据库管理类 (Database management class)"""
    
    def __init__(self, db_name: str = "example.db"):
        """
        初始化数据库连接 (Initialize database connection)
        
        Args:
            db_name: 数据库文件名 (Database file name)
        """
        self.db_name = db_name
        self.connection = None
        self.cursor = None
    
    @staticmethod
    def _is_safe_identifier(identifier: str) -> bool:
        """
        验证标识符是否安全（仅包含字母、数字、下划线）
        Validate if identifier is safe (contains only letters, numbers, underscores)
        """
        return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', identifier))
    
    def connect(self) -> None:
        """建立数据库连接 (Establish database connection)"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"成功连接到数据库: {self.db_name} (Successfully connected to database: {self.db_name})")
        except sqlite3.Error as e:
            print(f"数据库连接失败: {e} (Database connection failed: {e})")
            raise
    
    def disconnect(self) -> None:
        """关闭数据库连接 (Close database connection)"""
        if self.connection:
            self.connection.close()
            print("数据库连接已关闭 (Database connection closed)")
    
    def create_table(self, table_name: str, columns: str) -> None:
        """
        创建表 (Create table)
        
        Args:
            table_name: 表名 (Table name)
            columns: 列定义 (Column definitions)
            
        注意 (Note): 此方法不验证列定义的安全性。在生产环境中应使用ORM或严格验证输入。
        This method does not validate column definitions for security. Use ORM or strict validation in production.
        """
        if not self._is_safe_identifier(table_name):
            raise ValueError(f"不安全的表名: {table_name} (Unsafe table name: {table_name})")
        
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
            self.cursor.execute(query)
            self.connection.commit()
            print(f"表 '{table_name}' 创建成功 (Table '{table_name}' created successfully)")
        except sqlite3.Error as e:
            print(f"创建表失败: {e} (Table creation failed: {e})")
            raise
    
    def insert(self, table_name: str, columns: Tuple[str, ...], values: Tuple[Any, ...]) -> None:
        """
        插入数据 (Insert data)
        
        Args:
            table_name: 表名 (Table name)
            columns: 列名元组 (Column names tuple)
            values: 值元组 (Values tuple)
        """
        if not self._is_safe_identifier(table_name):
            raise ValueError(f"不安全的表名: {table_name} (Unsafe table name: {table_name})")
        
        for col in columns:
            if not self._is_safe_identifier(col):
                raise ValueError(f"不安全的列名: {col} (Unsafe column name: {col})")
        
        try:
            placeholders = ', '.join(['?' for _ in values])
            columns_str = ', '.join(columns)
            query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"数据插入成功 (Data inserted successfully)")
        except sqlite3.Error as e:
            print(f"插入数据失败: {e} (Data insertion failed: {e})")
            raise
    
    def select(self, table_name: str, columns: str = "*", condition: str = "") -> List[Tuple]:
        """
        查询数据 (Select data)
        
        Args:
            table_name: 表名 (Table name)
            columns: 列名，默认为所有列 (Column names, default is all columns)
            condition: WHERE条件 (WHERE condition)
            
        Returns:
            查询结果列表 (Query result list)
            
        注意 (Note): 此方法为简化示例。生产环境应使用参数化查询。
        This method is a simplified example. Use parameterized queries in production.
        """
        if not self._is_safe_identifier(table_name):
            raise ValueError(f"不安全的表名: {table_name} (Unsafe table name: {table_name})")
        
        try:
            query = f"SELECT {columns} FROM {table_name}"
            if condition:
                query += f" WHERE {condition}"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"查询数据失败: {e} (Data query failed: {e})")
            raise
    
    def update(self, table_name: str, set_clause: str, condition: str) -> None:
        """
        更新数据 (Update data)
        
        Args:
            table_name: 表名 (Table name)
            set_clause: SET子句 (SET clause)
            condition: WHERE条件 (WHERE condition)
            
        警告 (WARNING): 此方法不使用参数化查询。仅用于受信任的输入。
        This method does not use parameterized queries. Use only with trusted inputs.
        """
        if not self._is_safe_identifier(table_name):
            raise ValueError(f"不安全的表名: {table_name} (Unsafe table name: {table_name})")
        
        try:
            query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
            self.cursor.execute(query)
            self.connection.commit()
            print(f"数据更新成功，影响 {self.cursor.rowcount} 行 (Data updated successfully, {self.cursor.rowcount} rows affected)")
        except sqlite3.Error as e:
            print(f"更新数据失败: {e} (Data update failed: {e})")
            raise
    
    def delete(self, table_name: str, condition: str) -> None:
        """
        删除数据 (Delete data)
        
        Args:
            table_name: 表名 (Table name)
            condition: WHERE条件 (WHERE condition)
            
        警告 (WARNING): 此方法不使用参数化查询。仅用于受信任的输入。
        This method does not use parameterized queries. Use only with trusted inputs.
        """
        if not self._is_safe_identifier(table_name):
            raise ValueError(f"不安全的表名: {table_name} (Unsafe table name: {table_name})")
        
        try:
            query = f"DELETE FROM {table_name} WHERE {condition}"
            self.cursor.execute(query)
            self.connection.commit()
            print(f"数据删除成功，影响 {self.cursor.rowcount} 行 (Data deleted successfully, {self.cursor.rowcount} rows affected)")
        except sqlite3.Error as e:
            print(f"删除数据失败: {e} (Data deletion failed: {e})")
            raise
    
    def execute_query(self, query: str, params: Optional[Tuple] = None) -> Optional[List[Tuple]]:
        """
        执行自定义SQL查询 (Execute custom SQL query)
        
        Args:
            query: SQL查询语句 (SQL query statement)
            params: 查询参数 (Query parameters)
            
        Returns:
            查询结果（如果是SELECT语句） (Query results if SELECT statement)
            
        推荐 (RECOMMENDED): 使用params参数进行参数化查询以防止SQL注入。
        Use the params parameter for parameterized queries to prevent SQL injection.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            
            if query.strip().upper().startswith('SELECT'):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return None
        except sqlite3.Error as e:
            print(f"执行查询失败: {e} (Query execution failed: {e})")
            raise
    
    def __enter__(self):
        """上下文管理器入口 (Context manager entry)"""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出 (Context manager exit)"""
        self.disconnect()
