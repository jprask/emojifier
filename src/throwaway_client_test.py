import grpc

import emojifier_pb2
import emojifier_pb2_grpc


def request_iterator():
	for w in 'Ocean man word word house'.split():
		yield emojifier_pb2.ToEmojify(text=w, degree=5) 


def run():
	channel = grpc.insecure_channel('localhost:12345')
	stub = emojifier_pb2_grpc.EmojifierStub(channel)
	for w in stub.Emojify(request_iterator()):
		print(w.response)


if __name__ == '__main__':
    run()
