class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats= sorted(seats)
        output=0
        students=sorted(students)

        for i in range(len(seats)):
            output+= abs(seats[i]-students[i])
        return (output)
