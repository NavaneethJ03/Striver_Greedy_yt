class Solution:    
    def nMeetings(self , start , end):
        n = len(start)
        meetings = []
        # We are creating a custom data structure for this process
        for i in range(n):
            meetings.append((start[i] , end[i]))
        # we sort the above created data structure with the endtime 
        meetings.sort(key = lambda x: x[1])
        count = 1 
        limit = meetings[0][1]
        for i in range(1 , n):
            if meetings[i][0] > limit:
                count += 1 
                limit = meetings[i][1]

        return count 

# Time Complexity -> (2N + N log N) -> O(N log N)
# Space Complexity -> O(N)
