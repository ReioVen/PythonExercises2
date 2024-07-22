word = str(input("Enter the word: ")).capitalize()


output = ""

if word == 'Fizz':
    output = "Boom!"
if word == 'Buzz':
    output = "Are you a bee?"
if word == 'FizzBuzz':
    output = "What did you say?"

print(output)
