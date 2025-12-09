from pyspark.sql import SparkSession


spark = (
    SparkSession.builder
    .appName("IcebergTest")
    .master("spark://spark-master:7077")
    .config("spark.executor.cores", 1)
    .config("spark.cores.max", 2)
    .config("spark.executor.memory", "1024M")

    .getOrCreate()
)

print("SparkSession created.")


# Read back from Iceberg
spark.read.table("iceberg.test.sample_table").show()

spark.stop()