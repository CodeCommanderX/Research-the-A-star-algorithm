# Project Name

## Description

This project implements the A* search algorithm and provides a detailed explanation.

## Team Member
- VU MINH NGHIA

## A* Algorithm

### What is A* algorithm?

The A* algorithm is a combination of "UNIFORM COST SEARCH" and "BEST FIRST SEARCH" algorithms designed to enhance search efficiency. It utilizes a cost/distance function from the initial state to any state (f(n)), along with an estimated cost/distance function from a state to the goal state (g(n)). When the sum of these two values (h(n) = f(n) + g(n)) is achieved, and g(n) is an underestimate of the actual cost/distance function from n to the goal state, the best-first-search algorithm is called A*. The A* algorithm is particularly effective for search trees of moderate size.

### Example?

No.	Expandable node	O compilation set
0		S(6)
1	S	As(6),Bs(5)
2	Bs	As(6),Cb(6)
3	As	Cb(6),Da(8),Ga(7)
4	Cb	Da(8),Ga(7)
5	Ga	destination
![image](https://github.com/CodeCommanderX/Research-the-A-star-algorithm/assets/132070927/1fd47f23-937a-4c85-a191-d5ff8111cc71)


SHORTEST path: G← A← S
