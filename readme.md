# Concept - Next Generation Element 


**Intuition**
<!-- Describe your first thoughts on how to solve this problem. -->
Find the permutation of a given number and the smallest among all will be the next greater number of **n**
**Approach**
<!-- Describe your approach to solving the problem. -->
**Brute Force Approach :**

Find the permutation of a given number and sort it.
Finally check for the number which is just greater than n and within 2**31, if found return number or else return -1

**Complexity**
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(N!)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(N!)$$

---


**Approach**

**Find next greater permutation :** 

[Reference](https://www.geeksforgeeks.org/dsa/next-permutation/)

![Slide1.PNG](https://assets.leetcode.com/users/images/70392bf6-cb8c-4d5d-95e8-74d757175314_1752724696.2617145.png)
![Slide2.PNG](https://assets.leetcode.com/users/images/b6f6b03e-a98e-4494-94bc-94fd55878300_1752724701.1664383.png)
![Slide3.PNG](https://assets.leetcode.com/users/images/ebde143f-1e1b-47e6-bad5-2e54515365a1_1752724708.820846.png)
![Slide4.PNG](https://assets.leetcode.com/users/images/6fa66979-dd1d-43b6-9394-0e90b8ad05f0_1752724713.0911744.png)
![Slide5.PNG](https://assets.leetcode.com/users/images/64f9bfec-dad0-4a92-86b9-f96bc53cd62f_1752724719.1928244.png)
![Slide6.PNG](https://assets.leetcode.com/users/images/ab10b2f8-03d3-471a-8ea2-faede48f8b2f_1752724724.2358792.png)



**Complexity**
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$ O(D)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$ O(D)$$

where D is number of digits

---
# Trapping Water

**Intuition**
Total number of units water filled between the buildings

total=total+min(left_max,right_max)-arr[i]   

**Approach**

Brute Force :

Initialize the total=0
For each index starting from 1 until n-1 (inclusively)
left_max from i-1 until 0
right_max from i+1 until n-1
Add with total (Keep note negative values if there exist do not consider)
return total
**Complexity**

Time complexity:
O(N^2)

Space complexity:
O(1)



**Approach**
Prefix and Suffix sum Approach. Here we can just consider the suffix max array leaving prefix max because we are traversing from left to right

Suffix Max :

<img src='https://assets.leetcode.com/users/images/24940e28-9b87-46ae-93dc-ed904584e26f_1752846075.296077.png' />
<img src='https://assets.leetcode.com/users/images/55b1a58e-ff8a-4ff9-ab85-a9bcfdc53cea_1752846084.6826568.png' />
<img src='https://assets.leetcode.com/users/images/8e413c7b-37f3-40a9-97af-e034df92c833_1752846089.1883512.png' />
<img src='https://assets.leetcode.com/users/images/08cce4f5-f02d-4da5-861c-f327bf4e18fb_1752846094.2049174.png' />
<img src='[https://assets.leetcode.com/users/images/e8bceda9-d81b-4494-a55a-f41f2a2d98e5_1752846099.8652275.png' />

**Complexity**

Time complexity:
O(N)

Space complexity:
O(N)

**Approach**
Two pointers approach

<img src='https://assets.leetcode.com/users/images/0d9f2725-74ad-4c86-9c05-a9bf3f558b78_1752845211.9903376.png' />
<img src='https://assets.leetcode.com/users/images/928f13ad-a63f-4b8d-94b8-cf57a1e24f37_1752845226.112784.png' />
<img src='https://assets.leetcode.com/users/images/55d1c94b-c553-480c-b5b8-a6fb8d80b8bd_1752845231.9661117.png' />
<img src='https://assets.leetcode.com/users/images/f70e4ba1-3ffa-4894-9bcd-5296710b84f9_1752845236.8348687.png' />
<img src='https://assets.leetcode.com/users/images/462de70b-2af4-448f-a326-8b0ac2955dbf_1752845242.7939358.png' />
<img src='https://assets.leetcode.com/users/images/a315a458-c8e7-40b9-b07a-e474158095e8_1752845247.0111835.png' />
<img src='https://assets.leetcode.com/users/images/f3301635-117c-45db-ad86-0de5aa13cadd_1752845252.4319925.png' />
<img src='https://assets.leetcode.com/users/images/8e9fd3b5-279c-4498-b8b2-b9a8cfb3314c_1752845256.6722639.png' />

**Complexity**
Time complexity:
O(N)

Space complexity:
O(1)



