from tl.rename.case import transform_sentence_case
if __name__ == '__main__':
    input_data = [unicode(line.strip(), 'utf-8') for line in stdin]
    print transform_sentence_case([input_data])[0]
