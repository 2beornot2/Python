class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicity(self):
        print("PARENT implicity()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()
        print("CHILD ,AFTER PARENT altered()")



dad = Parent()
son = Child()

dad.implicity()
son.implicity()

dad.override()
son.override()

dad.altered()
son.altered()


