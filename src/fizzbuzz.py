#solution1
def fizzbuzz(dictionary,number):
    output=''
    for key in dictionary:
        if number%key==0:
           output+=dictionary[key]
           return output




#solution 2
#  def FizzBuzz(input_number):
#     output = ""
#     if input_number <=0:
#         return None
#     if input_number%3==0:
#         output += "Fizz"
#     if input_number%5==0:
#         output += "Buzz"
#     if output == "":
#         output += str(input_number)
#     return output

# solution3
# def FizzBuzz(input_number):
#     if input_number<=0:
#         return None
#     elif input_number%15==0:
#         return "FizzBuzz"
#     elif input_number%3==0:
#         return "Fizz"
#     elif input_number%5==0:
#         return "Buzz"
#     return str(input_number)