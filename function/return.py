# no explicit return
def print_name(fname, lname):
    print(fname, lname)

print_name('John', 'Doe')

# return

def get_name(fname, lname):
    return fname + ' ' + lname

full_name = get_name('Alasan', 'Mballow')
print(full_name)

def sum(x, y):
    return x + y

print(sum(12, 13))