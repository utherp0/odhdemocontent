from pyspark import SparkContext
sc = SparkContext("local", "first app")
# Calculating words count
text_file = sc.textFile("textfile.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
# Printing each word with its respective count
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))
# Stopping Spark Context
sc.stop()
