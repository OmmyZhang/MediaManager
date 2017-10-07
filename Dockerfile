FROM django

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000

EXPOSE 8000