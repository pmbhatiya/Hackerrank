// getNode function Of single linked list.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
int getNode(SinglyLinkedListNode* head, int positionFromTail) {
    struct SinglyLinkedListNode *ptr,*parentptr;
    ptr=head;
    
    int i=0,val=0;
   if(head==NULL){
       printf("Empty list !!");
   }else{
    while(ptr!=NULL){

        i++;
        ptr=ptr->next;
    }
    positionFromTail=i-positionFromTail;
    ptr=head;
    i=0;
    while(ptr!=NULL){
        if(positionFromTail==i)
        break;
        i++;
        parentptr=ptr;
        ptr=ptr->next;
}
val=parentptr->data;
}
return val;
}
