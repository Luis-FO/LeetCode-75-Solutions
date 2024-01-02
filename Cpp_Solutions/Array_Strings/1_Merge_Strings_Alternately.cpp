#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result = "";
        int len1 = word1.length(); 
        int len2 = word2.length();
        int max_len = max(len1, len2);
        
        for(int i = 0; i<max_len;i++){
            if(i<len1){
                result += word1[i];
            }
            if(i<len2){
                result += word2[i];
            }

        }
        return result;
    }
};

int main(){
    Solution S;
    string a = "abc";
    string b = "tcgfq";
    string r = S.mergeAlternately(a, b);
    cout<<r<<endl;
}