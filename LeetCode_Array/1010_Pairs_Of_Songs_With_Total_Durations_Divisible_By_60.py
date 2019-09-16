"""
1010. Pairs of Songs With total durations Divisible By 60
Category: Array
Difficulty: Easy
"""
"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
"""
class Solution(object):
    def numPairsDivisibleBy60_1(self,time):
        result = 0
        record = [0 for _ in range(60)]
        for i in time:
            record[i % 60] += 1
        #print(record)
        for i in range(60):
            if i == 0 or i == 30 and record[i] > 1:
                result += record[i]*(record[i]-1)
                record[i] = 0
            else:
                result += record[i]*record[60-i]
        return (result // 2)

    def numPairsDivisibleBy60_2(selfs,time):
        result = 0
        record = [0 for _ in range(60)]
        for i in time:
            record[i % 60] += 1
        result += record[0]*(record[0]-1)//2
        result += record[30]*(record[30]-1)//2
        for i in range(1,30):
            result += record[i]*record[60-i]
        return result


if __name__ == "__main__":
    print(Solution().numPairsDivisibleBy60_2([30,20,150,100,40]))
    print(Solution().numPairsDivisibleBy60_1([20,20,20,40,40]))