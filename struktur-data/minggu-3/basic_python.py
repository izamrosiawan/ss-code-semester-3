#Basic Python
nama   = "bramasta" + " jaya"
number = 30
weight = 61.5621025
grade  = 'A'
status = False

def basic_print():
    # Basic print
    print( "My name: ",nama,
        "\nMy age:",number,"years old",
        "\nMy Weight is ", weight)

    print(round(weight, 2)) # round( float data type, .n )

def basic_operator():
    # Basic logic operator
    print( not status )
    print( 0 > 1 and 1 > 2 )
    print( 0 > 1 or 1 > 2 )
    print( 10 ^ 9 ," | ", status ^ (not status) ) 


    print( type(nama) )  # type of data
    print( 77 + 2 )      # normal addition
    print( 77 - 7 )      # normal subtraction
    print( 22 / 7 )      # normal division
    print( 22 * 7 )      # normal multiplication
    print( 10 % 7 )      # modulus (nilai sisa)
    print( 10 // 6 )     # floor division
    print( 77 ** 2 )     # normal to the power

    print( (13 // 6 ) * 2/2 ) # normal operation

    # Basic comparison operator
    print( 'main' == 'main' )
    print( 22 >= 7 )
    print( 22 <= 7 )
    print( 22 > 7 )
    print( 22 < 7 )
    print( 25 != 25 )

def basic_if_else():
    # Basic if-else condition
    """
        0 = False
        1 = True
    """
    if True:
        print("condition: ", 0 == True or not 1 == False )
    elif(True and False == False):
        print("condition: ", 0 == True and not 1 == False)
    else:
        print("False")

def ternary_operator():
    n = int(input("Input n: "))
    tern = "Positive" if n > 0 else "Negative" if n < 0 else "Zero" # If nested using ternary syntax
    print(tern)
    tern2 = ("Ganjil", "Genap")[n%2==0]
    print(tern2)
    
def basic_list_tuple_dictionary():
    # LIST
    this_is_list = [
        0,False,2,3,"4"
    ] # Mutable, tipe data yang dapat menyimpan lebih dari satu tipe data dan dapat dimanipulasi (Add, Delete, Update)

    j=len(this_is_list)-1

    while j >= 0:
        print("current list: ", this_is_list)
        j-=1

    print(this_is_list[3]) 
    n=1
    for i in this_is_list: 
        print(f"index list[{n}] = ",i)
        n+=1 
    this_is_list.append(False)


    # TUPLE
    this_is_tuple = (
        True, 25, 9, 2025, "DS-04-05"
        ) # Immutable, menyimpan lebih dari satu tipe data, namun tidak dapat dimanipulasi
    print(this_is_tuple[0])
    #this_is_tuple.append(2.0)


    # DICTIONARY
    this_is_dictionary = {
        'kelas': 'Struktur Data Python',
        'angkatan':2025,
        'aktif': True,
        1: 'budi'
    } #Mutable, data yang menyimpan lebih dari satu tipe data menggunakan kunci khusus yang bersifat unik dan dapat digunakan sebagai index

    print(this_is_dictionary[1])
    for i, j in this_is_dictionary.items():
        print(i,"\t:", j) # \t = tab

def return_value(nama):
    print(nama)
    nama+=" agung"
    return nama    

if __name__ == "__main__":
    ternary_operator()