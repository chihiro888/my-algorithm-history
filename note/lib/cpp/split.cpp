#include <iostream>
#include <sstream>
#include <string>
#include <vector>

vector<string> split(string input)
{
    vector<string> result;
    stringstream ss(input);
    string token;

    while (getline(ss, token, ','))
    {
        result.push_back(token);
    }

    return result;
}