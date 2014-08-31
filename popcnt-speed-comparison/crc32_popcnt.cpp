// (c) Peter Kankowski, 2010. http://www.strchr.com  mailto:kankowski@narod.ru
// CRC-32C and population count benchmark

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#include <x86intrin.h>

#ifndef _DEBUG
//#define HTML_OUTPUT 
#endif

#define NUM_OF(A) (sizeof(A)/sizeof((A)[0]))

// ======= CRC ========

typedef uint32_t RES; // result type (32-bit for CRC32)
typedef RES (*CRC_FUNC) (const uint8_t *, size_t);

#define CRCPOLY 0x82f63b78 // reversed 0x1EDC6F41
#define CRCINIT 0xFFFFFFFF

static size_t Min(size_t x, size_t y) {
	// Branchless minimum (from http://graphics.stanford.edu/~seander/bithacks.html#IntegerMinOrMax)
	//return y ^ ((x ^ y) & -(x < y));
	return (x < y) ? x : y; // CMOV is used when /arch:SSE2 is on
}



// Algorithm by Dilip V. Sarwate (used in most programs)
uint32_t g_crc_precalc[256];

static void CRC_Init() {
	for (uint32_t i = 0; i <= 0xFF; i++) {
		uint32_t x = i;
		for (uint32_t j = 0; j < 8; j++)
			x = (x>>1) ^ (CRCPOLY & (-(INT)(x & 1)));
		g_crc_precalc[i] = x;
	}
}

static RES CRC_Sarwate(const BYTE* buf, size_t len) {
	RES crc = CRCINIT;
	const BYTE * end = buf + len;
	while (buf < end)
		crc = (crc >> 8) ^ g_crc_precalc[ (crc ^ *buf++) & 0xFF];
	return ~crc;
}



// Slicing-by-4 and slicing-by-8 algorithms by Michael E. Kounavis and Frank L. Berry from Intel Corp.
// http://www.intel.com/technology/comms/perfnet/download/CRC_generators.pdf

uint32_t g_crc_slicing[8][256];

static void CRC_SlicingInit() {
	for (uint32_t i = 0; i <= 0xFF; i++) {
		uint32_t x = i;
		for (uint32_t j = 0; j < 8; j++)
			x = (x>>1) ^ (CRCPOLY & (-(INT)(x & 1)));
		g_crc_slicing[0][i] = x;
	}

	for (uint32_t i = 0; i <= 0xFF; i++) {
		uint32_t c = g_crc_slicing[0][i];
		for (uint32_t j = 1; j < 8; j++) {
			c = g_crc_slicing[0][c & 0xFF] ^ (c >> 8);
			g_crc_slicing[j][i] = c;
		}
	}
}

static RES CRC_SlicingBy4(const BYTE* buf, size_t len) {
	RES crc = CRCINIT;

	// Align to DWORD boundary
	size_t align = (sizeof(DWORD) - (INT_PTR)buf) & (sizeof(DWORD) - 1);
	align = Min(align, len);
	len -= align;
	for (; align; align--)
		crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);

	size_t ndwords = len / sizeof(DWORD);
	for (; ndwords; ndwords--) {
		crc ^= *(DWORD*)buf;
		crc =
			g_crc_slicing[3][(crc      ) & 0xFF] ^
			g_crc_slicing[2][(crc >>  8) & 0xFF] ^
			g_crc_slicing[1][(crc >> 16) & 0xFF] ^
			g_crc_slicing[0][(crc >> 24)];
		buf += sizeof(DWORD);
	}

	len &= sizeof(DWORD) - 1;
	for (; len; len--)
		crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);
	return ~crc;
}

/*
static RES CRC_SlicingBy8_NoAlign(const BYTE* buf, size_t len) {
	RES crc = CRCINIT;
	size_t nqwords = len / (sizeof(DWORD) + sizeof(DWORD));
	for (; nqwords; nqwords--) {
		crc ^= *(DWORD*)buf;
		buf += sizeof(DWORD);
		uint32_t next = *(DWORD*)buf;
		buf += sizeof(DWORD);
		crc =
			g_crc_slicing[7][(crc      ) & 0xFF] ^
			g_crc_slicing[6][(crc >>  8) & 0xFF] ^
			g_crc_slicing[5][(crc >> 16) & 0xFF] ^
			g_crc_slicing[4][(crc >> 24)] ^
			g_crc_slicing[3][(next      ) & 0xFF] ^
			g_crc_slicing[2][(next >>  8) & 0xFF] ^
			g_crc_slicing[1][(next >> 16) & 0xFF] ^
			g_crc_slicing[0][(next >> 24)];
	}
	len &= sizeof(DWORD) * 2 - 1;
	for (; len; len--)
		crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);
	return ~crc;
}

// Alignment loop suggested by Dmitry Kostjuchenko
static RES CRC_SlicingBy8_Portable(const BYTE* buf, size_t len) {
    RES crc = CRCINIT;
    while (((((intptr_t)buf) & (sizeof(DWORD)-1)) != 0) && (len != 0))
    {
        crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);
        -- len;
    }
    size_t nqwords = len / (sizeof(DWORD) + sizeof(DWORD));
    for (; nqwords; nqwords--) {
        crc ^= *(DWORD*)buf;
        buf += sizeof(DWORD);
        uint32_t next = *(DWORD*)buf;
        buf += sizeof(DWORD);
        crc =
            g_crc_slicing[7][(crc      ) & 0xFF] ^
            g_crc_slicing[6][(crc >>  8) & 0xFF] ^
            g_crc_slicing[5][(crc >> 16) & 0xFF] ^
            g_crc_slicing[4][(crc >> 24)] ^
            g_crc_slicing[3][(next      ) & 0xFF] ^
            g_crc_slicing[2][(next >>  8) & 0xFF] ^
            g_crc_slicing[1][(next >> 16) & 0xFF] ^
            g_crc_slicing[0][(next >> 24)];
    }
    len &= sizeof(DWORD) * 2 - 1;
    for (; len; len--)
        crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);
    return ~crc;
}*/

