#include <iostream>

int main() {
    ListNode *a = new ListNode(1);  // a is a ptr point to a new ListNode
    cout<<a<<endl;                  // the position of the new ListNode: 0xe79c20
    cout<<(a->val)<<endl;           // 1
    
    ListNode b(2);                  // b is a new ListNode
    //cout<<b<<endl;                // error: cannot print a ListNode
    cout<<(b.val)<<endl;            // 2

    ListNode c(3);                  // c is a new ListNode
    ListNode *p = &c;               // p is a ListNode ptr point to c
    //cout<<c<<endl;                // error: cannot print a ListNode
    cout<<&c<<endl;                 // c's position: 0x7fffd1f4e3a0
    cout<<p<<endl;                  // c's position: 0x7fffd1f4e3a0
    cout<<&p<<endl;                 // p's position: 0x7fffd1f4e398
    //cout<<*p;                     // error: cannot print a ListNode
    cout<<(*p).val<<endl;           // 3
    
    //p->next = b;                  // error: p->next is a ptr of ListNode, while b is a ListNode
    p->next = &b;                   // p->next point to b
    cout<<p->next->val<<endl;       // 2
    cout<<c.next->val<<endl;        // 2
    
    
}