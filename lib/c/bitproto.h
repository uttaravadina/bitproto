// Copyright (c) 2021, hit9. https://github.com/hit9/bitproto
// Encoding library for bitproto in C language.
//
// Keep it simple:
// * No dynamic memory allocation (malloc).
// * All structs and functions named starting with 'Bp'.

#ifndef __BITPROTO_LIB_H__
#define __BITPROTO_LIB_H__ 1

#include <inttypes.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

#if defined(__cplusplus)
extern "C" {
#endif

#define BP_TYPE_BOOL 1
#define BP_TYPE_INT 2
#define BP_TYPE_UINT 3
#define BP_TYPE_BYTE 4
#define BP_TYPE_ENUM 5
#define BP_TYPE_ALIAS 6
#define BP_TYPE_ARRAY 7
#define BP_TYPE_MESSAGE 8

////////////////////
// Data Abstractions
////////////////////

// BpProcessorContext is the general encoding and decoding context, as an
// argument of processor functions.
struct BpProcessorContext {
    // Indicates whether current processing is encoding or decoding.
    bool is_encode;
    // Tracks the total bits processed.
    // Maintained by function BpEndecodeBaseType.
    int i;
    // Bytes buffer processing. It's the destination buffer under encoding
    // context, and source buffer under decoding context.
    unsigned char *s;
};

// BpJsonFormatContext is the context to format bitproto messages.
struct BpJsonFormatContext {
    // Number of bytes formatted.
    int n;
    // Target buffer to format into.
    char *s;
};

// BpProcessor function first constructs its own descriptor, and then continues
// the encoding and decoding processing with given context.
// BpProcessor functions will be generated by bitproto compiler.
typedef void (*BpProcessor)(void *data, struct BpProcessorContext *ctx);

// BpJsonFormatter function formats given data with its descriptor into json.
typedef void (*BpJsonFormatter)(void *data, struct BpJsonFormatContext *ctx);

// BpType is an abstraction for all bitproto types.
struct BpType {
    // Flag of this type.
    int flag;
    // Number of bits this type occupy in encoding.
    size_t nbits;
    // Number of bytes this type occupy in memory.
    size_t size;

    // Processor function for this type.
    // Sets if this type is message, enum, alias or array, otherwise NULL.
    BpProcessor processor;

    // JsonFormatter function for this type.
    // Sets if this type is message, enum, alias or array, otherwise NULL.
    BpJsonFormatter json_formatter;
};

// BpAliasDescriptor describes an alias definition.
struct BpAliasDescriptor {
    // The type alias to.
    struct BpType to;
};

// BpEnumDescriptor describes an enum definition.
struct BpEnumDescriptor {
    // Whether this enum is extensible.
    bool extensible;
    // The corresponding uint type.
    struct BpType uint;
};

// BpArrayDescriptor describes an array type.
struct BpArrayDescriptor {
    // Whether this array is extensible.
    bool extensible;
    // Capacity of this array.
    size_t cap;
    // The array element's type.
    struct BpType element_type;
};

// BpMessageFieldDescriptor describes a message field.
struct BpMessageFieldDescriptor {
    // The address of this field's data.
    void *data;
    // Type of this field.
    struct BpType type;
    // Name of this field.
    // Required for json formatter.
    char *name;
};

// BpMessageDescriptor describes a message.
struct BpMessageDescriptor {
    // Whether this message is extensible.
    bool extensible;
    // Number of fields this message contains.
    int nfields;
    // Number of bits this message occupy.
    size_t nbits;
    // List of descriptors of the message fields.
    struct BpMessageFieldDescriptor *field_descriptors;
};

////////////////
// Declarations
////////////////

// Context Constructor.
struct BpProcessorContext BpProcessorContext(bool is_encode, unsigned char *s);
struct BpJsonFormatContext BpJsonFormatContext(char *s);

// BpType Constructors.

struct BpType BpBool();
struct BpType BpInt(size_t nbits);
struct BpType BpUint(size_t nbits);
struct BpType BpByte();
struct BpType BpMessage(size_t nbits, size_t size, BpProcessor processor,
                        BpJsonFormatter formatter);
struct BpType BpEnum(size_t nbits, size_t size, BpProcessor processor,
                     BpJsonFormatter formatter);
struct BpType BpArray(size_t nbits, size_t size, BpProcessor processor,
                      BpJsonFormatter formatter);
struct BpType BpAlias(size_t nbits, size_t size, BpProcessor processor,
                      BpJsonFormatter formatter);

// Descriptor Constructors.

struct BpMessageDescriptor BpMessageDescriptor(
    bool extensible, int nfields, size_t nbits,
    struct BpMessageFieldDescriptor *field_descriptors);
struct BpMessageFieldDescriptor BpMessageFieldDescriptor(void *data,
                                                         struct BpType type,
                                                         char *name);
struct BpEnumDescriptor BpEnumDescriptor(bool extensible, struct BpType uint);
struct BpArrayDescriptor BpArrayDescriptor(bool extensible, size_t cap,
                                           struct BpType element_type);
struct BpAliasDescriptor BpAliasDescriptor(struct BpType to);

// Encoding & Decoding

void BpEncodeSingleByte(struct BpProcessorContext *ctx, void *data, int j,
                        int c);
void BpDecodeSingleByte(struct BpProcessorContext *ctx, void *data, int j,
                        int c);
void BpEndecodeSingleByte(struct BpProcessorContext *ctx, void *data, int j,
                          int c);
void BpEndecodeBaseType(struct BpType type, struct BpProcessorContext *ctx,
                        void *data);
void BpEndecodeMessageField(struct BpMessageFieldDescriptor *descriptor,
                            struct BpProcessorContext *ctx, void *data);
void BpEndecodeMessage(struct BpMessageDescriptor *descriptor,
                       struct BpProcessorContext *ctx, void *data);
void BpEndecodeAlias(struct BpAliasDescriptor *descriptor,
                     struct BpProcessorContext *ctx, void *data);
void BpEndecodeEnum(struct BpEnumDescriptor *descriptor,
                    struct BpProcessorContext *ctx, void *data);
void BpEndecodeArray(struct BpArrayDescriptor *descriptor,
                     struct BpProcessorContext *ctx, void *data);

// Extensible Processor.

void BpEncodeEnumExtensibleAhead(struct BpEnumDescriptor *descriptor,
                                 struct BpProcessorContext *ctx);
uint8_t BpDecodeEnumExtensibleAhead(struct BpEnumDescriptor *descriptor,
                                    struct BpProcessorContext *ctx);

void BpEncodeArrayExtensibleAhead(struct BpArrayDescriptor *descriptor,
                                  struct BpProcessorContext *ctx);
uint16_t BpDecodeArrayExtensibleAhead(struct BpArrayDescriptor *descriptor,
                                      struct BpProcessorContext *ctx);

void BpEncodeMessageExtensibleAhead(struct BpMessageDescriptor *descriptor,
                                    struct BpProcessorContext *ctx);
uint16_t BpDecodeMessageExtensibleAhead(struct BpMessageDescriptor *descriptor,
                                        struct BpProcessorContext *ctx);

// Json Formatting

void BpJsonFormatString(struct BpJsonFormatContext *ctx, const char *format,
                        ...);
void BpJsonFormatMessage(struct BpMessageDescriptor *descriptor,
                         struct BpJsonFormatContext *ctx, void *data);
void BpJsonFormatBaseType(struct BpType type, struct BpJsonFormatContext *ctx,
                          void *data);
void BpJsonFormatAlias(struct BpAliasDescriptor *descriptor,
                       struct BpJsonFormatContext *ctx, void *data);
void BpJsonFormatEnum(struct BpEnumDescriptor *descriptor,
                      struct BpJsonFormatContext *ctx, void *data);
void BpJsonFormatMessageField(struct BpMessageFieldDescriptor *descriptor,
                              struct BpJsonFormatContext *ctx);
void BpJsonFormatArray(struct BpArrayDescriptor *descriptor,
                       struct BpJsonFormatContext *ctx, void *data);

// Utils

size_t BpIntSizeFromNbits(size_t nbits);
size_t BpUintSizeFromNbits(size_t nbits);
int BpMin(int a, int b);
int BpSmartShift(int n, int k);
int BpGetMask(int k, int c);
int BpGetNbitsToCopy(int i, int j, int n);

#if defined(__cplusplus)
}
#endif

#endif