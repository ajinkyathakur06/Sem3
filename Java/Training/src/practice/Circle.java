package practice;

public class Circle extends Shape {
    private double radius;

    // Constructor
    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    // Getter for radius
    public double getRadius() {
        return radius;
    }

    @Override
    public String toString() {
        return "Circle[color=" + getColor() + ", radius=" + radius + "]";
    }

	@Override
	public double area() {
		// TODO Auto-generated method stub
		return Math.PI * radius * radius;
	}
}