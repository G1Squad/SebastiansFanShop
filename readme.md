# Sebastians FunShop
Välkommen till Sebastians FunShop - din destination för roliga och unika produkter! Denna webbshop är byggd med Python/Flask och erbjuder en enkel och smidig shoppingupplevelse. Här kan du bläddra bland produkter, lägga till dem i din varukorg och genomföra köp på ett säkert sätt.

## Installation
1. Se till att du har Python 3.8 eller senare installerat
2. Klona detta repository:
```bash
git clone https://github.com/G1Squad/SebastiansFanShop.git
cd SebastiansFanShop
```

## Konfigurering
3. Starta databasen med Docker:
```bash
docker-compose up -d
```

4. Kopiera exempel-miljöfilen och konfigurera den:

För Mac:
```bash
cp .env.example .env
```

För Windows:
```bash
copy .env.example .env
```
Öppna .env-filen och uppdatera inställningarna efter behov.

5. Skapa en virtuell miljö och aktivera den:

För Mac:
```bash
python -m venv venv
source venv/bin/activate
```

För Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

6. Installera dependencies:
```bash
pip install -r requirements.txt
```

7. Starta Flask-servern:
```bash
python app.py
```
eller
```bash
flask run
```

8. Öppna din webbläsare och gå till `http://127.0.0.1:5000` för att se hemsidan.