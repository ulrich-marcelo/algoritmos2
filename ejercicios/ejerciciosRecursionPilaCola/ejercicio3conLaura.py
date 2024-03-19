def intercalar(l1 : list[int], l2 : list[int]):
    if len(l1)==1:
        return l1 + l2
    else:
        return [l1[0],l2[0]] + intercalar(l1[1:],l2[1:])

def intercalarGral(l1 : list[int], l2 : list[int]):

    if len(l1)>len(l2):
        minil = l2
        granl = l1
    else:
        minil = l1
        granl = l2
        
    if len(minil)==1:
        return minil + granl
    else:
        return [minil[0],granl[0]] + intercalarGral(minil[1:],granl[1:])



li1=[1,2,3,7,8]
li2=[4,5,6]
print(intercalarGral(li1,li2))
