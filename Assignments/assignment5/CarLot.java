import java.util.ArrayList;

public class CarLot {
    protected Queue<Car> gasoline;
    protected Queue<Car> hybrid;
    protected Queue<Car> electric;

    public CarLot() {
        this.gasoline = new Queue<>();
        this.hybrid = new Queue<>();
        this.electric = new Queue<>();
    }

    public boolean addCar(Car car) {
        if (car.getPowerSource() == 1) {
            gasoline.enqueue(car);
            return true;
        } else if (car.getPowerSource() == 2) {
            hybrid.enqueue(car);
            return true;
        } else if (car.getPowerSource() == 3) {
            electric.enqueue(car);
            return true;
        }

        return false;
    }

    public ArrayList<Car> processRequests(CarRequests requests) {
        ArrayList<Car> output = new ArrayList<>();

        while (requests.hasPendingRequests()) {
            int currentRequest = requests.getRequest();

            if (currentRequest == 1) {
                if (this.gasoline.isEmpty()) {
                    output.add(new Car(0, 1, 0.00f));
                } else {
                    output.add(this.gasoline.dequeue());
                }
            } else if (currentRequest == 2) {
                if (this.hybrid.isEmpty()) {
                    System.out.println("empty");
                    output.add(new Car(0, 2, 0.00f));
                } else {
                    System.out.println("not empty");
                    output.add(this.hybrid.dequeue());
                }
            } else if (currentRequest == 3) {
                if (this.electric.isEmpty()) {
                    output.add(new Car(0, 3, 0.00f));
                } else {
                    output.add(this.electric.dequeue());
                }
            }
        }

        return output;
    }
}
