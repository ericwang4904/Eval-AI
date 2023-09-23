# Get user input for the underlined part
student_name = input("Enter the student's first name: ")

print()
print(f"You are now writing an eval for {student_name}.\n")

open_session_rank = input(f"How would you rank  {student_name}'s performance in open session? Type '0' for 'Needs improvement', '1' for 'Good', and '2' for 'Excellent!': ")

print()
print(f"You ranked {student_name}'s performance in open session as {open_session_rank}.\n\n")


if int(open_session_rank) == 0:
    open_session_word = 'good'
elif int(open_session_rank) == 1:
    open_session_word = 'great'
else:
    open_session_word = 'incredibly thoughtful'



# Generate the complete message
message = f"{student_name}, it was an absolute pleasure teaching you again. During open sessions, you gave {open_session_word} feedback and advice to your peers.\n\n"
message += "Additionally, throughout the mental health unit, you added helpful knowledge and perspectives. For example, during the lesson on current events and pop culture, you eloquently described the harms when society ignores people's struggles.\n\n"
message += "Your group presentation on Indigenous and Non-western Perspectives was excellent. I appreciated the important dialogue that professionals do not meet the current need of mental health struggles in any region of the world and less so in indigenous and non-Western regions. "
message += "I thought your group did a thorough job describing local practices to obtain positive mental health and treatments for mental illnesses in Latin America, East Asia, and Pacific Islands. Finally, your argument that Asian Americans receive less mental health support, because they are less likely to seek care and receive it was well supported. "
message += "I agree with you that strong factors are the model minority myth that perpetuates cultural stigmas against reaching out and racism/stereotypes that could lead to underdiagnosis or misdiagnosis.\n\n"
message += "All in all, you did a wonderful job in your last semester of SOM. It was a pleasure being your teacher, and I wish you all the best for a joyful and rejuvenating summer!"

# Print the complete message
print(message)