class Solution:
    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

	    # Only consider 2+ co-ordinate pairs:
	    if len(coordinates) > 2:
	
		    # Unpack the next three co-ordinates for 0 to n - 3
		    for i in range(len(coordinates) - 2):
			    (x1, y1), (x2, y2), (x3, y3) = coordinates[i: i + 3]

			    # Compare cross-products to verify co-linearity:
			    if (y3 - y2) * (x2 - x1) != (y2 - y1) * (x3 - x2):
				    return False
	    return True