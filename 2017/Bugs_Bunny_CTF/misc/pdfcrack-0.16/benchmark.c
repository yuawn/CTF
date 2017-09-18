/**
 * Copyright (C) 2006-2015 Henning Norén
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

#include <stdio.h>
#include <signal.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include "benchmark.h"
#include "common.h"
#include "md5.h"
#include "rc4.h"
#include "sha256.h"
#include "pdfcrack.h"

#define COMMON_MD5_SIZE 88
#define COMMON_SHA256_SIZE 40
#define COMMON_SHA256_SLOW_SIZE 56

#define BENCHINTERVAL 3 /** The interval to run the specific benchmarks */

static volatile bool finished = false;

/** interruptBench is used to stop the current benchmark */
static void
interruptBench() {
  finished = true;
}

/** print_and_clean was supposed to make the binary somewhat smaller but
    I think I failed and have not bothered to investigate it further (like 
    checking if the function is inlined or if one can force it to not be 
    inline). As this stuff is pretty boring and not critical to performance I 
    would prefer that all the boring stuff between benchmarks would be as 
    small as possible.
*/
static void
print_and_clean(const char *str, unsigned int nrprocessed,
		const clock_t *start, const clock_t *end) {
  printf("%s\t%.1f\n", str, 
	 nrprocessed/(((double)(*end-*start))/CLOCKS_PER_SEC));
  cleanPDFCrack();
  finished = false;
}

static void
sha256_bench(void) {
  uint8_t *buf;
  uint8_t hash[32];
  unsigned int nrprocessed = 0;
  clock_t startTime, endTime;

  buf = calloc(COMMON_SHA256_SLOW_SIZE, sizeof(uint8_t));

  alarm(BENCHINTERVAL);
  startTime = clock();
  while(!finished) {
    sha256f(buf, COMMON_SHA256_SIZE, hash);
    buf[0]++;
    nrprocessed++;
  }
  endTime = clock();
  print_and_clean("SHA256 (fast):\t", nrprocessed, &startTime, &endTime);

  buf[0] = 0;
  nrprocessed = 0;
  alarm(BENCHINTERVAL);
  startTime = clock();
  while(!finished) {
    sha256(buf, COMMON_SHA256_SLOW_SIZE, hash);
    buf[0]++;
    nrprocessed++;
  }
  endTime = clock();
  print_and_clean("SHA256 (slow):\t", nrprocessed, &startTime, &endTime);
  free(buf);
}


static void
md5_bench(void) {
  uint8_t *buf;
  uint8_t digest[16];
  unsigned int nrprocessed = 0;
  clock_t startTime, endTime;

  buf = calloc(COMMON_MD5_SIZE, sizeof(uint8_t));

  alarm(BENCHINTERVAL);
  startTime = clock();
  while(!finished) {
    md5(buf, COMMON_MD5_SIZE, digest);
    buf[0]++;
    nrprocessed++;
  }
  endTime = clock();
  print_and_clean("MD5:\t\t", nrprocessed, &startTime, &endTime);
  free(buf);
}

static void 
md5_50_bench(void) {
  uint8_t *buf;
  unsigned int nrprocessed = 0;
  clock_t startTime, endTime;
  int i;
  
  buf = calloc(16, sizeof(uint8_t));
  md5_50_init(16);
  alarm(BENCHINTERVAL);
  startTime = clock();
  while(!finished) {
    md5_50(buf, 16);
    buf[0]++;
    nrprocessed++;
  }
  endTime = clock();
  print_and_clean("MD5_50 (fast):\t", nrprocessed, &startTime, &endTime);

  buf[0] = 0;
  nrprocessed = 0;
  alarm(BENCHINTERVAL);
  startTime = clock();
  while(!finished) {
    for(i=0; i<50; i++) { md5(buf, 16, buf); }
    buf[0]++;
    nrprocessed++;
  }
  endTime = clock();
  print_and_clean("MD5_50 (slow):\t", nrprocessed, &startTime, &endTime);

  free(buf);
}

