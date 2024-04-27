import json

if __name__ == "__main__":
    auth = {
        "users": [
            {
                "email": "wakadrammeh@gmail.com",
                "password": "21712494",
                "name": "Muhammed Drammeh",
                "address": "Manjai"
            },
        ]
    }

    # print(json.dumps(auth))

    # Add user
    auth["users"].append({
                "email": "sjawneh23@gmail.com",
                "password": "1234",
                "name": "Sulayman Jawneh",
                "address": "Sukuta"
            })
    
    users = auth["users"]

    # Search up user
    for user in users:
        if user["email"] == "wakadrammeh@gmail.com":
            print("Found!")

    # Update user
    for user in users:
        if user["email"] == "wakadrammeh@gmail.com":
            user["dob"] = "1999-1-1"

    # Delete user
    for user in users:
        if user["email"] == "sjawneh23@gmail.com":
            users.remove(user)

    print(json.dumps(auth))

    # with open("auth.json", "wt") as f:
    #     json.dump(auth, f, indent=4)