static RES CRC_SlicingBy8(const BYTE* buf, size_t len) {
	RES crc = CRCINIT;

	// Align to DWORD boundary
	size_t align = (sizeof(DWORD) - (INT_PTR)buf) & (sizeof(DWORD) - 1);
	align = Min(align, len);
	len -= align;
	for (; align; align--)
		crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);

	size_t nqwords = len / (sizeof(DWORD) + sizeof(DWORD));
	for (; nqwords; nqwords--) {
		crc ^= *(DWORD*)buf;
		buf += sizeof(DWORD);
		uint32_t next = *(DWORD*)buf;
		buf += sizeof(DWORD);
		crc =
			g_crc_slicing[7][(crc      ) & 0xFF] ^
			g_crc_slicing[6][(crc >>  8) & 0xFF] ^
			g_crc_slicing[5][(crc >> 16) & 0xFF] ^
			g_crc_slicing[4][(crc >> 24)] ^
			g_crc_slicing[3][(next      ) & 0xFF] ^
			g_crc_slicing[2][(next >>  8) & 0xFF] ^
			g_crc_slicing[1][(next >> 16) & 0xFF] ^
			g_crc_slicing[0][(next >> 24)];
	}

	len &= sizeof(DWORD) * 2 - 1;
	for (; len; len--)
		crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);
	return ~crc;
}




// This code is copyright © 1993 Richard Black. All rights are reserved. You may use this code
// only if it includes a statement to that effect.
// http://www.cl.cam.ac.uk/research/srg/bluebook/21/crc/node6.html#SECTION00064000000000000000
static RES CRC_RichardBlack(const BYTE* buf, size_t len) {
	RES crc = CRCINIT;

	// Align to DWORD boundary
	size_t align = (sizeof(DWORD) - (INT_PTR)buf) & (sizeof(DWORD) - 1);
	align = Min(align, len);
	len -= align;
	for (; align; align--)
		crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);

	size_t ndwords = len / sizeof(DWORD);
	for (; ndwords; ndwords--) {
		crc ^= *(DWORD*)buf;
		crc = g_crc_precalc[crc & 0xff] ^ (crc >> 8);
		crc = g_crc_precalc[crc & 0xff] ^ (crc >> 8);
		crc = g_crc_precalc[crc & 0xff] ^ (crc >> 8);
		crc = g_crc_precalc[crc & 0xff] ^ (crc >> 8);
		buf += sizeof(DWORD);
	}

	len &= sizeof(DWORD) - 1;
	for (; len; len--)
		crc = g_crc_precalc[(crc ^ *buf++) & 0xFF] ^ (crc >> 8);
	return ~crc;
}


// Hardware-accelerated CRC-32C (using CRC32 instruction)
static RES CRC_Hardware(const BYTE * buf, size_t len) {
	RES crc = CRCINIT;

	// Align to DWORD boundary
	size_t align = (sizeof(DWORD) - (INT_PTR)buf) & (sizeof(DWORD) - 1);
	align = Min(align, len);
	len -= align;
	for (; align; align--)
		crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);

	size_t ndwords = len / sizeof(DWORD);
	for (; ndwords; ndwords--) {
		crc = _mm_crc32_u32(crc, *(DWORD*)buf);
		buf += sizeof(DWORD);
	}

	len &= sizeof(DWORD) - 1;
	for (; len; len--)
		crc = _mm_crc32_u8(crc, *buf++);
	return ~crc;
}

