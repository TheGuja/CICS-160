public class Car {
    private int id;
    private int powerSource;
    private float pricerPerDay;

    public Car(int id, int powerSource, float pricerPerDay) {
        this.id = id;
        this.powerSource = powerSource;
        this.pricerPerDay = pricerPerDay;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getId() {
        return this.id;
    }

    public void setPowerSource(int powerSource) {
        this.powerSource = powerSource;
    }

    public int getPowerSource() {
        return powerSource;
    }

    public void setPricerPerDay(float pricerPerDay) {
        this.pricerPerDay = pricerPerDay;
    }

    public float getPricerPerDay() {
        return pricerPerDay;
    }
}
