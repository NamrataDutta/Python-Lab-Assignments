bookscategory={"Python":50,"Software Engg":30,"OOPS":20,"JAVA":40}
finallist=[]
start=int(input("Enter the start range: "))
end=int(input("Enter the end range: "))
for key,value in bookscategory.items():
    if value >= start and value <= end:
        finallist.append(key)
result=','.join(finallist)
print("These books can be purchased for mentioned range ("+result+")")