static RES CRC_HardwareUnrolled(const BYTE * buf, size_t len) {
	RES crc = CRCINIT;

	// Align to DWORD boundary
	size_t align = (sizeof(DWORD) - (INT_PTR)buf) & (sizeof(DWORD) - 1);
	align = Min(align, len);
	len -= align;
	for (; align; align--)
		crc = g_crc_slicing[0][(crc ^ *buf++) & 0xFF] ^ (crc >> 8);

	size_t ndqwords = len / (sizeof(DWORD) * 4);
	for (; ndqwords; ndqwords--) {
		crc = _mm_crc32_u32(crc, *(DWORD*)buf);
		crc = _mm_crc32_u32(crc, *(DWORD*)(buf + sizeof(DWORD) ));
		crc = _mm_crc32_u32(crc, *(DWORD*)(buf + sizeof(DWORD) * 2 ));
		crc = _mm_crc32_u32(crc, *(DWORD*)(buf + sizeof(DWORD) * 3 ));
		buf += sizeof(DWORD) * 4;
	}

	len &= sizeof(DWORD) * 4 - 1;
	for (; len; len--)
		crc = _mm_crc32_u8(crc, *buf++);
	return ~crc;
}


// ======= POPCNT ========

// Modified from http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetParallel
// and http://www.hackersdelight.org/
static uint32_t PopCnt32(uint32_t v) {
	v = v - ((v >> 1) & 0x55555555);                    // reuse input as temporary
	v = (v & 0x33333333) + ((v >> 2) & 0x33333333);     // temp
	v = v + (v >> 4) & 0x0F0F0F0F;
	return (v * 0x01010101) >> 24; // count
}

/*static uint32_t PopCnt16(uint32_t v) {
	v = v - ((v >> 1) & 0x5555);                // reuse input as temporary
	v = (v & 0x3333) + ((v >> 2) & 0x3333);     // temp
	v = v + (v >> 4) & 0x0F0F;
	return v + (v >> 8) & 0x00FF; // count
}

static uint32_t PopCnt8(uint32_t v) {
	v = v - ((v >> 1) & 0x55);                // reuse input as temporary
	v = (v & 0x3333) + ((v >> 2) & 0x33);     // temp
	return v + (v >> 4) & 0x0F; // count
}

static RES POPCNT_BitHacks_NoAlign(const BYTE * buf, size_t len) {
	RES cnt = 0;
	size_t ndwords = len / sizeof(DWORD);
	for(; ndwords; ndwords--) {
		cnt += PopCnt32(*(DWORD*)buf);
		buf += sizeof(DWORD);
	}
	if (len & sizeof(WORD)) {
		cnt += PopCnt16(*(WORD*)buf);
		buf += sizeof(WORD);
	}
	if (len & sizeof(BYTE))
		cnt += PopCnt8(*buf);
	return cnt;
}*/


static RES POPCNT_BitHacks(const BYTE * buf, size_t len) {
	RES cnt = 0;

	// Align to DWORD boundary
	size_t align = (sizeof(DWORD) - (INT_PTR)buf) & (sizeof(DWORD) - 1);
	align = (len < align) ? 0 : align;
	if (align) {
		buf = (BYTE *)( (INT_PTR)buf & (-(INT_PTR)sizeof(DWORD)) );
		DWORD first = *(DWORD*)buf;
		first &= ~(0xFFFFFFFF >> (align * CHAR_BIT));
		cnt += PopCnt32(first);
		buf += sizeof(DWORD);
		len -= align;
	}
	
	size_t ndwords = len / sizeof(DWORD);
	for (; ndwords; ndwords--) {
		cnt += PopCnt32(*(DWORD*)buf);
		buf += sizeof(DWORD);
	}
	size_t remaining = len & (sizeof(DWORD) - 1);
	if (remaining) {
		DWORD last = *(DWORD*)buf;
		last &= ~(0xFFFFFFFF << (remaining * CHAR_BIT));
		cnt += PopCnt32(last);
	}
	return cnt;
}

// From http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetTable
static const unsigned char g_pop_cnt[256] = 
{
#   define B2(n) n,     n+1,     n+1,     n+2
#   define B4(n) B2(n), B2(n+1), B2(n+1), B2(n+2)
#   define B6(n) B4(n), B4(n+1), B4(n+1), B4(n+2)
    B6(0), B6(1), B6(1), B6(2)
};

static RES POPCNT_Table(const BYTE * buf, size_t len) {
	RES cnt = 0;
	size_t ndwords = len / 4;
	for(; ndwords; ndwords--) {
		uint32_t v = *(DWORD*)buf;
		cnt += g_pop_cnt[v & 0xff] + 
			   g_pop_cnt[(v >> 8) & 0xff] + 
			   g_pop_cnt[(v >> 16) & 0xff] + 
			   g_pop_cnt[v >> 24];
		buf += 4;
	}
	if (len & 2) {
		uint32_t v = *(WORD*)buf;
		cnt += g_pop_cnt[ v & 0xff ] +
			   g_pop_cnt[ v >> 8 ];
		buf += 2;
	}
	if (len & 1)
		cnt += g_pop_cnt[ *buf ];
	return cnt;
}



#define SHUFFLE4(i3, i2, i1, i0) ((i0) | ((i1) << 2) | ((i2) << 4) | ((i3) << 6))

