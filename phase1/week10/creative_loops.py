#pattern1 score tracker
scores = [100, 90, 80, 70, 60]
print("scores: ", scores)
for i, score in enumerate(scores,1):
    if score >= 90:
        print(f"Score {i}: {score} is an A")
    elif score >= 80:
        print(f"Score {i}: {score} is a B")
    elif score >= 70:
        print(f"Score {i}: {score} is a C")
    elif score >= 60:
        print(f"Score {i}: {score} is a D")
    else:
        print(f"Score {i}: {score} is an F")

#pattern 2 progress bar
tasks = ["loading", "downloading", "installing", "updating", "rebooting"]
import time
for i, task in enumerate(tasks,1):
    print(f"Task {i}: {task}")
    for j in range(10):
        print(f"Progress: {j*10}%")
        time.sleep(.1)
    print(f"Task {i} completed")



