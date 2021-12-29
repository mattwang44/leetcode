// LeetCode #160
// https://leetcode.com/problems/intersection-of-two-linked-lists/description/

// 1st try
// Space: O(m+n)
// time:  O(m+n)
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL){return NULL;}
        int countA = 0, countB = 0, count = 0;
        ListNode *headA1 = headA, *headB1 = headB;
        vector<ListNode*> A, B;
        while(headA1!=NULL)
            {countA++; A.push_back(headA1); headA1 = headA1->next;}
        while(headB1!=NULL)
            {countB++; B.push_back(headB1); headB1 = headB1->next;}
        while (true){ count++;
            if (A[countA-count]->val!=B[countB-count]->val) {count--; break;}
            if (count == countA || count == countB){break;}
        }
        if (count == 0){return NULL;}
        ListNode *head;
        if (countA<countB) 
            { count = countA-count; head = headA; }
        else               
            { count = countB-count; head = headB; }
        while (count != 0){
            head = head->next;  count--;
        }
        return head;
    }
};

// Solution from forum
// Space: O(1)
// time:  O(m+n)
class Solution2 {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *p1 = headA, *p2 = headB;
        if (p1 == NULL || p2 == NULL) return NULL;
        while (p1 != NULL && p2 != NULL && p1 != p2){
            p1 = p1->next;  p2 = p2->next;
            if (p1 == p2) return p1;
            if (p1 == NULL) p1 = headB;
            if (p2 == NULL) p2 = headA;
        }return p1;
    }
};