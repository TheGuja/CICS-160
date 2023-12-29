import java.util.ArrayList;

public class Queue<T> {
    private ArrayList<T> queue;

    public Queue() {
        this.queue = new ArrayList<T>();
    }

    public void enqueue(T e) {
        this.queue.add(e);
    }

    public T dequeue() {
        if (this.queue.isEmpty()) {
            return null;
        }

        return this.queue.remove(0);
    }

    public boolean isEmpty() {
        return this.queue.isEmpty();
    }

    public T peek() {
        if (this.queue.isEmpty()) {
            return null;
        }

        return this.queue.get(0);
    }
}
