from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from group import views

factory = APIRequestFactory()

groupPath = '/group'

groupJson = {}

groupJson['id'] = 0
groupJson['name'] = 'TESTGROUP'
groupJson['color'] = '#FF9900'

#TEST : CREATE A GROUP
request = factory.post(groupPath, groupJson, format='json')
force_authenticate(request, user=admin)  #This is not necessary
view = TheGroup.as_view()
response = view(request)

#TEST : GET ALL GROUP
request = factory.get(groupPath)
force_authenticate(request, user=admin)
view = TheGroup.as_view()
response = view(request)

#THEN WE GET THE ID OF ONE GROUP
SampleJson = response[0]
groupid = SampleJson['id']
groupIDPath = '/group/' + str(groupid)

#TEST : GET A GROUP BY ID
request = factory.get(groupIDPath)
force_authenticate(request, user=admin)
view = GroupById.as_view()
response = view(request)

#TEST : UPDATE ONE GROUP
request = factory.put(groupIDPath, groupJson, format='json')
force_authenticate(request, user=admin)
view = GroupById.as_view()
response = view(request)

#TEST : DELETE ONE GROUP
request = factory.delete(groupIDPath)
force_authenticate(request, user=admin)
view = GroupById.as_view()
response = view(request)
