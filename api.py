from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
class Member(BaseModel):
    id: int
    name: str

class MemberName(BaseModel):
    name: str

app = FastAPI()

@app.post('/member')
def addMember(member: Member):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("INSERT INTO member VALUES('"+str(member.id)+"', '"+member.name+"')")
    con.commit()
    return {"id": member.id, "name": member.name}

@app.put('/member/{member_id}')
def updateMember(member_id: int, member: MemberName):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("UPDATE member SET name = '"+member.name+"' WHERE id = '"+str(member_id)+"'")
    con.commit()
    return {
        "name": member.name,
        "member_id": member_id
    }

@app.get('/member/{member_id}')
def read_item(member_id: int):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM member WHERE id = '"+str(member_id)+"'")
    member = res.fetchone()
    print(member)
    return {
        "id": member[0],
        "name": member[1]
    }

@app.post('/createMember')
def createMember():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE member(id, name)")
    return {"message": "OK"}

@app.get("/member")
def getAllMember():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    allMember = []
    for row in cur.execute("SELECT * FROM member"):
        print(row)
        allMember.append({
            "id": row[0],
            "name": row[1]
        })
        
    return {"data": allMember}

@app.get("/")
def read_root():
    return {"Hello": "World"}
