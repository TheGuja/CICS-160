// package Lab.Lab 8;

class Lab8 {

    static boolean checkReply(String s, char c) {
        if (s.isEmpty()) {
            System.out.println("empty");
            return false;
        }

        char first = Character.toLowerCase(s.charAt(0));

        return Character.toLowerCase(c) == first;
    }

    public static void main(String[] args) {
        System.out.println(checkReply(" ", ' '));

    }

}
