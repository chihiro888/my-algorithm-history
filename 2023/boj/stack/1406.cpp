#include <iostream>
#include <string>
#include <stack>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

int main()
{
    // input
    string input;
    int input_size;
    cin >> input;
    cin >> input_size;
    cin.ignore();

    // stack
    stack<char> temp_stack;
    stack<char> current_stack;

    REP(i, input.size())
    {
        current_stack.push(input[i]);
    }

    REP(i, input_size)
    {
        string command;
        getline(cin, command);

        char opcode = command[0];
        char data = command[2];

        if (opcode == 'P')
        {
            current_stack.push(data);
        }
        else if (opcode == 'B' && !current_stack.empty())
        {
            current_stack.pop();
        }
        else if (opcode == 'L' && !current_stack.empty())
        {
            temp_stack.push(current_stack.top());
            current_stack.pop();
        }
        else if (opcode == 'D' && !temp_stack.empty())
        {
            current_stack.push(temp_stack.top());
            temp_stack.pop();
        }
    }

    while (!temp_stack.empty())
    {
        current_stack.push(temp_stack.top());
        temp_stack.pop();
    }

    // reverse print using stack
    while (!current_stack.empty())
    {
        temp_stack.push(current_stack.top());
        current_stack.pop();
    }

    while (!temp_stack.empty())
    {
        cout << temp_stack.top() << "";
        temp_stack.pop();
    }

    cout << endl;

    return 0;
}