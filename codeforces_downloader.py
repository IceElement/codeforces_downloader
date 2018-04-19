import re
import requests
import sys
import os
import html

#send 5 requests to the server, just in case the earlier ones do not get a response
def try_5_requests(s):
	for i in range(5):
		try:
			a=requests.get(s)
			return a
			break
		except:
			pass
		print('Network too unreliable!','Exiting!')
		sys.exit(0)

user_handle = "IceElement"
save_directory = "./codeforces/"+user_handle+"/"

if not os.path.exists(save_directory):
	os.makedirs(save_directory)

api_url = "http://codeforces.com/api/user.status?handle="
server_response = try_5_requests(api_url+user_handle)
server_response  = server_response.json()
server_response = server_response['result']

for problem_data in server_response:
	if problem_data['verdict']=='OK':
		
		contestId = problem_data['contestId']
		problemId = problem_data['problem']['index']
		problemName = problem_data['problem']['name']
		problemLanguage = problem_data['programmingLanguage']

		#submissions are by language, not by extension
		extension = ''
		if problemLanguage.find('C++')!=-1:
			extension='.cpp'
		elif problemLanguage.find('ython')!=-1:
			extension='.py'
		elif problemLanguage.find('C')!=-1:
			extension='.c'
		elif problemLanguage.find('ava')!=-1:
			extension='.java'

		file_name = str(contestId)+str(problemId)+' '+problemName
		file_name = re.sub(r'[\|><":/\*\?\\]',' ',file_name)

		if os.path.exists(save_directory+file_name+extension):
			print(file_name,'existed, skipped!')
			continue

		submissionId = problem_data['id']
		submissionUrl = "http://codeforces.com/contest/"+str(contestId)+"/submission/"+str(submissionId)
		submissionResponse = try_5_requests(submissionUrl)

		submissionResponse.encoding = 'utf-8'
		submissionHTML = submissionResponse.text
		submissionHTML = re.search(r'style="padding: 0\.5em;">(.*?)</pre>',submissionHTML,re.DOTALL)
		
		dirty_code = submissionHTML.group(1)
		clean_code = html.unescape(dirty_code)
		
		if len(clean_code)>20000:
			print(file_name,'codeforces sent an unexpected response for this file, please try manually')
			continue
			
		with open(save_directory+file_name+extension,'wb+') as file:
			file.write( clean_code.encode('utf-8') 	) 
		print(file_name,'saved!')
print('All problems with accepted verdict saved!')