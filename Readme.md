# **Local Spark Iceberg Environment**


## **How To Run**
- Start by downloading the jar files needed for spark
-- `iceberg-spark-runtime`
-- `hadoop-aws`
-- `aws-java-sdk`
-- `postgresql-jdbc`

```bash
chmod +x jars.sh
./jars.sh
```

<br/>
<br/>

- Pull and run docker images

```bash
docker compose up -d
```

<br/>

- Check environment

Hit `localhost:8080` in your browser, you should see your spark master with 3 workers


Run test scripts
```bash
docker exec -it spark-master /opt/spark/bin/spark-submit  --master spark://spark-master:7077   /opt/spark/data/iceberg_write_test.py
```

```bash
docker exec -it spark-master /opt/spark/bin/spark-submit  --master spark://spark-master:7077   /opt/spark/data/iceberg_read_test.py
```


<br/>
<br/>

## **Storage Engine**
In this environment i used Minio, you can run it separately on your local machine, 
or you can use the following docker compose file

```
services:
    minio:
    image: minio/minio
    ports:
        - "9000:9000" # MinIO API port
        - "9001:9001" # MinIO Console port
    volumes:
        - ~/minio/data:/data # Preserve minio data
    environment:
        MINIO_ROOT_USER: minioadmin
        MINIO_ROOT_PASSWORD: minioadmin
        MINIO_DEFAULT_BUCKETS: mybucket # Optional: create a default bucket
    command: server /data --console-address ":9001"
```

You can then login to Minio with the link `localhost:9001` with default username and password, 
and it's important to create a bucket with the name present in the `spark-defaults.conf`

`spark.sql.catalog.iceberg.warehouse=s3a://lakehouse/ # lakehouse is the bucket name`