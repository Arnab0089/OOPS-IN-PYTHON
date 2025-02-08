#include<iostream>
using namespace std;

class Student{
    public:
    string name;
    int age;
    bool gender;

   void printInfo(){
       cout<<"Name = ";
       cout<<name<<endl;
       cout<<"Age = ";
       cout<<age<<endl;
       cout<< "Gender = ";
        cout<<gender<<endl;
    }
};

int main(){
    Student a;
    a.name = "Rahul";
    a.age = 21;
    a.gender  = 1;

    a.printInfo();

//    array of objects
    Student arr[3];
    for(int i=0;i<3;i++){
        cout<<"Name = ";
        cin>>arr[i].name;
        cout<<"Age = ";
        cin>>arr[i].age;
        cout<<"GENDER = ";
        cin>>arr[i].gender;
    }
    for(int i=0;i<3;i++){
        arr[i].printInfo();
    }
    return 0;
}