// Based on the algoritm from the book by Henry S. Warren, Jr.  http://www.hackersdelight.org/
// Adapted for SSE2 by Peter Kankowski.
static __m128i POPCNTto8(__m128i v, __m128i mask1, __m128i mask2, const __m128i * mask4) {
	v = _mm_add_epi8( _mm_and_si128(v, mask1), _mm_and_si128(_mm_srli_epi16(v, 1), mask1) );
	v = _mm_add_epi8( _mm_and_si128(v, mask2), _mm_and_si128(_mm_srli_epi16(v, 2), mask2) );
	return _mm_and_si128( _mm_add_epi8(v, _mm_srli_epi16(v, 4)), *mask4 );
}

static __m128i Sum8to32(__m128i block_sum) {
	// Horizontally sum up byte counters (the method by Wojciech Muła http://wm.ite.pl/articles/sse-popcount.html )
	const __m128i zero = _mm_setzero_si128();
	return _mm_sad_epu8(block_sum, zero);
}

static RES HorSum32(__m128i sum) {
	// Horizontally add 32-bit accumulators
	sum = _mm_add_epi32(_mm_shuffle_epi32(sum, SHUFFLE4(1,0,3,2)), sum);
	return _mm_cvtsi128_si32(sum);
}

static __m128i GetMasked(__m128i v, INT len, __m128i cmp_mask) {
	// Mask out invalid bytes
	INT len32 = (len | (len << 8));
	len32 |= len32 << 16;
	__m128i mask = _mm_cmpgt_epi8(_mm_shuffle_epi32(_mm_cvtsi32_si128(len32), 0), cmp_mask);
	return _mm_and_si128(mask, v);
}



static RES POPCNT_SSE(const BYTE * buf, size_t len) {
	__m128i sum = _mm_setzero_si128();
	// Put masks in the main function to avoid reloading
	const __m128i mask1 = _mm_set1_epi8(0x55);
	const __m128i mask2 = _mm_set1_epi8(0x33);
	const __m128i mask4 = _mm_set1_epi8(0x0F);

	// Alignment
	size_t align = sizeof(__m128i) - (INT_PTR)buf & (sizeof(__m128i) - 1);
	align = (len < align) ? 0 : align; // optimized to branchless code by MSVC++
	if (align) {
		buf = (BYTE *)( (INT_PTR)buf & (-(INT_PTR)sizeof(__m128i)) );
		__m128i first = _mm_load_si128((__m128i *)buf);
		first = GetMasked(first, (INT)align, _mm_set_epi8(0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf));
		sum = Sum8to32(POPCNTto8(first, mask1, mask2, &mask4));

		buf += sizeof(__m128i);
		len -= align;
	}

	size_t ndqwords = len / sizeof(__m128i);
	while (ndqwords) {
		__m128i block_sum = _mm_setzero_si128();
		size_t block_ndqwords = Min(ndqwords, 31); // At most 31 ones can be summed up in one byte
		ndqwords -= block_ndqwords;
		for (; block_ndqwords; block_ndqwords--) {
			__m128i cnt = POPCNTto8( _mm_load_si128((__m128i *)buf), mask1, mask2, &mask4 );
			block_sum = _mm_add_epi8(block_sum, cnt);
			buf += sizeof(__m128i);
		}

		sum = _mm_add_epi32(sum, Sum8to32(block_sum));
	}

	// Remaining bytes
	len &= 15;
	if (len) {
		__m128i last = _mm_loadu_si128((__m128i *)buf);
		last = GetMasked(last, (INT)len, _mm_setr_epi8(0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf));
		__m128i last_sum = Sum8to32(POPCNTto8(last, mask1, mask2, &mask4));
		sum = _mm_add_epi32(sum, last_sum);
	}
	return HorSum32(sum);
}


// The method by Wojciech Muła http://wm.ite.pl/articles/sse-popcount.html
static __m128i POPCNTto8_PSHUFB(__m128i v, __m128i mask_lo, __m128i mask_popcnt) {
	__m128i lo = _mm_and_si128(v, mask_lo);
	__m128i hi = _mm_and_si128(_mm_srli_epi16(v, 4), mask_lo);
	lo = _mm_shuffle_epi8(mask_popcnt, lo);
	hi = _mm_shuffle_epi8(mask_popcnt, hi);
	return _mm_add_epi8(lo, hi);
}

