#include <iostream>
#include <queue>

using namespace std;

template <typename T>
void printPriorityQueue(priority_queue<T> queue) {
    if (queue.empty()) cout << "empty";
    while (!queue.empty()) {
        cout << queue.top() << " ";
        queue.pop();
    }
    cout << endl;
}

template <typename T>
void clearPriorityQueue(priority_queue<T> &queue) {
    while( !queue.empty() ) queue.pop();
}

int main() {
    // TODO
    return 0;
}