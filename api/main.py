# src/server.py
import aiosqlite
import sqlite3
import os 
from sanic import Sanic, text

app = Sanic(__name__)

@app.get("/cards/delete/{}")
async def removeCard(cardId):
    await asyncio.sleep(1)
    return text("")

@app.get("/cards/create/{}")
async def createCard(GroupId, Text, CardImageID, Title, Type, OptionID_1, OptionID_2, OptionID_3, OptionID_4):
    await asyncio.sleep(1)
    return text("")

@app.get("/cards/view/{}")
async def viewCard(cardId):
    await asyncio.sleep(1)
    return text("")

@app.get("/cards/edit/{}")
async def editCard(CardID, GroupID, Text, CardImageID, Title, Type, OptionID_1, OptionID_2, OptionID_3, OptionID_4):
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
    return text("")

@app.get("/cards/AIGeneratedCard/{}")
async def AIGeneratedCard(Type):
    await asyncio.sleep(1)
    return text("")




if __name__ == "__main__":
    sql_path = os.path.abspath(f"{__file__}/../production.sqlite")
    if os.path.isfile(sql_path):
        print(sql_path + "exists!")
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
                CREATE TABLE "cards" (
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

    app.run(host="0.0.0.0", port=8000)