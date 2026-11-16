class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # for example we have two lists 
        # [1,3] and [2,6]
        #  2 is less than 3 and we have to merge them since they are overlappping
        #we have to sort the array so that we only have to compare the first item and the last item
        intervals.sort()
        #the first item in the list is alreay sorted
        results = [intervals[0]]

        #looping through the list, i is a list in this case and we are starting from 1 since 0 is already sorted
        for i in intervals[1:]:
            #pointer for first list start and end
            resultStart = results [-1][0]
            resultEnd = results [-1][1]

            interStart = i[0]
            interEnd = i[1]

            if interStart <= resultEnd:
                #that means they overlapp
                newEnd = max(resultEnd,interEnd)
                # the last item in the result would be
                results[-1] = [resultStart, newEnd]
                
            else:
                #no overlap, ujust add
                results.append([interStart,interEnd])

        return results
            







        