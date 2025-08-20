#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    if (!getline(cin, s)) return 0;

    auto l = s.find_first_not_of(" \t\r\n");
    if (l == string::npos) { cout << "." << "\n"; return 0; }
    auto r = s.find_last_not_of(" \t\r\n");
    s = s.substr(l, r - l + 1);


    for (char &c : s) c = static_cast<char>(tolower(static_cast<unsigned char>(c)));

    string vowels = "aeiouy";
    vector<char> parts;
    for (char c : s) if (vowels.find(c) == string::npos) parts.push_back(c);

    cout << '.';
    for (size_t i = 0; i < parts.size(); ++i) {
        if (i) cout << '.';
        cout << parts[i];
    }
    cout << '\n';
    return 0;