import java.util.ArrayList;

public abstract class Tree extends Vegetation implements Localizable, Comparable<Tree> {
    private float height;

    public Tree(String name, float height) {
        super(name);
        this.height = height;
    }

    public void setHeight(float height) {
        this.height = height;
    }

    public float getHeight() {
        return this.height;
    }

    @Override
    public boolean producesFruit() {
        return false;
    }

    @Override
    public ArrayList<Integer> getLocation() {
        ArrayList<Integer> location = new ArrayList<>();
        location.add(0);
        location.add(0);

        return location;
    }

    @Override
    public int compareTo(Tree otherTree) {
        if (this.height < otherTree.height) {
            return -1;
        } else if (this.height > otherTree.height) {
            return 1;
        } else {
            return 0;
        }
    }
}
