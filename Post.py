class Post:
    def __init__(self, user, postDate, postPrivacy, postField):
        self.user = user
        self.postDate = postDate
        self.postPrivacy = postPrivacy
        self.postField = postField
        self.postAction = []
        self.postComments = []
        self.postShare = []

    # methods

    def editPost(self, post):
        self.postPrivacy = post.postPrivacy
        self.postField = post.postField

    def addAction(self, action):
        # adding reactions under the post
        self.postAction.append(action)

    def deleteAction(self, action):
        self.postAction.remove(action)

    def share(self, post):
        self.postShare.append(post)

    def deleteShare(self, post):
        self.postShare.remove(post)

    def addComment(self, comment):
        self.addComment.append(comment)

    def deleteComment(self, comment):
        self.postComments.remove(comment)
