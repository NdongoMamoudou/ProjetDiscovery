#!/bin/bash

if [ "$SPARK_MODE" = "master" ]; then
    echo "Démarrage de Spark Master..."
    /spark/bin/spark-class org.apache.spark.deploy.master.Master \
        --host spark-master \
        --port 7077 \
        --webui-port 8080

elif [ "$SPARK_MODE" = "worker" ]; then
    echo "Démarrage de Spark Worker..."
    /spark/bin/spark-class org.apache.spark.deploy.worker.Worker \
        --webui-port 8081 \
        $SPARK_MASTER
else
    echo "ERREUR: SPARK_MODE doit être 'master' ou 'worker'."
    exit 1
fi
