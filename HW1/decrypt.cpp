#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

string caeserDecrypt(string input, string keys)
{
    string message = input, buffer;
    int key = stoi(keys);

    for(int x = 0; x < message.size(); x++)
    {
        if(message[x] >= 'a' && message[x] <= 'z')
        {
            char ch = message[x] + key;
            if(ch > 'z'){
                ch = ch - 'z' + 'a' - 1;
            }
            buffer += ch;
            continue;
        }
        else if(message[x] >= 'A' && message[x] <= 'Z')
        {
            char ch = message[x] + key;
            if(ch  > 'Z'){
                ch = ch - 'Z' + 'A' - 1;
            }
            buffer += ch;
            continue;
        }
        buffer += message[x];
    }
    return buffer;
}

string playfairDecrypt(string input, string key)
{
    int x, y,  k = 0, n = 5;
 
    string message = input;
    vector<vector<char>> a(n, vector<char>(n, ' '));
    map<char,int> mp;

    k=0;
    int px, py;
    for(x = 0; x < n;x++)
    {
        for(y = 0;y < n; y++)
        {
            while(mp[key[k]] > 0 && k < key.size())
            {
                k++;
            }
            if(k < key.size())
            {
                a[x][y] = key[k];
                mp[key[k]]++;
                px=x;
                py=y;
            }
            
            if(k == key.size()) break;
        }
        if(k == key.size()) break;  
    }

    k=0;
    for(;x < n; x++)
    {
        for(;y < n; y++){
            while(mp[char(k + 'a')] > 0 && k < 26)
            {
                k++;
            }
            if(char(k + 'a') == 'j')
            {
                y--;
                k++;
                continue;
            }
            if(k < 26)
            {
                a[x][y] = char(k + 'a');
                mp[char(k + 'a')]++;
            }
        }
        y=0;
    }

    string anser;
    map<char,pair<int,int>> mp2;

    for(x=0; x < n; x++)
    {
        for(y = 0; y < n; y++)
        {
            mp2[a[x][y]] = make_pair(x,y);
        }
    }
    for(x = 0;x < message.size() - 1; x+=2)
    {
        int y1 = mp2[message[x]].first;
        int x1 = mp2[message[x]].second;
        int y2 = mp2[message[x + 1]].first;
        int x2 = mp2[message[x + 1]].second;
        if(y1==y2)
        {
            anser +=a[y1][(x1-1)%5];
            anser +=a[y1][(x2-1)%5];
        }
        else if(x1==x2)
        {
            anser += a[(y1-1)%5][x1];
            anser +=a[(y2-1)%5][x2];    
        }
        else 
        {
            anser +=a[y1][x2];
            anser +=a[y2][x1];
        }
    }

    if(anser[anser.size()-1]=='x') anser[anser.size()-1]='\0';
    for(x = 1;x < anser.size(); x++)
    {
        if(anser[x]=='x') anser[x] = anser[x-1];
    }
    
    return anser;
}

string vernamDecrypt(string input, string key)
{
    string message = input;

    int mod = key.size();
    for(int x = key.size(), y = 0;x < message.size(); x++, y++)
    {
        key += key[y % mod];
    }

    string anser;
    for(int x = 0; x < message.size(); x++)
    {
        anser += (message[x] - key[x] + 26) % 26 + 'A';
    }
    
    return anser;

}

string railfenceDecrypt(string input, string keys)
{
    string message = input, buffer;
    int key = stoi(keys);

    vector<vector<char>> a(key, vector<char>(message.size(),' ')); 

    int flag=0;
    for(int x = 0, y = 0; x < message.size(); x++)
    {
        a[y][x] = '0';
        if(y == key - 1) flag = 1;
        else if(y == 0) flag=0;

        if(flag==0) y++;
        else y--;
    }

    int temp =0;
    for(int x = 0; x < key;x++)
    {
        for(int y = 0;y < message.size(); y++)
        {
            if(a[x][y] == '0') a[x][y] = message[temp++];
        }
    }

    flag=0;
    for(int x = 0, y = 0;x < message.size(); x++)
    {
        buffer += a[y][x];
        if(y == key - 1) flag=1;
        else if(y == 0) flag=0;
        
        if(flag==0) y++;
        else y--;
    }   
    return buffer;
}

string rowDecrypt(string input, string key)
{
    string message = input;
    int k = 0,n = 26;
    vector<vector<char> > a(n, vector<char>(n));

    for(int x = 0; x < n; x++)
    {
        k = x;
        for(int y = 0; y < n; y++)
        {
            a[x][y] = 'A' + k;
            k++;
            if(k==26) k=0;
        }
    }

    k = 0;
    for(int x = key.size(); x < message.size(); x++)
    {
        key += key[k];
        k++;
    }

    string buffer;
    for(int x = 0;x < message.size(); x++)
    {
        for(int y = 0; y < n; y++)
        {
            if(a[y][key[x] - 'A'] == message[x])
            {
                buffer += 'A'+ y;
                break;
            }
        }
    }
    return buffer;
}

int main(int argc, char *argv[])
{
    string  method, input, key;
    
    if(7 != argc)
    {
        return 1;
    }

    method = (string)argv[2];
    input = (string)argv[4];
    key = (string)argv[6];

    // Method: caesar/playfair/vernam/railfence/row
    if("caeser" == method)
    {
        cout << caeserDecrypt(input, key) << endl;
    }
    else if("playfair" == method)
    {
        cout << playfairDecrypt(input, key) << endl;
    }
    else if("vernam" == method)
    {
        cout << vernamDecrypt(input, key) << endl;
    }   
    else if("railfence" == method)
    {
        cout << railfenceDecrypt(input, key) << endl;
    }
    else if("row" == method)
    {
        cout << rowDecrypt(input, key) << endl;
    }
    return 0;
}
