class Vector:
     """ Represents a vector in mluidimentional space """

     def __init__(self,d):
         """ Create d-dimensional vector of zeros """
         self._coords = [0] * d

     def __len__(self):
         """Return the dimention of the vector """
         return len(self._coords)

     def __getitem__(self,j):
         """Return jth coordiante of vector """
         return self._coords[j]


     def __setitem__(self,j,v):
         """set jth coordiante of vector to given value """
         self._coords[j] = v

     def __add__(self,other):
         """Return sum of two vectors"""

         if len(self) != len(other):
             raise ValueError('dimentions must agree ')
         result  = Vector(len(self))  #start with vector of zeros
         for  j in range(len(self)):
             result[j] = self[j] + other[j]

         return result

     def __eq__(self,other):
         """Return True if vector has same coordiante as other """

         return self._coords == other._coords
     def __ne__(self,other):
         """Return False if vector diifers from other """
         return not self == other

     def __str__(self):
         """Produce string representation of vector"""

         return '<' + str(self._coords)[1:-1] + '>' #adapt list representation



v =  Vector(10)
