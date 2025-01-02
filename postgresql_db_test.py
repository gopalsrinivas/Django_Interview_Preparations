import asyncpg
import asyncio

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@r2schools.czu6s64ao2fk.ap-south-1.rds.amazonaws.com/fastapi_hostel_app"


async def connect_to_db():
    try:
        conn = await asyncpg.connect(
            user="postgres",
            password="postgres",
            database="fastapi_hostel_app",
            host="r2schools.czu6s64ao2fk.ap-south-1.rds.amazonaws.com",
            port=5432,
        )
        print("Successfully connected to the database!")
        await conn.close()
    except Exception as e:
        print(f"Failed to connect to the database: {e}")


# Run the connection
asyncio.run(connect_to_db())
