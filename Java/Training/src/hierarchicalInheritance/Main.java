package hierarchicalInheritance;

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();  // From Animal
        dog.bark(); // From Dog

        Cat cat = new Cat();
        cat.eat();  // From Animal
        cat.meow(); // From Cat
    }
}