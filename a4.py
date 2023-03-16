import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int)
parser.add_argument("--print", action="store_true")
args = parser.parse_args()
sum = 0

# n - number of vertices on convex polygon
# offset - amount by which we shift the coordinates of diagonals (for recursive calls)
# top - true if this is the first call made to method so we only ever add to the sum at top of recursion stack
def tri(n, offset, top):
    global sum # sum of distinct triangulations to add to in first call to tri
    if n == 3:
        yield []
        if top:
            sum += 1
    if n > 3:    
        for pivot in range(1, n - 1):
            diagL = (pivot, n - 1)
            diagR = (0, pivot)
            # if the pivot triangle doesn't produce an ear, we have our normal case.
            if not leftEar(diagR, diagL, n) and not rightEar(diagR, diagL, n):
                # shift diagonal by offset so correct diagonal appears in printed version
                diagL = (pivot + offset, n - 1 + offset)
                diagR = (offset, pivot + offset)
                for diag1 in tri(pivot + 1, offset, False):
                    for diag2 in tri(n - pivot, offset + pivot, False):
                        yield [diagL, diagR] + diag1 + diag2
                        if top:
                            sum += 1 # if top recursive call, add 1 to sum
            elif rightEar(diagR, diagL, n):
                diagL = (pivot + offset, n - 1 + offset)
                # if pivot produces a right ear, only need to explore triangulations 
                # with fixed left diagonal 
                for diag in tri(n - pivot, offset + pivot, False):
                    yield [diagL] + diag
                    if top:
                        sum += 1 # if top recursive call, add 1 to sum
            elif leftEar(diagR, diagL, n): 
                diagR = (offset, pivot + offset)
                # if pivot produces a left ear, only need to explore triangulations 
                # with fixed right diagonal 
                for diag in tri(pivot + 1, offset, False):

                    yield [diagR] + diag 
                    if top:
                        sum += 1 # if top recursive call, add 1 to sum

def leftEar(diagR, diagL, n):
    return abs(diagL[1] - diagL[0]) == 1 

def rightEar(diagR, diagL, n):
    return abs(diagR[1] - diagR[0]) == 1 

triangulations = tri(args.n, 0, True)
if args.print:
    for v in triangulations:
        print(v)
print("Total distinct triangulations: " + str(sum))

