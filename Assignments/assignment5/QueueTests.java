import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;

import org.junit.Before;
import org.junit.Test;

public class QueueTests {

    private Queue<Integer> testQueue;

    @Before
    public void setUp() {
        this.testQueue = new Queue<>();
        testQueue.enqueue(2);
        testQueue.enqueue(5);
    }

    @Test
    public void constructorTest() {
        assertEquals(Queue.class, testQueue.getClass());
        assertTrue(testQueue.peek() == 2);
    }

    @Test
    public void enqueueTest() {
        ArrayList<Integer> expected = new ArrayList<>();
        ArrayList<Integer> actual = new ArrayList<>();

        expected.add(2);
        expected.add(5);

        actual.add(testQueue.dequeue());
        actual.add(testQueue.dequeue());

        assertArrayEquals(expected.toArray(), actual.toArray());

    }

    @Test
    public void dequeueTest() {
        assertTrue(2 == testQueue.dequeue());
    }

    @Test
    public void dequeueEmptyTest() {
        testQueue.dequeue();
        testQueue.dequeue();

        assertNull(testQueue.dequeue());
    }

    @Test
    public void peekEmptyTest() {
        testQueue.dequeue();
        testQueue.dequeue();

        assertNull(testQueue.peek());
    }

    @Test
    public void peekTest() {
        assertTrue(2 == testQueue.peek());
    }

    @Test
    public void isEmptyTestFalse() {
        assertTrue(false == testQueue.isEmpty());
    }

    @Test
    public void isEmptyTestTrue() {
        testQueue.dequeue();
        testQueue.dequeue();

        assertTrue(true == testQueue.isEmpty());
    }
}
