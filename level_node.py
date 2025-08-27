
class LevelNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.children = []

def player_tranverse(node):
    if node is None:
        print("You've reacehd a dead end!")
        return

    print(f"\nYou are at node: {node.data}")
    

    #Check if this is a leaf node
    if node.left is None and node.right is None:
        print("This is a leaf node. No further moves.")
        return 

    choices = []
    if node.left:
        print("L: Go to left child", node.left.data)
        choices.append('L')
    if node.right:
        print("R: Go to right child", node.right.data)
        choices.append('R')

    while True:
        choice = input("Choose your next move (" + "/".join(choices) + "): ").strip().upper()
        if choice == 'L' and 'L' in choices:
            player_tranverse(node.left)
            break
        elif choice == 'R' and 'R' in choices:
            player_tranverse(node.right)
            break
        else:
           print("Invalid choice. Try again")





class Background:
    pass

def main():

    root = LevelNode(0)
    node1 = LevelNode(1)
    node2 = LevelNode(2)
    node3 = LevelNode(3)
    node4 = LevelNode(4)
    node5 = LevelNode(5)
    node6 = LevelNode(6)
    node7 = LevelNode(7)
    node8 = LevelNode(8)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    node3.left = node7
    node3.right = node8

    print("Starting interactive transversal")
    player_tranverse(root)
    


    


if __name__ == "__main__":
    main()
