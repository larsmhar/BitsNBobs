#https://www.reddit.com/r/ProgrammerHumor/comments/89uhql/wtf_why_did_i_fail_this_interview_question/

"""
Make this box
##########
##      ##
# #    # #
#  #  #  #
#   ##   #
#   ##   #
#  #  #  #
# #    # #
##      ##
##########

"""
"""
def printStuff(side = 10):
	for row in range(1, side + 1):
		for col in range(1, side + 1):
			isHash = row == 1 or col == 1 or row == side or col == side or col == row or col == side - row + 1
			print("#", end="") if isHash == True else print(" ", end="")
		print("")

printStuff(20)
"""

s=10
x = range
p = print
for r in x(1,11):
    for c in x(1,11):p("#"if(r==1or c==1or r==s or c==s or c==s-r+1or c==r)==1 else " ",end="")
    p("")








