from user import User

fname = 'Osama'
lname = 'Sakhi'
email = 'msakhi21@gmail'
password = 'lucy70'
userid = 1234

print 'fname: {}'.format(fname)
print 'lname: {}'.format(lname)
print 'email: {}'.format(email)
print 'password: {}'.format(password)
print 'userid: {}'.format(userid)

print '================MY USER ============'

myuser = User(fname, lname, email, password, userid)
print 'fname: {}'.format(myuser.fname)
print 'lname: {}'.format(myuser.lname)
print 'email: {}'.format(myuser.email)
print 'password: {}'.format(myuser.password)
print 'userid: {}'.format(myuser.userid)


jsonuser = myuser.create_json()

print jsonuser

print '================FROM JSON ============'

clone = User.read_json(jsonuser)
print 'fname: {}'.format(clone.fname)
print 'lname: {}'.format(clone.lname)
print 'email: {}'.format(clone.email)
print 'password: {}'.format(clone.password)
print 'userid: {}'.format(clone.userid)


print '==================FROM DB ============='
fromdb = {
	"fname" : "Osama",
	"lname" : "Sakhi",
	"email" : "blah@gmail.com",
	"password" : "pass1234",
	"userid" : 1234
}
user_fromdb = User.read_json(fromdb)
print 'fname: {}'.format(user_fromdb.fname)
print 'lname: {}'.format(user_fromdb.lname)
print 'email: {}'.format(user_fromdb.email)
print 'password: {}'.format(user_fromdb.password)
print 'userid: {}'.format(user_fromdb.userid)