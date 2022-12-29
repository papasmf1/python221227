# db1.py
import sqlite3
#1)연결객체(임시로 메모리에서 작업)
con = sqlite3.connect(":memory:")
#2)커서객체(실제 SQL구문을 실행하고 결과 다루기)
cur = con.cursor()
#테이블(데이터 구조 만들기):ANSI SQL 92, 99
cur.execute("create table PhoneBook (name text, phoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick','010-123');")
#1건 파라메터로 입력
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber) )

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

