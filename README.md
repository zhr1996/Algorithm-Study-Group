# Algorithms

This repo has the solution for the Online Problems I have learned and solved.

## June Challenge
### Palindrome Pairs (June 13th) 
> Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome. 
It literally takes me three days to solve this challenge. It looks simple at first glance but at essence it is a hard one. I may write a blog about this problem but now I will briefly describe how I approached it. 

At first glance, I realized I could use a brute force to check every pair. It's not hard to determine whether a string is a palindrome once we have a pair. So we have a quick solution to this. The time complexity is O(n^2w), which I actually would argue is good, if there are not too many words in the list. But unfortunatelly, there are at most 5000 words in the list and each word is at most 300 character. So we need to think a way around this. At first, I couldn't think any way to reduce the computation. So I stopped on this and read several blogs.

Waking up next morning, I realized there is actually a way out. The key to realize is that a parlindrome can be made up of three pars: part a + part b + part c. Part a is reverse of part c. And part b itself is a palindrome. With this in mind, we could actually solve the computation by using more memory: storing all word in a map, and once we have a part a or part c, we could quickly determine if there is reverse in the word list. Then I start to implement it. But when implementing, I made a mistake. I thought to prevent replication, I have to check the word after current index. For example, if I am looking at word[i], I could only find the counter part in words after word[i]. After implementing this, I found the result is not right.

So in the third day, I realized that this is not right. If we see a word in two parts, part a + part b and we use ~a as the reverse. If part b is palindrome, and we found ~a in word list, then we could form a + b + ~a. And when we are checking this word: ~a, it can't be paired with the first word, because b is not null. 

And that's the last evil on the road, the NULL. The "" is a corner case we need to attend to. We can avoid replication by only spliting word in "" and word but not word and "". This looks confusing, but once implementing, this will be clear. Because (word + "") + ~word is a replicate of word + ("" + ~word). But once we do this, another problem is that we could overlook the case where the word itself is a palindrome and there exists a "" in the word list. In this case, we are only taking accoung in ("" + word) + ""(this "" is a word in the list). We are overlooking "" + (word + ""). To remedy this, we need to manually add in whenever we detect part a is "" and part b is a palindrome. 

This is it. After considering all this, the problem will be solved at last! Now back to the first sentence, I said this is a hard problem at essence. First, it requires some thinkging before one can realize the way of saving computation. Second, after thinking out the idea, it stills requires careful implementaion and clear thought to solve it. This is what a hard problem is like. Either one of the above condition can make a problem moderate. 

But considering this, I also have two ideas. One is always considering storage in exchange of computation. Second is test drived development. I found Leetcode is doing too much testing, but once we take the time to think about the testcases, we will have some corner cases in mind. And it is not necessary to come up with all these implementation details at once. We can take on it gradually.
