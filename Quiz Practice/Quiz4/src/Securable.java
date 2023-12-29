public interface Securable {
    public boolean hasAccess(String id);

    public void removeAccess(String id);

    public void addAccess(String id);
}
