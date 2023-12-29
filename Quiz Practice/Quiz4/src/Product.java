public abstract class Product {
    protected String productName;
    protected double price;

    public Product(String product, double price) {
        this.productName = product;
        this.price = price;
    }
}
