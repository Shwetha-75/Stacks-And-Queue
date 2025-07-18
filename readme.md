<h3 align='center'>Concept - Next Generation Element</h3>


# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Find the permutation of a given number and the smallest among all will be the next greater number of **n**
# Approach
<!-- Describe your approach to solving the problem. -->
**Brute Force Approach :**

Find the permutation of a given number and sort it.
Finally check for the number which is just greater than n and within 2**31, if found return number or else return -1

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(N!)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(N!)$$

---


# Approach

**Find next greater permutation :** 

[Reference](https://www.geeksforgeeks.org/dsa/next-permutation/)

![Slide1.PNG](https://assets.leetcode.com/users/images/70392bf6-cb8c-4d5d-95e8-74d757175314_1752724696.2617145.png)
![Slide2.PNG](https://assets.leetcode.com/users/images/b6f6b03e-a98e-4494-94bc-94fd55878300_1752724701.1664383.png)
![Slide3.PNG](https://assets.leetcode.com/users/images/ebde143f-1e1b-47e6-bad5-2e54515365a1_1752724708.820846.png)
![Slide4.PNG](https://assets.leetcode.com/users/images/6fa66979-dd1d-43b6-9394-0e90b8ad05f0_1752724713.0911744.png)
![Slide5.PNG](https://assets.leetcode.com/users/images/64f9bfec-dad0-4a92-86b9-f96bc53cd62f_1752724719.1928244.png)
![Slide6.PNG](https://assets.leetcode.com/users/images/ab10b2f8-03d3-471a-8ea2-faede48f8b2f_1752724724.2358792.png)



# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$ O(D)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$ O(D)$$

where D is number of digits

---
<h3 align='center'>Trapping Water</h3>

<a href='https://leetcode.com/problems/trapping-rain-water/solutions/6974433/two-pointers-approach-by-shwetha_k-dvb8' target='_blank'>Reference</a>
