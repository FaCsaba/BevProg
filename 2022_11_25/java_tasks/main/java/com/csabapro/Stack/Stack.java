package Stack;

import java.util.ArrayList;
import java.util.List;

public class Stack<T> {
    List<T> internal;

    public Stack() {
        internal = new ArrayList<T>();
    }

    public Stack(List<T> init) {
        internal = init;
    }

    public boolean isEmpty() {
        return internal.isEmpty();
    }

    public void push(T item) {
        internal.add(item);
    }

    public T pop() {
        T item;
        try {
            item = internal.get(internal.size() - 1);
        } catch (IndexOutOfBoundsException e) {
            return null;
        }

        internal.remove(internal.size() - 1);

        return item;
    }

    public String toString() {
        return "[ " + internal.parallelStream().collect(StringBuilder::new, (x, y) -> x.append(y), (a,b) -> a.append(", ").append(b));
    }
}