from fastapi import FastAPI
# 1. First, import the CORS tool
from fastapi.middleware.cors import CORSMiddleware

# 2. Create the app instance
app = FastAPI()

# 3. Add the CORS Middleware (Place this BEFORE your routes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allows DartPad and other browsers
    allow_credentials=True,
    allow_methods=["*"],      # Allows GET, POST, etc.
    allow_headers=["*"],      # Allows all headers
)

# 4. Your Routes (The code you already wrote)
@app.get("/")
async def root():
    return {"message": "PBT Roadworks API is Live!"}

@app.get("/samples")
async def get_sample_roadworks():
    return [
        {
            "id": 1,
            "pbt": "MBPJ",
            "road": "Jalan Universiti",
            "status": "Active",
            "lat": 3.1209,
            "lng": 101.6538
        }
    ]
