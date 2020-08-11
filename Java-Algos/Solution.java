
class Node {
    public int val;
    public Node left, right;

    public Node(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    public static boolean helper(Node root, Integer lower, Integer upper) {
        if (root == null) {
            return true;
        }

        int val = root.val;

        if (((lower == null) || (val > lower)) && ((upper == null) || (val < upper))) {
            if (helper(root.right, val, upper) && helper(root.left, lower, val)) {
                return true;
            } else {
                return false;
            }    
        } else {
            return false;
        }
    }

    public static boolean isValidBST(Node root) {
        if (root != null ) {
            return helper(root, null, null);
        } else {
            return true;
        }
    }

    public static void main(String[] args) {
        Node node = new Node(5);
        node.left = new Node(4);
        node.right = new Node(7);
        System.out.println(node.right.val);
        System.out.println(isValidBST(node));
    }
}
