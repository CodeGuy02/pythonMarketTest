request_value_string = ''
text_file = open("symbol_list_TDAmeritrade.txt", "r")
for symbol in text_file.readlines(1):
    request_value_string = request_value_string + str(symbol) + ', '

print request_value_string

request_value_string = request_value_string[0:len(request_value_string) - 2]

print ' --------\n'
print request_value_string

request_value_string = str(request_value_string)

print ' string: '
print request_value_string