static RES POPCNT_SSE_PSHUFB(const BYTE * buf, size_t len) {
	__m128i sum = _mm_setzero_si128();
	// Put masks in the main function to avoid reloading
	const __m128i mask_lo = _mm_set1_epi8(0x0F);
	const __m128i mask_popcnt = _mm_setr_epi8(0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4);

	// Alignment
	size_t align = sizeof(__m128i) - (INT_PTR)buf & (sizeof(__m128i) - 1);
	align = (len < align) ? 0 : align; // optimized to branchless code by MSVC++
	if (align) {
		buf = (BYTE *)( (INT_PTR)buf & (-(INT_PTR)sizeof(__m128i)) );
		__m128i first = _mm_load_si128((__m128i *)buf);
		first = GetMasked(first, (INT)align, _mm_set_epi8(0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf));
		sum = Sum8to32(POPCNTto8_PSHUFB(first, mask_lo, mask_popcnt));

		buf += sizeof(__m128i);
		len -= align;
	}

	size_t ndqwords = len / sizeof(__m128i);
	while (ndqwords) {
		__m128i block_sum = _mm_setzero_si128();
		size_t block_ndqwords = Min(ndqwords, 31); // At most 31 ones can be summed up in one byte
		ndqwords -= block_ndqwords;
		for (; block_ndqwords; block_ndqwords--) {
			__m128i cnt = POPCNTto8_PSHUFB( _mm_load_si128((__m128i *)buf), mask_lo, mask_popcnt );
			block_sum = _mm_add_epi8(block_sum, cnt);
			buf += sizeof(__m128i);
		}

		sum = _mm_add_epi32(sum, Sum8to32(block_sum));
	}

	// Remaining bytes
	len &= 15;
	if (len) {
		__m128i last = _mm_loadu_si128((__m128i *)buf);
		last = GetMasked(last, (INT)len, _mm_setr_epi8(0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf));
		__m128i last_sum = Sum8to32(POPCNTto8_PSHUFB(last, mask_lo, mask_popcnt));
		sum = _mm_add_epi32(sum, last_sum);
	}
	return HorSum32(sum);
}


/*static RES POPCNT_SSE_Loop(const BYTE * buf, size_t len) {
	__m128i sum = _mm_setzero_si128();
	const __m128i mask1 = _mm_set1_epi8(0x55);
	const __m128i mask2 = _mm_set1_epi8(0x33);
	const __m128i mask4 = _mm_set1_epi8(0x0F);

	RES res = 0;
	size_t align = sizeof(__m128i) - (INT_PTR)buf & (sizeof(__m128i) - 1);
	align = Min(align, len);
	len -= align;
	for (; align; align--)
		res += g_pop_cnt[*buf++];

	size_t ndqwords = len / sizeof(__m128i);
	while (ndqwords) {
		__m128i block_sum = _mm_setzero_si128();
		size_t block_ndqwords = Min(ndqwords, 31); // At most 31 ones can be summed up in one byte
		ndqwords -= block_ndqwords;
		for (; block_ndqwords; block_ndqwords--) {
			__m128i cnt = POPCNTto8( _mm_load_si128((__m128i *)buf), mask1, mask2, &mask4 );
			block_sum = _mm_add_epi8(block_sum, cnt);
			buf += sizeof(__m128i);
		}
		
		sum = _mm_add_epi32(sum, Sum8to32(block_sum));
	}
	res += HorSum32(sum);

	len &= 15;
	for (; len; len--)
		res += g_pop_cnt[*buf++];
	return res;
}

static RES POPCNT_SSE_NoAlign(const BYTE * buf, size_t len) {
	__m128i sum = _mm_setzero_si128();
	const __m128i mask1 = _mm_set1_epi8(0x55);
	const __m128i mask2 = _mm_set1_epi8(0x33);
	const __m128i mask4 = _mm_set1_epi8(0x0F);

	size_t ndqwords = len / sizeof(__m128i);
	while (ndqwords) {
		__m128i block_sum = _mm_setzero_si128();
		size_t block_ndqwords = Min(ndqwords, 31); // At most 31 ones can be summed up in one byte
		ndqwords -= block_ndqwords;
		for (; block_ndqwords; block_ndqwords--) {
			__m128i cnt = POPCNTto8( _mm_loadu_si128((__m128i *)buf), mask1, mask2, &mask4 );
			block_sum = _mm_add_epi8(block_sum, cnt);
			buf += sizeof(__m128i);
		}
		
		sum = _mm_add_epi32(sum, Sum8to32(block_sum));
	}
	RES res = HorSum32(sum);

	len &= 15;
	for (; len; len--)
		res += g_pop_cnt[*buf++];
	return res;
}

// Alignment loop suggested by Dmitry Kostjuchenko
static RES POPCNT_SSE_Dmitry(const BYTE * buf, size_t len) {
    RES res = 0;

    // Align 'buf' to 16 bytes to utilize _mm_load_si128
    while (((((intptr_t)buf) & ((16)-1)) != 0) && (len != 0))
    {
        res += g_pop_cnt[*buf++];
        -- len;
    }

    __m128i sum = _mm_setzero_si128();
    size_t ndqwords = len / sizeof(__m128i);
    const __m128i mask1 = _mm_set1_epi8(0x55);
    const __m128i mask2 = _mm_set1_epi8(0x33);
    const __m128i mask4 = _mm_set1_epi8(0x0F);

    while (ndqwords) {
        __m128i block_sum = _mm_setzero_si128();
        size_t block_ndqwords = Min(ndqwords, 31); // At most 31 ones can be summed up in one byte
        ndqwords -= block_ndqwords;
        for (; block_ndqwords; block_ndqwords--) {
			__m128i cnt = POPCNTto8( _mm_load_si128((__m128i *)buf), mask1, mask2, &mask4 );
			block_sum = _mm_add_epi8(block_sum, cnt);
			buf += sizeof(__m128i);
		}
		
		sum = _mm_add_epi32(sum, Sum8to32(block_sum));
    }    
    res += HorSum32(sum);

    len &= 15;
    for (; len; len--)
        res += g_pop_cnt[*buf++];

    return res;
}
*/
 




