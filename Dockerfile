FROM python:3.11-slim
LABEL authors="delissgt"

WORKDIR /app

COPY  requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]


#ENTRYPOINT ["top", "-b"]