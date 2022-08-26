<h3> Binary Search Tree </h3>

-> A binary tree is a tree whose elements can have atmost two children. Since each element in a binary tree can have only 2 children, we typically name them the left and right children. 

-> A Binary Tree node contains the following parts.
<ul>
<li> Data </li>
<li> Pointer to left child </li>
<li> Pointer to the right child </li>
</ul>

-> The left subtree of a node contains only nodes with keys lesser than the node’s key.
-> The right subtree of a node contains only nodes with keys greater than the node’s key.
-> The left and right subtree each must also be a binary search tree.
-> BST is fast in insertion and deletion when balanced.

<h3> Searching Element </h3>

-> Start from the root.
-> Compare the searching element with root, if less than root, then recurse for left, else recurse for right.
-> If the element to search is found anywhere, return true, else return false.

<h3> Insertion of a key  </h3>

-> Start from the root.
-> Compare the inserting element with root, if less than root, then recurse for left, else recurse for right.
-> After reaching the end, just insert that node at left(if less than current) else right.