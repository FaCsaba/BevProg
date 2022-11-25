package Stack;

public class TestingStack {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<Integer>();
        s.push(1);
        s.push(5);
        s.push(9);
        s.push(7);
        System.out.println(s.toString());
        System.out.println("Popped: " + s.pop());
        System.out.println(s.toString());
        System.out.println("Is empty: " + s.isEmpty());
        s.pop();
        s.pop();
        s.pop();
        s.pop();
        s.pop();
        System.out.println("Popped: " + s.pop());
        System.out.println("Is empty: " + s.isEmpty());
    }
}