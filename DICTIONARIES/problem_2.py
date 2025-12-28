"""
Problem 2: Update Operations
Given:
profile = {"name": "Shahzaib", "age": 17, "country": "Pakistan"}

Do this:
1- Update age to 18
2- Add a new key: "interest": "AI Engineering"
3- Remove "country"
4- Print final result
"""

profile = {
            "name": "Shahzaib", 
            "age": 17, 
            "country": "Pakistan"
}


# Task 1 & 2: Update Profile Dictionary
profile.update({
                "age" : 18,
                "interest" : "AI Engineering",
})

# Task 3: Remove Country From the Updated Dictionary
profile.pop("country")


for key, value in profile.items():
    print(key.capitalize(), ":", value)