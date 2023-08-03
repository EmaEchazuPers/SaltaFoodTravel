class ControladorReviews:
    def __init__(self,app,reviews):
        self.app = app
        self.reviews = reviews

    def getReviews(self):
        return self.reviews