/**
 * Copyright (C) 2014-2015 Henning Norén
 * Copyright (C) 1996-2011 Glyph & Cog, LLC
 * 
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, 
 * USA.
 */

#include "sha256.h"
#include "string.h"

/** Rotate right  **/
#define ROTR(x, n) (( x >> n ) | ( x << (32 - n)))

#define Choice(x, y, z) ( z ^ ( x & ( y ^ z )))
#define Majority(x, y, z) (( x & y ) ^ ( z & ( x ^ y )))

#define Sigma0(x) (ROTR(x, 2) ^ ROTR(x, 13) ^ ROTR(x, 22))
#define Sigma1(x) (ROTR(x, 6) ^ ROTR(x, 11) ^ ROTR(x, 25))

#define sigma0(x) (ROTR(x, 7) ^ ROTR(x, 18) ^ (x >> 3))
#define sigma1(x) (ROTR(x, 17) ^ ROTR(x, 19) ^ (x >> 10))

#define ROUND(a,b,c,d,e,f,g,h,k,data)			\
  h += Sigma1(e) + Choice(e, f, g) + k + data;		\
  d += h;						\
  h += Sigma0(a) + Majority(a ,b ,c);

static void sha256HashBlock(const uint8_t *blk, uint32_t *hash) {
  uint32_t W[64];
  uint32_t A, B, C, D, E, F, G, H;
  int i;

  /* 1. Prepare the message schedule */
  for (i = 0; i < 16; ++i) {
    W[i] = ((unsigned)blk[i*4    ] << 24) 
         | ((unsigned)blk[i*4 + 1] << 16) 
         | ((unsigned)blk[i*4 + 2] << 8) 
         |  blk[i*4 + 3];
  }
  for (; i < 64; ++i) {
    W[i] = sigma1(W[i-2]) + W[i-7] + sigma0(W[i-15]) + W[i-16];
  }

  /* 2. Initialize the eight working variables */
  A = hash[0];
  B = hash[1];
  C = hash[2];
  D = hash[3];
  E = hash[4];
  F = hash[5];
  G = hash[6];
  H = hash[7];
  
  /* 3. Compression loop unrolled */
  ROUND(A, B, C, D, E, F, G, H, 0x428a2f98, W[ 0]);
  ROUND(H, A, B, C, D, E, F, G, 0x71374491, W[ 1]);
  ROUND(G, H, A, B, C, D, E, F, 0xB5C0FBCF, W[ 2]);
  ROUND(F, G, H, A, B, C, D, E, 0xE9B5DBA5, W[ 3]);
  ROUND(E, F, G, H, A, B, C, D, 0x3956C25B, W[ 4]);
  ROUND(D, E, F, G, H, A, B, C, 0x59F111F1, W[ 5]);
  ROUND(C, D, E, F, G, H, A, B, 0x923F82A4, W[ 6]);
  ROUND(B, C, D, E, F, G, H, A, 0xAB1C5ED5, W[ 7]);
  ROUND(A, B, C, D, E, F, G, H, 0xD807AA98, W[ 8]);
  ROUND(H, A, B, C, D, E, F, G, 0x12835B01, W[ 9]);
  ROUND(G, H, A, B, C, D, E, F, 0x243185BE, W[10]);
  ROUND(F, G, H, A, B, C, D, E, 0x550C7DC3, W[11]);
  ROUND(E, F, G, H, A, B, C, D, 0x72BE5D74, W[12]);
  ROUND(D, E, F, G, H, A, B, C, 0x80DEB1FE, W[13]);
  ROUND(C, D, E, F, G, H, A, B, 0x9BDC06A7, W[14]);
  ROUND(B, C, D, E, F, G, H, A, 0xC19BF174, W[15]); 
  ROUND(A, B, C, D, E, F, G, H, 0xE49B69C1, W[16]);
  ROUND(H, A, B, C, D, E, F, G, 0xEFBE4786, W[17]);
  ROUND(G, H, A, B, C, D, E, F, 0x0FC19DC6, W[18]);
  ROUND(F, G, H, A, B, C, D, E, 0x240CA1CC, W[19]);
  ROUND(E, F, G, H, A, B, C, D, 0x2DE92C6F, W[20]);
  ROUND(D, E, F, G, H, A, B, C, 0x4A7484AA, W[21]);
  ROUND(C, D, E, F, G, H, A, B, 0x5CB0A9DC, W[22]);
  ROUND(B, C, D, E, F, G, H, A, 0x76F988DA, W[23]);
  ROUND(A, B, C, D, E, F, G, H, 0x983E5152, W[24]);
  ROUND(H, A, B, C, D, E, F, G, 0xA831C66D, W[25]);
  ROUND(G, H, A, B, C, D, E, F, 0xB00327C8, W[26]);
  ROUND(F, G, H, A, B, C, D, E, 0xBF597FC7, W[27]);
  ROUND(E, F, G, H, A, B, C, D, 0xC6E00BF3, W[28]);
  ROUND(D, E, F, G, H, A, B, C, 0xD5A79147, W[29]);
  ROUND(C, D, E, F, G, H, A, B, 0x06CA6351, W[30]);
  ROUND(B, C, D, E, F, G, H, A, 0x14292967, W[31]);
  ROUND(A, B, C, D, E, F, G, H, 0x27B70A85, W[32]);
  ROUND(H, A, B, C, D, E, F, G, 0x2E1B2138, W[33]);
  ROUND(G, H, A, B, C, D, E, F, 0x4D2C6DFC, W[34]);
  ROUND(F, G, H, A, B, C, D, E, 0x53380D13, W[35]);
  ROUND(E, F, G, H, A, B, C, D, 0x650A7354, W[36]);
  ROUND(D, E, F, G, H, A, B, C, 0x766A0ABB, W[37]);
  ROUND(C, D, E, F, G, H, A, B, 0x81C2C92E, W[38]);
  ROUND(B, C, D, E, F, G, H, A, 0x92722C85, W[39]);
  ROUND(A, B, C, D, E, F, G, H, 0xA2BFE8A1, W[40]);
  ROUND(H, A, B, C, D, E, F, G, 0xA81A664B, W[41]);
  ROUND(G, H, A, B, C, D, E, F, 0xC24B8B70, W[42]);
  ROUND(F, G, H, A, B, C, D, E, 0xC76C51A3, W[43]);
  ROUND(E, F, G, H, A, B, C, D, 0xD192E819, W[44]);
  ROUND(D, E, F, G, H, A, B, C, 0xD6990624, W[45]);
  ROUND(C, D, E, F, G, H, A, B, 0xF40E3585, W[46]);
  ROUND(B, C, D, E, F, G, H, A, 0x106AA070, W[47]);
  ROUND(A, B, C, D, E, F, G, H, 0x19A4C116, W[48]);
  ROUND(H, A, B, C, D, E, F, G, 0x1E376C08, W[49]);
  ROUND(G, H, A, B, C, D, E, F, 0x2748774C, W[50]);
  ROUND(F, G, H, A, B, C, D, E, 0x34B0BCB5, W[51]);
  ROUND(E, F, G, H, A, B, C, D, 0x391C0CB3, W[52]);
  ROUND(D, E, F, G, H, A, B, C, 0x4ED8AA4A, W[53]);
  ROUND(C, D, E, F, G, H, A, B, 0x5B9CCA4F, W[54]);
  ROUND(B, C, D, E, F, G, H, A, 0x682E6FF3, W[55]);
  ROUND(A, B, C, D, E, F, G, H, 0x748F82EE, W[56]);
  ROUND(H, A, B, C, D, E, F, G, 0x78A5636F, W[57]);
  ROUND(G, H, A, B, C, D, E, F, 0x84C87814, W[58]);
  ROUND(F, G, H, A, B, C, D, E, 0x8CC70208, W[59]);
  ROUND(E, F, G, H, A, B, C, D, 0x90BEFFFA, W[60]);
  ROUND(D, E, F, G, H, A, B, C, 0xA4506CEB, W[61]);
  ROUND(C, D, E, F, G, H, A, B, 0xBEF9A3F7, W[62]);
  ROUND(B, C, D, E, F, G, H, A, 0xC67178F2, W[63]);
  
  /* 4. Compute the intermediate hash value */
  hash[0] += A;
  hash[1] += B;
  hash[2] += C;
  hash[3] += D;
  hash[4] += E;
  hash[5] += F;
  hash[6] += G;
  hash[7] += H;
}

