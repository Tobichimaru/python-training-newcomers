class ContMen():
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.file_path, self.mode)
        return self.open_file

    def __exit__(self, exc_type, exc, exc_tb):
        self.open_file.close()


if __name__ == "__main__":
    file_path = 'k:\python-training\python-training-newcomers\week4\logs-info.txt'

    with ContMen(file_path, "a") as infile:
        infile.write("Some log.\n")





