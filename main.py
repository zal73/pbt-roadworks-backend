from fastapi import FastAPI

app = FastAPI()

# 1. The 'Hello World' Home Route
@app.get("/")
async def root():
    return {"message": "PBT Roadworks API is Live!"}

# 2. A sample endpoint for your Flutter App to fetch
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
