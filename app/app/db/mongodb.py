from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import certifi

def get_mongo_client():
    # Add retryWrites and w=majority for better reliability
    connection_string = f"{settings.MONGO_URI}"
    
    # Configure SSL with certifi CA certificates
    client = AsyncIOMotorClient(
        "mongodb+srv://thekoustavofficial:hackathon@cluster0.3n6vx8g.mongodb.net/HO_MySarkar?retryWrites=true&w=majority&appName=Cluster0",
        tls=True,
        tlsCAFile=certifi.where(),
        tlsAllowInvalidCertificates=False,
        ssl_cert_reqs=ssl.CERT_REQUIRED,
        serverSelectionTimeoutMS=5000 
    )
    print(await client.server_info())
    return client

# Initialize the client
client = get_mongo_client()
db = client.get_default_database()
users_collection = db["users"]
