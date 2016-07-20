#make a random_list
import random
len_of_list = int(raw_input('Enter the len of list of numbers 1 to 100 '))
list_to_sort = random.sample(range(1,100),len_of_list)
print 'The list to sort is %s' % list_to_sort
def main():
	for i in range(len(list_to_sort)):
		print list_to_sort
		bubble_sort(list_to_sort[:len(list_to_sort)-i])

def bubble_sort(list_object):
	for i in range(len(list_object)-1):
		if list_object[i] > list_object[i+1]:
			list_object[i],list_object[i+1] = list_object[i+1],list_object[i]
			# print list_object
if __name__ == '__main__':
	main()
	print 'The sorted list is %s' % list_to_sort
