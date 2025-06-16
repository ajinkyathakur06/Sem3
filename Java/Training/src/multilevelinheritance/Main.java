package multilevelinheritance;

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();  // From Animal
        dog.walk(); // From Mammal
        dog.bark(); // From Dog
    }
}