from UnitTest import UnitTest

class Stupid:
    pass

class Foo:

    def __init__(self, v):
        self._v = v

    def __nonzero__(self):
        return self._v>0

    def __len__(self):
        return 1

class Bar:

    def __init__(self, v):
        self._v = v

    def __len__(self):
        return self._v


class BoolTest(UnitTest):

    def testBaseTypes(self):
        # meta test first
        self.assertTrue(True)
        self.assertFalse(False)

        # booleans
        self.assertTrue(bool(True))
        self.assertFalse(bool(False))
        self.assertTrue(True == True)
        self.assertFalse(False == True)

        # ints
        self.assertTrue(bool(1))
        self.assertFalse(bool(0))
        self.assertTrue(1)
        self.assertFalse(0)

        # strings
        self.assertTrue(bool('a'))
        self.assertFalse(bool(''))
        self.assertTrue('a')
        self.assertFalse('')

    def testObjects(self):

        # objects
        self.assertTrue(bool(Stupid()))
        self.assertTrue(Stupid())

        # __nonzero__ has precidence
        self.assertFalse(bool(Foo(0)))
        self.assertTrue(bool(Foo(1)))
        self.assertFalse(Foo(0))
        self.assertTrue(Foo(1))

        # __len__ is used secondary
        self.assertFalse(bool(Bar(0)))
        self.assertTrue(bool(Bar(1)))
        self.assertFalse(Bar(0))
        self.assertTrue(Bar(1))


        # lists
        self.assertFalse(bool([]))
        self.assertTrue(bool([1]))
        self.assertFalse([])
        self.assertTrue([1])

        # dicts
        self.assertFalse(bool({}))
        self.assertTrue(bool({'x':1}))
        self.assertFalse({})
        self.assertTrue({'x':1})


    def testIfStatement(self):
        if([]):
            self.fail("Empty lists should not evaluate to True in If")
        if([1]):
            return
        self.fail("None-empty lists should evaluate to True in If")

    def testWhileStatement(self):
        while([]):
            self.fail("Empty lists should not evaluate to True in While")
            break;
        while([1]):
            return
        self.fail("None-empty lists should evaluate to True in While")

