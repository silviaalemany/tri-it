# Counting Distinct Triangulations
This program counts the number of distinct triangulations for a convex polygon on n vertices and returns the result.
To run, do: 
``python3 tri.py n``
from the same directory as tri.py, where n is the number of vertices.

If you want to print all of the distinct triangulations, the second argument should be ``--print``.

## Example
To get the list AND number of distinct triangulations for a pentagon, do:
``python3 tri.py 5 --print``

To just get the number of distinct triangulations for a pentagon, do:
``python3 tri.py 5``

## Details
This program uses an offset argument to allow for a minimum amount of auxiliary data structures/memory. My approach is similar in concept to the textbooks diagram of 3.12. Using the edge connecting the last and first index (ie, vertices n - 1 and 0), I iterate through possible pivot triangles to force certain diagonals and check the triangulations efficiently. When a pivot triangle is checked, it is used to partition the polygon, and I track the possible unique triangulated of the regions that the original polygon is partitioned to using recursion. I track the offset of the partitioned regions from the original indexing in order to accurately output edges while not having to store a list of vertices. I used python's yield to create a generator for the list of distinct triangulation, such that we do not have to store the entired list and can print triangulations on the fly using the generator produced by the method call if the --print flag is passed. Because I do not need to store any vertices to compute these triangulations (due to the offset), and I use yield to generate distinct triangulations for printing, I suspect the bottleneck will be time. 
