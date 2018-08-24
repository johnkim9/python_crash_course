#3-4 (Guest List)
guest_list = ['obama','lincoln','washington','clinton']
message ="Dear President " + guest_list[0].title() + ", I would like to invite you to our special dinner on Friday."
print (message)
message_lincoln = "Dear President " + guest_list[1].title() + ", I would like to invite you to our special dinner on Friday."
print (message_lincoln)
message_washington = "Dear President " +guest_list[2].title() + ", I would like to invite you to our special dinner on Friday."
print (message_washington)
message_clinton = "Dear Preisdent " +guest_list[3].title() + ", I would like to invite you to our special dinner on Friday."
print (message_clinton)

#3-5 (Changing Guest List)
unavailable_guest = guest_list.pop()
print (guest_list)
guest_list.append('bush')
print (guest_list)

