package practice;

public class Rectangle extends Shape {
    private double length;
    private double width;

    // Constructor
    public Rectangle(String color, double length, double width) {
        super(color);
        this.length = length;
        this.width = width;
    }

    // Getters for length and width
    public double getLength() {
        return length;
    }

    public double getWidth() {
        return width;
    }

    @Override
    public String toString() {
        return "Rectangle[color=" + getColor() + ", length=" + length + ", width=" + width + "]";
    }

	@Override
	public double area() {
		// TODO Auto-generated method stub
		return length * width;
	}
}
