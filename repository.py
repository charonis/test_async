from datebase import engine
from sqlalchemy import text
class Repository:
    @classmethod
    async def test_bd_aa(cls):
        async with engine.connect() as conn:
            res = await conn.execute(text("SELECT 1,2,3 UNION select 4,5,6"))
            return res
