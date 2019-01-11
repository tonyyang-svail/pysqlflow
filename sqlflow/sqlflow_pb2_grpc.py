# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sqlflow_pb2 as sqlflow__pb2


class SQLFlowStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Run = channel.unary_stream(
        '/sqlflowserver.SQLFlow/Run',
        request_serializer=sqlflow__pb2.RunRequest.SerializeToString,
        response_deserializer=sqlflow__pb2.RunResponse.FromString,
        )


class SQLFlowServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Run(self, request, context):
    """Run runs a SQL statement and returns a stream of RunResponse.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SQLFlowServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Run': grpc.unary_stream_rpc_method_handler(
          servicer.Run,
          request_deserializer=sqlflow__pb2.RunRequest.FromString,
          response_serializer=sqlflow__pb2.RunResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sqlflowserver.SQLFlow', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
