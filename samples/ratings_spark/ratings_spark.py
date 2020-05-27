from pyspark import SparkConf, SparkContext
import string

# run code with linux command : spark-submit ratings_spark.py

# configure spark environment and context
conf = SparkConf().setMaster('local').setAppName('MovieRate')
sc = SparkContext(conf = conf)

# function to find id (2nd term in line)
def findids(line):
    words = line.split(",")
    return words[1]

# read ratings into RDD
RDDvar = sc.textFile("ratings.csv")

# RDD words has key (ids) and values (ratings)
words = RDDvar.map(lambda line: (str(line.split(",")[1]), float(str(line.split(",")[2]))))

# find RDD of ids only 
ids = RDDvar.map(findids)

# map count of "1" to each id, to count each instance of id
idcount = ids.map(lambda word: (str(word),1))

# aggregate "words" to find sum of ratings values for each id
wordagg = words.reduceByKey(lambda a, b: a+b)

# aggregate "idcount" to find count of instances each id
idagg = idcount.reduceByKey(lambda a, b: a+b)

#join count and sum values
joiner = wordagg.join(idagg)

# use count and sums to find average for each id
result = joiner.mapValues(lambda a: a[0] / a[1])

# find movies that have rating average between 0 and 1, assign new value of rating class "1"
result1 = result.filter(lambda keyValue: 0 < keyValue[1] and  keyValue[1] <= 1)
result1b = result1.map(lambda a: (a[0], 1))

# find movies that have rating average between 1 and 2, assign new value of rating class "2"
result2 = result.filter(lambda keyValue: 1 < keyValue[1] and  keyValue[1] <= 2)
result2b = result2.map(lambda a: (a[0], 2))

# find movies that have rating average between 2 and 3, assign new value of rating class "3"
result3 = result.filter(lambda keyValue: 2 < keyValue[1] and  keyValue[1] <= 3)
result3b = result3.map(lambda a: (a[0], 3))

# find movies that have rating average between 3 and 4, assign new value of rating class "4"
result4 = result.filter(lambda keyValue: 3 < keyValue[1] and  keyValue[1] <= 4)
result4b = result4.map(lambda a: (a[0], 4))

# find movies that have rating average between 4 and 5, assign new value of rating class "5"
result5 = result.filter(lambda keyValue: 4 < keyValue[1] and  keyValue[1] <= 5)
result5b = result5.map(lambda a: (a[0], 5))

# create union of all results
finala = result1b.union(result2b)
finalb = finala.union(result3b)
finalc = finalb.union(result4b)
final = finalc.union(result5b)

# save union as text file 
# view with linux command : cat ratings_spark.txt/*
final.saveAsTextFile("ratings_spark.txt")
