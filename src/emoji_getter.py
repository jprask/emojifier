import json
import grpc
import time
import random
from os import path
from concurrent import futures

import emojifier_pb2
import emojifier_pb2_grpc


class EmojiGetterServicer(emojifier_pb2_grpc.EmojiGetterServicer):
	def __init__(self, emojis):
		super()
		self.emojis = emojis

	def Get(self, request, context):
		word = request.text.lower()
		singular, plural = (word[0:-1], word + 's') if word.endswith('s') else (None, None)
		dg = request.degree
		match = []
		for e in self.emojis:
			if self.emojis[e]['category'] == 'flags':
				continue
			if sum([word == kw or singular == kw or plural == kw for kw in self.emojis[e]['keywords']]):
				match.append(self.emojis[e]['char'])
		while len(match) > dg:
			match.remove(match[random.randint(0, len(match) - 1)])
		
		print('returning {} / {}'.format(word, ' '.join(match)))
		return emojifier_pb2.WordEmoji(word=word, emoji=' '.join(match))

def main():
	emojis = json.load(
		open(path.abspath(path.join(path.dirname(__file__), '..', 'emoji', 'emojis.json')), encoding='UTF-8')
	)
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	emojifier_pb2_grpc.add_EmojiGetterServicer_to_server(
		EmojiGetterServicer(emojis), server
	)
	server.add_insecure_port('[::]:50051')
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
