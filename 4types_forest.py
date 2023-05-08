# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#
#      def__init__(self):                                                                       # __init__(self):
#         self.life_is_like_a_box_of = Forest._life_is_like_a_box_of
#
# mama_said = Forest()
# print(mama_said._life_is_like_a_box_of)                                                       # prints: chocolate
#
############################################################## 2 #######################################################
# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#
# mama_said = Forest()
# print(mama_said._life_is_like_a_box_of)                                                       # prints: chocolate
#
############################################################## 3 #######################################################
# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#
#     def life_is_like_a_box_of(self):                                                                # def
#         return self._life_is_like_a_box_of
#
# mama_said = Forest()
# print(mama_said.life_is_like_a_box_of())      #ניגש דרך הפונקציה לכן יש סוגריים בסוף#         prints: chocolate
#
############################################################## 4 #######################################################
# class Forest:
#
#     def __init__(self,name):
#         self.name = name + ' vegam zormot'
#
#     @classmethod
#     def clasmeth_get_name(cls,name):
#         return cls(name)
#
#     def print_name(self):
#        print(self.name)
#
# beitsim = Forest("yogev")
#
# Forest.name.print_na
# # mama_said.print_name()


# ########################################################################################################################
# class Student:
#
#   name = 'kobikobi'
#
#   def print_name(obj):
#       print(obj.name)
#
# #Student.print_name = classmethod(Student.print_name)
#
# Student.print_name()
#$print(mama_said.life_is_like_a_box_of)     #ניגש דרך הפונקציה אך ללא סוגריים בגלל הפרופרטי#     prints: chocolate
