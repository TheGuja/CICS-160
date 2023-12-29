public class GasolineCar extends Car {

    private double gasTankSize;
    public GasolineCar(String makeAndModel, int maximumNumberOfPassengers, int numberOfDoors, double gasTankSize) {
        super(makeAndModel, maximumNumberOfPassengers, numberOfDoors);
        this.gasTankSize = gasTankSize;
    }

    public void setGasTankSize(double g) {
        this.gasTankSize = g;
    }

    public double getGasTankSize() {
        return this.gasTankSize;
    }

    @Override
    public String toString() {
        return super.toString() + "\nGas Tank Size: " + String.valueOf(getGasTankSize());
    }
}
