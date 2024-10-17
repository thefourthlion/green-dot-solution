class MadLibs:
    def __init__(self, template):
        self.template = template
        self.words = {}

    def add_word(self, placeholder, word):
        self.words[placeholder] = word

    def generate_story(self):
        story = self.template
        for placeholder, word in self.words.items():
            story = story.replace(placeholder, word)
        return story


template = "Once upon a time there was a very {adjective} {noun}. Everyday {pronoun} would {verb}."
mad_lib = MadLibs(template)
mad_lib.add_word("{adjective}", "gloomy")
mad_lib.add_word("{noun}", "ghost")
mad_lib.add_word("{pronoun}", "it")
mad_lib.add_word("{verb}", "haunt the old mansion")

print(mad_lib.generate_story())