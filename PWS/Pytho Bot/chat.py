from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('James')

bot.set_trainer(ListTrainer)
# Training 
bot.train(['What is your name?', 'My name is James'])
bot.train(['Who are you?', 'I am a bot, created by you' ])

bot.train(['Do you know me?', 'Yes, you created me', 'No', 'Sahil?', 'No idea'])

from chatterbot.trainers import ChatterBotCorpusTrainer
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

for files in os.listdir('./english/'):
    data=open('./english/'+files,'r').readlines()
    bot.train(data)

# To exit say "Bye"
while True:
        # Input from user
    message=input('\t\t\tYou:')
        #if message is not "Bye"
    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('Candice:',reply)
        # if message is "Bye"
    if message.strip()=='Bye':
        print('Candice: Bye')
        break