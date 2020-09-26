import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree4
    def insert(self, value):
        # Compare target value to node.value
        if value >= self.value:
            # Go right
            # If node.right is None:
            if self.right is None:
                # Create the new node there
                self.right = BSTNode(value)
            else: # self.right is a BSTNode
                # Do the same thing (aka recurse)
                # Insert value into node.right
                # right_child is a BSTNode, so we can call insert on it
                right_child = self.right
                right_child.insert(value)
        # Else if value < node.value
        if value < self.value:
            # Go left
            # If node.left is None:
            if self.left is None:
                # Create node
                self.left = BSTNode(value)
            else: 
                # Do the same thing (aka recurse)
                # Insert value into node.left
                left_child = self.left
                left_child.insert(value)
       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if root is the target value
        if target == self.value:
            return True
        # check if target value is greater than root
        elif target > self.value:
            # If node.right is none that means we have not found the target value within our tree
            if self.right is None:
                return False
            # Repeat the process
            else:
                return self.right.contains(target)
        else:
            # check if target value is smaller than root
            if target < self.value:
                # If node.left is none that means we have not found the target value within our tree
                if self.left is None:
                    return False
                # Repeat the process
                else:
                    return self.left.contains(target)

bst = BSTNode("")

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
