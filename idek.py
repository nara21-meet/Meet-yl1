list2=[2,4,6]
list4=[8,2,12]
def nara(l1,l2):
	listdiam=[]
	for num in l1:
		if num in l2:
			listdiam.append(num)
	return sum(listdiam)
print(nara(list2,list4))
    #sum(listdiam)-





    {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w',