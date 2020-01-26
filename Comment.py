class Comment:
    def __init__(self, user, content, commentDate, commentPrivacy):
        self.user = user
        self.content = content
        self.commentDate = commentDate
        self.commentPrivacy = commentPrivacy
        self.replyComment = []

        # methods

    def editComment(self, text):
        self.content = text

    def replyComment(self, comment):
        self.replyComment.append(comment)
