from sqlalchemy import create_engine,text
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(os.getenv("URL_DB_CONNECTION"), echo=True)
conn = engine.connect()
req1 = conn.execute(text(f"CREATE TABLE IF NOT EXISTS voice_ai (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(255) NOT NULL, filename VARCHAR(255) NOT NULL)")) 

def rendeur_de_requetes (prompt :str, filename) :
    cleaned_prompt = prompt.replace('"', '_').replace("'", '_')[:250]
    req2 = conn.execute(text(f'INSERT INTO voice_ai (text, filename) VALUES ("{cleaned_prompt}", "{filename}")'))
    return [req2]
