import grpc, time
from concurrent import futures

import emojifier_pb2
import emojifier_pb2_grpc


class Emojifier(emojifier_pb2_grpc.EmojifierServicer):
	
	def Emojify(self, request_iterator, context):
		channel = grpc.insecure_channel('localhost:50051')
		stub = emojifier_pb2_grpc.EmojiGetterStub(channel)
		for request in request_iterator:
			word = request.text
			dg = request.degree
			we = stub.Get(emojifier_pb2.ToEmojify(text=word, degree=dg))
			print('yielding {}'.format(we))
			yield emojifier_pb2.Emojified(response='{} {}'.format(we.word, we.emoji))


def main():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	emojifier_pb2_grpc.add_EmojifierServicer_to_server(Emojifier(), server)
	server.add_insecure_port('[::]:12345')
	server.start()
	print('Server started')
	try:
		while True:
			time.sleep(60 * 60 * 24)
	except KeyboardInterrupt:
		print('bye')
		server.stop(0)


if __name__ == '__main__':
	main()