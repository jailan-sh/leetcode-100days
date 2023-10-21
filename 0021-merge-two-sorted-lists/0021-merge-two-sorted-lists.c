/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
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
    if (list1->val <= list2->val)
    {
        dummy = list1;
        list1 = list1->next;
    }
    else{
        dummy = list2;
        list2 = list2->next;
    }
    head = dummy;
    while(list1 && list2)
    {
        if (list1->val <= list2->val){
            dummy->next = list1;
            dummy = list1;
            list1 = dummy->next;
        }
        else
        {
            dummy->next = list2;
            dummy = list2;
            list2 = dummy->next;
        }
    }
    if (list1 == NULL){
        dummy->next = list2;
    }
    else
    {
        dummy->next = list1;
    }
    return (head);
}