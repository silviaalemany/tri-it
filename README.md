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
 My approach is similar in concept to the diagram 3.12 in Discrete and Computational
Geometry by Devadoss & O'Rourke. Using the edge connecting the last and first index (ie, vertices n - 1 and 0), I iterate through possible pivot triangles incident on this "base edge" to force certain diagonals and check the triangulations efficiently. When a pivot triangle is checked, it is used to partition the polygon, and I track the unique triangulations of the regions that the original polygon is partitioned into using recursion. The method to count distinct triangulations uses an "offset" argument in an attempt to minimize the amount of auxiliary data structures needed to store vertices. I track the offset of the partitioned regions from the original indexing in order to accurately output edges while not having to store a list of vertices. I also used python's ``yield`` to create a generator for the list of distinct triangulations. I did not want to store the entire list of distinct triangulations; yields allows us to can print/count the distinct triangulations "on the fly" by iterating through the generator produced by the method call. Because I do not need to store any vertices to compute these triangulations (due to the offset), and I use yield to generate distinct triangulations for counting/printing, I suspect the bottleneck of my implementation will be time. 
