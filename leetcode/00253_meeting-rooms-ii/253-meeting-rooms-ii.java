class Solution {
    public int minMeetingRooms(int[][] intervals) {
        HashMap<Integer, Integer> memo = new HashMap<Integer, Integer>(0);
        for (int i = 0; i < intervals.length; i++) {
            memo.put(intervals[i][0], memo.getOrDefault(intervals[i][0], 0) + 1);
            memo.put(intervals[i][1], memo.getOrDefault(intervals[i][1], 0) - 1);
        }

        Integer max_room = 0;
        Integer curr_room = 0;
        SortedSet<Integer> keys = new TreeSet<>(memo.keySet());
        for (Integer key : keys) { 
            curr_room += memo.get(key);
            max_room = Math.max(max_room, curr_room);
        }
        return max_room;
    }
}
