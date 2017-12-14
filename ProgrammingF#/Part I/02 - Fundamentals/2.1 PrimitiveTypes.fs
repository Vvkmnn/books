// -----------------------------------------------------
// Intro

(* 
    A type is a concept enforcing safety; they represent a proof that a a conversion will work. 

    Some types, like integers, are straightforward, but others are more abstract, like functions. 

    F# is statically typed, meaning that type checking is done at compile time; if you pass a function the wrong type of argument, the code will just not run. 
*)

// To creat a value, you use the let binding 

let x = 1

// -----------------------------------------------------
// Numeric Primitives 

 // These come in two varieties: integers and floats. They are defined by size to determine how much memory they need. We also define them with optional prefixes and suffixes to further define their type.

let answerToEverything = 42UL

let pi = 3.1415926M

let avogadro = 6.022e23


// We can use special prefixes to specify values in hex (0x), oct (0o), or binary (0b) notation.

let hex = 0xFCAF

let oct =  0o7771L

let bin = 0b00101010y


// -----------------------------------------------------
// Arithmetic

// The types have to match, and the power operation only takes floats. 
// Addition
1 + 2

// Subtraction
1 - 2

// Multiplication
3 * 4

// Division
4 / 2

// Power
4.0 ** 2.0

// Modulus
7 % 3

// There are also a few common mathematical operations included by default.
// Absolute Value
abs -1.0

//  Ceiling (round up)
ceil 9.1

// Exponent (raise to power of e)
exp 1.0

// Floor (round down)
floor 9.9

// Sign (show sign using 1)
sign -2
sign 2

// Natural log
log 2.71828

// Log base 10
log10 1000.0

// Square root
sqrt 4.0

// Cosine 
cos 0.0

// Sine
sin 0.0

// Tanget
tan 1.0

// Power of N (Raise an integer to a power) 
pown 2 10

// -----------------------------------------------------
// Conversion Routines

// F# does not convert anything behind the scenes; if you want to change the type of something, then you have to manually define that change

int16 1.00000

float 10

byte 42

// -----------------------------------------------------
// BigInteger

// If you are dealing with data larger than 2**64, F# uses the bigint type (suffix I) for arbitrarily large numbers. We will use data storage as an example. 

let megabyte  = 1024I    * 1024I
let gigabyte  = megabyte * 1024I
let terabyte  = gigabyte * 1024I
let petabyte  = terabyte * 1024I
let exabyte   = petabyte * 1024I
let zettabyte = exabyte  * 1024I

// -----------------------------------------------------
// Bitwise Operations

// Bitwise operations manipulate values at a binary level

// Bitwise And (bits that are the same in both values) 
0b1111 &&& 0b0011 // 0b0011

// Bitwise Or (bits that are in either value)
0xFF00 ||| 0x00FF // 0xFFFF

//Exclusive Or (if bit is the same, 0, if bit is different, 1) 

// Left Shift (Shift the bits left by n)
0b0001 <<< 3 // 0b1000

// Right Shift (Shift the bits right by n)
0b1000 >>> 3 // 0b0001

// -----------------------------------------------------
// Characters

// We can use unicode characters.

let vowels = ['a'; 'e'; 'i'; 'o'; 'u']

// We also have escapable character sequence, like \`, \", \\, \b, \n, \r,\t 

// -----------------------------------------------------
// Strings

// Strings are defined using the quotes, and their characters indexed.

let password = "abracadabra"

let multiline = "This string
takes up 
multiple lines"

multiline.[0]
multiline.[1]
multiline.[2]
multiline.[3]


// And break up long strings with a \ to skip all whitespace.

let longString = "abc-\
                        def-\
    ghi" 

// We can use triple quotes to avoid needing to escape things.

let xmlFragment = """ <Ship Name="Prometheus"></foo> """

// We use the @ prefix to create a raw (verbatim text), which also ignores escape characters

let normalString = "Normal.\n.\n.\t.\t.String"

let verbatimString = @"Verbatim.\n.\n.\t.\t.String"

// -----------------------------------------------------
// Boolean Values

// And 
true && true

// Or
true || false

// Not
not false

/// Print a truth table for the given comparison
let printTruthTable f =
    printfn "       |true   | false |"
    printfn "       +-------+-------+"
    printfn " true  | %5b | %5b |" (f true true)  (f true false)
    printfn " true  | %5b | %5b |" (f false true) (f false false)
    printfn "       +-------+-------+"
    printfn ""
    ()

// And TruthTable
printTruthTable(&&)

// Or TruthTable
printTruthTable(&&)

