from jsonpath_ng import jsonpath,parse
import json
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext
  
f = open('/storage/emulated/0/HttpCanary/download/que/response_body.json')
data=(json.load(f))

jsonpath_expr = parse("$..statement")
res=[match.value for match in jsonpath_expr.find(data)]

jsonpath_expra = parse("$..choices")
resa=jsonpath_expra.find(data)
for k, v in (resa).items():
	if is_correct == true :
		resan=v.choice_statement
	

f = open("/storage/emulated/0/HttpCanary/download/question.txt", "w")
for ele in res:
    f.write(cleanhtml(ele))


f1 = open("/storage/emulated/0/HttpCanary/download/answer.txt", "w")
for ele in resan:
    f1.write(resan)



