#Charles O'Connell
#SE126.02
#FINAL PROJECT
#2/18/2025

#prompt: This will be a program that allows you to sort and search for olivia rodrigo songs and allows you to play Olivia Rodrigo songs.

#var library


#tts
#https://pypi.org/project/pyttsx3/ 

#https://www.geeksforgeeks.org/convert-text-speech-python/



#Questions and answers



#imports
from os import system,name

import csv

import winsound #THIS ONE LIBRARY TOOK ME HOURS TO FIND FOR PLAYING AUDIO FILES BECAUSE EXTERNAL LIBRARIES LIKE PLAYSOUND WOULD NOT WORK IN TERMINAL FOR SOME REASON BUT I FINALLY FOUND ONE THAT WORKS 


#functions

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




def swap(i,listName): #used in bubble sorting 
    temp_val = listName[i]

    listName[i] = listName[i + 1]

    listName[i+1] = temp_val

#----------------------------------MAIN CODE----------------------------------------------#


clear() # for clean terminal 



#---initializations---

ans = "y" #loop control

#empty lists for appending later 
song_name = []

album = []

spotify_streams = []

genre = []

wav_file = []

year= []

#gaining data from olivia rodrigo csv file 

with open("final_project_folder/olivia_rodrigo.csv") as csvfile: #looks at data in oliva rodrigo csv file 
    file = csv.reader(csvfile)

    for rec in file:
        
        #appends data to lists 
        
        song_name.append(rec[0])
        
        album.append(rec[1])
        
        year.append(rec[2])
        
        spotify_streams.append(rec[3])    
        
        genre.append(rec[4]) #COULD NOT HAVE COMMAS IN NUMBERS OF STREAMS DUE TO IT MESSING UP CSV FILE 
        
        wav_file.append(rec[5]) #will not be displayed to user mostly just for processing 
        


while ans == "y":
    
    print("WELCOME TO THE OLIVIA RODRIGO SONGS PROGRAM")
    print("HERE IS THE MENU AND OPTIONS")
    print("1.Show all songs sorted by Name")
    print("2.Show all songs sorted by number of spotify streams (descending)")
    print("3.Search by Album")
    print("4.Search by Year")
    print("5.Search by Song and play song")
    print("6.EXIT")
    
    user_choice = input("\nPlease enter the number choice for your option:")
    
    
    if user_choice == "1":
        
        print("\nShowing all SONGS Alphabetically")
        #BUBBLE SORT----------------------------------------

        for i in range(0, len(song_name) - 1):#outer loop

            

            for index in range(0, len(song_name) - 1):#inner loop

                

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(song_name[index] > song_name[index + 1]):


                    #if above is true, swap places!

                    swap(index,song_name)

                    #swap all other values

                    swap(index,album)
                    swap(index,spotify_streams)
                    swap(index,genre)
                    swap(index, wav_file)
                    swap(index,year)
        print("-"*80)
        print(f"{'SONG':31}  {'ALBUM':8} {'YEAR':10} {'GENRE':11} {'SPOTIFY STREAMS':10}  ")
        
        print("-"*80)
        for i in range(0,len(genre)):
            print(f"{song_name[i]:30}  {album[i]:8} {year[i]:8}  {genre[i]:13} {spotify_streams[i]:10} ")
        print("-"*78)



    elif user_choice =="2":
        print("\nShowing all SONGS BY STREAMS")
        #BUBBLE SORT----------------------------------------

        for i in range(0, len(spotify_streams) - 1):#outer loop

            

            for index in range(0, len(spotify_streams) - 1):#inner loop

                

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(int(spotify_streams[index]) < int(spotify_streams[index + 1])):


                    #if above is true, swap places!

                    swap(index,spotify_streams)

                    #swap all other values

                    swap(index,album)
                    swap(index,song_name)
                    swap(index,genre)
                    swap(index, wav_file)
                    swap(index,year)
        print("-"*80)
        print(f"{'SONG':31}  {'ALBUM':8} {'YEAR':10} {'GENRE':11} {'SPOTIFY STREAMS':10}  ")
        
        print("-"*80)
        for i in range(0,len(genre)):
            print(f"{song_name[i]:30}  {album[i]:8} {year[i]:8}  {genre[i]:13} {spotify_streams[i]:10} ")
        print("-"*78)
        
        
    elif user_choice =="3":
        #will be used
        found = []

        #gets user input
        search_album = input ("Please type in the ALBUM name of the OLIVA Rodrigo songs you would like to see:")
        
        for i in range (0,len(album)):

            if search_album.lower() == album[i].lower():

                found.append(i)
        
        if not found:
            #tells user the department was not found
            print(f" Your search for {search_album} was *NOT* found")
        
        else:
            #tells user the department was found 

            print(f" Your search for {search_album} was found")
            
            for i in range(0,len(found)):
                print(f"{song_name[found[i]]:30}  {album[found[i]]:8} {year[found[i]]:8}  {genre[found[i]]:13} {spotify_streams[found[i]]:10} ")
            print("-"*78)

    elif user_choice =="4":
        #will be used
        found = []

        #gets user input
        search_year = input ("Please type in the year of the OLIVA Rodrigo songs you would like to see:")
        
        for i in range (0,len(year)):

            if int(search_year) == int(year[i]):

                found.append(i)
        
        if not found:
            #tells user the department was not found
            print(f" Your search for {search_year} was *NOT* found")
        
        else:
            #tells user the department was found 

            print(f" Your search for {search_year} was found")
            
            for i in range(0,len(found)):
                print(f"{song_name[found[i]]:30}  {album[found[i]]:8} {year[found[i]]:8}  {genre[found[i]]:13} {spotify_streams[found[i]]:10} ")
            print("-"*78)
        
        
    elif user_choice =="5":
        
        #REMINDER TO SELF DO SEQUENTIAL SEARCH THAT IS EXACT WITH .LOWER() METHOD
        
        #will be used
        found = -1
        
        #gets user input
        search_song = input ("Please type in the song from OLIVA Rodrigo that you would like to see and hear:")
        
        for i in range (0,len(song_name)):

            if search_song.lower() == song_name[i].lower():
                
                found = 
                
        
        
        
    elif user_choice =="6":
        
        print("EXITING PROGRAM...")
        ans="n"
        
    else:
        
        print("***INVALID ENTRY***")
        print("PLEASE ENTER A NUMBER 1-6")
        ans = "y"
        



print("THANK YOU FOR USING THE PROGRAM HAVE A GOOD DAY :) ")




