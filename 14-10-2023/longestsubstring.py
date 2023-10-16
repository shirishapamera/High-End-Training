'''leetcode-3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
def lengthOfLongestSubstring(s):
    l,longestsubstring=0,0
    sw=set()
    for r in range(len(s)):
        while s[r] in sw:
            sw.remove(s[l])
            l+=1
        sw.add(s[r])
        longestsubstring=max(longestsubstring,(r-l+1))
    return longestsubstring
s=input()
print(lengthOfLongestSubstring(s))