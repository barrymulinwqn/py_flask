import datetime
import os
import sys
import sqlite3
# conn = sqlite3.connect('testdb.db')
import click

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text, inspect

engine = create_engine('sqlite:///testdb.db', pool_size=10)


def concurrent_access():
    with engine.connect() as conn:
        insp = inspect(engine)
        print(insp.has_table("EX399"))
        print(insp.has_index("EX399","index_name"))


        # conn.execute(text("CREATE TABLE movie(title, year, score)"))

        # conn.execute(text('CREATE TABLE "EX3" ('
        #                'id INTEGER NOT NULL,'
        #                'name VARCHAR, email VARCHAR, phone VARCHAR, nationality VARCHAR, username VARCHAR, dateofbirth VARCHAR,'
        #                 'updatetime DATETIME)'))

        # conn.execute(text('CREATE TABLE "EX1" ('
        #                'id INTEGER NOT NULL,'
        #                'name VARCHAR, '
        #                'PRIMARY KEY (id));'))

        # try:
        #     # conn.execute(text("delete from some_table where x=1"))
        #     curidx = 0
        #     item = []
        #
        #     statement = text("""
        #     INSERT INTO EX3 (id, name, email, phone, nationality, username, dateofbirth, updatetime)
        #      VALUES(:id, :name, :email, :phone, :nationality, :username, :dateofbirth, :updatetime)
        #     """)
        #
        #     for idx in range(1, 70000):
        #         curidx = curidx + 1
        #         item.append({"id": curidx, "name": 'name', "email":'email', "phone":'phone',
        #                             "nationality":'nationality', "username":'username', "dateofbirth":'dateofbirth',
        #                             "updatetime":datetime.datetime.now()})
        #
        #     datas = tuple(item)
        #     conn.execute(statement, datas)
        #
        #         # data = ({"id": 1, "title": "The Hobbit", "primary_author": "Tolkien"},
        #         #         {"id": 2, "title": "The Silmarillion", "primary_author": "Tolkien"},
        #         #         )
        #
        #         # statement = text("""
        #         # INSERT INTO EX3 (id, name, email, phone, nationality, username, dateofbirth, updatetime)
        #         #  VALUES(:id, :name, :email, :phone, :nationality, :username, :dateofbirth, :updatetime)
        #         # """)
        #         #
        #         # ddl = f"insert into EX3 (id, name, email, phone, nationality, username, dateofbirth, updatetime) values ({++curidx}, 'name', 'email', 'phone', 'nationality', 'username', 'dateofbirth', {datetime.datetime.now()})"
        #         # conn.execute(ddl)
        #
        #     conn.commit()
        #     print("成功")
        # except Exception as e:
        #     print(f"{e}")
        #     conn.rollback()
        #     print("失败，回滚")

        # # insert a raw
        # conn.execute(text('INSERT INTO "EX1" '
        #                '(id, name) '
        #                'VALUES (2,"raw1")'))
        # conn.commit()

        result = conn.execute(text("select * from EX3"))
        alldata = result.fetchall()

        len(alldata)
        print(f"total count {len(alldata)}")
        # for row in alldata:
        #     print(row)


if __name__ == '__main__':
    concurrent_access()
    print(f"test sqlite purpose!!")