import sqlite3

class SQLiteDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns_str = ', '.join([f'{col} {datatype}' for col, datatype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        columns_str = ', '.join(data.keys())
        values_str = ', '.join(['?' for _ in data.values()])
        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def select_data(self, table_name, columns='*', condition=None):
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_data(self, table_name, updates, condition):
        updates_str = ', '.join([f"{col} = ?" for col in updates.keys()])
        query = f"UPDATE {table_name} SET {updates_str} WHERE {condition}"
        self.cursor.execute(query, tuple(updates.values()))
        self.conn.commit()

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    # 使用示例
    db = SQLiteDatabase('test.db')

    # 创建表
    db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'})

    # 插入数据
    db.insert_data('users', {'name': '张三', 'age': 25})
    db.insert_data('users', {'name': '李四', 'age': 30})

    # 查询数据
    rows = db.select_data('users')
    for row in rows:
        print(row)

    # 更新数据
    db.update_data('users', {'age': 26}, "name = '张三'")

    # 删除数据
    db.delete_data('users', "name = '李四'")

    # 关闭数据库连接
    db.close()
