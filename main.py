import json

class Solver:
    def __init__(self):
        data = json.load(open('data.json', 'r+'))
        triangles = data['triangles']


        triangle = triangles[0]
        side = self.solve(triangle)

        for curr in triangles:

            if 'c' in curr:
                triangle = curr
                triangle['a'] = side

            else:
                triangle = curr
                triangle['b'] = side

            side = self.solve(triangle)
            
            temp = {}
            for var in ['a', 'b', 'c']:
                if not var in triangle:
                    temp[var] = side

            print(triangle)

        for var in ['a', 'b', 'c']:
            if not var in triangle:
              triangle[var] = side

        print('Triangle: ', triangle)

            
                



    def solve(self, sides):
        a = sides.get('a')
        b = sides.get('b')
        c = sides.get('c')
        if not 'c' in sides:
            side = ((a**2)+(b**2))**0.5

        else:
            side = ((c**2)-(a**2))**0.5
            
        return side

if __name__ == "__main__":
    Solver()