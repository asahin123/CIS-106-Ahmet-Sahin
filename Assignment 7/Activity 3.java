import java.util.*;
import java.lang.Math;

public class JavaApplication {
    private static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        // This program asks the user to select US or Metric conversion and input a given distance. Then the program converts the given distance to miles and displays the result.
        double miles;
        String choice;
        
        miles = getInputMiles();
        choice = getChoiceChar();
        if (choice.equals("U") || choice.equals("u")) {
            processUsDistance(miles);
        } else {
            if (choice.equals("M") || choice.equals("m")) {
                processMetricDistance(miles);
            } else {
                System.out.println("You must enter U to convert distance into US distance or M to convert into Metric distance!");
            }
        }
        
        // References: https://www.youtube.com/watch?v=VcZG_PxP7wQ&t=34s
    }
    
    public static String getChoiceChar() {
        String choice;
        
        System.out.println("Enter U to convert to US distance or M to convert to Metric distance.");
        choice = input.nextLine();
        
        return choice;
    }
    
    public static double getInputMiles() {
        System.out.println("Enter distance in terms of miles");
        double miles;
        
        miles = input.nextDouble();
        
        return miles;
    }
    
    public static void processMetricDistance(double miles) {
        double kilometers;
        double meters;
        double centimeters;
        
        kilometers = miles * 1.609344;
        meters = miles * 1609.344;
        centimeters = miles * 160934.4;
        System.out.println(Double.toString(miles) + " mile(s) is equivalent to " + kilometers + " km, " + meters + " m, " + centimeters + " cm");
    }
    
    public static void processUsDistance(double miles) {
        double yards;
        double feet;
        double inches;
        
        yards = miles * 1760;
        feet = miles * 5280;
        inches = miles * 63360;
        System.out.println(Double.toString(miles) + " mile(s) is equivalent to " + yards + " yards, " + feet + " ft, " + inches + " inches");
    }
}
