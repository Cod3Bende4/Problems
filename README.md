# Problems
Here I will be uploading amazing problems with Answers

Problem [Start_Finish]:

1. There is a Maze[n*m Matrix]
2. There are two poins inside the Maze, one is START and one is FINISH
3. Take matrix size as input and take co-ordinates from users as START and FINISH, for example (1,1) for taking first element as START and (n,m) for taking last element as START, same goes for FINISH.
4. Calculate number of ways by which one can travel from element to element to reach the FINISH point, starting from START, but one can't travel back to the same element which he had already traveled inside his START-FINISH journey.

Example 

Input:

2 3		# Maze Size (n*m)
1,1		# START
2,3		# FINISH

Output:

4		# Number of ways to travel from START to FINISH without forming loop.

Explaination:

		Matrix: 

			*(S) *    *
			*    *    *(F)

Total number of ways to go from S to F are 4.