// Hardware-accelerated population count (using POPCNT instruction)
static RES POPCNT_Hardware(const BYTE * buf, size_t len) {
	RES cnt = 0;
	size_t ndwords = len / sizeof(DWORD);
	for(; ndwords; ndwords--) {
		cnt += __popcnt(*(DWORD*)buf);
		buf += sizeof(DWORD);
	}
	if (len & sizeof(WORD)) {
		cnt += __popcnt(*(WORD*)buf);
		buf += sizeof(WORD);
	}
	if (len & sizeof(BYTE))
		cnt += __popcnt(*buf);
	return cnt;
}

// by Subbu N, http://www.strchr.com/crc32_popcnt?allcomments=1#comment_482
static RES POPCNT_HardwareSubbuN(const BYTE * buf, size_t len) {
	RES cnt = 0;

	size_t align = sizeof(DWORD) - (INT_PTR)buf & (sizeof(DWORD) - 1);
	align = (len < align) ? 0 : align;
	if (align) {
		buf = (BYTE *)( (INT_PTR)buf & (-(INT_PTR)sizeof(DWORD)) );
		DWORD first = *(DWORD*)buf;
		first &= ~(0xFFFFFFFF >> (align * CHAR_BIT));
		cnt = __popcnt(first);
		buf += sizeof(DWORD);
		len -= align;
	}

	/*
	INT_PTR ndwords = len / sizeof(DWORD);
	DWORD* pInt = (DWORD*)buf + ndwords;
	ndwords = -ndwords;
	while(ndwords)
		cnt += __popcnt(pInt[ndwords++]);
	*/
	size_t ndwords = len / sizeof(DWORD);
	DWORD* pInt = (DWORD*)buf;
	while(ndwords)
		cnt += __popcnt(pInt[--ndwords]); // performance optimization: Removed ptr addition.

	buf += len / sizeof(DWORD) * sizeof(DWORD);

	if (len & sizeof(WORD)) {
		cnt += __popcnt(*(WORD*)buf);
		buf += sizeof(WORD);
	}
	if (len & sizeof(BYTE))
		cnt += __popcnt(*buf);
	return cnt;
}

static RES POPCNT_HardwareUnrolled(const BYTE * buf, size_t len) {
	RES cnt = 0;
	
	size_t align = sizeof(DWORD) - (INT_PTR)buf & (sizeof(DWORD) - 1);
	align = (len < align) ? 0 : align;
	if (align) {
		buf = (BYTE *)( (INT_PTR)buf & (-(INT_PTR)sizeof(DWORD)) );
		DWORD first = *(DWORD*)buf;
		first &= ~(0xFFFFFFFF >> (align * CHAR_BIT));
		cnt = __popcnt(first);
		buf += sizeof(DWORD);
		len -= align;
	}

	size_t ndqwords = len / (sizeof(DWORD) * 4);
	for(; ndqwords; ndqwords--) {
		cnt += __popcnt(*(DWORD*)buf) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) )) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) * 2 )) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) * 3 ));
		buf += sizeof(DWORD) * 4;
	}

	len &= (sizeof(DWORD) * 4 - 1);
	for (; len; len--)
		cnt += __popcnt(*buf++);

	return cnt;
}

/*static RES POPCNT_HardwareUnrolled_Loop(const BYTE * buf, size_t len) {
	RES cnt = 0;
	
	size_t align = sizeof(DWORD) - (INT_PTR)buf & (sizeof(DWORD) - 1);
	align = Min(align, len);
	len -= align;
	for (; align; align--)
		cnt += __popcnt(*buf++);

	size_t ndqwords = len / (sizeof(DWORD) * 4);
	for(; ndqwords; ndqwords--) {
		cnt += __popcnt(*(DWORD*)buf) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) )) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) * 2 )) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) * 3 ));
		buf += sizeof(DWORD) * 4;
	}
	len &= sizeof(DWORD) * 4 - 1;
	for (; len; len--)
		cnt += __popcnt(*buf++);
	return cnt;
}

static RES POPCNT_HardwareUnrolled_NoAlign(const BYTE * buf, size_t len) {
	RES cnt = 0;
	size_t ndqwords = len / (sizeof(DWORD) * 4);
	for(; ndqwords; ndqwords--) {
		cnt += __popcnt(*(DWORD*)buf) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) )) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) * 2 )) +
			   __popcnt(*(DWORD*)(buf + sizeof(DWORD) * 3 ));
		buf += sizeof(DWORD) * 4;
	}
	len &= sizeof(DWORD) * 4 - 1;
	for (; len; len--)
		cnt += __popcnt(*buf++);
	return cnt;
}*/



