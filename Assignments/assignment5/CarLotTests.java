import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;

import org.junit.Before;
import org.junit.Test;

public class CarLotTests {
    private CarLot lotTest;

    @Before
    public void setUp() {
        this.lotTest = new CarLot();
    }

    @Test
    public void constructorCarLotTest() {
        assertEquals(CarLot.class, lotTest.getClass());
    }

    @Test
    public void addCarTrueTest() {
        assertTrue(true == lotTest.addCar(new Car(1, 1, 5.00f)));
        assertTrue(true == lotTest.addCar(new Car(2, 2, 2.50f)));
        assertTrue(true == lotTest.addCar(new Car(3, 3, 2.00f)));
    }

    @Test
    public void addCarFalseTest() {
        assertTrue(false == lotTest.addCar(new Car(4, 0, 2.50f)));
        assertTrue(false == lotTest.addCar(new Car(5, 4, 2.50f)));
    }

    @Test
    public void addCarGasolineTest() {
        lotTest.addCar(new Car(1, 1, 5.00f));
        lotTest.addCar(new Car(2, 1, 5.00f));

        ArrayList<Integer> expected = new ArrayList<>();
        ArrayList<Integer> actual = new ArrayList<>();

        expected.add(1);
        expected.add(2);

        actual.add(lotTest.gasoline.dequeue().getId());
        actual.add(lotTest.gasoline.dequeue().getId());

        assertArrayEquals(expected.toArray(), actual.toArray());
    }

    @Test
    public void addCarHybridTest() {
        lotTest.addCar(new Car(3, 2, 2.50f));
        lotTest.addCar(new Car(4, 2, 2.50f));

        ArrayList<Integer> expected = new ArrayList<>();
        ArrayList<Integer> actual = new ArrayList<>();

        expected.add(3);
        expected.add(4);

        actual.add(lotTest.hybrid.dequeue().getId());
        actual.add(lotTest.hybrid.dequeue().getId());

        assertArrayEquals(expected.toArray(), actual.toArray());
    }

    @Test
    public void addCarElectricTest() {
        lotTest.addCar(new Car(5, 3, 2.00f));
        lotTest.addCar(new Car(6, 3, 2.00f));

        ArrayList<Integer> expected = new ArrayList<>();
        ArrayList<Integer> actual = new ArrayList<>();

        expected.add(5);
        expected.add(6);

        actual.add(lotTest.electric.dequeue().getId());
        actual.add(lotTest.electric.dequeue().getId());

        assertArrayEquals(expected.toArray(), actual.toArray());
    }

    @Test
    public void processRequestsAllAvailable() {
        lotTest.addCar(new Car(1, 1, 5.00f));
        lotTest.addCar(new Car(2, 1, 5.00f));
        lotTest.addCar(new Car(3, 2, 2.50f));
        lotTest.addCar(new Car(4, 2, 2.50f));
        lotTest.addCar(new Car(5, 3, 2.00f));
        lotTest.addCar(new Car(6, 3, 2.00f));

        CarRequests request = new CarRequests();
        request.addRequest(1);
        request.addRequest(2);
        request.addRequest(2);
        request.addRequest(3);

        ArrayList<Car> output = lotTest.processRequests(request);

        assertTrue((1 == output.get(0).getId()) && (1 == output.get(0).getPowerSource())
                && (output.get(0).getPricerPerDay() == 5.00f));
        assertTrue((3 == output.get(1).getId()) && (2 == output.get(1).getPowerSource())
                && (output.get(1).getPricerPerDay() == 2.50f));
        assertTrue((4 == output.get(2).getId()) && (2 == output.get(2).getPowerSource())
                && (output.get(2).getPricerPerDay() == 2.50f));
        assertTrue((5 == output.get(3).getId()) && (3 == output.get(3).getPowerSource())
                && (output.get(3).getPricerPerDay() == 2.00f));
    }

    @Test
    public void processRequestsSomeNotAvailable() {
        lotTest.addCar(new Car(1, 1, 5.00f));
        lotTest.addCar(new Car(2, 1, 5.00f));
        lotTest.addCar(new Car(3, 2, 2.50f));
        lotTest.addCar(new Car(4, 2, 2.50f));
        lotTest.addCar(new Car(5, 3, 2.00f));
        lotTest.addCar(new Car(6, 3, 2.00f));

        CarRequests request = new CarRequests();
        request.addRequest(1);
        request.addRequest(1);
        request.addRequest(2);
        request.addRequest(2);
        request.addRequest(1);
        request.addRequest(3);
        request.addRequest(2);

        ArrayList<Car> output = lotTest.processRequests(request);

        assertTrue((1 == output.get(0).getId()) && (1 == output.get(0).getPowerSource())
                && (output.get(0).getPricerPerDay() == 5.00f));
        assertTrue((2 == output.get(1).getId()) && (1 == output.get(0).getPowerSource())
                && (output.get(1).getPricerPerDay() == 5.00f));
        assertTrue((3 == output.get(2).getId()) && (2 == output.get(2).getPowerSource())
                && (output.get(2).getPricerPerDay() == 2.50f));
        assertTrue((4 == output.get(3).getId()) && (2 == output.get(3).getPowerSource())
                && (output.get(3).getPricerPerDay() == 2.50f));
        assertTrue(0 == output.get(4).getId());
        assertTrue((5 == output.get(5).getId()) && (3 == output.get(5).getPowerSource())
                && (output.get(5).getPricerPerDay() == 2.00f));
        assertTrue(0 == output.get(6).getId());
    }

}
