public class CarRequests {
    private Queue<Integer> vehicleTypes;

    public CarRequests() {
        this.vehicleTypes = new Queue<>();
    }

    public void addRequest(int x) {
        this.vehicleTypes.enqueue(x);
    }

    public int getRequest() {
        return this.vehicleTypes.dequeue();
    }

    public boolean hasPendingRequests() {
        return !(this.vehicleTypes.isEmpty());
    }

}
