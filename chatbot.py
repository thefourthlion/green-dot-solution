from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",],
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",],
    ],
    [
        r"what is your name ?",
        ["I am a bot. You can call me ChatBot.",],
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You ?",],
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",],
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",],
    ],
    [
        r"quit",
        ["Bye. It was nice talking to you. See you soon :)"],
    ],
]


def chat_bot():
    print("Hi, I'm the chatbot you created")

chat = Chat(pairs, reflections)
chat.converse()
if __name__ == "__main__":
    chat_bot()