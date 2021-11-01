from typing import Dict, List, Tuple


def suma(a: int, b: int) -> int:
    return a + b


def run():
    print(suma(1,3))

    positives: List[int] = [1,2,3,4,5]

    users: Dict[str,int] = {
        'argentina':1,
        'mexico':34,
        'colombia':45,
    }

    countries: List[Dict[str,str]]= [
        {
            'name':'Argentina',
            'people': '450000',
        },
        {
            'name':'México',
            'people': '9000000',
        },
        {
            'name':'Colombia',
            'people': '999999999999999',
        },
    ]

    numbers: Tuple[int,float,int]=(1,0.5,1)

    print(positives)
    print(users)
    print(numbers)
    print(countries)

    CoordinatesType = List[Dict[str,Tuple[int,int]]]

    coordinates: CoordinatesType = [
        {
            'coord1':(1,2),
            'coord2':(3,5),
        },
        {
            'coord1':(0,1),
            'coord2':(2,5),
        }
    ]

    print(coordinates)


if __name__ == '__main__':
    run()