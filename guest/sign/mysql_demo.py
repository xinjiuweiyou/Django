from  pymysql import cursors, connect

#连接数据库
con = connect(host='127.0.0.1',
              user='root',
              passwordd='qwe123',
              db='guest',
              charset='utf8mb4',
              cursorclass=cursors.DictCursor)

try:
    with con.cursor() as cursors:
        sql = 'INSERT INTO sign_guest (realname,phone,email,sign,event_id,"creat_time") VALUES ("TOM",178978978978,"tom@mail.com",0,1,NOW());'
        cursors.execute(sql)
#提交事物
con.commit()

with con.cursor() as  cursors:
    sql = "SELECT realname,phone FROM sign_guest WHERE phone=%s"
    cursors.execute(sql,('178978978978',))
    result = cursors.fetchone()
    print(result)
finally:
    con.close()