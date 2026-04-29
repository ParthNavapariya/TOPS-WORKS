// Create a class BankAccount with data members like balance and member functions
// like deposit and withdraw. Implement encapsulation by keeping the data members
// private.

#include<iostream>
using namespace std;
class BankAccount{
    private:
    int balance;
    
    public:
    void input(){
        cout<<"enter inital balance :";
        cin>>balance;
    } 

    void deposit(int amount){   
        balance = balance + amount;
        cout<<"deposited; "<<amount<<endl;
    }
    void withdraw(int amount){
        if(amount <= balance){
            balance = balance - amount;
            cout<<"withdraw :" <<amount<<endl;
        }
        else{
            cout<<"Insufficient balance!"<<endl;
        }
    }
    void display(){
        cout<<"eurrent balance: "<<balance<<endl;
    }
};
int main(){
    BankAccount b1;
      b1.input();       
    b1.deposit(500);  
    b1.withdraw(200);  
    b1.display();      

}
