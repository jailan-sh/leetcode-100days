/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* current = head;
    struct ListNode* tmp = head;
    int num = 0;
    int index;

    while(tmp){
        num++;
        tmp = tmp->next;
    }
    tmp = head;
    index = num - n;
    if (index == 0)
    {
        head = head->next;
        free(current);
        return (head);
    }
    while(index > 1)
    {
        tmp = tmp->next;
        index--;
    }
    current = tmp->next;
    tmp->next = current->next;
    free(current);
    return head;
}