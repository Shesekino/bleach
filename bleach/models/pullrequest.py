class PullRequest(object):
    def __init__(self, repo, createdAt, user, title, url=None):
        self.repo = repo.encode('ascii', 'ignore')
        self.createdAt = createdAt
        self.user = user
        self.title = title.encode('ascii', 'ignore')
        self.url = url.encode('ascii', 'ignore')
