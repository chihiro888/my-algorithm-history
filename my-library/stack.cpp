#include <iostream>
#include <stack>

using namespace std;

template <typename T>
void printStack(stack<T> stack) {
    if (stack.empty()) cout << "empty";
    while (!stack.empty()) {
        cout << stack.top() << " ";
        stack.pop();
    }
    cout << endl;
}

template <typename T>
void clearStack(stack<T> &stack) {
    while( !stack.empty() ) stack.pop();
}

int main() {
    // TODO
    return 0;
}