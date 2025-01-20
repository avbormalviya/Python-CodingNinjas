import heapq
import os.path


class Node:
    def __init__(self, freq, char=''):
        self.char = char  # Character represented by the node
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child node
        self.right = None  # Right child node

    def __lt__(self, other):
        # Comparison function for heapq to prioritize lower frequencies
        return self.freq < other.freq

    def __eq__(self, other):
        # Equality function for nodes with equal frequency
        return self.freq == other.freq


class HuffmanCoding:
    def __init__(self, path):
        self.path = path  # Path to the input file
        self.__heap = []  # Min-heap to store nodes for Huffman tree
        self.__root = None  # Root of the Huffman tree
        self.__codes = {}  # Dictionary to store character-to-code mapping
        self.__reverse_codes = {}  # Dictionary to store code-to-character mapping

    def __make_freq_dict(self, text):
        """Create a frequency dictionary from the input text."""
        freq_dict = {}

        for char in text:
            freq_dict[char] = freq_dict.get(char, 0) + 1

        return freq_dict

    def __build_heap(self, freq_dict):
        """Build a min-heap from the frequency dictionary."""
        for char, freq in freq_dict.items():
            node = Node(freq, char)
            heapq.heappush(self.__heap, node)

    def __build_tree(self):
        """Build the Huffman tree from the min-heap."""
        while len(self.__heap) > 1:
            left = heapq.heappop(self.__heap)  # Extract the two smallest nodes
            right = heapq.heappop(self.__heap)

            # Create a new node with combined frequency
            node = Node(left.freq + right.freq)
            node.left = left
            node.right = right

            heapq.heappush(self.__heap, node)  # Push the new node back into the heap

        self.__root = heapq.heappop(self.__heap)  # Final node is the root of the tree

    def __find_code(self, root, char, code):
        """Recursively find the code for a character in the Huffman tree."""
        if root is None:
            return

        if root.char == char:
            self.__codes[char] = code
            self.__reverse_codes[code] = char

        self.__find_code(root.left, char, code + '0')  # Traverse left with '0'
        self.__find_code(root.right, char, code + '1')  # Traverse right with '1'

    def __build_code(self, freq_dict):
        """Build the code dictionary for all characters."""
        for char in freq_dict:
            self.__find_code(self.__root, char, '')

    def __get_encoded_text(self, text):
        """Convert the input text to its encoded binary string."""
        encoded_text = ''

        for char in text:
            encoded_text += self.__codes[char]

        return encoded_text

    def __get_padded_encoded_text(self, encoded_text):
        """Pad the encoded text to make its length a multiple of 8."""
        padded_amount = 8 - (len(encoded_text) % 8)
        encoded_text += '0' * padded_amount  # Append padding
        padded_info = "{:08b}".format(padded_amount)  # Store padding info as 8-bit binary

        return padded_info + encoded_text

    def __get_bytes_array(self, padded_encoded_text):
        """Convert the padded binary string to a byte array."""
        bytes_array = []

        for i in range(0, len(padded_encoded_text), 8):
            bytes_array.append(int(padded_encoded_text[i:i + 8], 2))

        return bytes(bytes_array)

    def compress(self):
        """Compress the file using Huffman coding."""
        file_name, file_extension = os.path.splitext(self.path)
        output_path = file_name + "_compressed" + '.bin'

        with open(self.path, 'r') as file, open(output_path, 'wb') as output_file:
            text = file.read()
            freq_dict = self.__make_freq_dict(text)

            self.__build_heap(freq_dict)
            self.__build_tree()
            self.__build_code(freq_dict)

            encoded_text = self.__get_encoded_text(text)
            padded_encoded_text = self.__get_padded_encoded_text(encoded_text)
            bytes_array = self.__get_bytes_array(padded_encoded_text)

            output_file.write(bytes_array)

        return output_path

    def __remove_padding(self, text):
        """Remove the padding from the binary string."""
        padding = int(text[:8], 2)  # Extract padding info

        return text[8:-padding]  # Remove padding bits

    def __decode_text(self, bits_text):
        """Decode the binary string back to the original text."""
        code = ""
        text = ""

        for char in bits_text:
            code += char

            if code in self.__reverse_codes:
                text += self.__reverse_codes[code]
                code = ""

        return text

    def decompress(self, input_path):
        """Decompress the compressed file back to the original text."""
        file_name, file_extension = os.path.splitext(input_path)
        output_path = file_name + "_decompressed" + '.txt'

        with open(input_path, 'rb') as file, open(output_path, 'w') as output_file:
            bit_string = ""
            byte = file.read(1)

            while byte:
                byte_value = ord(byte)
                bits = bin(byte_value)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            bits_text = self.__remove_padding(bit_string)
            decoded_text = self.__decode_text(bits_text)

            output_file.write(decoded_text)

        return output_path


if __name__ == '__main__':
    hc = HuffmanCoding("./demo.txt")
    output_path = hc.compress()
    hc.decompress(output_path)
