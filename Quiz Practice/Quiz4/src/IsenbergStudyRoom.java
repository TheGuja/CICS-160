import java.util.ArrayList;

public class IsenbergStudyRoom extends StudyRoom {

    public IsenbergStudyRoom(String building, int number) {
        super(building, number);
    }

    public IsenbergStudyRoom(String building, int number, ArrayList<String> access_id) {
        super(building, number, access_id);
    }

    @Override
    public boolean hasAccess(String id) {
        return super.hasAccess(id);
    }

    @Override
    public void removeAccess(String id) {
        super.removeAccess(id);
    }

    @Override
    public void addAccess(String id) {
        super.addAccess(id);
    }
}