static void
rc4_bench(void) {
  uint8_t *enckey;
  uint8_t match[32] = {0xDE, 0xAD, 0xBE, 0xAD,
		       0xDE, 0xAD, 0xBE, 0xAD,
		       0xDE, 0xAD, 0xBE, 0xAD,
		       0xDE, 0xAD, 0xBE, 0xAD,
		       0xDE, 0xAD, 0xBE, 0xAD,
		       0xDE, 0xAD, 0xBE, 0xAD,
		       0xDE, 0xAD, 0xBE, 0xAD,
		       0xDE, 0xAD, 0xBE, 0xAD};
  uint8_t cipher[32] = {0xBE, 0xAD, 0xDE, 0xAD,
			0xBE, 0xAD, 0xDE, 0xAD,
			0xBE, 0xAD, 0xDE, 0xAD,
			0xBE, 0xAD, 0xDE, 0xAD,
			0xBE, 0xAD, 0xDE, 0xAD,
			0xBE, 0xAD, 0xDE, 0xAD,
			0xBE, 0xAD, 0xDE, 0xAD,
			0xBE, 0xAD, 0xDE, 0xAD};
  unsigned int nrprocessed = 0;
  clock_t startTime, endTime;

  enckey = calloc(16, sizeof(uint8_t));

  alarm(BENCHINTERVAL);
  startTime = clock();
  while(!finished) {
    rc4Match40b(enckey, cipher, match);
    enckey[0]++;
    nrprocessed++;
  }
  endTime = clock();
  print_and_clean("RC4 (40, static):", nrprocessed, &startTime, &endTime);
  setrc4DecryptMethod(40);
  nrprocessed = 0;
  alarm(BENCHINTERVAL);
  startTime = clock();
  while(!finished) {
    rc4Decrypt(enckey, cipher, 3, match);
    enckey[0]++;
    nrprocessed++;
  }
  endTime = clock();
  print_and_clean("RC4 (40, no check):", nrprocessed, &startTime, &endTime);
 
  setrc4DecryptMethod(128);
  nrprocessed = 0;
  alarm(BENCHINTERVAL);
  startTime = clock();
  while(!finished) {
    rc4Decrypt(enckey, cipher, 3, match);
    enckey[0]++;
    nrprocessed++;
  }
  endTime = clock();
  print_and_clean("RC4 (128, no check):", nrprocessed, &startTime, &endTime);

  free(enckey);
}

static const uint8_t password[] = "Forty-Two is the Ultimate Answer";
static char handler[] = "Standard";
static const char charset[] = "abcdefghij";

static void
pdf_128b_bench(void) {
  clock_t startTime, endTime;
  uint8_t o_string[32] =   { 0xcf, 0xeb, 0x57, 0x1b, 0xa4, 0x56, 0x35, 0x19,
			     0x4e, 0x09, 0x95, 0x24, 0x23, 0xf3, 0x9b, 0x81,
			     0x05, 0xae, 0xbc, 0xb2, 0x8c, 0x18, 0xd2, 0xbb,
			     0xff, 0x00, 0xc9, 0xaa, 0x3f, 0x36, 0xe3, 0x13 };
  uint8_t u_string[32] =   { 0x72, 0xf6, 0x56, 0x9e, 0xda, 0x7d, 0x20, 0x1a,
			     0x10, 0x6d, 0x8a, 0x5b, 0xfa, 0xb2, 0xe9, 0xc0,
			     0x28, 0xbf, 0x4e, 0x5e, 0x4e, 0x75, 0x8a, 0x41,
			     0x64, 0x00, 0x4e, 0x56, 0xff, 0xfa, 0x01, 0x08 }; 
  uint8_t fileid[16] =     { 0xc9, 0xaa, 0x55, 0xc3, 0x6f, 0x3f, 0x5e, 0x84,
			     0x0d, 0x3d, 0x96, 0x8b, 0x97, 0xdb, 0xb2, 0xfe };
  EncData e = {
    handler,
    o_string,
    u_string,
    fileid,
    true,
    16, 1, 4, 128, -2359344, 3, 2
  };

  initPDFCrack(&e, NULL, true, NULL, Generative, NULL, charset, 0, 4, true);

  startTime = clock();
  runCrackRev3();
  endTime = clock();
  print_and_clean("PDF (128, user):", getNrProcessed(), &startTime, &endTime);

  initPDFCrack(&e, NULL, false, NULL, Generative, NULL, charset, 0, 4, true);

  startTime = clock();
  runCrackRev3_o();
  endTime = clock();

  print_and_clean("PDF (128, owner):", getNrProcessed(), &startTime, &endTime);

  initPDFCrack(&e,password, false, NULL, Generative, NULL, charset, 0, 4,true);

  startTime = clock();
  runCrackRev3_of();
  endTime = clock();

  print_and_clean("PDF (128, owner, fast):", 
		  getNrProcessed(), &startTime, &endTime);
}

