import cognitive_face as CF
from global_variables import personGroupId

Key = 'd45ebcdf3bb8479980a4224f0944a24d'
CF.Key.set(Key)
BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.delete(personGroupId);
res = CF.person_group.create(personGroupId);
print (res)
