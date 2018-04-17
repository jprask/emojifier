import grpc

import emojifier_pb2
import emojifier_pb2_grpc


def request_iterator(inp):
	for w in inp.split():
		yield emojifier_pb2.ToEmojify(text=w, degree=2)


def run():
	channel = grpc.insecure_channel('localhost:12345')
	stub = emojifier_pb2_grpc.EmojifierStub(channel)
	response = ''
	for w in stub.Emojify(request_iterator(input('Emojify: '))):
		response += w.response + ' '
	print('\n\nEmojified:\n\n' + response)


if __name__ == '__main__':
    run()
