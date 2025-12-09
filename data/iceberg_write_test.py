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

# Create a simple DataFrame
data = [
    (1, "u1", 100.5),
    (2, "u2", 200.0),
    (3, "u3", 300.7),
]

columns = ["id", "name", "value"]

df = spark.createDataFrame(data, columns)

print("DataFrame created:")
df.show()



# Create namespace if not exists
spark.sql("CREATE NAMESPACE IF NOT EXISTS iceberg.test")



# Create Iceberg table
spark.sql("""
    CREATE TABLE IF NOT EXISTS iceberg.test.sample_table (
        id INT,
        name STRING,
        value DOUBLE
    )
    USING iceberg
""")

print("Iceberg table created.")



# Write DataFrame to Iceberg
df.writeTo("iceberg.test.sample_table").append()

print("Data written to Iceberg table.")



# Read back from Iceberg
print("Reading back from table:")
spark.read.table("iceberg.test.sample_table").show()

spark.stop()