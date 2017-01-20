import random, wikiquote
from halibot import HalModule

def make_title(ls):
	return ' '.join([ x[0].upper() + x[1:].lower() for x in ls ])

class Adage(HalModule):
	def receive(self, msg):
		args = msg.body.split(' ')

		if len(args) > 0 and args[0] == '!adage':
			if len(args) == 1:
				title = wikiquote.random_titles(max_titles=1)[0]
			else:
				title = make_title(args[1:])

			try:
				body = '"' + random.choice(wikiquote.quotes(title)) + '" -' + title
			except:
				body = 'There is no page of adages by that title'
			self.reply(msg, body=body)

