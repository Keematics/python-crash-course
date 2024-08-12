famous_person = "Albert Einstein"
message = "\"A person who never made a mistake never tried anything new.\""
print(f"{famous_person} once said, {message}")

voters = ['alice', 'bob', 'smith']
favourite_languages = {
    'alice': 'python',
    'tyson': 'C#',
    'Ali': 'Golang'
}
if voters:
    for voter in voters:
        voter.lower()
        if voter in favourite_languages:
            print(f"Dear {voter.title()}, thanks for responding to our poll")
        else:
            print(f"Hey {voter.title()}, you're invited to take this poll")
else:
    print("Oh no! No voters yet.")