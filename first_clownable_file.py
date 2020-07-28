class Shape:
    nameofshape = str;
    numberofsides = int;
    length = int;
    width = int;
    height = int;
    volume = int;

    def getdetailsofshape(self, nameofshape=str, numberofsides=int, length=int, width=int, height=int):
        self.nameofshape = nameofshape;
        self.numberofsides = numberofsides;
        self.length = length;
        self.width = width;
        self.height = height;
        print("The details of the ", nameofshape, "is that it has ", numberofsides,
              " sides. A length of ", length, " a width of ", width, " and a height of", height);
        return length, width

    def get_len_width(self):
        print(self.length) #Carries length input
        print(self.width) #Carries width input
        len_woid_decl = str
        len_woid_decl = ' '
        print('the ')
        return self.length
        return self.width





firstshape = Shape()

if __name__ == "__main__":
    firstshapewithparam = firstshape.getdetailsofshape('Rectangle', 4, 6, 10, 15)
    Second_shape_instance = firstshape.get_len_width()
