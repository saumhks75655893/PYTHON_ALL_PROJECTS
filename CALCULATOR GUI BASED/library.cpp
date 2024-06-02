#include <iostream>
#include <mysql.h>
#include <mysqld_error.h>
#include <window.h>
#include <sstream>

const char *host = "localhost";
const char *user = "root";
const char *passward = " ";
const char *database = "db";

class student
{
private:
    srting id;

public:
    student() : id("") {}

    void setid(string id)
    {
        id = myid;
    }

    string getid()
    {
        return id;
    }
};
class library
{
private:
    string name;
    int quantity;

public:
    library() : name(""), quantity(0) {}

    void setname(string name)
    {
        name = myname;
    }
    void setquantity(int quantity)
    {
        quantity = quant;
    }
    void setname()
    {
        return name;
    }
    void setquantity()
    {
        return quantity;
    }
};
void admin(mysql *conn, library 1, student s)
{
    bool closed = false;
    while (!closed)
    {
        int choice;
        cout << "1.add book" << endl;
        cout << "2.add student" << endl;
        cout << "0.exist" << endl;
        cout << "enter choice";
        cin >> choice;

        if (choice == 1)
        {
            system("cls");
            string name;
            int quant;
            cout << "book name : ";
            cin >> name;
            l.setname(name);

            cout << "enter quantity : ";
            cin >> quant;
            l.setquantity(quant);

            int iq = l.getqunatity();
            stringstream ss;
            ss << iq;
            string sq = ss.str();

            strin book = "insert into lib(name,quantity)values('" + l.getname() + "','" + l.sq() + "')";
            if (mysql_query(conn, book.c_str()))
            {
                cout << "error" << mysql_error(conn) << endl;
            }
            else
            {
                cout << "book insertrd successfully" << endl;
            }
        }
        else if (choice == 2)
        {
            system("cls");
            string myid;
            cout << "enter student myid";
            cin >> myid;
            s.setid(myid);
            string st = "insert into student(id) values('" + s.getid + "')";

            if (mysql_query(conn, st.c_str()))
            {
                cout << "error" << mysql_error(conn) << endl;
            }
            else
            {
                cout << "student insertrd successfully" << endl;
            }
        }
        else if (choice == 0)
        {
            closed == true;
            cout << "system is closing" << endl;
        }
    }
    sleep(3000);
}
void display(mysql *conn)
{
    system("cls")
            cout
        << "available book" << endl;
    cout << "*" << endl;

    string disp = "select * from lib";
    if (mysql_query(conn, disp.c_str()))
    {
        cout << "error" << mysql_error(conn) << endl;
    }
    else
    {
        mysql_result *res;
        res = mysql_store_result(conn);
        if (res)
        {
            int num = mysql_num_fields(res);
            mysql row ro;
            while (ro = mysql_fetch_ro(res))
            {
                for (int i = 0; i < num; i++)
                {
                    cout << " " << ro[i];
                }
                cout << endl;
            }
            mysql_free_result(res);
        }
    }
}
int book(mysql *conn, string bname)
{
    string exist = "select name,quantity from lib where name='" + bname + "'";
    if (mysql_query(conn, exist.c_str()))
    {
        cout << "error" << mysql_error(conn) << endl;
    }
    else
    {
        mysql_result *res;
        res = mysql_store_result(conn);
        if (res)
        {
            int num = mysql_num_fields(res);
            mysql row ro;
            while (ro = mysql_fetch_ro(res))
            {
                for (int i = 0; i < num; i++)
                {
                    if (bname == ro[i])
                    {
                        int quant = atoi(ro[i + 1]) return quant;
                    }
                    else
                    {
                        cout << "book not found" << endl;
                    }
                }
            }
            mysql_free_result(res);
        }
    }
    return 0;
    sleep(5000);
}
void user(mysql *conn, library l, student s)
{
    system("cls");
    display(conn);
    string sid;
    cout << "enter id";
    cin >> sid;

    string com = "select * from student where id ='" + sid + "''";
    if (mysql_query(conn, com.c_str()))
    {
        cout << "error" << mysql_error(conn) << endl;
    }
    else
    {
        mysql_result *res;
        res = mysql_store_result(conn);
        if (res)
        {
            int num = mysql_num_row(ro);
            if (num == 1)
            {
                cout << "student id found" << endl;
                string bname;
                cout << "enter book name ";
                cin >> bname;
                if (book(conn, bname) > 0)
                {
                    int bookquantity = book(conn, bname) - 1;
                    stringstream ss;
                    ss << bookquantity;
                    string sb = ss.str();

                    string upd = "update lin set quantity='" + sb + "'where name='" + bname + "'";
                    if (mysql_query(conn, ipd.c_str()))
                    {
                        cout << "error" << mysql_error(conn) << endl;
                    }
                    else
                    {
                        cout << "book is available,borrowing book...." << endl;
                    }
                }
                else
                {
                    cout << "book is not available" << endl;
                }
            }
            else if (num == 0)
            {
                cout << "this student not registered : " << endl;
            }
        }
        mysql_free_result(res);
    }
}
int main()
{
    student s;
    library l;
    mysql *conn;
    conn = mysql_init(null);

    if (!mysql_real_connect(conn, host, user, passward, database, 3306, null, 0))
    {
        cout << "error" << mysql_error(conn) << endl;
    }
    else
    {
        cout << "logged in" << endl;
    }
    sleep(3000);
    bool exist = false;
    while (!exist)
    {
        system = ("cls");
        int val;
        cout << "welcome to library management system" << endl;
        cout << "*" << endl;
        cout << "1.administration" << endl;
        cout << "2.user " << endl;
        cout << "0.exist" << endl;
        cout << "enter choice";
        cin >> value;

        if (value == 1)
        {
            system("cls");
            admin(conn, l, s);
        }
        else if (value == 2)
        {
            user(conn, l, s);
            sleep(5000);
        }
        else if (value == 0)
        {
            exist = true;
            cout << "good work" << endl;
            sleep(3000);
        }
    }
    mysql_close(conn);

        return 0;
}