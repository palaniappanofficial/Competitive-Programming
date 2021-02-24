def rotate(array,start,end):
    for i in range(start+1):
        rotateonebyone(array,end)
    print(array)
def rotateonebyone(array,end):
    temp=array[0]
    for i in range(end):
        array[i]=array[i+1]
    array[i+1]=temp
    return array

array=[0,1,2,3,4,5,6,7,8,9]
rotate(array,2,9)