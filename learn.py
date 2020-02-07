#练习题1：计算1-2之和。
#注意range的函数解释
total = 0
for i in range(1, 3):
    total += i
print(total)

#练习题2：打出1-20的质数
#思路：构建一个是否能除被除的函数,并返回true，false
def judge(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for i in range(2,21):
    if judge(i) == 1:
        print(i)

#数据结构
#二叉树及python实现方法
#创建一个节点，节点有2个分点
#问题：没传参数，index，root怎么传进去的
class Node(object):
    def __init__(self,index):
        self.index = index
        self.left_child = None
        self.right_child = None

#创建二叉树类，及遍历方法
class BinaryTree(object):
    def __init__(self,root):
        self.root = root

    #前遍历,先访问根节点，再先序遍历左子树，然后再先序遍历右子树。总的来说是根—左—右
    def pre_travel(self, node):
        if not node:
            return None
        print(node.index)
        self.pre_travel(node.left_child)
        self.pre_travel(node.right_child)

    #中序遍历,先中序访问左子树，然后访问根，最后中序访问右子树。总的来说是左—根—右
    def mid_travel(self, node):
        if not node:
            return None
        self.mid_travel(node.left_child)
        print(node.index)        
        self.mid_travel(node.right_child)

    #后序遍历,先后序访问左子树，然后后序访问右子树，最后访问根。总的来说是左—右—根
    def back_travel(self, node):
        if not node:
            return None
        self.back_travel(node.left_child)
        self.back_travel(node.right_child)
        print(node.index) 

#创建二叉树
node_dict = {}
# node_dict = []
for i in range(1, 10):
    node_dict[i] = Node(i)
node_dict[1].left_child = node_dict[2]
node_dict[1].right_child = node_dict[3]
node_dict[2].left_child = node_dict[5]
node_dict[2].right_child = node_dict[6]
node_dict[3].left_child = node_dict[7]
node_dict[7].left_child = node_dict[8]
node_dict[7].right_child = node_dict[9]

#遍历
tree = BinaryTree(node_dict[1])
tree.pre_travel(tree.root)
tree.mid_travel(tree.root)
tree.back_travel(tree.root)