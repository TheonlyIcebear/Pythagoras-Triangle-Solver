from decimal import Decimal as D
import json

class Solver:
    def __init__(self):
        data = json.load(open('data.json', 'r+'))
        triangles = data['triangles']
        frac = self.frac


        triangle = triangles[0]

        if not 'c' in triangle:
            triangle['b'] = frac(triangle['b']) ** frac(2)
            given = triangle['b']
        else:
            triangle['a'] = frac(triangle['a']) ** frac(2)
            given = triangle['a']

        side = self.solve(triangle, given)

        
 

        for triangle in triangles[1:]:

            temp = dict(triangle)

            for key in triangle.keys():
                if not triangle[key]:
                    triangle[key] = side
                    temp[key] = f"sqrt('{side}')"
                else:
                    given = side

            side = self.solve(triangle, given)

            for key in ['a', 'b', 'c']:
                if not key in triangle:
                    temp[key] = f"sqrt('{side}')"

            temp = { key:value for (key, value) in sorted(temp.items())}

            print(temp)
                

    def frac(self, num):
        return D(str(num))

    def solve(self, sides, given):
        frac = self.frac

        for key in sides.keys():
            if sides[key] != given:
                sides[key] = frac(sides[key]) ** frac(2)

        a = sides.get('a')
        b = sides.get('b')
        c = sides.get('c')

        if not c:
            side = float( a + frac(b) )

        else:
            side = float(( frac(c)) - frac(a))
            
        return side

if __name__ == "__main__":
    Solver()