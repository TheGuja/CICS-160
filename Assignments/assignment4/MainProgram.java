import java.util.Scanner;

public class MainProgram {

    public static void main(String[] args) {
        FleetOfCars cars = new FleetOfCars();

        Scanner scanner = new Scanner(System.in);
        String in = "";

        while (!(in.equalsIgnoreCase("q"))) {
            System.out.print("Enter option from list below:" + "\n1) Display complete directory" + "\n2) Enter new Car" + "\n3) Search for Car" + "\n4) Modify Car information" + "\n5) Delete a record" + "\nQ) Quit" + "\nEnter your option: ");
            in = scanner.nextLine();

            if (in.equals("1")) {
                System.out.println(cars);
            } else if (in.equals("2")) {
                System.out.println("What type of car is it (Car, Gasoline, Electric)? ");
                String carObject = scanner.nextLine();
                System.out.println("What is the make and model of the car? ");
                String makeAndModel = scanner.nextLine();
                System.out.println("How many doors does your car have? ");
                int doors = scanner.nextInt();
                System.out.println("How many passengers can you seat? ");
                int maximumNumberOfPassengers = scanner.nextInt();
                scanner.nextLine();


                if (carObject.equalsIgnoreCase("Gasoline")) {
                    System.out.println("What is the gas tank size? ");
                    double gasTankSize = scanner.nextDouble();
                    scanner.nextLine();

                    cars.add(new GasolineCar(makeAndModel, doors, maximumNumberOfPassengers, gasTankSize));
                } else if (carObject.equalsIgnoreCase("Electric")) {
                    System.out.println("What is the battery size? ");
                    double batterySize = scanner.nextDouble();
                    scanner.nextLine();

                    cars.add(new ElectricCar(makeAndModel, doors, maximumNumberOfPassengers, batterySize));
                } else {
                    cars.add(new Car(makeAndModel, doors, maximumNumberOfPassengers));
                }
            } else if (in.equals("3")) {
                System.out.println("What car would you like to search for? ");
                String search = scanner.nextLine();

                System.out.println(cars.search(search));
            } else if (in.equals("4")) {
                System.out.println("What car do you want to modify?");

                String results = scanner.nextLine();

                FleetOfCars modify = cars.search(results);

                for (int modifiable = 0; modifiable < modify.getSize(); modifiable++) {
                    System.out.println(modify.get(modifiable));
                    System.out.println("Do you want to modify this car?");

                    String response_modify = scanner.nextLine();

                    if (response_modify.equalsIgnoreCase("y")) {
                        System.out.println("What is the make and model of the car? ");
                        String makeAndModel_modify = scanner.nextLine();
                        modify.get(modifiable).setMakeAndModel(makeAndModel_modify);
                        System.out.println("How many doors does your car have? ");
                        int doors_modify = scanner.nextInt();
                        modify.get(modifiable).setNumberOfDoors(doors_modify);
                        System.out.println("How many passengers can you seat? ");
                        int maximumNumberOfPassengers_modify = scanner.nextInt();
                        scanner.nextLine();
                        modify.get(modifiable).setMaximumNumberOfPassengers(maximumNumberOfPassengers_modify);
                    } else {
                        System.out.println("Car not modified.");
                    }
                }

                System.out.println(modify);

            } else if (in.equals("5")) {
                System.out.println("What index do you want to delete?");

                int index_del = scanner.nextInt();
                scanner.nextLine();

                if ((index_del >= 0) && (index_del < cars.getSize())) {

                    System.out.println(cars.get(index_del));

                    System.out.println("Do you want to delete this car?");
                    String response = scanner.nextLine();


                    if (response.equalsIgnoreCase("y")) {
                        cars.delete(index_del);
                    } else {
                        System.out.println("Car did not delete.");
                    }
                } else {
                    System.out.println("No record deleted, index out of bounds.");
                }
            }
        }

        scanner.close();

    }
}