static void
pdf_40b_bench(void) {
  clock_t startTime, endTime;
  uint8_t o_string[32] =   { 0xb7, 0x81, 0xc8, 0x3d, 0x93, 0x79, 0x21, 0xcc,
			     0x0f, 0x3d, 0x40, 0xed, 0x18, 0xe7, 0x7f, 0x7e,
			     0xc0, 0x15, 0xb1, 0x63, 0xf5, 0xc8, 0x34, 0xe0,
			     0x54, 0x37, 0x41, 0x29, 0xe7, 0xc5, 0x1d, 0xe3 };
  uint8_t u_string[32] =   { 0x61, 0x74, 0x7c, 0x5c, 0xb5, 0x38, 0x3d, 0xdd,
			     0x6f, 0xcb, 0xb2, 0xf2, 0xfe, 0xe3, 0x34, 0x8d,
			     0x81, 0xe2, 0x49, 0x99, 0xc4, 0x14, 0xf6, 0x6f,
			     0xd0, 0x0f, 0x97, 0xe8, 0xb8, 0x29, 0xe6, 0x27 };
  uint8_t fileid[16] =     { 0x21, 0x76, 0x36, 0x66, 0x67, 0xf0, 0x86, 0xd5,
			     0x09, 0x88, 0xc3, 0xa7, 0xe9, 0x3a, 0x92, 0xca };
  EncData e = {
    handler,
    o_string,
    u_string,
    fileid,
    true,
    16, 1, 4, 40, -64, 2, 1
  };

  initPDFCrack(&e, NULL, true, NULL, Generative, NULL, charset, 0, 5, true);

  startTime = clock();
  runCrackRev2();
  endTime = clock();

  print_and_clean("PDF (40, user):\t",getNrProcessed(),&startTime, &endTime);

  initPDFCrack(&e, NULL, false, NULL, Generative, NULL, charset, 0, 5, true);

  startTime = clock();
  runCrackRev2_o();
  endTime = clock();

  print_and_clean("PDF (40, owner):",getNrProcessed(), &startTime, &endTime);
  initPDFCrack(&e, password, false, NULL, Generative, NULL, charset,0, 5,true);

  startTime = clock();
  runCrackRev2_of();
  endTime = clock();

  print_and_clean("PDF (40, owner, fast):",
		  getNrProcessed(), &startTime, &endTime);
}

void
runBenchmark(void) {
  struct sigaction act;
  act.sa_handler = interruptBench;
  sigemptyset(&act.sa_mask);
  act.sa_flags = 0;
  sigaction(SIGALRM, &act, 0);

  printf("Benchmark:\tAverage Speed (calls / second):\n");
  sha256_bench();
  printf("\n");
  md5_bench();
  md5_50_bench();
  printf("\n");
  rc4_bench();
  printf("\n");
  printf("Benchmark:\tAverage Speed (passwords / second):\n");
  pdf_40b_bench();
  printf("\n");
  pdf_128b_bench();

  return;
}
