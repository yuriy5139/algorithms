"""
Задание 2.
Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter, deque


# создадим собственный класс узла, как нам предлагал преподаватель на уроке
class Node():
    def __init__(self, left=None, right=None, value=None, weight=0):
        self.__left = left
        self.__right = right
        self.value = value
        self.weight = weight

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        if isinstance(node, Node) and node != self:
            self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        if isinstance(node, Node) and node != self:
            self.__right = node

    def __repr__(self):
        if not self.__right and not self.__left:
            return f"left:|right:|value:{self.value if self.value else ''}|weight:{self.weight}"
        elif self.__left and not self.__right:
            return f"left:{self.__left}>|right:|value:{self.value if self.value else ''}|weight:{self.weight}"
        elif self.__right and not self.__left:
            return f"left:|right:<{self.__right}>|value:{self.value if self.value else ''}|weight:{self.weight}"
        else:
            return f"left:<{self.__left}>|right:<{self.__right}>|value:{self.value if self.value else ''}|weight:{self.weight}"


# Функция вставки узла в dequeue. Чтобы не загромождать основную функцию - вынесем сюда
def deq_insert(queue, item):
    for i, elem in enumerate(queue):
        if elem.weight < item.weight:
            continue
        else:
            queue.insert(i, item)
            return
    queue.append(item)


# Функция прохода по бинарному дереву и наполнения словаря букв кодами
def traverse(node, dct, path=None):
    if not path:
        path = []

    if not node.left and not node.right:
        dct[node.value] = path
        return

    if node.left:
        pathleft = path[:]
        pathleft.append(0)
        traverse(node.left, dct, path=pathleft)

    if node.right:
        pathright = path[:]
        pathright.append(1)
        traverse(node.right, dct, path=pathright)


# Функция построения дерева
def get_codes(line):
    codes = {}
    c = Counter(line)
    queue = deque()
    for k, v in c.most_common():
        queue.appendleft(Node(value=k, weight=v))
    # for item in queue: print(item)
    while len(queue) > 1:
        left, right = queue.popleft(), queue.popleft()
        newnode = Node(left=left, right=right, weight=left.weight + right.weight)
        # print("\ninserting new", newnode)
        deq_insert(queue, newnode)
        # for item in queue: print(item)

    root = queue.popleft()
    traverse(root, codes)

    return codes


if __name__ == "__main__":
    line = "beep boop beer!"
    encoder = get_codes(line)
    print("Будем кодировать строку", line)
    print("Закодированная строка = ", end='')
    for char in line:
        print(encoder[char], end='')
