from pyspark.sql import SparkSession
from functools import lru_cache
import os
from pyspark.sql.functions import current_date, current_timestamp


os.environ['JAVA_HOME']="C:\java"


@lru_cache(maxsize=None)
def get_spark():
    return (SparkSession.builder
                .master("local")
                .appName("gill")
                .getOrCreate())

spark=get_spark()

dateDF=spark.range(10)\
 .withColumn("today",current_date())\
 .withColumn("now",current_timestamp())

#print(spark.range(5000).where("id > 500").selectExpr("sum(id)").collect())

print(dateDF.collect())