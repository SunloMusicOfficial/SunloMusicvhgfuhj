import logging
from motor.motor_asyncio import AsyncIOMotorClient
from redis.asyncio import Redis
from config import config

class Database:
    def __init__(self):
        self.mongo = None
        self.redis = None
        self.db = None

    async def connect(self):
        try:
            # MongoDB Connection
            if config.MONGO_URL:
                self.mongo = AsyncIOMotorClient(config.MONGO_URL)
                self.db = self.mongo.sunlomusic
                logging.info("✅ MongoDB Connected")
            else:
                logging.warning("⚠️ No Mongo URL provided. DB features won't work.")

            # Redis Connection (Queue / Cache ke liye)
            if config.REDIS_URL:
                self.redis = Redis.from_url(config.REDIS_URL, decode_responses=True)
                await self.redis.ping()
                logging.info("✅ Redis Connected (Fastest Cache Ready)")
            else:
                logging.warning("⚠️ No Redis URL provided.")

        except Exception as e:
            logging.error(f"❌ DB Connection Failed: {e}")

db = Database()
