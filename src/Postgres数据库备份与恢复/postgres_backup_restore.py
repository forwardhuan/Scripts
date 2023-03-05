#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# ======================================================
# @File:  : postgres_backup_restore
# @Author : forward_huan
# @Date   : 2023/3/4 21:24
# @Desc   :
# ======================================================
# import subprocess


# def backup(save_path, host, user_name, db_name, port=5432):
#     cmd = f'pg_dump.exe --file "{save_path}"  --host {host} --port {port} --username {user_name} ' \
#           f"--no-password --format=c --blobs {db_name}"
#     print(cmd)
#     proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
#     proc.wait()
#     result = f'{proc.stderr.read().decode("gbk")}'
#     if result:
#         print(result)
# backup(r"F:\\test_database.backup", "localhost", "postgres", "test")


import subprocess
import psycopg2


def delete_all_table(host, user_name, pwd, db_name, port=5432):
    db = f"host={host}  user={user_name} dbname={db_name} port={port} password={pwd}"
    try:
        conn: psycopg2._psycopg.connection = psycopg2.connect(db)
        cursor: psycopg2._psycopg.cursor = conn.cursor()
        cursor.execute(
            "select " + "table_name from information_schema.tables where table_schema='public'")
        table_names = [item[0] for item in cursor.fetchall()]
        for table_name in table_names:
            cursor.execute("drop " + f"table if exists {table_name}")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as ex:
        print(ex)


def restore(backup_path, host, user_name, db_name, port=5432):
    cmd = f'pg_restore.exe --host {host} --port {port} --username {user_name} --no-password ' \
          f'--dbname {db_name}  "{backup_path}"'
    print(cmd)
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
    proc.wait()
    result = f'{proc.stderr.read().decode("gbk")}'
    if result:
        print(result)


if __name__ == '__main__':
    delete_all_table("localhost", "postgres", "postgres", "test")
    restore(r"F:\\test_database.backup", "localhost", "postgres", "test")
