from sqlalchemy import create_engine,text
engine =create_engine("mysql+mysqlconnector://root:@localhost:3306/sql", echo=True)
conn = engine.connect()
req1 = conn.execute(text(f"CREATE TABLE IF NOT EXISTS voice_ai (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(255) NOT NULL, filename VARCHAR(255) NOT NULL)")) 

def rendeur_de_requetes (prompt :str, filename) :
    req2 = conn.execute(text(f"INSERT INTO voice_ai (text, filename) VALUES (\"{prompt.replace('\"','_').replace('\'','_')[0:250]}\", '{filename}')")) 
    return [req2]