public abstract class ElectronicProduct extends Product implements Discountable{
    public ElectronicProduct(String product, double price) {
        super(product, price);
    }

    @Override
    public double findDiscount(double discountPercentage) {
        return (this.price * (1 - discountPercentage));
    }

    @Override
    public void resetPrice() {
        return;
    }
}
