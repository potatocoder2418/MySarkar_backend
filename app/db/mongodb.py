from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import certifi

def get_mongo_client():
    # Add retryWrites and w=majority for better reliability
    connection_string = f"{settings.MONGO_URI}"
    
    # Configure SSL with certifi CA certificates
    client = AsyncIOMotorClient(
        connection_string,
        tls=True,
        tlsCAFile=certifi.where(),
        tlsAllowInvalidCertificates=False,
        serverSelectionTimeoutMS=5000  # 5 second timeout
    )
    return client

# Initialize the client
client = get_mongo_client()
db = client.get_default_database()
users_collection = db["users"]
