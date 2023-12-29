import java.util.ArrayList;

public class FleetOfCars {
    private ArrayList<Car> cars;
    private int items;

    public FleetOfCars() {
        this.cars = new ArrayList<Car>();
        this.items = 0;
    }

    public void add(Car car) {
        this.cars.add(car);
        this.items++;
    }

    public void delete(int index) {
        if ((this.getSize() == 0) || (index > this.getSize() - 1) || (index < 0)) {
            return;
        }

        this.cars.remove(index);
        this.items--;
    }

    public int getSize() {

        return this.items;
    }

    public Car get(int i) {

        return this.cars.get(i);
    }

    public FleetOfCars search(String s) {
        FleetOfCars search = new FleetOfCars();
        for (int i = 0; i < this.items; i++) {
            if (this.cars.get(i).getMakeAndModel().equalsIgnoreCase(s)) {
                search.add(get(i));
            }
        }

        return search;
    }

    @Override
    public String toString() {
        String stringToReturn = "";
        for (int i = 0; i < this.items; i++) {
            if (this.cars.get(i) instanceof ElectricCar) {
                stringToReturn = stringToReturn + "\nMake: " + this.cars.get(i).getMakeAndModel() + "\nCapacity: " + this.cars.get(i).getMaximumNumberOfPassengers() + "\nNumber of Doors: " + this.cars.get(i).getNumberOfDoors() + "\nBattery Size: " + ((ElectricCar) this.cars.get(i)).getBatterySize() + "\n";
            } else if (this.cars.get(i) instanceof GasolineCar) {
                stringToReturn = stringToReturn + "\nMake: " + this.cars.get(i).getMakeAndModel() + "\nCapacity: " + this.cars.get(i).getMaximumNumberOfPassengers() + "\nNumber of Doors: " + this.cars.get(i).getNumberOfDoors() + "\nBattery Size: " + ((GasolineCar) this.cars.get(i)).getGasTankSize() + "\n";
            } else {
                stringToReturn = stringToReturn + "\nMake: " + this.cars.get(i).getMakeAndModel() + "\nCapacity: " + this.cars.get(i).getMaximumNumberOfPassengers() + "\nNumber of Doors: " + this.cars.get(i).getNumberOfDoors() + "\n";
            }
        }

        return stringToReturn;
    }

    public static void main(String[] args) {
        FleetOfCars cars = new FleetOfCars();
        Car car1 = new Car("Car1", 4, 5);
        Car car2 = new Car("Car2", 4, 5);
        Car car3 = new Car("Car3", 4, 5);

        // test for add method
        cars.add(car1);
        // should print car1
        System.out.println(cars);

        cars.add(car2);
        cars.add(car3);
        // should print car1, car2, and car3
        System.out.println(cars);

        // test for delete method
        cars.delete(1);
        // should print car1 and car3
        System.out.println(cars);

        cars.delete(4);
        // should not delete anything, should print car1 and car3
        System.out.println(cars);

        cars.delete(-1);
        // should not delete anything, should print car1 and car3
        System.out.println(cars);

        cars.delete(1);
        cars.delete(0);
        // should print nothing since all cars are now deleted
        System.out.println(cars);

        cars.delete(0);
        // should print nothing
        System.out.println(cars);
    }
}
