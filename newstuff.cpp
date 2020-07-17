#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// int main() 
// {
//     int x, y, answer;
//     string calc;
//     cout << "Hello Human!" << endl;
//     cout << "Type a number: ";
//     cin >> x;
//     cout << "Type another number: ";
//     cin >> y;

//     do
//     {
//         cout << "Enter evaluation: ";
//         cin >> calc;
//     }
//     while ((calc == "sum") && (calc == "minus") && (calc == "divide") && (calc == "multi"));

//     if (calc == "sum")
//     {
//         answer = x + y;
//     }
//     else if (calc == "minus")
//     {
//         answer = x - y;
//     }
//     else if (calc == "divide")
//     {
//         answer = x / y;
//     }
//     else if (calc == "multi")
//     {
//         answer = x * y;
//     }        

//     cout << "Answer is: " << answer << endl;
// }

// int main()
// {
//     string credit;
//     cout << "Enter credit card Number" << endl;
//     cin >> credit;
//     cout << "The length of the credit card is: " << credit.length();
// }

// int main()
// {
//     string hello = "Hello!";
//     cout << hello.substr(0,4) << endl;
//     cout << hello[0];
// }

// int main()
// {
//     string name;
//     cout << "Enter full name" << endl;
//     getline(cin, name);
//     cout << "Your full name is " << name; 
// }

// int main()
// {
//     string myString = "Hello";
//     myString[0] = 'J';
//     cout << myString;
// }

// int main()
// {
//     int i = 0;
//     // while (i < 10){
//     //     cout << i << endl;
//     //     i++;
//     // }    
//     for (i; i < 10; i++)
//     {
//         if (i == 5)
//         {
//             cout << "lazy" << endl;
//             continue;            
//         }
//         cout << i << endl;
//     }    
// }

// int main()
// {
//     int i = 0;
//     do
//     {        
//         if (i == 5)
//         {
//             i++;
//             continue;
//         }
//         cout << i << endl;
//         i++;
//     } 
//     while (i < 10);
    
// }

// int main()
// {
//     string cars[4];
//     cout << "Enter car names: ";
//     //getline(cin, cars[4]);
//     cin >> cars[0] >> cars[1] >> cars[2] >> cars[3];
//     //cars[4] = {"Volvo", "Baby", "Clark", "Fatty"};
//     for (int i = 0; i < 4; i++)
//     {
//         if (i == 3)
//         {
//             cout << i << ":Hello World" << endl;
//             continue;
//         }
//         cout << i << ":" << cars[i] << endl;
//     }
// }

// string hello(string x)
// {
//     return ("Hello " + x); 
// }

// int main()
// {
//     string bat = hello("david");
//     cout << bat << endl;
// }

// void swapNums(int &x, int &y) {
//   int z = x;
//   x = y;
//   y = z;
// }

// int main() {
//   int firstNum = 10;
//   int secondNum = 20;

//   cout << "Before swap: " << "\n";
//   cout << firstNum << secondNum << "\n";

//   // Call the function, which will change the values of firstNum and secondNum
//   swapNums(firstNum, secondNum);

//   cout << "After swap: " << "\n";
//   cout << firstNum << secondNum << "\n";

//   return 0;
// }

// class Car {
//     public:
//     string brand;
//     string model;
//     int year;
// };

// int main()
// {
//     Car carobj;
//     carobj.brand = "BMW";
//     carobj.model = "X5";
//     carobj.year = 1995;

//     Car carobj2;
//     carobj2.brand = "Mercedez";
//     carobj2.model = "C-class";
//     carobj2.year = 2002;

//     cout << carobj.brand << " " << carobj.model << " " << carobj.year << endl;
//     cout << carobj2.brand << " " << carobj2.model << " " << carobj2.year << endl;
// }

int convert2AM(int hour);

int main()
{
    int hour; string AMPM; string den;
    cout << "Input time: ";
    cin >> hour;
    int a = convert2AM(hour);
    if (hour < 12)
    {
        den = "AM";
    }
    else if (hour == 24)
    {
        den = "AM";
    }
    else
    {
        den = "PM";
    }
    
    cout << a << den << endl;
}

int convert2AM(int hour)
{
    int time;
    if (hour < 12)
    {
        time = hour;
    }
    else if (hour >= 12)
    {
        time = hour - 12;
    }
    return time;    
}