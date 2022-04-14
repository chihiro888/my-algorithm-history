# queue

https://www.cplusplus.com/reference/queue/queue/  

queue is container adaptor

## Time complexity
```
O(n)
```

## how to import?
```c
#include <queue>
```

## how to init?
```c
queue<int> sampleQueue;
```

## how to push?
```c
queue<int> sampleQueue;

sampleQueue.push(1);
sampleQueue.push(2);
sampleQueue.push(3);
```

## how to swap?
```c
stack<int> sampleQueue1;
stack<int> sampleQueue2;

sampleQueue1.push(1);
sampleQueue2.push(2);

swap(sampleQueue1, sampleQueue2);
```

## how to check empty?
```c
queue<int> sampleQueue;

sampleQueue.empty()
```
- if queue is empty then 1
- if queue is not empty then 0

## how to check count?
```c
queue<int> sampleQueue;

sampleQueue.count();
```

### how to clear queue?
```c
queue<int> sampleQueue;

while( !sampleQueue.empty() ) sampleQueue.pop();
```

### how to initialize based deque?
```c
vector<int> data (3, 50); // vector with 3 elements {50, 50, 50}
queue<int, vector<int>> sampleQueue (data);
```

### how to initialize based vector?
```c
deque<int> data (3, 50); // vector with 3 elements {50, 50, 50}
queue<int> sampleQueue (data); // 50, 50, 50
```

### how to initialize based list?
```c
list<int> data (3, 50); // vector with 3 elements {50, 50, 50}
queue<int, list<int>> sampleQueue (data); // 50, 50, 50
```