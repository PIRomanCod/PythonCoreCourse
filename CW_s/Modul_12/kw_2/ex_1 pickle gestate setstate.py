import pickle
from datetime import datetime
from time import sleep

class RememberAll:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        state = self.__dict__.copy()  # всі властивості класу (поля, методи) зберігаються в цьому __dict__
        state['saved'] = datetime.now()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)  # все що було в ньому буде замінено на state, що прийшов
        self.restored = datetime.now()  # self.restored - час, а self?
        print(self.restored)
        print(dir(self.restored))


if __name__ == "__main__":
    r = RememberAll(1, 2, 3, 4, 5, 6)
    print(r.data)
    r_dump = pickle.dumps(r)
    sleep(1)
    r_load = pickle.loads(r_dump)
    print(r.saved, r.restored)
    print(r_load.saved, r_load.restored)