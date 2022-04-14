#include <iostream>
#include <queue>

using namespace std;

template <typename T>
void printQueue(queue<T> queue) {
    if (queue.empty()) cout << "empty";
    while (!queue.empty()) {
        cout << queue.front() << " ";
        queue.pop();
    }
    cout << endl;
}

template <typename T>
void clearQueue(queue<T> &queue) {
    while( !queue.empty() ) queue.pop();
}

int main() {
    // TODO
    return 0;
}