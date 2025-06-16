package practice;

public class Main {
	public static void main(String[] args) {
        Shape circle = new Circle("Red", 5.5);
        Shape rectangle = new Rectangle("Blue", 10.0, 4.0);

        System.out.println(circle.toString());
        System.out.println("Area: " + circle.area());
        System.out.println(rectangle.toString());
        System.out.println("Area: " + rectangle.area());
    }
}
