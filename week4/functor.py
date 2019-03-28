class Strip:
    def __init__(self, characters):
        self.characters = characters

    def __call__(self, string):
        sp = string.split(" ")
        new_massage = ""
        for i in sp:
            new_massage += " " + i.strip(self.characters)
        return new_massage.strip(" ")


strip_punctuations = Strip(",;:.?!")
s = "Please, strip punctuations from this string!"
print(strip_punctuations(s))
