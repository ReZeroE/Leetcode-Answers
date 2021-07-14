/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* temp = calloc(1, sizeof(struct ListNode));
    struct ListNode* result = calloc(1, sizeof(struct ListNode));
    result = temp;
    
    while(l1 != NULL && l2 != NULL){
        if(l1->val > l2->val){
            temp->next = l2;
            l2 = l2->next;
        }
        else if(l1->val <= l2->val){
            temp->next = l1;
            l1 = l1->next;
        }
        temp = temp->next;
    }
    
    if(l1 == NULL) temp->next = l2;
    else if(l2 == NULL) temp->next = l1;
    
    return result->next;
}