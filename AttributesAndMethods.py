class MyClass:
    # SELF KEYWORD IS USED TO CONNECT ATTRIBUTES AND METHODS TO CLASS,
    # SO THAT WE CAN ACCESS THESE THROUGH INSTANCE(S) OF THE CLASS.

    # CLASS OBJECT ATTRIBUTES VALUES ARE SAME FOR ALL INSTANCE
    classObject = "SameValueForAllInstance"

    # INIT WILL BE CALLED WHEN AN INSTANCE OF A CLASS IS CREATED
    # LIKE CONSTRUCTOR IN C#
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    # METHODS ARE LIKE FUNCTION BUT INSIDE CLASS AND CAN BE ALSO CALLED AS OPERATIONS/ACTIONS
    def method(self):
        print(self.param1)


myClass = MyClass("HELLO", "WORLD")
myClass.method()
