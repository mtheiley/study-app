import aiosqlite
import asyncio
import sqlite3
import os
import uuid
from sanic import Sanic, text
from sanic.request import Request
from sanic.response import text

sql_path = os.path.abspath(f"{__file__}/../production.sqlite")

app = Sanic(__name__)

async def get_conn(sql_path):
    return await aiosqlite.connect(sql_path)

@app.get("/cards/delete/<card_id>")
async def removeCard(card_id, db_conn = get_conn(sql_path)):
    await db_conn.cursor.execute(f"DELETE FROM Cards WHERE cardID = ?", card_id)
    await db.commit()
    return text("Operation Successful")

@app.get("/cards/create")
async def createCard(request: Request, uuid = uuid.uuid4().hex, db_conn = get_conn(sql_path)):
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
async def viewCard(cardId, db_conn = get_conn(sql_path)):
    if card_group == "all":
        await db_conn.cursor('select * from cards')
    else:
        await db_conn.cursor("select * from cards WHERE GroupID = ?", card_group)
    return await cur.fetchall()

'''
@app.get("/cards/<card_id>/edit")
async def editCard(request):
    ...
    return text("")


@app.get("/cards/setCardGroup/{}")
async def setCardGroup(CardID, GroupId):
    ...


@app.get("/cards/random/")
async def randomCard():
    ...

@app.get("/cards/setCardImage/{}")
async def setCardImage(CardImageID, Image):
    ...

@app.get("/cards/getCardImage/{}")
async def getCardImage(CardImageID):
    ...


@app.get("/cards/AIGeneratedCard/{}")
async def AIGeneratedCard(Type):
    ...


@app.get("/option/createOption/{}")
async def createOption(Text, OptionImageID, Type, IsCorrect):
    ...

@app.get("/option/removeOption/{}")
async def removeOption(OptionID):
    ...


@app.get("/option/viewOption/{}")
async def viewOption(OptionID):
    ...

@app.get("/option/editOption/{}")
async def editOption(OptionID, Text, OptionImageID, Type, IsCorrect):
    ...

@app.get("/option/setOptionImage/{}")
async def setOptionImage(OptionImageID, Image):
    ...
@app.get("/option/createOptionImage/{}")
async def createOptionImage(Image):
    ...

@app.get("/option/getOptionImage/{}")
async def getOptionImage(OptionImageID):
    ...

@app.get("/group/createGroup/{}")
async def createGroup(Creator, Title, Description,IDs):
    ...

@app.get("/group/removeGroup/{}")
async def removeGroup(GroupID):
    ...

@app.get("/group/viewGroupInfo/{}")
async def viewGroupInfo(GroupID):
    ...

@app.get("/group/viewGroupCards/{}")
async def viewGroupCards(GroupID):
    ...

@app.get("/group/viewGroupList/{}")
async def viewGroupList():
    ...

@app.get("/group/editGroupInfo/{}")
async def editGroupInfo(GroupID, Creator, Title, Description):
    ...

@app.get("/group/groupAddCard/{}")
async def groupAddCard(GroupID, CardID):
    ...

@app.get("/group/groupRemoveCard/{}")
async def groupRemoveCard(GroupID, CardID):
    ...
'''

if __name__ == "__main__":
    if os.path.isfile(sql_path):
        print(sql_path + "exists!")
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