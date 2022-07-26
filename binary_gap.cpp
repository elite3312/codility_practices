#include "pch.h"
#include <iostream>
/***********/
using namespace std;
#include <bitset>
/*A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].*/

int solution(int N) {
	/*A binary gap within a positive integer N is any maximal sequence of consecutive zeros 
	that is surrounded by ones at both ends in the binary representation of N.
	this function returns the length of the longset binary gap in N.
	*/
	std::string str = std::bitset<32>(N).to_string();
	std::cout << str<<endl;

	int binary_gap_len = 0, max_binary_gap_len = 0;
	bool has_seen_one=false;
	for (auto i = 0; i < str.length();i++) {
		if (str[i] == '1') {
			if(!has_seen_one)
				has_seen_one = true;
			else {//has_seen_one
				if (max_binary_gap_len < binary_gap_len) {
					max_binary_gap_len = binary_gap_len;
				}
				binary_gap_len = 0;
			}
		}
		else {//'0'
			if (has_seen_one)binary_gap_len++;
		}
	}
	return max_binary_gap_len;
}
/************/
int main()
{
	/*codility: Producing output might cause your solution to fail performance tests.
	You should remove code that produces output before you submit your solution.
	
	Detected some errors.*/
    std::cout <<endl<< solution(144);
	
	return 0;
}