void sha256(const uint8_t *msg, const int msgLen, uint8_t *hash) {
  uint8_t blk[64];
  uint32_t H[8];
  int blkLen, i;

  H[0] = 0x6a09e667;
  H[1] = 0xbb67ae85;
  H[2] = 0x3c6ef372;
  H[3] = 0xa54ff53a;
  H[4] = 0x510e527f;
  H[5] = 0x9b05688c;
  H[6] = 0x1f83d9ab;
  H[7] = 0x5be0cd19;

  for (i = 0; i + 64 <= msgLen; i += 64) {
    sha256HashBlock(msg+i, H);
  }
  blkLen = msgLen - i;
  memcpy(blk, msg + i, blkLen);

  /* pad the message */
  blk[blkLen++] = 0x80;
  if (blkLen > 56) {
    while (blkLen < 64) {
      blk[blkLen++] = 0;
    }
    sha256HashBlock(blk, H);
    blkLen = 0;
  }
  while (blkLen < 56) {
    blk[blkLen++] = 0;
  }
  blk[56] = 0;
  blk[57] = 0;
  blk[58] = 0;
  blk[59] = 0;
  blk[60] = (uint8_t)(msgLen >> 21);
  blk[61] = (uint8_t)(msgLen >> 13);
  blk[62] = (uint8_t)(msgLen >> 5);
  blk[63] = (uint8_t)(msgLen << 3);
  sha256HashBlock(blk, H);

  /* copy the output into the buffer (convert words to bytes) */
  for (i = 0; i < 8; ++i) {
    hash[i*4]     = (uint8_t)(H[i] >> 24);
    hash[i*4 + 1] = (uint8_t)(H[i] >> 16);
    hash[i*4 + 2] = (uint8_t)(H[i] >> 8);
    hash[i*4 + 3] = (uint8_t)H[i];
  }
}

