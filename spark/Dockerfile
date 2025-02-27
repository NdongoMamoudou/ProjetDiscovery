FROM bde2020/spark-worker:3.3.0-hadoop3.3

WORKDIR /app

COPY requirements-spark.txt requirements-spark.txt

RUN pip install --no-cache-dir -r requirements-spark.txt

COPY . .

# S’assurer que start-spark.sh a les bons droits
RUN chmod +x /app/start-spark.sh

CMD ["/bin/bash", "/app/start-spark.sh"]
