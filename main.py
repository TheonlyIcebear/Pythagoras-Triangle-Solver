from decimal import Decimal as D
import json

class Solver:
    def __init__(self):
        data = json.load(open('data.json', 'r+'))
        triangles = data['triangles']


        triangle = triangles[0]
        triangle['b'] **= 2 

        places = [str(side)[::-1].find('.') for side in triangle.values() ]
        side = round(self.solve(triangle), max(places)+1 if max(places) > 0 else 0)

        print(side)
      
        for curr in triangles:

            temp = dict(curr)

            if 'c' in curr:
                triangle = curr
                triangle['a'] = side
                temp['a'] = f'sqrt({side})'

            else:
                triangle = curr
                triangle['b'] = side
                temp['b'] = f'sqrt({side})'

            places = [str(side)[::-1].find('.') for side in triangle.values() ]
            side = round(self.solve(triangle), max(places)+1 if max(places) > 0 else 0)
            
            for var in ['a', 'b', 'c']:
                if not var in triangle:
                    temp[var] = f'sqrt({float(side)})'

            print({key: value for key, value in sorted(temp.items())})

        for var in ['a', 'b', 'c']:
            if not var in triangle:
              triangle[var] = f'sqrt({side})'

        print('Triangle: ', temp)

            
                



    def solve(self, sides):
        a = sides.get('a')
        b = sides.get('b')
        c = sides.get('c')
        if not 'c' in sides:
            side = float((D(a)**D(2))+D(b))

        else:
            side = float((D(c)**D(2))-D(a))
            
        return side

if __name__ == "__main__":
    Solver()