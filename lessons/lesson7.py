import sqlite3
#
db = sqlite3.connect("Users.db")
cursor = db.cursor()
#
#
def create_table():
    cursor.execute("""
     create table if not exists Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
        )
                    """)
db.commit()

create_table()

db.close()
#
# def add_user(name, age, hobby):
#     cursor.execute(
#         'INSERT INTO Users(name, age,hobby) VALUES (?,?,?)',
#         (name, age, hobby)
#     )
#     db.commit()
#     print(f"добавили{name}")
#
# # add_user(" john doe-mini", 15,"бокс")
# # add_user(" Jonah Doe", 25, "плавать")
#
#
#
# def update_user_by_rowid(name=None, age=None, hobby=None,rowid=None):
#    if name:
#     cursor.execute(
#         'UPDATE Users SET name=? WHERE rowid=?',
#         (name, rowid)
#     )
#
#
#     if age:
#      cursor.execute(
#         'UPDATE Users SET age=? WHERE rowid=?',
#         (age, rowid)
#      )
#
#     if hobby:
#      cursor.execute(
#         'UPDATE Users SET hobby=? WHERE rowid=?',
#         (hobby, rowid)
#      )
#
#
# # db.commit()
#
# print('update success')
#
# # update_user_by_rowid(name = " hhg пупке", rowid=5)
#
# # db.close()
#
#
#
#
# def delete_user_by_rowid(rowid):
#     cursor.execute(
#         'DELETE FROM Users WHERE rowid=?',
#         (rowid,)
#     )
# # db.commit()
#
# print('delete success')
#
# delete_user_by_rowid(4)
# delete_user_by_rowid(1)
# delete_user_by_rowid(2)
# delete_user_by_rowid(3)
# delete_user_by_rowid(14)
# delete_user_by_rowid(15)
# delete_user_by_rowid(16)
# delete_user_by_rowid(13)
# delete_user_by_rowid(12)
# delete_user_by_rowid(11)
# delete_user_by_rowid(9)
# delete_user_by_rowid(10)
# delete_user_by_rowid(8)
#
#
# db.commit()
# # db.close()
#
#
#
#
# def get_all_users():
#     cursor.execute('select * from Users')
#     users = cursor.fetchall()
#     print(f"-----{users}")
#
#     if users:
#         print("список всех пользователей")
#         for user in users:
#             print(f"name: {user[0]}, age: {user[1]}, hobby: {user[2]}")
#     else:
#         print(f"список пользователей пуст")
#
# get_all_users()
# # db.close()
#
#
# import sqlite3


def detail_view_user_by_id(user_id):
    conn = sqlite3.connect('Users.db')
    cursors = conn.cursor()

    try:
        cursors.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
        user = cursors.fetchone()

        if user:
            user_data = {
                'id': user[0],
                'name': user[1],
                'age': user[2],
                'hobby': user[3],
                }
            print(user_data)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Ошибка при запросе к базе данных: {e}")


    finally:

        conn.close()


# db.commit()

# detail_view_user_by_id(2)

# db.close()

