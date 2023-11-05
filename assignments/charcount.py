""" Importing modules """
import os
import argparse
import time
from loguru import logger
import matplotlib.pyplot as plt


def process(file_path,bool):
    """ Main processing method.
        Takes a file path and a boolean variable in imput
        Returns a dictionary with frequencies for each letter.
    """
    # Basic sanity check: make sure that the file_argument points to an
    # existing text file.
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)

    # Open the input file (note that we are taking advantage of context
    # management, using a with statement).
    logger.info(f'Opening imput file {file_path}...')
    # 'with' block is tipically used to open and read a file
    with open(file_path) as input_file:
        data = input_file.read()
        # Proceeds to cut intro and licence if the boolean in imput is True
        if bool:
            # Cut intro and licence from the 'book'
            logger.info('Excluding introduction and license from process')
            start_index=data.find('THE REPUBLIC.\n')
            end_index=data.find('*** END')
            data=data[start_index:end_index]

    logger.info(f'Done. {len(data)} character(s) found.')

    # Prepare a dictionary to hold the letter frequencies, and initialize
    # all the counts to zero.
    letters = 'abcdefghijklmnopqrstuvwxyz'
    freq_dict = {}
    for character in letters:
        freq_dict[character] = 0

    # Loop over the input data (note the call to the lower() string method
    # that is casting everything in lower case).
    for character in data.lower():
        # Condition to exclude anything that is not a letter
        if character in letters:
            freq_dict[character] += 1

    # One last loop over the letters to normalize the occurrences to 1.
    num_chars = float(sum(freq_dict.values()))

    for character in letters:
        freq_dict[character] /= num_chars

    # We're done---print the glorious output. (And here it is appropriate to
    # use print() instead of logging.)
    for character, freq in freq_dict.items():
        print('{}: {:.3f}%'.format(character, freq * 100.))

    return freq_dict


def republic_charcount_barchart(letters,frequencies):
    """ Generating bar chart with frequencies of the letter of the
        alphabet contained in 'The Republic'
    """
    start_time = time.time()

    logger.info('Generating bar chart of character frequencies')
    try:
        plt.bar(letters, frequencies, edgecolor='black', alpha=0.9)
    except ValueError as e:
        print('Ops... Cannot produce the barchart if the arguments are not two lists of the same lenght')

    plt.ylabel('Relative frequencies')
    plt.title('The Republic: characters count')

    # Showing total elapsed time for generating bar chart
    logger.info('Bar chart printed in {:.3f}s'.format(time.time()-start_time))

    # Showing bar chart
    plt.show()




if __name__ == '__main__':
    # Option to show a brief description with --help
    parser = argparse.ArgumentParser(description=
    'Measure the releative frequencies of letters in a text file')
    parser.add_argument('infile',type=str, help='path to the input file')
    # Option to plot the bar chart with character frequencies
    # with '--p' flag
    parser.add_argument('--p',action='store_true',help='plot bar chart')

    # Option to exclude introduction and license from the process with '--e'
    parser.add_argument('--e',action='store_true',help='exclude introduction and license')

    args = parser.parse_args()

    start_time=time.time()

    # Assigning 'True' to the boolean variable 'exclude' if the option of
    # cutting the introduction and licence is requested
    exclude=args.e

    # Main process. Returns a dictionary with relative frequencies
    # of each letter.
    frequencies_dict=process(args.infile,exclude)

    # Creating a list for the frequencies and a list for the letters
    # to build the bar chart
    frequencies_list = list(frequencies_dict.values())
    letters_list = list(frequencies_dict.keys())

    end_time=time.time()
    logger.info('Total elapsed time {:.3f}s'.format(end_time-start_time))

    barchart_option=args.p

    if barchart_option:
        republic_charcount_barchart(letters_list, frequencies_list)
