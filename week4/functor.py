class Strip:
    def __init__(self, characters):
        self.characters = characters

    def __call__(self, string):
        sp = string.split(" ")
        new_massage = " ".join(i.strip(self.characters) for i in sp)
        return new_massage


strip_punctuations = Strip(",;:.?!")
s = "Please, strip punctuations from this string!"
print(strip_punctuations(s))
