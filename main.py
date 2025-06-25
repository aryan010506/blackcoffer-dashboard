from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

# Setup
app = FastAPI()
client = MongoClient("mongodb://localhost:27017")
db = client["blackcofferDB"]
collection = db["insights"]

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.get("/")
def home():
    return {"message": "Backend API working!"}

@app.get("/insights")
def get_all_data():
    data = list(collection.find({}, {"_id": 0}))  # exclude _id field
    return data

@app.get("/filters")
def get_filters():
    return {
        "topics": collection.distinct("topic"),
        "countries": collection.distinct("country"),
        "sectors": collection.distinct("sector"),
        "regions": collection.distinct("region"),
        "pestles": collection.distinct("pestle"),
        "sources": collection.distinct("source"),
        "swots": collection.distinct("swot"),
        "end_years": collection.distinct("end_year"),
    }
