class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:


        for i in range(len(coordinates)-2):
            # print(a)
            if int(((coordinates[i+2][1]-coordinates[i][1])*(coordinates[i+1][0] - coordinates[i][0])) - ((coordinates[i+1][1] - coordinates[i][1])*(coordinates[i+2][0] - coordinates[i][0]))) == 0:
                continue
            else:
                return False
        
        return True

