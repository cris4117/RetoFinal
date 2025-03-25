# Para crear el entorno virtual e instalar los requerimientos:
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Para levantar la aplicación:

python .\app.py

# Para crear la imagen
docker build --force-rm -t flights-app . --no-cache

# Para levantar el contenedor
docker run -d -p 8000:8000 --name flights-container flights-app

# Para ejecutar el docker-compose
docker compose -p flask-docker-compose up -d

# Para hacer el build de docker-compose
docker compose down
docker compose build --no-cache
docker compose up -d
