package practice;

public abstract class Shape {
	private String color;

    // Constructor
    public Shape(String color) {
        this.color = color;
    }

    // Getter for color
    public String getColor() {
        return color;
    }

    // Abstract method toString
    public abstract String toString();
    public abstract double area();
}
