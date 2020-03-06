//==========================================//
//   C++ code to implement Vigenere Cipher  //
//==========================================//
/*

Encryption
----------
The plaintext(P) and key(K) are added modulo 26.
Ei = (Pi + Ki) mod 26

Decryption
----------
Di = (Ei - Ki + 26) mod 26
 
*/


#include<bits/stdc++.h> 
using namespace std;

string generateKey(string str, string key) 
{ 
	int x = str.size(); 

	for (int i = 0; ; i++) 
	{ 
		if (x == i) 
			i = 0; 
		if (key.size() == str.size()) 
			break; 
		key.push_back(key[i]); 
	} 
	return key; 
} 

string cipherText(string str, string key) 
{ 
	string cipher_text; 

	for (int i = 0; i < str.size(); i++) 
	{ 
		// converting in range 0-25 
		int x = (str[i] + key[i]) %26; 

		// convert into alphabets(ASCII) 
		x += 'A'; 

		cipher_text.push_back(x); 
	} 
	return cipher_text; 
} 

string originalText(string cipher_text, string key) 
{ 
	string orig_text; 

	for (int i = 0 ; i < cipher_text.size(); i++) 
	{ 
		// converting in range 0-25 
		int x = (cipher_text[i] - key[i] + 26) %26; 

		// convert into alphabets(ASCII) 
		x += 'A'; 
		orig_text.push_back(x); 
	} 
	return orig_text; 
} 

/* ====================================================
 * 
 *                      MAIN PROGRAM
 * 
 * ==================================================== */ 
int main() 
{ 
	string str = "SAYAMAKANNASI";
	string keyword = "PASSWORD"; 

	string key = generateKey(str, keyword); 
	string cipher_text = cipherText(str, key); 

	cout << "\nGenerated key: " << key << "\n";
	cout << "Ciphertext: " << cipher_text << "\n"; 

	cout << "Original/Decrypted Text: " << originalText(cipher_text, key) << "\n"; 
	return 0; 
} 
