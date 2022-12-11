from tkinter import* 
root = Tk()
root.title("Fibonacci project")
root.geometry("400x400")

enter_number=Entry(root)
fibonacci_series = Label(root)
fibonacci_sum = Label(root)

def find_sum():
    user_input=10
    user_input=int(enter_number.get())
    first_no=0
    second_no=1
    sum=0
    counter = 1
    sum2=0 
    while(counter <= user_input):
        fibonacci_series["text"]+=str(sum)+" "
        counter=counter+1
        first_no=second_no
        second_no=sum
        sum=first_no+second_no
        sum2= sum+sum2 
        fibonacci_sum["text"]= "Fibonacci sum = " + str(sum2)
        
        
btn= Button(root, text="show Fibonacci Series", command = find_sum)
btn.pack()
fibonacci_series.pack()
fibonacci_sum.pack()
enter_number.pack()

root.mainloop()
        