import java.lang.reflect.Array;
import java.util.ArrayList;

public abstract class StudyRoom extends Room implements Securable, Comparable<StudyRoom>{

    private ArrayList<String> access_id = new ArrayList<>();

    public StudyRoom(String building, int number) {
        super(building, number);
    }

    public StudyRoom(String building, int number, ArrayList<String> access_id) {
        super(building, number);
        this.access_id = access_id;
    }

    @Override
    public int compareTo(StudyRoom other) {
        if (this.building.equalsIgnoreCase(other.building)) {
            return 0;
        } else {
            return this.number - other.number;
        }
    }

    public boolean hasAccess(String id) {
        if (access_id.contains(id)) {
            return true;
        }

        return false;
    }


    @Override
    public void removeAccess(String id) {
        if (access_id.contains(id)) {
            access_id.remove(access_id.indexOf(id));
        } else {
            System.out.println("This id doesn't have access.");
        }
    }

    public void addAccess(String id) {
        if (access_id.contains(id)) {
            System.out.println("This id has access already.");
        } else {
            access_id.add(id);
        }
    }
}
