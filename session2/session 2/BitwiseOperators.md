Bitwise operators

Bitwise operators in Python are used to perform operations on the binary representations of integers. These operators work directly on the bits of the numbers. Here are the bitwise operators available in Python:

1. Bitwise AND (&)
Performs a bitwise AND operation.

Each bit of the output is 1 if both corresponding bits of the operands are 1; otherwise, it is 0.

Example:

python
Copy
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Binary: 0001 (Decimal: 1)
print(result)  # Output: 1
2. Bitwise OR (|)
Performs a bitwise OR operation.

Each bit of the output is 1 if at least one of the corresponding bits of the operands is 1; otherwise, it is 0.

Example:

python
Copy
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a | b  # Binary: 0111 (Decimal: 7)
print(result)  # Output: 7
3. Bitwise XOR (^)
Performs a bitwise XOR (exclusive OR) operation.

Each bit of the output is 1 if the corresponding bits of the operands are different; otherwise, it is 0.

Example:

python
Copy
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a ^ b  # Binary: 0110 (Decimal: 6)
print(result)  # Output: 6
4. Bitwise NOT (~)
Performs a bitwise NOT operation (one's complement).

Inverts all the bits of the number. Since Python uses signed integers, the result is -(x + 1).

Example:

python
Copy
a = 5  # Binary: 0101
result = ~a  # Binary: 1010 (Decimal: -6)
print(result)  # Output: -6
5. Bitwise Left Shift (<<)
Shifts the bits of the number to the left by the specified number of positions.

Zeros are added to the right.

Example:

python
Copy
a = 5  # Binary: 0101
result = a << 1  # Binary: 1010 (Decimal: 10)
print(result)  # Output: 10
6. Bitwise Right Shift (>>)
Shifts the bits of the number to the right by the specified number of positions.

Zeros are added to the left (for unsigned numbers).

Example:

python
Copy
a = 5  # Binary: 0101
result = a >> 1  # Binary: 0010 (Decimal: 2)
print(result)  # Output: 2
Summary Table of Bitwise Operators:
Operator Description Example
& Bitwise AND a & b
` ` Bitwise OR `a | b`
^ Bitwise XOR a ^ b
~ Bitwise NOT (one's complement) ~a
<< Bitwise Left Shift a << n
>> Bitwise Right Shift a >> n
Key Notes:
Bitwise operators work on integers.

The result of bitwise operations depends on the binary representation of the numbers.

Bitwise operations are often used in low-level programming, such as working with hardware, cryptography, and optimizing certain algorithms.
