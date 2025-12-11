"""
Python数据库示例 (Python Database Example)
展示如何使用database.py模块进行数据库操作 (Demonstrates how to use the database.py module)
"""

from database import Database


def main():
    """主函数，演示数据库的基本操作 (Main function demonstrating basic database operations)"""
    
    print("=" * 60)
    print("Python数据库示例程序 (Python Database Example Program)")
    print("=" * 60)
    print()
    
    # 使用上下文管理器自动管理数据库连接 (Use context manager to automatically manage database connection)
    with Database("example.db") as db:
        
        # 1. 创建用户表 (Create users table)
        print("\n1. 创建用户表 (Creating users table)...")
        db.create_table(
            "users",
            "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, email TEXT"
        )
        
        # 2. 插入数据 (Insert data)
        print("\n2. 插入用户数据 (Inserting user data)...")
        users_data = [
            ("张三", 25, "zhangsan@example.com"),
            ("李四", 30, "lisi@example.com"),
            ("王五", 28, "wangwu@example.com"),
        ]
        
        for name, age, email in users_data:
            db.insert("users", ("name", "age", "email"), (name, age, email))
        
        # 3. 查询所有数据 (Query all data)
        print("\n3. 查询所有用户 (Querying all users)...")
        results = db.select("users")
        print(f"找到 {len(results)} 个用户: (Found {len(results)} users:)")
        for row in results:
            print(f"  ID: {row[0]}, 姓名: {row[1]}, 年龄: {row[2]}, 邮箱: {row[3]}")
        
        # 4. 条件查询 (Conditional query)
        print("\n4. 查询年龄大于26的用户 (Querying users older than 26)...")
        results = db.select("users", condition="age > 26")
        print(f"找到 {len(results)} 个用户: (Found {len(results)} users:)")
        for row in results:
            print(f"  ID: {row[0]}, 姓名: {row[1]}, 年龄: {row[2]}, 邮箱: {row[3]}")
        
        # 5. 更新数据 (Update data)
        print("\n5. 更新用户数据 (Updating user data)...")
        db.update("users", "age = 31", "name = '李四'")
        
        # 验证更新 (Verify update)
        results = db.select("users", condition="name = '李四'")
        if results:
            print(f"  更新后的数据: ID: {results[0][0]}, 姓名: {results[0][1]}, 年龄: {results[0][2]}, 邮箱: {results[0][3]}")
        
        # 6. 删除数据 (Delete data)
        print("\n6. 删除用户数据 (Deleting user data)...")
        db.delete("users", "name = '王五'")
        
        # 验证删除 (Verify deletion)
        results = db.select("users")
        print(f"删除后剩余 {len(results)} 个用户 (Remaining {len(results)} users after deletion)")
        
        # 7. 自定义查询 (Custom query)
        print("\n7. 执行自定义查询 (Executing custom query)...")
        results = db.execute_query("SELECT name, age FROM users ORDER BY age DESC")
        print("按年龄降序排列的用户: (Users sorted by age descending:)")
        for row in results:
            print(f"  姓名: {row[0]}, 年龄: {row[1]}")
        
        # 8. 显示最终数据 (Show final data)
        print("\n8. 最终用户列表 (Final user list)...")
        results = db.select("users")
        print(f"总共 {len(results)} 个用户: (Total {len(results)} users:)")
        for row in results:
            print(f"  ID: {row[0]}, 姓名: {row[1]}, 年龄: {row[2]}, 邮箱: {row[3]}")
    
    print("\n" + "=" * 60)
    print("数据库操作完成！(Database operations completed!)")
    print("=" * 60)


if __name__ == "__main__":
    main()
