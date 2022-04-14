# stack

https://www.cplusplus.com/reference/stack/stack/  

stack is container adaptor

## Time complexity
```
O(n)
```

## how to import?
```c
#include <stack>
```

## how to init?
```c
stack<int> sampleStack;
```

## how to push?
```c
stack<int> sampleStack;

sampleStack.push(1);
sampleStack.push(2);
sampleStack.push(3);
```

## how to swap?
```c
stack<int> sampleStack1;
stack<int> sampleStack2;

sampleStack1.push(1);
sampleStack2.push(2);

swap(sampleStack1, sampleStack2);
```

## how to check empty?
```c
stack<int> sampleStack;

sampleStack.empty()
```
- if stack is empty then 1
- if stack is not empty then 0

## how to check count?
```c
stack<int> sampleStack;

sampleStack.count();
```

### how to clear stack?
```c
stack<int> sampleStack;

while( !sampleStack.empty() ) sampleStack.pop();
```

### how to initialize based deque?
```c
vector<int> data (3, 50); // vector with 3 elements {50, 50, 50}
stack<int, vector<int>> sampleStack (data);
```

### how to initialize based vector?
```c
deque<int> data (3, 50); // vector with 3 elements {50, 50, 50}
stack<int> sampleStack (data); // 50, 50, 50
```

### how to initialize based list?
```c
list<int> data (3, 50); // vector with 3 elements {50, 50, 50}
stack<int, list<int>> sampleStack (data); // 50, 50, 50
```