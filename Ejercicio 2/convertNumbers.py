"""
convertNumbers.py

This script converts numbers to binary and hexadecimal base, 
for a given file containing numerical data.
"""
import sys
import time

def to_binary(number, bits=32):
    """Converts a decimal number to binary using a basic algorithm."""
    if number == 0:
        return '0'
    if number < 0:
        number = (1 << bits) + number
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def to_hexadecimal(number, bits=32):
    """Converts a decimal number to hexadecimal using a basic algorithm."""
    if number == 0:
        return '0'
    if number < 0:
        number = (1 << bits) + number
    hex_digits = '0123456789ABCDEF'
    hexadecimal = ''
    while number > 0:
        hexadecimal = hex_digits[number % 16] + hexadecimal
        number //= 16
    return hexadecimal

def process_file(input_file, output_file):
    """Processes the input file and generates the results on screen and in the file."""
    start_time = time.time()

    try:
        with open(input_file, 'r', encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' is not found.")
        sys.exit(1)

    results = []

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        try:
            decimal_number = int(line)
        except ValueError:
            print(f"Error on line {line_number}: '{line}' not a valid number.")
            continue
        binary = to_binary(decimal_number)
        hexadecimal = to_hexadecimal(decimal_number)
        results.append(f"Decimal: {decimal_number}, Binary: {binary}, Hexadecimal: {hexadecimal}")

    elapsed_time = time.time() - start_time

    # Escribir resultados en el archivo de salida
    with open(output_file, 'w', encoding="utf-8") as file:
        file.write("\n".join(results))
        file.write(f"\nTotal execution time: {elapsed_time:.2f} seconds\n")

    # Mostrar resultados en pantalla
    for result in results:
        print(result)
    print(f"\nTotal execution time: {elapsed_time:.2f} seconds")

def main():
    """Main function that reads a file from the command line, 
    computes convertion, and writes the results to a file."""
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "ConvertionResults.txt"

    process_file(input_file, output_file)

if __name__ == "__main__":
    main()
