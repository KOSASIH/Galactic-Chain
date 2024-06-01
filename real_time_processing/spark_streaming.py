from pyspark.streaming import StreamingContext

class SparkStreamingProcessor:
    def __init__(self, sc):
        self.sc = sc

    def process_data(self, data):
        # Process the data using Spark Streaming
        # For example, calculate the average value of the data
        stream = self.sc.parallelize(data)
        average = stream.reduce(lambda x, y: x + y) / len(data)
        print(f"Average value: {average}")

if __name__ == "__main__":
    sc = StreamingContext("local[2]", "Spark Streaming Processor", 1)
    processor = SparkStreamingProcessor(sc)
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    processor.process_data(data)
    sc.start()
    sc.awaitTermination()
