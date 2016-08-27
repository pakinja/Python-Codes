user_data = raw_input("Enter the file name: ")
lines_list = [line.strip("\n") for line in open(user_data, 'r')]


def find_spam_confidence(data):
    confidence_sum = 0
    confidence_count = 0
    for line in lines_list:
        if line.find("X-DSPAM-Confidence") == -1:
            pass
        else:
            confidence_index = line.find(" ") + 1
            confidence = float(line[confidence_index:])
            confidence_sum += confidence
            confidence_count += 1
    print "Average spam confidence: " + str(confidence_sum / confidence_count)

find_spam_confidence(lines_list)
