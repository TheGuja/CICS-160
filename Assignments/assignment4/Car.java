public class Car {

    private String makeAndModel;
    private int maximumNumberOfPassengers;
    private int numberOfDoors;

    public Car(String makeAndModel, int maximumNumberOfPassengers, int numberOfDoors) {
        this.makeAndModel = makeAndModel;
        this.maximumNumberOfPassengers = maximumNumberOfPassengers;
        this.numberOfDoors = numberOfDoors;
    }

    public void setMakeAndModel(String make) {
        this.makeAndModel = make;
    }

    public String getMakeAndModel() {
        return this.makeAndModel;
    }

    public void setMaximumNumberOfPassengers(int passengers) {
        this.maximumNumberOfPassengers = passengers;
    }

    public int getMaximumNumberOfPassengers() {
        return this.maximumNumberOfPassengers;
    }

    public void setNumberOfDoors(int doors) {
        this.numberOfDoors = doors;
    }

    public int getNumberOfDoors() {
        return this.numberOfDoors;
    }

    @Override
    public String toString() {
        return "Make: " + getMakeAndModel() + "\nCapacity: " + getMaximumNumberOfPassengers() + "\nNumber of Doors: " + getNumberOfDoors();
    }
}