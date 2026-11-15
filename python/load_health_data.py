import os 
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()

url = URL.create(
    "mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME"),
)

engine = create_engine(url)

df = pd.read_csv("data/health_clean.csv", keep_default_na=False)
print("Row in file", len(df))

with engine.begin() as conn:
    conn.execute(text("DELETE FROM patients"))

df.to_sql("patients", engine, if_exists="append", index=False, chunksize=5000)

count = pd.read_sql("SELECT COUNT(*) AS row_loaded FROM patients", engine)
print(count)