// ======= Benchmarks ============

uint32_t64 inline GetRDTSC() {
   __asm {
      ; Flush the pipeline
      XOR eax, eax
      CPUID
      ; Get RDTSC counter in edx:eax
      RDTSC
   }
}

uint32_t Benchmark(CRC_FUNC func, const BYTE * buffer, size_t length, OUT RES & result) {
	uint32_t min_time = uint32_t_MAX;
	RES res = 0;

	for (uint32_t j = 0; j < 20; j++) {
		uint32_t64 start_time = GetRDTSC();
		res = func(buffer, length);
		uint32_t time = (uint32_t)(GetRDTSC() - start_time);
		min_time = min(min_time, time);
	}
	result = res;
	return min_time;
}

BYTE g_buffer[1024 * 1024];
// Length is not always a power of 2 to avoid bias in favor of unrolled implementations.
static const size_t g_lengths[] = {250, 1025, 4103, 16384, 65537, 262151, NUM_OF(g_buffer)};


void BenchmarkFunction(CRC_FUNC func, const CHAR * func_name, const CHAR * func_long_name) {
	#ifdef HTML_OUTPUT
		UNREFERENCED_PARAMETER(func_name);
		printf("<tr><td class=\"l\">%s</td>", func_long_name);
	#else
		UNREFERENCED_PARAMETER(func_long_name);
		printf("%-15s", func_name);
	#endif

	for (size_t len_index = 0; len_index < NUM_OF(g_lengths); len_index++) {
		RES res;
		uint32_t time;
		time = Benchmark(func, g_buffer + 1, g_lengths[len_index] - 1, OUT res);

		#ifdef HTML_OUTPUT
			printf("<td>%d</td>", (uint32_t)time);
		#else
			printf("%8d [%8x]", (uint32_t)time, res);
		#endif
	}

	#ifdef HTML_OUTPUT
		printf("</tr>");
	#else
		printf("\n");
	#endif
}

void PrintHeader() {
	// Header
	#ifdef HTML_OUTPUT
		printf("<table><tr><th>File size, bytes</th>");
		for (size_t len_index = 0; len_index < NUM_OF(g_lengths); len_index++)
			printf("<th>%d</th>", g_lengths[len_index]);
		printf("</tr>");
	#else
		printf("%15c", ' ');
		for (size_t len_index = 0; len_index < NUM_OF(g_lengths); len_index++)
			printf("%19d", g_lengths[len_index]);
		printf("\n");
	#endif
}

void PrintFooter() {
	#ifdef HTML_OUTPUT
		printf("</table>\n\n");
	#else
		printf("\n\n");
	#endif
}


// =======================
// Tests
void TestCRCFunc(CRC_FUNC crc_func) {
	UNREFERENCED_PARAMETER(crc_func);
	// Check value from http://regregex.bbcmicro.net/crc-catalogue.htm and other values
	// calculated with http://www.zorc.breitbandkatze.de/crc.html
	static const char nums[] = "123456789";
	assert(crc_func(NULL, 0) == 0);
	assert(crc_func((BYTE*)nums, 9) == 0xE3069283);
	assert(crc_func((BYTE*)(nums + 1), 8) == 0xBFE92A83);
	assert(crc_func((BYTE*)"1234567890", 10) == 0xf3dbd4fe);
	assert(crc_func((BYTE*)"The quick brown fox jumps over the lazy dog", 43) == 0x22620404);
}

