#!/bin/bash

# Download necessary JARs

echo "Setting up Spark Iceberg environment..."

# Create directories
mkdir -p jars
mkdir -p data

# Download required JARs
echo "Downloading Iceberg and dependencies..."

wget -P jars https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.4.3/iceberg-spark-runtime-3.5_2.12-1.4.3.jar


# AWS SDK for S3 support
wget -P jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -P jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar


# PostgreSQL JDBC driver
wget -P jars https://jdbc.postgresql.org/download/postgresql-42.6.0.jar