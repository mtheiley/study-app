# src/server.py
import aiosqlite
from sanic import Sanic, text # if you don't have sanic, just pip install sanic 

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
    app.run(host="0.0.0.0", port=8000)