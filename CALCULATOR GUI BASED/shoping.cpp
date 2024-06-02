#include <iostream>
#include <fstream>
using namespace std;

class shopping
{
private:
    int pcode;
    float price;
    float dis;
    string pname;

public:
    void menu();
    void administrator();
    void buyer();
    void add();
    void edit();
    void remove();
    void list();
    void receipt();
};

using namespace std;
void shopping ::menu()
{
    int choice;
    string email;
    string password;

    cout << "super market main menu" << endl;
    cout << "1 administrator" << endl;
    cout << "2 buyer" << endl;
    cout << "3 exit" << endl;

    cout << "please select";
    cin >> choice;

    switch (choice)
    {
    case 1:
        cout << "please login" << endl;
        cout << "enter email" << endl;
        cin >> email;
        cout << "enter password" << endl;
        cin >> password;

        if (email == "dimplemishra689@gmail.com" && password == "juhimishra")
        {
            administrator();
        }
        else
        {
            cout << "wrong email/password";
        }
        break;

    case 2:
    {
        buyer();
    }
    case 3:
    {
        exit(0);
    }
    default:
    {
        cout << "please select given option";
        break;
    }
    }
}

void shopping ::administrator()
{
m:
    int choice;
    cout << "administrator" << endl;
    cout << "1 add the product" << endl;
    cout << "2 modify the product" << endl;
    cout << "3 delet the product" << endl;
    cout << "4 go to main menu" << endl;

    cout << "enter your choice";
    cin >> choice;

    switch (choice)
    {
    case 1:
        add();
        break;

    case 2:
        edit();
        break;

    case 3:
        remove();
        break;

    case 4:
        menu();
        break;

    default:
        cout << "wrong choice";
    }
    goto m;
}
void shopping ::buyer()
{
m:
    int choice;
    cout << "buyer" << endl;
    cout << "1 buy product" << endl;
    cout << "2 go back" << endl;
    cout << "enter choice";
    cin >> choice;

    switch (choice)
    {
    case 1:
        receipt();
        break;
    case 2:
        menu();
        break;
    default:
        cout << "wrong choice" << endl;
    }
    goto m;
}
void shopping ::add()
{
m:
    fstream data;
    int p;
    int token = 0;
    string n;
    float c;
    float d;
    cout << "add new product" << endl;
    cout << "code of product" << endl;
    cin >> p;
    cout << "name of product" << endl;
    cin >> n;
    cout << "price of product" << endl;
    cin >> c;
    cout << "dicount of product" << endl;
    cin >> d;

    data.open("database.txt", ios::in);
    if (!data)
    {
        data.open("database.txt", ios::app | ios::out);
        data << " " << p << " " << n << " " << c << " " << d << endl;
        data.close();
    }
    else
    {
        data >> p >> c >> n >> d;
        while (!data.eof())
        {
            if (c == pcode)
            {
                token++;
            }
            data >> c >> n >> p >> d;
        }
        data.close();

        if (token == 1)
            goto m;
        else
        {
            data.open("database.txt", ios::app | ios::out);
            data << " " << pname << " " << pcode << " " << price << " " << dis << endl;
            data.close();
        }
    }
    cout << "record inserted"
         << endl;
}
void shopping::edit()
{
    fstream data, data1;
    int pkey;
    int token = 0;
    int c;
    float p;
    float d;
    string n;
    string pname;

    cout << "modify the record" << endl;
    cout << "product code" << endl;
    cin >> pkey;

    data.open("database", ios::in);
    if (data)
    {
        cout << "file not exist" << endl;
    }
    else
    {
        data1.open("database1.txt", ios::app | ios::out);
        data >> pcode >> pname >> price >> dis;
        while (!data.eof())
        {
            if (pkey == pcode)
            {
                cout << "product new code" << endl;
                cin >> c;
                cout << "name of product" << endl;
                cin >> pname;
                cout << "priceof product" << endl;
                cin >> p;
                cout << "discount" << endl;
                cin >> d;
                data1 << " " << c << " " << pname << " " << p << " " << d << endl;
                cout << "edited";
                token++;
            }
            else
            {
                data1 << " " << pcode << " " << pname << " " << price << " " << dis << endl;
            }
            data >> pcode >> pname >> price >> dis;
        }
        data.close();
        data1.close();

        remove();
        rename("database1.txt", "database.txt");

        if (token == 0)
        {
            cout << "record not found ";
        }
    }
}
void shopping::remove()
{
    fstream data, data1;
    int pkey;
    int token = 0;
    cout << "delete product";
    cout << "product code" << endl;
    cin >> pkey;
    data.open("database.txt", ios::in);
    if (!data)
    {
        cout << "file does not exist" << endl;
    }
    else
    {
        data1.open("database1.txt", ios::app | ios::out);
        data >> pcode >> pname >> price >> dis ;
        cout<<endl; 
        while (!data.eof())
        {
            if (pcode == pkey)
            {
                cout << "product delete successfully";
                token++;
            }
            else
            {
                data << " " << pcode << " " << pname << " " << price << " " << dis << endl;
            }
            data >> pcode >> pname >> price >> dis;
        }
        data.close();
        data1.close();
        remove();
        rename("database1.txt", "database.txt");

        if (token == 0)
        {
            cout << "record not found";
        }
    }
}
void shopping::list()
{
    fstream data;
    data.open("database.txt", ios::in);
    cout << "pcode,pname,price,discount" << endl;
    data >> pcode >> pname >> price >> dis;
    while (!data.eof())
    {
        cout << pcode << "" << pname << "" << price << "" << dis << endl;
        data >> pcode >> pname >> price >> dis;
    }
    data.close();
}
void shopping ::receipt()
{
    fstream data;

    int arrc[100];
    int arrq[100];
    char choice;
    int c = 0;
    float amount;
    float dis = 0;
    float total = 0;

    cout << "receipt" << endl;
    data.open("databae.txt", ios::in);
    if (!data)
    {
        cout << "empty database" << endl;
    }
    else
    {
        data.close();

        list();
        cout << "please place order" << endl;
        do
        {
        m:
            cout << "enter product code" << endl;
            cin >> arrc[c];
            cout << "enter product quantity" << endl;
            cin >> arrq[c];
            for (int i = 0; i < c; i++)
            {
                if (arrc[c == arrc[i]])
                {
                    cout << "duplicate product" << endl;
                    goto m;
                }
            }
            c++;
            cout << "do you want to buy another if yes then a else b";
            cin >> choice;
        }while (choice == 'a');
        cout << "receipt" << endl;
        cout << "pno, pname,pquantity,price,discount" << endl;

        for (int i = 0; i < c; i++)
        {
            data.open("database.txt", ios::in);
            data >> pcode >> pname >> price >> dis;
            while (!data.eof())
            {
                if (pcode == arrc[i])
                {
                    amount = price * arrq[i];
                    dis = amount - (amount * dis / 100);
                    total = total + dis;
                    cout << " " << pcode << " " << pname << " " << price << " " << dis << endl;
                }
                data >> pcode >> pname >> price >> dis;
            }
        }
        data.close();
    }
    cout << "total amount" << total;
}

int main()
{
    shopping s;
    s.menu();
}