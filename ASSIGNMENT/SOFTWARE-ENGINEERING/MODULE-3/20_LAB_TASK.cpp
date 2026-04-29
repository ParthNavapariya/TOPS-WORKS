// 3. Inheritance Example
// o Write a program that implements inheritance using a base class Person and derived
// classes Student and Teacher. Demonstrate reusability through inheritance.
// o Objective: Learn the concept of inheritance

#include<iostream>
using namespace std;

// Base class
class Person {
    protected:
    string name;
    int age;

    public:
    void inputPerson() {
        cout << "Enter name: ";
        cin >> name;
        cout << "Enter age: ";
        cin >> age;
    }

    void displayPerson() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

// Derived class - Student
class Student : public Person {
    private:
    int marks;

    public:
    void inputStudent() {
        inputPerson();  // reuse base class function
        cout << "Enter marks: ";
        cin >> marks;
    }

    void displayStudent() {
        displayPerson();  // reuse base class function
        cout << "Marks: " << marks << endl;
    }
};

// Derived class - Teacher
class Teacher : public Person {
    private:
    int salary;

    public:
    void inputTeacher() {
        inputPerson();  // reuse base class function
        cout << "Enter salary: ";
        cin >> salary;
    }

    void displayTeacher() {
        displayPerson();  // reuse base class function
        cout << "Salary: " << salary << endl;
    }
};

int main() {
    Student s;
    Teacher t;

    cout << "\n--- Student Details ---\n";
    s.inputStudent();
    s.displayStudent();

    cout << "\n--- Teacher Details ---\n";
    t.inputTeacher();
    t.displayTeacher();

    return 0;
}