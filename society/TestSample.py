from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

factory = APIRequestFactory()

FollowPath1 = '/user/1/following/2'
FollowPath2 = '/user/1/followint/3'
FollowingPath = '/user/1/following'
FollowerPath = '/user/2/follower
CommentPath = '/comment'
NullJson = {}

CommentJson_Get = {}
CommentJson_Star = {}
CommentJson_Score = {}
CommentJson_Comment = {}

CommentJson_Star['id'] = 0
CommentJson_Star['fileID'] = 'TESTFILE'
CommentJson_Star['userID'] = 1
CommentJson_Star['date'] = '2017-11-11T02:37:42.490Z
CommentJson_Star['type'] = 'star'
CommentJson_Star['star'] = True

CommentJson_Score['id'] = 0
CommentJson_Score['fileID'] = 'TESTFILE'
CommentJson_Score['userID'] = 1
CommentJson_Score['date'] = '2017-11-11T02:38:42.490Z'
CommentJson_Score['type'] = 'score'
CommentJson_Score['score'] = 4


CommentJson_Comment['id'] = 0
CommentJson_Comment['fileID'] = 'TESTFILE'
CommentJson_Comment['userID'] = 1
CommentJson_Comment['date'] = '2017-11-11T02:39:42.490Z'
CommentJson_Comment['type'] = 'comment'
CommentJson_Comment['comment'] = 'This is a test'

CommentJson_Get['fileID'] = 'TESTFILE'
CommentJson_Get['type'] = 'star'

#TEST : 1 FOLLOW 2
request = factory.post(FollowPath1, NullJson, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = followSb.as_view()
response = view(request)
#This is a test, you can copy this

#TEST : 1 FOLLOW 3
request = factory.post(FollowPath2, NullJson, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = followSb.as_view()
response = view(request)

#TEST : GET FOLLOWING OF 1
request = factory.GET(FollowingingPath, NullJson, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = getFolloweeList.as_view()
response = view(request)

#TEST : GET FOLLOWER OF 2
request = factory.GET(FollowerPath, NullJson, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = getFolloweeList.as_view()
response = view(request)

#TEST : 1 UNFOLLOW 3
request = factory.delete(FollowPath2, NullJson, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = followSb.as_view()
response = view(request)

#TEST : 1 COMMENT TESTFILE
request = factory.put(CommentPath, CommentJson_Comment, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = followSb.as_view()
response = view(request)

#TEST : 1 STAR TESTFILE
request = factory.put(CommentPath, CommentJson_Star, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = followSb.as_view()
response = view(request)

#TEST : 1 SCORE TESTFILE
request = factory.put(CommentPath, CommentJson_Score, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = followSb.as_view()
response = view(request)

#TEST : GET ALL COMMENT
request = factory.get(CommentPath, CommentJson_Get, format='json')
force_authenticate(request, user=user)  #This is not necessary
view = followSb.as_view()
response = view(request)
