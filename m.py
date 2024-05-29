# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start

#     def __iter__(self):
#         self.current = self.start  
#         return self

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration 
#         else:
#             current = self.current
#             self.current += 1
#             return current

# my_range = MyRange(1, 5)

# for num in my_range:
#     print(num)


# class MyCollection:
#     objects = []

#     def __init__(self, value):
#         self.value = value
#         MyCollection.objects.append(self)
    
#     def __iter__(self):
#         return MyCollectionIterator(MyCollection.objects)

#     def __repr__(self):
#         return f"MyCollection(value={self.value})"

# class MyCollectionIterator:
#     def __init__(self, objects):
#         self._objects = objects
#         self._index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._index < len(self._objects):
#             result = self._objects[self._index]
#             self._index += 1
#             return result
#         else:
#             raise StopIteration

# obj1 = MyCollection(1)
# obj2 = MyCollection(2)
# obj3 = MyCollection(3)

# for obj in MyCollection.objects:
#     print(obj)


# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age}, gender='{self.gender}')"

#     def __iter__(self):
#         return PersonIterator(self)

# class PersonIterator:
#     def __init__(self, person):
#         self.person = person
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             self.index += 1
#             return self.person
#         else:
#             raise StopIteration()

# persons = [
#     Person("John Doe", 35, "Male"),
#     Person("Jane Smith", 28, "Female"),
#     Person("Bob Johnson", 42, "Male"),
#     Person("Sarah Lee", 31, "Female")
# ]

# for person in persons:
#     print(person)

# print("---")

# adult_persons = [p for p in persons if p.age > 30]
# for person in adult_persons:
#     print(person)

# print("---")

# male_persons = [p for p in persons if p.gender == "Male"]
# for person in male_persons:
#     print(person)

# print("---")

# female_persons = [p for p in persons if p.gender == "Female"]
# for person in female_persons:
#     print(person)


# class IdIterable:
#     def __init__(self, objects):
#         self.objects = objects
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.objects):
#             obj = self.objects[self.index]
#             self.index += 1
#             return obj.id
#         else:
#             raise StopIteration()

# class Person:
#     def __init__(self, id, name, age, gender):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def __repr__(self):
#         return f"Person(id={self.id}, name='{self.name}', age={self.age}, gender='{self.gender}')"

# persons = [
#     Person(1, "John Doe", 35, "Male"),
#     Person(2, "Jane Smith", 28, "Female"),
#     Person(3, "Bob Johnson", 42, "Male"),
#     Person(4, "Sarah Lee", 31, "Female")
# ]

# for person_id in IdIterable(persons):
#     print(person_id)
