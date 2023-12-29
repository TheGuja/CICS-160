import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

public class CarTests {

    private Car car;

    @Before
    public void setUp() {
        this.car = new Car(1, 1, 2.50f);
    }

    @Test
    public void constructor() {
        assertTrue(car.getId() == 1);
        assertTrue(car.getPowerSource() == 1);
        assertTrue(car.getPricerPerDay() == 2.50f);
        assertEquals(Car.class, car.getClass());
    }

    @Test
    public void getIdTest() {
        assertTrue(1 == car.getId());
    }

    @Test
    public void getPowerSourceTest() {
        assertTrue(1 == car.getPowerSource());
    }

    @Test
    public void getPricerPerDayTest() {
        assertEquals(2.50f, car.getPricerPerDay(), 0);
    }

    @Test
    public void setIdTest() {
        car.setId(3);
        assertTrue(3 == car.getId());
    }

    @Test
    public void setPowerSourceTest() {
        car.setPowerSource(2);
        assertTrue(2 == car.getPowerSource());
    }

    @Test
    public void setPricerPerDayTest() {
        car.setPricerPerDay(5.00f);
        assertEquals(5.00f, 5.00f, 0);
    }
}
