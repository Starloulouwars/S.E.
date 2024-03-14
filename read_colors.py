class read_color_parameters:

    def __init__(self):
        self.c = {}
    
    def readColors(self, file):
        with open(file, "r") as f:
            contents = f.readlines()
            for i in range(len(contents)):
                contents[i] = contents[i].rstrip("\n")
                contents[i] = contents[i].split("=")
            for elt in contents:
                self.c[elt[0]] = elt[1]
