global names
global scores
names = ["" for i in range(11)]
scores = [0 for i in range(11)]

def ReadHighScores():
	file = open('HighScore.txt','r')
	for i in range(10):
		names[i] = file.readline().strip()
		scores[i] = int(file.readline().strip())
		
	file.close()

def OutputHighScores():
	for i in range(10):
		print(names[i], " ", scores[i])

print("List of players with the top 10 scores: \n")
ReadHighScores()
OutputHighScores()

newName = input("Enter the 3-character name of the player: ")
while len(newName) != 3:
	newName = input("Please try again: ")

newScore = int(input("Enter the score of the player between 1 and 100000 inclusive: "))
while newScore < 1 or newScore > 100000:
	newScore = int(input("Please try again: "))

def TopTen(name, score):
	for i in range(10):
		if score >= scores[i]:
			for j in range(10, i - 1, -1):
				scores[j] = scores[j - 1]
				names[j] = names[j - 1]
				
			scores[i] = score
			names[i] = name
			break

TopTen(newName, newScore)
print("Updated list of players with the top 10 scores: \n")
OutputHighScores()

def WriteTopTen():
	file = open('NewHighScore.txt','w')
	for i in range(10):
		file.write(names[i])
		file.write(" ")
		file.write(str(scores[i])+'\n')
		
	file.close()
