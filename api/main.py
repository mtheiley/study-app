import aiosqlite
import sqlite3
import os
import uuid
from sanic import Sanic, text
from sanic.response import text

sql_path = os.path.abspath(f"{__file__}/../production.sqlite")

app = Sanic(__name__)

@app.post("/cards/delete/<card_id>")
async def removeCard(card_id):
    db_conn = await aiosqlite.connect(sql_path)
    await db_conn.execute(f"DELETE FROM Cards WHERE cardID = ?", (card_id,))
    await db.commit()
    return text("Operation Successful")

@app.post("/group/delete/<group_id>")
async def removeGroup(group_id):
    db_conn = await aiosqlite.connect(sql_path)
    await db_conn.execute("UPDATE Cards SET GroupID = "" WHERE GroupID = ?", (group_name,))
    await db.commit()
    return text("Operation Successful")

@app.post("/cards/create")
async def createCard(request, card_uuid = uuid.uuid4().hex):
    db_conn = await aiosqlite.connect(sql_path)
    print(request.json)
    print(request.body)
    await db_conn.execute('''
        INSERT INTO Cards (
            CardID,
            GroupID,
            Title,
            Option_1,
            Option_2,
            Option_3,
            Option_4,
            image_base64
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        card_uuid,
        request.json['GroupID'],
        request.json['Title'],
        request.json['Option_1'],
        request.json['Option_2'],
        request.json['Option_3'],
        request.json['Option_4'],
        request.json['image_base64']
    ))
    await db_conn.commit()
    return text("Operation Successful")

@app.post("/groups/view/<card_group>")
async def viewCard(card_group):
    db_conn = await aiosqlite.connect(sql_path)
    if card_group == "all":
        cur = await db_conn.execute('select * from Cards')
    else:
        cur = await db_conn.execute("select * from Cards WHERE GroupID = ?", (card_group))
    return text(str(await cur.fetchall()))

'''
@app.post("/cards/edit")
async def editCard(request: Request, db_conn = get_conn()):
    await 
'''

@app.post("/cards/<card_id>/set_group/<group_name>")
async def setCardGroup(request, card_id, group_name):
    db_conn = await aiosqlite.connect(sql_path)
    await db_conn.execute("UPDATE Cards SET GroupID = ? WHERE CardID = ?", (group_name, card_id))
    await db_conn.commit()

@app.post("/group/<group_id>/edit_info")
async def editGroupInfo(group_id, request):
    db_conn = await aiosqlite.connect(sql_path)
    if request.json['description'] is not None:
        await db_conn.execute("UPDATE Group SET Description = ? WHERE ID = ?", (request.json['description'], group_id))
    if request.json['title'] is not None:
        await db_conn.execute("UPDATE Group SET Title = ? WHERE ID = ?", (request.json['title'], group_id))
    await db_conn.commit()

if __name__ == "__main__":
    if os.path.isfile(sql_path):
        print(sql_path + "exists!")
        app.run(host="0.0.0.0", port=8000, auto_reload=True)
    else:
        with sqlite3.connect(sql_path) as connection:
            connection.execute('''
                CREATE TABLE "Group" (
                    "Creator"    TEXT,
                    "Title"      TEXT,
                    "Description" TEXT,
                    "GroupID"         TEXT
                )
            ''')
            connection.execute('''
                CREATE TABLE "Cards" (
                    "CardID"    TEXT,
                    "GroupID"   TEXT,
                    "Title"     TEXT,
                    "Option_1"  TEXT,
                    "Option_2"  TEXT,
                    "Option_3"  TEXT,
                    "Option_4"  TEXT,
                    "image_base64" TEXT
                )
            ''')

            connection.commit()
            print("DB created, restart app.")
            exit(1)