/** Fast sha256 for msgLen < 56 */
void sha256f(const uint8_t *msg, const int msgLen, uint8_t *hash) {
  uint8_t blk[64];
  uint32_t H[8];
  int blkLen, i;

  H[0] = 0x6a09e667;
  H[1] = 0xbb67ae85;
  H[2] = 0x3c6ef372;
  H[3] = 0xa54ff53a;
  H[4] = 0x510e527f;
  H[5] = 0x9b05688c;
  H[6] = 0x1f83d9ab;
  H[7] = 0x5be0cd19;

  blkLen = msgLen;
  memcpy(blk, msg, blkLen);

  /* pad the message */
  blk[blkLen++] = 0x80;

  while (blkLen < 56) {
    blk[blkLen++] = 0;
  }
  blk[56] = 0;
  blk[57] = 0;
  blk[58] = 0;
  blk[59] = 0;
  blk[60] = (uint8_t)(msgLen >> 21);
  blk[61] = (uint8_t)(msgLen >> 13);
  blk[62] = (uint8_t)(msgLen >> 5);
  blk[63] = (uint8_t)(msgLen << 3);
  sha256HashBlock(blk, H);

  /* copy the output into the buffer (convert words to bytes) */
  for (i = 0; i < 8; ++i) {
    hash[i*4    ] = (uint8_t)(H[i] >> 24);
    hash[i*4 + 1] = (uint8_t)(H[i] >> 16);
    hash[i*4 + 2] = (uint8_t)(H[i] >> 8);
    hash[i*4 + 3] = (uint8_t)H[i];
  }
}
