/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode* two = list2;
    struct ListNode* one = list1;
    struct ListNode* head;
    struct ListNode* dummy;
    if (list1 == NULL && list2 == NULL){
        return list1;
    }
    if(list1 == NULL){
        return list2;
    }
    if (list2 == NULL){
    return (list1);
    }
    if (one->val <= two->val)
    {
        dummy = one;
        one = one->next;
    }
    else{
        dummy = two;
        two = two->next;
    }
    head = dummy;
    while(one && two)
    {
        if (one->val <= two->val){
            dummy->next = one;
            dummy = one;
            one = dummy->next;
        }
        else
        {
            dummy->next = two;
            dummy = two;
            two = dummy->next;
        }
    }
    if (one == NULL){
        dummy->next = two;
    }
    else
    {
        dummy->next = one;
    }
    return (head);
}