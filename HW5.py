class Animals:

    def __init__(self, typeOfAn, area, typeFeed, numberOfPaws):
        self.typeOfAn = typeOfAn
        self.area = area
        self.typeFeed = typeFeed
        self._numberOfPows = numberOfPaws

    def presentation(self):
        return f'I am a {self.typeOfAn}. I live in {self.area} and like eat {self.typeFeed}'

    def feed(self):
        return f'I am animal. Feed me. I like {self.typeFeed}. I have {self._numberOfPows} paws'

    def set_area(self, new_area):
        self.area = new_area


bird = Animals('bird', 'Europe', 'grain', 2)
print(bird.presentation())
bird.set_area('Africa')
print(bird.presentation())

cat = Animals('cat', 'home', 'whiskas', 4)
print(cat.presentation())
print(cat.feed())

class Mammals(Animals):

    def __init__(self, typeOfAn, area, typeFeed, numberOfPaws, environment):
        super().__init__(typeOfAn, area, typeFeed, numberOfPaws)
        self.environment = environment



    def hello(self):
        return 'I am mammal'


elephant = Mammals('elephant', 'Africa', 'grass', 4, 'jungles')
print(elephant.hello())
print(cat._numberOfPows)
print(cat.__dict__)