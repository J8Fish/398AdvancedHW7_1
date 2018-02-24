#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

double calc(int a, int b, string op) {
	if (op == "+")
		return a + b;
	else if (op == "-") 
		return a - b;
	else if (op == "*")
		return a * b;
	else if (op == "/")
		return a / b;
}

int main() {
	cout << "<Num> <Op> <Num>" << endl;
	int a, b;
	string op;
	cin >> a >> op >> b;
	cout << calc(atoi(a), atoi(b), op) << endl;
}