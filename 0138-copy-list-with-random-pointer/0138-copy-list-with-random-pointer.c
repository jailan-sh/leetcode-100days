/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *next;
 *     struct Node *random;
 * };
 */

struct Node* createNode(int val) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->val = val;
    newNode->next = NULL;
    newNode->random = NULL;
    return newNode;
}

struct Node* copyRandomList(struct Node* head) {
    if (head == NULL) {
        return NULL;
    }

    struct Node* current = head;
    while (current != NULL) {
        struct Node* newNode = createNode(current->val);
        newNode->next = current->next;
        current->next = newNode;
        current = newNode->next;
    }

    current = head;
    while (current != NULL) {
        if (current->random != NULL) {
            current->next->random = current->random->next;
        }
        current = current->next->next;
    }

    current = head;
    struct Node* newHead = head->next;
    struct Node* newCurrent = newHead;
    while (current != NULL) {
        current->next = newCurrent->next;
        if (newCurrent->next != NULL) {
            newCurrent->next = newCurrent->next->next;
        }
        current = current->next;
        newCurrent = newCurrent->next;
    }

    return newHead;
}