package lib;

import java.util.ArrayList;

public class Main {
        public static void main(String[] args) {
                Car gasoline1 = new Car(1, 1, 5.00f);
                Car gasoline2 = new Car(2, 1, 5.00f);
                Car gasoline3 = new Car(3, 1, 5.00f);
                Car gasoline4 = new Car(4, 1, 5.00f);
                Car gasoline5 = new Car(5, 1, 5.00f);
                Car gasoline6 = new Car(6, 1, 5.00f);
                Car gasoline7 = new Car(7, 1, 5.00f);
                Car gasoline8 = new Car(8, 1, 5.00f);
                Car gasoline9 = new Car(9, 1, 5.00f);

                Car hybrid1 = new Car(1, 2, 2.00f);
                Car hybrid2 = new Car(2, 2, 2.00f);
                Car hybrid3 = new Car(3, 2, 2.00f);
                Car hybrid4 = new Car(4, 2, 2.00f);
                Car hybrid5 = new Car(5, 2, 2.00f);
                Car hybrid6 = new Car(6, 2, 2.00f);
                Car hybrid7 = new Car(7, 2, 2.00f);
                Car hybrid8 = new Car(8, 2, 2.00f);
                Car hybrid9 = new Car(9, 2, 2.00f);

                Car electric1 = new Car(1, 3, 1.00f);
                Car electric2 = new Car(2, 3, 1.00f);
                Car electric3 = new Car(3, 3, 1.00f);
                Car electric4 = new Car(4, 3, 1.00f);
                Car electric5 = new Car(5, 3, 1.00f);
                Car electric6 = new Car(6, 3, 1.00f);
                Car electric7 = new Car(7, 3, 1.00f);
                Car electric8 = new Car(8, 3, 1.00f);
                Car electric9 = new Car(9, 3, 1.00f);

                CarLot lot = new CarLot();
                lot.addCar(gasoline1);
                lot.addCar(gasoline2);
                // lot.addCar(gasoline3);
                // lot.addCar(gasoline4);
                // lot.addCar(gasoline5);
                // lot.addCar(gasoline6);
                // lot.addCar(gasoline7);
                // lot.addCar(gasoline8);
                // lot.addCar(gasoline9);
                lot.addCar(hybrid1);
                // lot.addCar(hybrid2);
                // lot.addCar(hybrid3);
                // lot.addCar(hybrid4);
                // lot.addCar(hybrid5);
                // lot.addCar(hybrid6);
                // lot.addCar(hybrid7);
                // lot.addCar(hybrid8);
                // lot.addCar(hybrid9);
                lot.addCar(electric1);
                // lot.addCar(electric2);
                // lot.addCar(electric3);
                // lot.addCar(electric4);
                // lot.addCar(electric5);
                // lot.addCar(electric6);
                // lot.addCar(electric7);
                // lot.addCar(electric8);
                // lot.addCar(electric9);

                CarRequests requests = new CarRequests();
                requests.addRequest(1);
                requests.addRequest(1);
                requests.addRequest(2);
                requests.addRequest(3);
                // requests.addRequest(3);
                // requests.addRequest(2);
                // requests.addRequest(1);
                //
                System.out.println(lot.processRequests(requests));

        }
}
