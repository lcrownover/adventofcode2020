class Course:
    def __init__(self, input_file):
        self.score = 0
        with open(input_file, 'r') as f:
            self.course = [line.strip() for line in f.readlines()]

    def _traverse_right(self):
        for i,row in enumerate(self.course):
            x = row[1:]
            row = x+row[0]
            self.course[i] = row

    def _traverse_down(self):
        self.course.pop(0)
        if len(self.course) == 0:
            self.course = None

    def _score(self):
        if not self.course:
            return
        if self.course[0][0] == '#':
            self.score += 1

    def _report(self):
        print(self.score)

    def traverse(self, right, down):
        while self.course:
            for i in range(0,right):
                self._traverse_right()
            for i in range(0,down):
                self._traverse_down()
            self._score()
        self._report()

    def traverse_once(self, right, down):
        for i in range(0,right):
            self._traverse_right()
        for i in range(0,down):
            self._traverse_down()
        self._score()
        self._report()

    def display(self,rows=0):
        if not self.course:
            return
        if rows == 0:
            for row in self.course:
                print(row)
        else:
            for i,row in enumerate(self.course):
                if i <= rows:
                    print(row)
