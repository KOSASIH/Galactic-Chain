import tensorflow as tf
from tensorflow_serving.apis import prediction_service_pb2

class ModelServing:
    def __init__(self, model):
        self.model = model

    def deploy_model(self, host, port):
        export_path = '/tmp/model'
        builder = tf.saved_model.builder.SavedModelBuilder(export_path)
        builder.add_meta_graph_and_variables(
            self.model,
            [tf.saved_model.tag_constants.SERVING],
            signature_def_map={
                'predict': self.model.signature_def,
            },
        )
        builder.save()

        # Start TensorFlow Serving
        start_server = tf.saved_model.server.SavedModelServer(export_path,
                                                                config=tf.saved_model.server.ServerOptions(
                                                                    port=port))
        start_server.start()

        # Create a gRPC channel and stub
        channel = grpc.insecure_channel(host)
        stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

        # Send request
        request = prediction_service_pb2.PredictRequest()
        request.model_spec.name = 'model'
        request.model_spec.signature_name = 'predict'
        request.inputs['input'].CopyFrom(
            tf.contrib.util.make_tensor_proto(self.model.input_data))

        # Receive response
        result = stub.Predict(request, 10.0)  # 10 secs timeout

        # Close the channel when done
        channel.close()
