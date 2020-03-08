
// Complete the reversePrint function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
void reversePrint(SinglyLinkedListNode* head) {
    struct SinglyLinkedListNode *ptr;
    struct SinglyLinkedListNode * prev = NULL; 
    struct SinglyLinkedListNode* current = head; 
    struct SinglyLinkedListNode* next = NULL;
    while (current != NULL) { 
        next = current->next; 
        current->next = prev; 
        prev = current; 
        current = next; 
    } 
    head = prev; 
    ptr=head;
    while(ptr!=NULL){
        printf("%d\n",ptr->data);
        ptr=ptr->next;
    }

}

