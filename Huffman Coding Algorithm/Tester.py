"""
    Tester for the Huffman Algorithm
"""
import HuffmanNode as HFM


class Tester:

    def main(self):

        # Creating an instance of the Huffman class
        Queue = HFM.SinglyLinkedList()
        
        path = "https://learn.alueducation.com/assets/courseware/v1/0bb2add1ebd1cf1dcdee878759a4f62c/asset-v1:ALU+CSDSARW1819+2019_T2+type@asset+block/test_input.txt"

        # Message extracted from a text file
        file_info = Queue.file_opener(path)
        
        print(file_info)
        
        print("Here")
        
        print("Here too")
        
        # Passing message to generate frequency table
        #Frequency_table = Queue.generate_freq_table(file_info)
        
        # Passing message to generate Huffman Tree
        #Huffman_tree = Queue.generate_tree(file_info)


test = Tester()

test.main()
