
import numpy
 
# initializing matrices
x = numpy.array([[1, 2]])
y = numpy.array([[7, 8], [9, 10]])
 
# using sqrt() to print the square root of matrix
print ("The element wise square root is : ")
print (numpy.sqrt(x))
 
# using sum() to print summation of all elements of matrix
print ("The summation of all matrix element is : ")
print (numpy.sum(y))
 
# using sum(axis=0) to print summation of all columns of matrix
print ("The column wise summation of all matrix  is : ")
print (numpy.sum(y,axis=0))
 
# using sum(axis=1) to print summation of all columns of matrix
print ("The row wise summation of all matrix  is : ")
print (numpy.sum(y,axis=1))
 
# using "T" to transpose the matrix
print ("The transpose of given matrix is : ")
print (x.T)




