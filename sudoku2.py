#Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column,
#each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.
#Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the 
#layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

def sudoku2(grid):
        grid2 = [row[:] for row in grid]
        grid3 = [row[:] for row in grid]
        grid4 = [row[:] for row in grid]
        
        # checks rows
        for i in range(0,9):
                row=grid2[i]
                while True:
                        try:
                                row.remove('.')
                        except ValueError:
                                break
                if len(set(row)) != len(row):
                        return False
                
        
        # check columns
        for i in range(0,9):
                column=[x[i] for x in grid3]
                while True:
                        try:
                                column.remove('.')
                        except ValueError:
                                break
                if len(set(column)) != len(column):
                        return False 
        
        # check each 3x3 sub-grid

        for start in range(0, 9, 3):
                print (start)
                end = start+3
                for start2 in range(0, 9, 3):
                        end2 = start2+3
                        #printing out each subgroup individually
                        subgrid = []
                        for i in range(start2,end2):
                                #print(grid3[i][start:end])
                                subgrid.append(grid3[i][start:end])
                        print (subgrid[0]+subgrid[1]+subgrid[2])
                        subg = (subgrid[0]+subgrid[1]+subgrid[2])
                        print("-------")
                        while True:
                                try:
                                        subg.remove('.')
                                except ValueError:
                                        break
                        if len(set(subg)) != len(subg):
                                
                                print("False")
                                return False
        return True
