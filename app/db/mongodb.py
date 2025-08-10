from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import certifi
import ssl

def get_mongo_client():
    """Create MongoDB client with proper SSL configuration"""
    # Simplified connection - let MongoDB Atlas handle SSL automatically
    connection_string = f"{settings.MONGO_URI}"
    
    # Basic client with minimal SSL config - Atlas handles most SSL setup
    client = AsyncIOMotorClient(
        connection_string,
        serverSelectionTimeoutMS=30000,  # Increased timeout
        connectTimeoutMS=20000,
        socketTimeoutMS=20000,
        retryWrites=True,
        w="majority"
    )
    
    return client

# Alternative: Direct connection string approach (recommended)
def get_mongo_client_simple():
    """Simpler approach - let Atlas handle SSL automatically"""
    client = AsyncIOMotorClient(
        "mongodb+srv://thekoustavofficial:hackathon@cluster0.3n6vx8g.mongodb.net/HO_MySarkar?retryWrites=true&w=majority&appName=Cluster0",
        serverSelectionTimeoutMS=30000
    )
    return client

# Initialize the client (don't call async methods here)
client = get_mongo_client_simple()
db = client.HO_MySarkar  # Explicitly specify database name
users_collection = db["users"]

# Test connection in an async function
async def test_connection():
    """Test the MongoDB connection"""
    try:
        # Test the connection
        await client.admin.command('ping')
        print("MongoDB connection successful!")
        
        # Get server info
        server_info = await client.server_info()
        print(f"Connected to MongoDB version: {server_info.get('version')}")
        
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

# Example usage in your FastAPI app
async def verify_db_connection():
    """Call this in your FastAPI startup event"""
    await test_connection()