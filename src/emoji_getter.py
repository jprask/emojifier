import json
import grpc
import random
from os import path

import emojifier_pb2
import emojifier_pb2_grpc

class GetEmojiServicer(emojifier_pb2_grpc.EmojiGetterServicer):
	def __init__(self, emojis):
		super()
		self.emojis = emojis

	def Get(self, request, context):



def main():
	emojis = json.load(open(
		path.abspath(path.join(path.dirname(__file__), '..', 'emoji', 'emojis.json')), encoding='UTF-8')
	)



if __name__ == '__main__':
	main()