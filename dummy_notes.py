from note import Note


title = "Sidra's Notes"
date_created ="10/20/2015"
date_modified = "10/30/2015"
content = "This is a test file. Testing testing 123."
userId = 456
noteId = 456789



print 'title: {}'.format(title)
print('date_created:{}'.format(date_created))
print("date_modified : {} ".format(date_modified))
print("content : {} ".format(content))
print("userId : {} ".format(userId))
print("noteId : {} ".format(noteId))

print("===========DICTIONARY====")

mynote= Note(title,date_created,date_modified,content,userId,noteId)
print "title: {} ".format(mynote.title)
print "date_created: {} ".format(mynote.date_created)
print "date_modified: {} ".format(mynote.date_modified)
print "content: {} ".format(mynote.content)
print "userId: {} ".format(mynote.userId)
print "noteId: {} ".format(mynote.noteId)
