# find all duplicate values from list

def list_duplicates(values):
  values.sort()

  res=[]
  result = set(res)

  i=1;
  while i < len(values):
    if values[i]==values[i-1] :
       result.add(values[i])
       i=i+1
    else :
      i=i+1

  res = list(result)
  return res



student_id = [1,27,7,7,7,7,7,8,9,9,4,3,4]
ans=list_duplicates(student_id)
print(ans)
