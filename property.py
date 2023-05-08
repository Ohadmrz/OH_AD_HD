# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#
#     # def __init__(self):
#     #     self.life_is_like_a_box_of = Forest._life_is_like_a_box_of
#
# mama_said = Forest()
# daddy_nothing = Forest()
# print(Forest._life_is_like_a_box_of)
# print(mama_said._life_is_like_a_box_of)
# print(daddy_nothing._life_is_like_a_box_of,'\n')
#
# mama_said._life_is_like_a_box_of = 'pargiot'
#
# #print(Forest._life_is_like_a_box_of)
# print(mama_said._life_is_like_a_box_of)
# print(daddy_nothing._life_is_like_a_box_of,'\n')
#
# Forest._life_is_like_a_box_of = 'mike_tyson'
#
# #print(Forest._life_is_like_a_box_of)
# print(mama_said._life_is_like_a_box_of)
# print(daddy_nothing._life_is_like_a_box_of)

############################################################## 1 #######################################################
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
#     _life_is_like_a_box_of: str = 'chocolate'
#
#     @property                                                                                      # @property
#     def life_is_like_a_box_of(self):                                                                 # def
#         return self._life_is_like_a_box_of
#
# mama_said = Forest()
# print(mama_said.life_is_like_a_box_of)     #ניגש דרך הפונקציה אך ללא סוגריים בגלל הפרופרטי#     prints: chocolate
#
########################################################################################################################
