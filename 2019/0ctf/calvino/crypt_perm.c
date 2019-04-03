/* vi:set ts=8 sts=4 sw=4 noet:
 *
 * VIM - Vi IMproved	by Bram Moolenaar
 *
 * Do ":help uganda"  in Vim to read copying and usage conditions.
 * Do ":help credits" in Vim to see a list of people who contributed.
 * See README.txt for an overview of the Vim source code.
 */

/*
 * crypt_perm.c: Permutation encryption support.
 */
#include "vim.h"

#if defined(FEAT_CRYPT) || defined(PROTO)
// "...literature itself is merely the permutation of a finite set of elements and functions..."
// "...but constantly straining to escape from the bonds of this finite quantity..."
/* 
 * Just a weird homemade permutation algorithm. 
 * At least it's reversible.
 * TODO: Add support for large file. Currently it only works for small file.
 */

/* The state of encryption, referenced by cryptstate_T. */
typedef struct {
    int key;
    int shift;
    int step;
    int orig_size;
    int size;
    int cur_idx;
    char_u *buffer;
} perm_state_T;

    int
is_prime(int p)
{
    // since p should be small
    int tmp;
    tmp = 2;
    while (tmp*tmp<=p)
    {
        if (p%tmp==0)
            return FALSE;
        tmp++;
    }
    return TRUE;
}

    void
crypt_perm_init(
    cryptstate_T    *state,
    char_u	    *key,
    char_u	    *salt UNUSED,
    int		    salt_len UNUSED,
    char_u	    *seed UNUSED,
    int		    seed_len UNUSED)
{
    char_u	*p;
    perm_state_T	*ps;

    ps = (perm_state_T *)alloc(sizeof(perm_state_T));
    ps->key = 0;
    state->method_state = ps;

    for (p = key; *p != NUL; ++p)
    {
    ps->key = 131*ps->key + *p;
    }
}

    void
crypt_perm_encode(
    cryptstate_T *state,
    char_u	*from,
    size_t	len,
    char_u	*to)
{
    perm_state_T *ps = state->method_state;
    size_t	i;

    /* 
     * A dirty way to introduce IV: using the first 4 bytes and keeping them unchanged 
     */
    if (len<=4)
    {
        for (i = 0; i < len; ++i)
            to[i] = from[i];
        return;
    }

    unsigned int iv;

    for (i = 0; i < 4; ++i)
    {
        to[i] = from[i];
        iv = (iv<<8) + from[i];
    }
    ps->orig_size = len-4;
    ps->size = ps->orig_size;
    /* We need a prime order for reversibility */
    while (!is_prime(ps->size))
        ps->size++;

    ps->shift = ps->key % (len-4);
    if (ps->shift > 0)
        ps->buffer = alloc(ps->shift);
    /* Xor with iv so that we have different value for addition and multiplication */
    ps->step = ps->key ^ iv;
    /* Do not forget the corner case */
    if (ps->step % ps->size == 0)
        ps->step++;
    ps->cur_idx = 0;

    /* Step 1: Addition */
    for (i = 0; i < ps->shift; ++i)
        ps->buffer[i] = from[len-ps->shift+i];
    for (i = len-1; i >= 4+ps->shift; --i)
        from[i] = from[i-ps->shift];
    for (i = 0; i < ps->shift; ++i)
        from[i+4] = ps->buffer[i];

    /* Step 2: Multiplication */
    i = 4;
    while (i < len)
    {
        if (ps->cur_idx < ps->orig_size)
        {
            to[i] = from[ps->cur_idx+4];
            i++;
        }
        ps->cur_idx = (ps->cur_idx+ps->step)%ps->size;
    }

    /* We should recover the "from" array */
    for (i = 0; i < ps->shift; ++i)
        ps->buffer[i] = from[i+4];
    for (i = 4+ps->shift; i < len; ++i)
        from[i-ps->shift] = from[i];
    for (i = 0; i < ps->shift; ++i)
        from[len-ps->shift+i] = ps->buffer[i];

    if (ps->shift > 0)
        vim_free(ps->buffer);
}

    void
crypt_perm_decode(
    cryptstate_T *state,
    char_u	*from,
    size_t	len,
    char_u	*to)
{
    perm_state_T *ps = state->method_state;
    size_t	i;

    if (len<=4)
    {
        for (i = 0; i < len; ++i)
            to[i] = from[i];
        return;
    }

    unsigned int iv;
    for (i = 0; i < 4; ++i)
    {
        to[i] = from[i];
        iv = (iv<<8) + from[i];
    }
    ps->orig_size = len-4;
    ps->size = ps->orig_size;
    while (!is_prime(ps->size))
        ps->size++;

    ps->shift = ps->key % (len-4);
    if (ps->shift > 0)
        ps->buffer = alloc(ps->shift);
    ps->step = ps->key ^ iv;
    if (ps->step % ps->size == 0)
        ps->step++;
    ps->cur_idx = 0;

    /* Step 1: Inverse of Multiplication */
    i = 4;
    while (i < len)
    {
        if (ps->cur_idx < ps->orig_size)
        {
            to[ps->cur_idx+4] = from[i];
            i++;
        }
        ps->cur_idx = (ps->cur_idx+ps->step)%ps->size;
    }

    /* Step 2: Inverse of Addition */
    for (i = 0; i < ps->shift; ++i)
        ps->buffer[i] = to[i+4];
    for (i = 4+ps->shift; i < len; ++i)
        to[i-ps->shift] = to[i];
    for (i = 0; i < ps->shift; ++i)
        to[len-ps->shift+i] = ps->buffer[i];

    if (ps->shift > 0)
        vim_free(ps->buffer);
}

#endif /* FEAT_CRYPT */