public abstract class Vegetation {
    private String name;

    public Vegetation(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    abstract boolean producesFruit();
}
