#include <iostream>
#include <sstream>
using namespace std;

class Student {
private:
    int age;
    string first_name;
    string last_name;
    int standard;

public:
    // Setters
    void set_age(int a) { age = a; }
    void set_first_name(const string& fname) { first_name = fname; }
    void set_last_name(const string& lname) { last_name = lname; }
    void set_standard(int s) { standard = s; }

    // Getters
    int get_age() const { return age; }
    string get_first_name() const { return first_name; }
    string get_last_name() const { return last_name; }
    int get_standard() const { return standard; }

    // to_string as specified
    string to_string() const {
        stringstream ss;
        ss << age << "," << first_name << "," << last_name << "," << standard;
        return ss.str();
    }
};
/*
Enter code for class Student here.
Read statement for specification.
*/

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
