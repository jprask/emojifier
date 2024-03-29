# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import emojifier_pb2 as emojifier__pb2


class EmojifierStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Emojify = channel.stream_stream(
        '/Emojifier/Emojify',
        request_serializer=emojifier__pb2.ToEmojify.SerializeToString,
        response_deserializer=emojifier__pb2.Emojified.FromString,
        )


class EmojifierServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Emojify(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EmojifierServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Emojify': grpc.stream_stream_rpc_method_handler(
          servicer.Emojify,
          request_deserializer=emojifier__pb2.ToEmojify.FromString,
          response_serializer=emojifier__pb2.Emojified.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Emojifier', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class EmojiGetterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/EmojiGetter/Get',
        request_serializer=emojifier__pb2.ToEmojify.SerializeToString,
        response_deserializer=emojifier__pb2.WordEmoji.FromString,
        )


class EmojiGetterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EmojiGetterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=emojifier__pb2.ToEmojify.FromString,
          response_serializer=emojifier__pb2.WordEmoji.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'EmojiGetter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
