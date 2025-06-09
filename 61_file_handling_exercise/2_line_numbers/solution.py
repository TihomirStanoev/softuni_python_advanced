from string import punctuation


def count_letters(sentence: str) -> int:
    return sum(1 for letter in sentence if letter.isalpha())


def count_punctuation(sentence: str) -> int:
    return sum(1 for character in sentence if character in punctuation)


def file_process(file_name: str) -> list:
    processed_lines = []

    with open(file_name, 'r') as input_file:
        for index, line in enumerate(input_file, start=1):
            total_letters = count_letters(line)
            total_punctuation = count_punctuation(line)
            text = line.strip()
            processed_lines.append(f'Line {index}: {text}({total_letters})({total_punctuation})')

    return processed_lines



INPUT_FILE = 'text.txt'
OUTPUT_FILE = 'output.txt'
all_processed_lines = []

try:
    all_processed_lines = file_process(INPUT_FILE)
except FileNotFoundError:
    print('File not found!')


with open(OUTPUT_FILE, 'w') as output_file:
    output_file.write('\n'.join(all_processed_lines))
