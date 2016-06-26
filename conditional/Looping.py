# largest = None
# smallest = None
# while True:
#     num = raw_input("Enter a number: ")
#     if num == 'done':
#         break
#     try:
#         inp = int(num)
#     except:
#         print "Invalid input"
#         continue
#     if largest is None:
#         largest = inp
#         smallest = inp
#     elif inp > largest:
#         largest = inp
#     elif inp < largest:
#         smallest = inp
# print "Maximum is",largest
# print "Minimum is", smallest





text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
print pos
ln = len(text)
print ln
print text[pos:]