void TestPopCntFunc(CRC_FUNC pop_cnt_func) {
	UNREFERENCED_PARAMETER(pop_cnt_func);
	static const BYTE test_bits[21] = {0x30, 0x0B, 0, 0x80, 0x03,
		0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
	assert(pop_cnt_func(test_bits, 0) == 0);
	assert(pop_cnt_func(test_bits + 1, 1) == 3);
	assert(pop_cnt_func(test_bits, 2) == 5);
	assert(pop_cnt_func(test_bits, 3) == 5);
	assert(pop_cnt_func(test_bits, 4) == 6);
	assert(pop_cnt_func(test_bits, 5) == 8);
	assert(pop_cnt_func(test_bits + 5, 16) == 128);
	assert(pop_cnt_func(test_bits, 21) == 136);
}


int main() {
	static const CRC_FUNC crc_funcs[] = {CRC_Sarwate, CRC_RichardBlack, CRC_SlicingBy4, CRC_SlicingBy8,
		/*CRC_SlicingBy8_Portable, CRC_SlicingBy8_NoAlign*/};
	static const CHAR * crc_func_names[] = {"Dilip Sarwate", "Richard Black", "Slicing-by-4", "Slicing-by-8",
		/*"SlicingDmitry", "SlicingNoAlign"*/};
	static const CHAR * crc_long_names[] = {"Dilip Sarwate",
		"<A href=\"http://www.cl.cam.ac.uk/research/srg/bluebook/21/crc/node6.html#SECTION00064000000000000000\">"
			"Richard Black</A>",
		"<A href=\"http://www.intel.com/technology/comms/perfnet/download/CRC_generators.pdf\">"
			"Slicing-by-4</A>", "Slicing-by-8",
		/*"SlicingDmitry", "SlicingNoAlign"*/};
	assert(NUM_OF(crc_funcs) == NUM_OF(crc_func_names) && NUM_OF(crc_funcs) == NUM_OF(crc_long_names));

	static const CRC_FUNC popcnt_funcs[] = {POPCNT_BitHacks, /*POPCNT_BitHacks_NoAlign,*/ POPCNT_Table,
		POPCNT_SSE, /*POPCNT_SSE_Loop, POPCNT_SSE_Dmitry, POPCNT_SSE_NoAlign*/};
	static const CHAR * popcnt_func_names[] = {"Bit Hacks", /*"BitH-NoAlign",*/ "Table",
		"SSE2", /*"SSE - Loop", "SSE - Dmitry", "SSE - NoAlign"*/};
	static const CHAR * popcnt_long_names[] = {
		"<A href=\"http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetParallel\">Bit hacks</A>",
		/*"BitH-NoAlign",*/
		"<A href=\"http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetTable\">Table</A>",
		"SSE2", /*"SSE - Loop", "SSE - Dmitry", "SSE - NoAlign"*/};
	assert(NUM_OF(popcnt_funcs) == NUM_OF(popcnt_func_names));

	// =============
	// Init
	CRC_Init();
	CRC_SlicingInit();

	srand(2015695684); // Initialize to some fixed number
	for (size_t i = 0; i < NUM_OF(g_buffer); i++)
		g_buffer[i] = rand() & 0xFF;

	const INT POPCNT_SUPPORTED = 1 << 23, SSE4_2_SUPPORTED = 1 << 20, SSSE3_SUPPORTED = 1 << 9;
	INT a[4];
	__cpuid(a, 1);

	// =============
	// Tests
	for (size_t i = 0; i < NUM_OF(crc_funcs); i++)
		TestCRCFunc(crc_funcs[i]);
	if (a[2] & SSE4_2_SUPPORTED) {
		TestCRCFunc(CRC_Hardware);
		TestCRCFunc(CRC_HardwareUnrolled);
	}

	for (size_t i = 0; i < NUM_OF(popcnt_funcs); i++)
		TestPopCntFunc(popcnt_funcs[i]);
	if (a[2] & POPCNT_SUPPORTED) {
		TestPopCntFunc(POPCNT_Hardware);
		TestPopCntFunc(POPCNT_HardwareUnrolled);
	}
	//TestPopCntFunc(POPCNT_HardwareUnrolled_Loop);
	//TestPopCntFunc(POPCNT_HardwareUnrolled_NoAlign);
	if (a[2] & SSSE3_SUPPORTED)
		TestPopCntFunc(POPCNT_SSE_PSHUFB);

	// Execute on one processor
	SetThreadAffinityMask(GetCurrentThread(), 1);

	// =============
	// CRC benchmark
	PrintHeader();

	for (size_t i = 0; i < NUM_OF(crc_funcs); i++)
		BenchmarkFunction(crc_funcs[i], crc_func_names[i], crc_long_names[i]);

	if (a[2] & SSE4_2_SUPPORTED) {
		printf("\n");
		BenchmarkFunction(CRC_Hardware, "Hardware", "Hardware");
		BenchmarkFunction(CRC_HardwareUnrolled, "HardwareUnrl", "Hardware, unrolled");
	} else
		printf("CRC32 instruction is not supported on this processor\n");

	PrintFooter();

	// ================
	// POPCNT benchmark
	PrintHeader();

	for (size_t i = 0; i < NUM_OF(popcnt_funcs); i++)
		BenchmarkFunction(popcnt_funcs[i], popcnt_func_names[i], popcnt_long_names[i]);
	printf("\n");

	if (a[2] & POPCNT_SUPPORTED) {
		BenchmarkFunction(POPCNT_Hardware, "Hardware", "Hardware");
		BenchmarkFunction(POPCNT_HardwareSubbuN, "HardwareSubbuN", "<a href=\"http://www.strchr.com/crc32_popcnt?allcomments=1#comment_482\">Hardware by Subbu N</a>");
		BenchmarkFunction(POPCNT_HardwareUnrolled,  "HardwareUnrl", "Hardware, unrolled");
		//BenchmarkFunction(POPCNT_HardwareUnrolled_Loop,  "HardwareLoop");
		//BenchmarkFunction(POPCNT_HardwareUnrolled_NoAlign,  "HardwareNoAlgn");
	} else
		printf("POPCNT instruction is not supported on this processor\n");

	if (a[2] & SSSE3_SUPPORTED)
		BenchmarkFunction(POPCNT_SSE_PSHUFB, "SSSE3", "<a href=\"http://wm.ite.pl/articles/sse-popcount.html\">SSSE3</a>");
	else
		printf("PSHUFB instruction is not supported on this processor\n");

	PrintFooter();

	return 0;
}



