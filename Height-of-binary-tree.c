# Height of a binary Tree Hackerrank solution

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

struct node* insert( struct node* root, int data ) {
		
	if(root == NULL) {
	
        struct node* node = (struct node*)malloc(sizeof(struct node));

        node->data = data;

        node->left = NULL;
        node->right = NULL;
        return node;
	  
	} else {
      
		struct node* cur;
		
		if(data <= root->data) {
            cur = insert(root->left, data);
            root->left = cur;
		} else {
            cur = insert(root->right, data);
            root->right = cur;
		}
	
		return root;
	}
}


int getHeight(struct node* root) {
    // Write your code here
   // int lefth=0,righth=0;
    if(root==NULL)
    return 0;
   
    else{
        int lefth=getHeight(root->left);
        int righth=getHeight(root->right);
        if(lefth>righth)
        return (lefth+1);
        else 
        return (righth+1);
       
    }
}


int main() {
  
    struct node* root = NULL;
    
    int t;
    int data;

    scanf("%d", &t);

    while(t-- > 0) {
        scanf("%d", &data);
        root = insert(root, data);
    }
  
	printf("%d",getHeight(root));
    return 0;
}
