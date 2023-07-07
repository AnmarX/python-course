import requests 
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import datetime
token=os.getenv("pixle_token")
username=os.getenv("username_")
graph_name=os.getenv("graph_name")
graph_id=os.getenv("graph_id")


the_url="https://pixe.la/v1/users"
# #data= will return any data on other format than json
# #json= will return or send the data in json format 
user_parm={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes"
    # "notMinor":"yes"


}
res=requests.post(the_url,json=user_parm)
print(res.status_code)
print(res.text)

# graph_parm={
#     "id":graph_id,
#     "name":graph_name,
#     "unit":"Km",
#     "type":"int",
#     "color":"ajisai"
# }

# token_header={
#     "X-USER-TOKEN":user_parm["token"]

# }
# graph_endpoint=f"{the_url}/{user_parm['username']}/graphs"

# # res=requests.post(graph_endpoint,json=graph_parm,headers=token_header)
# # print(res.status_code)
# # print(res.text)
# today=datetime.now()

# post_pixel_parm={
#     "date":today.strftime("%Y%m%d"),
#     "quantity":"7"
# }

# post_pixel=f"{graph_endpoint}/{graph_id}"

# # res=requests.post(post_pixel,headers=token_header,json=post_pixel_parm)
# # print(res.status_code)
# # print(res.text)

