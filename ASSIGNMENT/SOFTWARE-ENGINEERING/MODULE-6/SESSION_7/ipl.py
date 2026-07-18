# Given the following string: 'Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match', write a function word_freq_dict(text) that returns a dictionary with the frequency of each word.

def word_freq_dict(text):
      count = {}
      final =  text.split()
      for i in final:
            if i in count:
                  count[i]=+1
            else:
                  count[i] = 1
      return count


result = 'Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match'

print(word_freq_dict(result))