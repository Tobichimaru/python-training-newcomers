class Lister():
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.file_path, self.mode)
        return self.open_file

    def __exit__(self, exc_type, exc, exc_tb):
        self.open_file.close()


def person_lister(f):
    def inner(people):
        return f(people)
    return inner


@person_lister
def name_format(people):
    for i in range(len(people) - 1):
        for j in range(len(people) - i - 1):
            if people[j][1] > people[j + 1][1]:
                people[j], people[j + 1] = people[j + 1], people[j]
    return people


if __name__ == '__main__':
   ''' people = [raw_input().split() for i in range(int(raw_input()))]
    print('\n'.join(name_format(people)))'''


file_path = 'k:\python-training\python-training-newcomers\week4\input.txt'
with Lister(file_path, "r") as infile:
    people = [infile.readline().split() for i in range(int(infile.readline()))]
    new_people = []
    for p in people:
        new_people.append(tuple([p[0] + " " + p[1], p[2], p[3]]))
    new_people = name_format(new_people)
    new_people2 = []
    for p2 in new_people:
        if p2[2] is "M":
            new_people2.append("Mr. " + p2[0])
        else:
            new_people2.append("Ms. " + p2[0])
    new_people = new_people2
    print(new_people)

file_path2 = 'k:\python-training\python-training-newcomers\week4\output.txt'
with open(file_path2, "w") as file_object:
    for line in new_people:
        file_object.write(line + "\n")
