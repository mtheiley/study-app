# src/server.py
import aiosqlite
import sqlite3
import os 
from sanic import Sanic, text

app = Sanic(__name__)

@app.get("/cards/delete/{}")
async def async_task(request):
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