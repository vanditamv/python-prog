
#Merge intervals by first sorting them based on their start times and then iterating through the intervals to merge overlapping ones. 
#Here's a Python program to achieve that:

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals based on their start times
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]
    
    for interval in intervals[1:]:
        # If the current interval overlaps with the last merged interval, merge them
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1])]
        else:
            # If there's no overlap, add the current interval to the merged intervals list
            merged_intervals.append(interval)
    
    return merged_intervals

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
print("Merged intervals:", merge_intervals(intervals))
# output Merged intervals: [[1, 6], [8, 10], [15, 18]]
