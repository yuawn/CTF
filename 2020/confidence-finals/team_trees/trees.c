#include <stdio.h>
#include <stdlib.h>


struct Node{
    int n;
    int gap;
    struct Node *chds[3];
};


struct Node* init_list( int n ){
    struct Node* root = malloc(0x20);
    root->n = 0;

    for ( int i = 0; i < n; ++i )
    {
        struct Node* new = malloc(0x20);
        new->n = 1;
        new->chds[0] = root;
        root = new;
    }

    return root;
}


struct Node* deep_copy(struct Node *a){
    struct Node *b = malloc(0x20);

    if ( !b )
    {
        puts("Out of memory ;_;");
        abort();
    }

    b->n = a->n;
    for ( int i = 0; a->n > i; ++i )
        b->chds[i] = deep_copy(a->chds[i]);

    return b;
}


int check( struct Node *node , int _p ){
    //puts("check");
    int p = _p;

    if ( node->n > 1 && _p )
        return 0;

    if ( node->n > _p ){
        p = node->n;
    }

    int p2 = p - 1;
    if ( p2 < 0 )
        p2 = 0;

    for ( int i = 0; node->n > i; ++i )
    {
        if ( check(node->chds[i], p2) ^ 1 )
            return 0;
    }
    return 1;
}

int traverse( struct Node* node ){
    //puts("traverse");
    if ( !node->n )
        return 0;

    for ( int i = 0; node->n > i; ++i )
    {
        if ( traverse(node->chds[i]) )
            return 1;
    }

    if ( node->n > 2 )
    {
        node->n = 1;
        return 0;
    }
    else
    {
        node->chds[node->n] = deep_copy(node->chds[0]);
        ++node->n;
        return 1;
    }

}


void swap(uint64_t *x, uint64_t *y)
{
	*x ^= *y;
	*y ^= *x;
	*x ^= *y;
}


int main(){

    uint64_t ans = 4647842135137215109;
    uint64_t rdx = 0x82F96AC97429A68B;
    uint64_t rcx = 0x32B9B6BCA55548ED;

    // 40000000000
    for( uint64_t i = 0 ; i < ans ; ++i ){
        if( i % 10000000 == 0 )
            printf( "%lld\n" , i );

        rdx = rdx + rdx * 2;
        rdx = rdx + rcx*2 + 4;
        uint64_t t = rdx;
        rdx = rcx;
        rcx = t;
        //swap( &rdx, &rcx );

        if( i > 3 && ( rdx == 0x82F96AC97429A68B || rdx == 0x32B9B6BCA55548ED ) ){
            printf( "%lld\n" , i );
            break;
        }
    }

    return 0;


/*
    struct Node *root = init_list(4);

    long ans = 0;


    do{
        if( check( root , 0 ) ){
            ++ans;
            //printf( "root->n = %d\n" , root->n );
            printf( "%lld\n" , ans );
        }
    }while( traverse(root) );
*/

}

/*
1 3
2 5
3 15


*/