class Privacy:
    def __init__(self, pricavyList):
        self.privacyList = pricavyList

    def hasAccess(self, user):
        # Check if element exists in list using python “in” Operator
        return user in self.privacyList
