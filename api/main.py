# src/server.py
import aiosqlite
import asyncio
import sqlite3
import os
import uuid
from sanic import Sanic, text
from sanic.request import Request
from sanic.response import text

app = Sanic(__name__)

async def get_conn(sql_path):
    return await aiosqlite.connect(sql_path)

@app.get("/cards/delete/<card_id>")
async def removeCard(card_id, db_conn = get_conn()):
    await db_conn.cursor.execute(f"DELETE FROM Cards WHERE cardID = ?", card_id)
    await db.commit()
    return text("Operation Successful")

@app.get("/cards/create")
async def createCard(request: Request, uuid = uuid.uuid4().hex, db_conn = get_conn()):
    await db_conn.cursor.execute('''INSERT INTO table_name()
        "CardID",
        "GroupID",
        "Title",
        "Option_1",
        "Option_2",
        "Option_3",
        "Option_4",
        "image_url"
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', uuid, request.json['CardID'], request.json['GroupID'], request.json['Title'], request.json['Option_1'], request.json['Option_2'], request.json['Option_3'], request.json['Option_4'], request.json['image_url'])
    await db.commit()
    return text("Operation Successful")

@app.get("/cards/view/<card_group>")
async def viewCard(cardId, db_conn = get_conn()):
    if card_group == "all":
        await db_conn.cursor('select * from cards')
    else:
        await db_conn.cursor("select * from cards WHERE GroupID = ?", card_group)
    return await cur.fetchall()

@app.get("/cards/edit")
async def editCard(request):
    await asyncio.sleep(1)
    return text("")

@app.get("/cards/setCardGroup/{}")
async def setCardGroup(CardID, GroupId):
    await asyncio.sleep(1)
    return text("")

@app.get("/cards/random/{}")
async def randomCard():
    await asyncio.sleep(1)
    return text("")

@app.get("/cards/setCardImage/{}")
async def setCardImage(CardImageID, Image):
    await asyncio.sleep(1)
    return text("")

@app.get("/cards/getCardImage/{}")
async def getCardImage(CardImageID):
    await asyncio.sleep(1)
    return await execute('select * from table')

@app.get("/cards/AIGeneratedCard/{}")
async def AIGeneratedCard(Type):
    await asyncio.sleep(1)
    return text("")


if __name__ == "__main__":
    sql_path = os.path.abspath(f"{__file__}/../production.sqlite")
    if os.path.isfile(sql_path):
        print(sql_path + "exists!")
        export_db_conn = asyncio.run(get_conn(sql_path))
        app.run(host="0.0.0.0", port=8000)
    else:
        with sqlite3.connect(sql_path) as connection:
            connection.execute('''
                CREATE TABLE "Group" (
                    "Creator"    TEXT,
                    "Title"      TEXT,
                    "Description" TEXT,
                    "Group"      TEXT,
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
                    "image_url" TEXT
                )
            ''')

            connection.commit()
            print("DB created, restart app.")
            exit(1)