import datetime
from Search import *
from Menu import *
import csv


class Note:
    def __init__(self, note_id, note_subject, note_text):
        self.note_id = note_id
        self.note_subject = note_subject
        self.note_text = note_text
        self.note_data_save = self.Data_time()



    def __str__(self):
        return (f'{self.note_id};{self.note_subject};{self.note_text};{self.note_data_save}')
    def Note_save(self):
        try:
            file = open('Note_book.csv')
        except IOError as e:
            with open('Note_book.csv','w',newline='',encoding='UTF-8') as f:
                header = ['id','subject','text','save_data']
                write = csv.writer(f,delimiter=';')
                write.writerow(header)
                f.close()
                self.Note_save(self.note_id, self.note_subject, self.note_text, self.note_data_save)


        else:

                with open('Note_book.csv','a',newline='',encoding='UTF-8') as f:
                    write = csv.writer(f,delimiter=';')
                    sample = (self.note_id,self.note_subject,self.note_text,self.note_data_save)
                    print (*sample)
                    write.writerow(sample)


    def Data_time(self):
        data_time = datetime.datetime.now()
        note_data_save = data_time.strftime("%b %d %Y - %H:%M:%S")

        return note_data_save













    
    
    
